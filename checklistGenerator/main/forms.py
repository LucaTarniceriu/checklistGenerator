from django import forms

class SiteForm(forms.Form):
    contract = forms.CharField(max_length=100)
    beneficiar = forms.CharField(max_length=100)
    locatie = forms.CharField(max_length=100)
    nr_comanda = forms.CharField(max_length=100)



DoorChoices = (
    ("1", "Antifoc"),
    ("2", "Automata"),
    ("3", "Burduf"),
    ("4", "Metalica"),
    ("5", "Rampa"),
    ("6", "Rapida"),
    ("7", "Sectionala")
)
class AddDoorForm(forms.Form):
    tip_usa = forms.ChoiceField(choices=DoorChoices)


class UsaAntifocForm(forms.Form):
    nr_canate = forms.ChoiceField(
        choices=[("1", "1"), ("2", "2")],
        widget=forms.RadioSelect
    )
    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100)

class UsaAutomataForm(forms.Form):
    nr_canate = forms.ChoiceField(
        choices=[("1", "1"), ("2", "2")],
        widget=forms.RadioSelect
    )
    model = forms.RadioSelect(choices=(("1", "GEZE"), ("2", "DORMA")))
    model = forms.ChoiceField(
        choices=[("1", "GEZE"), ("2", "DORMA")],
        widget=forms.RadioSelect
    )
    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100)

class BurdufForm(forms.Form):

    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100)

class UsaMetalicaForm(forms.Form):

    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100)

class RampaForm(forms.Form):

    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100)

class UsaRapidaForm(forms.Form):

    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100)

class UsaSectionalaForm(forms.Form):

    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100)