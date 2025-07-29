from django import forms

class SiteForm(forms.Form):
    contract = forms.CharField(max_length=100)
    beneficiar = forms.CharField(max_length=100)
    locatie = forms.CharField(max_length=100)
    nr_comanda = forms.CharField(max_length=100)
