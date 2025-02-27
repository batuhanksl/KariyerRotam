from django.db import models

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')  # Stores the uploaded resume file
    text = models.TextField()  # Stores the extracted text from the resume

    def __str__(self):
        return f"Resume {self.id}"
