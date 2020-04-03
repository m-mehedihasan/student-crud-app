from django import forms
from app.models import Student

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
		widgets = {
		'roll': forms.TextInput(attrs={'type':'number','placeholder':'Your roll no','min':'1', 'class':'form-control'}),
		'first_name': forms.TextInput(attrs={'placeholder':'Your first name', 'class':'form-control'}),
		'last_name': forms.TextInput(attrs={'placeholder':'Your last name', 'class':'form-control'}),
		'Class': forms.TextInput(attrs={'placeholder':'Which class do you read?', 'class':'form-control'}),
		'email': forms.TextInput(attrs={'type':'email' ,'placeholder':'Your E-mail address', 'class': 'form-control'}),
		}


