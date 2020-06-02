from django import forms

class codigo(forms.Form):
    codigoText = forms.CharField(widget=forms.Textarea)