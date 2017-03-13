from django import forms

class AGOL_AdminForm(forms.ModelForm):
	class Meta:
		widgets = {
			'name': forms.TextInput(attrs={'size': 50}),
			'external_layer_url': forms.TextInput(attrs={'size': 80}),
			'comments': forms.TextInput(attrs={'size': 80})
		}