from tkinter import Widget
from django import forms
from .models import stud_data1
from .models import stud_login

class student(forms.ModelForm):
    class Meta:
        model=stud_data1
        fields=['RollNo','Name','Email','Department','MobileNo']
        widgets={
            'RollNo':forms.NumberInput(attrs={'class':'form-control'}),
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Department':forms.TextInput(attrs={'class':'form-control'}),
            'MobileNo':forms.NumberInput(attrs={'class':'form-control'}),
        }

class student1(forms.ModelForm):
    class Meta:
        model=stud_login
        fields=['Email','Password']
        widgets={
            
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Password':forms.NumberInput(attrs={'class':'form-control'}),
        }        