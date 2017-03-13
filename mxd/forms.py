from django import forms

class MXD_AdminForm(forms.ModelForm):
	class Meta:
		widgets = {
			'name': forms.TextInput(attrs={'size': 60}),
			'path': forms.TextInput(attrs={'size': 80})
		}