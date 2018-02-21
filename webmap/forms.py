from django import forms


class Webmap_AdminForm(forms.ModelForm):
    class Meta:
        widgets = {
            'name': forms.TextInput(attrs={'size': 50}),
            'url': forms.TextInput(attrs={'size': 80}),
            'purpose': forms.TextInput(attrs={'size': 80})
        }


class Webmap_App_AdminForm(forms.ModelForm):
    class Meta:
        widgets = {
            'name': forms.TextInput(attrs={'size': 50}),
            'url': forms.TextInput(attrs={'size': 80}),
            'purpose': forms.TextInput(attrs={'size': 80})
        }
