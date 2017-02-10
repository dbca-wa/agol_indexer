from django import forms

class CreateGroupForm(forms.Form):
	name = forms.CharField(max_length=30)
	description = forms.TextInput()

class CreateWebmapItemsForm(forms.Form):
	name = forms.CharField(max_length=30)
	description = forms.TextInput()