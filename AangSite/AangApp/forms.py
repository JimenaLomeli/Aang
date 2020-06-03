from django import forms


class codigo(forms.Form):
    code = open('input.txt', 'r')
    content = code.read()
    code.close()

    codigoText = forms.CharField(widget=forms.Textarea, initial=content)
    codigoText.widget.attrs.update(initial="sadas")
