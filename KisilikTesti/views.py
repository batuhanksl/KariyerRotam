from django.shortcuts import render
from .models import Sorular,Kisilik

def sorular(request):
    questions = Sorular.objects.all()
    description = Kisilik.objects.all()

    question_map = []

    # Prepare the questions and track factors
    for question in questions:
        question_text = question.soruTR if question.soruTR else question.soruEN
        question_factor = -1 if question.factor == 'negative' else 1
        
        # Add question data to the map
        question_map.append({
            "id": question.id,
            "text": question_text,
            "factor": question_factor,
            "category": question.kategori
        })

    if request.method == 'POST':
        my_data = {}

        # Get all the answers from the form
        for question in question_map:
            question_id = question['id']
            answer = request.POST.get(str(question_id))  # Use question_id as the name in the form
            if answer:
                my_data[question_id] = int(answer)  # Convert answer to integer

        # Adjust answers based on factor (negative or positive)
        for question in question_map:
            question_id = question['id']
            factor = question['factor']
            if question_id in my_data:
                answer = my_data[question_id]
                if factor == -1:  # For negative factors, flip the answer
                    my_data[question_id] = 6 - answer

        # Calculate category scores using question_map's category
        category_scores = {}
        for question in question_map:
            category = question['category']
            question_id = question['id']

            if question_id in my_data:
                if category not in category_scores:
                    category_scores[category] = 0  # Initialize category score if not present
                category_scores[category] += my_data[question_id]

        description_map = {}
        for item in description:
            for category, score in category_scores.items():
                if item == category:
                    if score < item.alt_sinir:
                        description_map[category] = item.dusuk_aciklama
                    elif item.alt_sinir <= score <= item.ust_sinir:
                        description_map[category] = item.ortalama_aciklama
                    else:
                        description_map[category] = item.yuksek_aciklama

        return render(request, 'kisiliktestisonuc.html', {'answers': my_data, 'category_scores': category_scores, 'description': description_map})

    return render(request, 'kisiliktestisorular.html', {'questions': question_map})
