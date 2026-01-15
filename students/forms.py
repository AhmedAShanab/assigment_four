from django import forms
from .models import Student
import re
from django.core.exceptions import ValidationError

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'university_id', 'national_id', 'mobile_number', 'address', 'dob', 'image']
        labels = {
            'name': 'Full Name',
            'university_id': 'University ID',
            'national_id': 'ID Number',
            'mobile_number': 'Mobile Number',
            'address': 'Address',
            'dob': 'Date of Birth',
            'image': 'Image',
        }
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not re.match(r'^[a-zA-Z\s]+$', name):
            raise ValidationError("Name must only contain letters and spaces (no numbers or symbols).")
        return name

    def clean_university_id(self):
        uid = str(self.cleaned_data.get('university_id'))
        if len(uid) != 9:
            raise ValidationError("University ID must be exactly 9 digits.")
        if uid[0] not in ['1', '2']:
            raise ValidationError("University ID must start with 1 or 2.")
        return uid

    def clean_national_id(self):
        nid = str(self.cleaned_data.get('national_id'))
        if len(nid) != 9:
            raise ValidationError("ID Number must be exactly 9 digits.")
        if nid[0] not in ['9', '8', '4']:
            raise ValidationError("ID Number must start with 9, 8, or 4.")
        return nid

    def clean_mobile_number(self):
        mobile = self.cleaned_data.get('mobile_number')
        if len(mobile) != 10:
            raise ValidationError("Mobile number must be exactly 10 digits.")
        if not (mobile.startswith('059') or mobile.startswith('056')):
            raise ValidationError("Mobile number must start with 059 or 056.")
        if not mobile.isdigit():
            raise ValidationError("Mobile number must contain digits only.")
        return mobile

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            extension = image.name.split('.')[-1].lower()
            if extension not in ['jpg', 'png', 'jpeg']:
                raise ValidationError("Image must be in jpg or png format only.")
        return image
