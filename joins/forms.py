from django import forms

class CreateGroupForm(forms.Form):
	name = forms.CharField(max_length=30)
	description = forms.CharField(max_length=100)

class CreateWebmapItemsForm(forms.Form):
	name = forms.CharField(max_length=30)
	description = forms.CharField(max_length=100)

class CreateMxdForm(forms.Form):
	name = forms.CharField(max_length=60)
	path = forms.CharField(max_length=500)
	description = forms.CharField(max_length=255)
	client = forms.CharField(max_length=5)
	created_by = forms.CharField(max_length=5)
	created_on = forms.CharField()
	