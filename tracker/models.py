from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class StudyRecord(models.Model):
    STUDY_TYPES = [
        ('lecture', 'Lecture'),
        ('reading', 'Reading'),
        ('revision', 'Revision'),
        ('practice', 'Practice'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    study_type = models.CharField(max_length=50, choices=STUDY_TYPES)
    duration_mins = models.PositiveIntegerField()
    study_date = models.DateField()
    reflection_note = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.study_date})"