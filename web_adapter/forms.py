from django import forms

class WebAdapter_AdminForm(forms.ModelForm):
	class Meta:
		widgets = {
			'machine_name': forms.TextInput(attrs={'size': 25}),
			'enviroment': forms.TextInput(attrs={'size': 5}),
			'alias': forms.TextInput(attrs={'size': 40})
		}