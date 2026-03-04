from django import forms
from .models import StudyRecord

class StudyRecordForm(forms.ModelForm):
    class Meta:
        model = StudyRecord
        fields = ['title', 'study_type', 'duration_mins', 'study_date', 'reflection_note']
        widgets = {
            'study_date': forms.DateInput(attrs={'type': 'date'}),
            'duration_mins': forms.NumberInput(attrs={'min': 1}),
            'reflection_note': forms.Textarea(attrs={'rows': 3}),
        }

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError('Passwords do not match.')
        return cleaned_data