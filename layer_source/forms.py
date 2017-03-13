from django import forms

class LayerSource_AdminForm(forms.ModelForm):
	class Meta:
		widgets = {
			'name': forms.TextInput(attrs={'size': 60}),
			'location': forms.TextInput(attrs={'size': 40}),
			'owner': forms.TextInput(attrs={'size': 40})
		}