from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ResumeUploadForm
from .models import Resume
from .utils import convert_pdf_to_txt_pages  # Import your text conversion function
from MeslekSorgulama.models import Meslek, Bolum, Yetenek, MeslekBolum
from django.db.models import Sum, Case, When, Value, IntegerField, Subquery, OuterRef



def check_ats_compatibility(text):
    readable_text = str(text).replace(" ", "").replace("    ", "")
    
    # Check if text contains problematic characters
    if "" not in text and any(char.isalpha() for char in text):
        return "Özgeçmiş ATS uyumlu. Diğer adaylardan 1-0 öndesin!", None
    else:
        if "" in text:
            rows = str(text).split("\n")
            rows_with_special_char = [row for row in rows if "" in row]
            return "Özgeçmişinde aşşağıdaki satırlarda türkçe karakterler problemli! Kullanılan fontlar tüm aday takip sistemleri tarafından okunamamaktadır. Özgeçmişinizi hazırlarken okunabilirliği yüksek, resmi ve standart fontlar kullanmaya özen gösterin.", rows_with_special_char
        elif len(readable_text) < 3:
            return "Özgeçmiş yazı içermemekte! Özgeçmişlerinizi resim formatında hazırlamak aday takip sistemlerinin başarı oranını azaltır. En doğru sonuçlar için özgeçmişinizi word ile hazırlamanız tavsiye edilir.", None
        else:
            return "En doğru sonuçlar için özgeçmişinizi word ile hazırlamanızı tavsiye ederiz!", None



def upload_resume(request):
    if request.method == 'POST' and request.FILES['file']:
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.text = convert_pdf_to_txt_pages(resume.file)  # Convert PDF to text
            resume.save()  # Save the resume object with extracted text

            # Perform ATS compatibility check
            message, problematic_rows = check_ats_compatibility(resume.text)

            return render(request, 'uyumsorgula.html', {'resume': resume, 'message': message, 'problematic_rows': problematic_rows})

    else:
        form = ResumeUploadForm()

    return render(request, 'atsuyum.html', {'form': form})


def upload_and_process_resume(request):
    matching_meslek_sorted = None
    resume = None

    if request.method == 'POST' and request.FILES.get('file'):
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded resume
            resume = form.save(commit=False)
            resume.text = convert_pdf_to_txt_pages(resume.file)  # Convert PDF to text
            resume.save()  # Save the resume object with extracted text

            # Now, start matching bolum and yetenek from the resume text
            extracted_text = resume.text
            bolumum = []
            my_skills = []

            # Matching Bolum based on text (adjusting for lowercase comparison)
            for bolum_keyword in Bolum.objects.all():
                if bolum_keyword.bolum_adi.lower() in extracted_text.lower():
                    bolumum.append(bolum_keyword)

            # Matching Yetenek based on text (adjusting for lowercase comparison)
            for skill_keyword in Yetenek.objects.all():
                if skill_keyword.yetenek_adi.lower() in extracted_text.lower():
                    my_skills.append(skill_keyword)

            # Assume bolumum is the selected department and my_skills is a list of skills
            matching_meslek = Meslek.objects.filter(
                bolumler__in=bolumum, yetenekler__in=my_skills
            ).distinct()

            # Sort by matching score
            matching_meslek_sorted = matching_meslek.annotate(
                matching_score=Sum(
                    Case(
                        When(yetenekler__in=my_skills, then=Value(1)),
                        default=Value(0),
                        output_field=IntegerField(),
                    )
                ) * Subquery(
                    MeslekBolum.objects.filter(
                        meslek=OuterRef('pk'),
                        bolum__in=bolumum
                    ).values('yuzde')[:1]
                )
            ).order_by('-matching_score')

            # Pass the resume and matching_meslek_sorted to the template
            return render(request, 'oneri.html', {'resume': resume, 'matching_meslek': matching_meslek_sorted,"bolumum":bolumum,"yeteneklerim":my_skills})

    else:
        form = ResumeUploadForm()

    # If not POST or if POST fails, render the form to upload resume
    return render(request, 'meslekoner.html', {'form': form})



