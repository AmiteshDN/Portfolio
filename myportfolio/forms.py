from django import forms

class HireMeForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', required=True)
    ROLE_CHOICES = [('student', 'Student'), ('professional', 'Professional'),]
    role = forms.ChoiceField(label='You are a', choices=ROLE_CHOICES, widget=forms.RadioSelect, required=True)
    SERVICE_TYPE_CHOICES = [('assignment', 'Assignment'), ('project','Project'), ('tutor', 'Tutor')]
    service_type = forms.ChoiceField(label='Hiring me for', choices=SERVICE_TYPE_CHOICES, widget=forms.RadioSelect, required=True)
    duration = forms.ChoiceField(label='Duration in weeks', choices=[(i, str(i)) for i in range(1,5)]+['6+', '6+'],
                                 required=False)
    description = forms.CharField(label='Assigment/Project Description', widget=forms.Textarea)
    reference = forms.CharField(label='How did you hear about me?', required=False)
    
