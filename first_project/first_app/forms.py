from django import forms
from django.core import validators
from first_app.models import Student

class MyFormName(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("name needs to start with z")

class MyAdvanceForm(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    department = forms.CharField(validators=[validators.MaxLengthValidator(3)])
    mobile = forms.IntegerField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your emai again')

    def clean(self):
        all_cleaned_data = super().clean()
        mail = all_cleaned_data['email']
        vmail = all_cleaned_data['verify_email']
        if mail != vmail:
            raise forms.ValidationError("Make sure emais match")

class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = '__all__'
