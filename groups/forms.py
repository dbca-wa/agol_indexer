from django import forms

class Group_AdminForm(forms.ModelForm):
	class Meta:
		widgets = {
			'name': forms.TextInput(attrs={'size': 80})
		}