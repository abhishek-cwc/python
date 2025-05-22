from django import forms

class ClassBaseForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)