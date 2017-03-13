from django import forms

class WebService_AdminForm(forms.ModelForm):
	class Meta:
		widgets = {
			'actual_url': forms.TextInput(attrs={'size': 80}),
			'alias_url': forms.TextInput(attrs={'size': 80})
		}