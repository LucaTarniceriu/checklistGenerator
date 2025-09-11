from django import forms
import datetime

class SiteForm(forms.Form):
    contract = forms.CharField(max_length=100)
    beneficiar = forms.CharField(max_length=100)
    locatie = forms.CharField(max_length=100)
    nr_comanda = forms.CharField(max_length=100)
    oras = forms.CharField(max_length=50)

    formName = forms.CharField(max_length=100, widget=forms.HiddenInput(), initial='siteForm')

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
    formName = forms.CharField(max_length=100, widget=forms.HiddenInput(), initial='addDoorForm')


class UsaAntifocForm(forms.Form):
    nr_canate = forms.ChoiceField(
        choices=[("1", "1"), ("2", "2")],
        widget=forms.RadioSelect
    )
    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField()
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100, required=False)
    formName = forms.CharField(max_length=100, widget=forms.HiddenInput(), initial='doorForm')
    id = forms.CharField(widget=forms.HiddenInput(), initial="empty")
    data_inspectiei = forms.CharField(initial=str(datetime.date.today().strftime("%d/%m/%Y")), required=True)
    tehnician = forms.CharField(max_length=30)
     

    lipsuri = forms.BooleanField(initial=False, required=False)
    informare = forms.BooleanField(initial=False, required=False)


class UsaAutomataForm(forms.Form):
    nr_canate = forms.ChoiceField(
        choices=[("1", "1"), ("2", "2")],
        widget=forms.RadioSelect
    )
    model = forms.ChoiceField(
        choices=[("1", "GEZE"), ("2", "DORMA")],
        widget=forms.RadioSelect
    )
    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField()
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100, required=False)
    formName = forms.CharField(max_length=100, widget=forms.HiddenInput(), initial='doorForm')
    id = forms.CharField(widget=forms.HiddenInput(), initial="empty")
    data_inspectiei = forms.CharField(initial=str(datetime.date.today().strftime("%d/%m/%Y")), required=True)
    tehnician = forms.CharField(max_length=30)
     

    lipsuri = forms.BooleanField(initial=False, required=False)
    informare = forms.BooleanField(initial=False, required=False)

class BurdufForm(forms.Form):

    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField()
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100, required=False)
    formName = forms.CharField(max_length=100, widget=forms.HiddenInput(), initial='doorForm')
    id = forms.CharField(widget=forms.HiddenInput(), initial="empty")
    data_inspectiei = forms.CharField(initial=str(datetime.date.today().strftime("%d/%m/%Y")), required=True)
    tehnician = forms.CharField(max_length=30)
     

    lipsuri = forms.BooleanField(initial=False, required=False)
    informare = forms.BooleanField(initial=False, required=False)

class UsaMetalicaForm(forms.Form):

    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField()
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100, required=False)
    formName = forms.CharField(max_length=100, widget=forms.HiddenInput(), initial='doorForm')
    id = forms.CharField(widget=forms.HiddenInput(), initial="empty")
    data_inspectiei = forms.CharField(initial=str(datetime.date.today().strftime("%d/%m/%Y")), required=True)
    tehnician = forms.CharField(max_length=30)
     

    lipsuri = forms.BooleanField(initial=False, required=False)
    informare = forms.BooleanField(initial=False, required=False)

class RampaForm(forms.Form):

    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField()
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100, required=False)
    formName = forms.CharField(max_length=100, widget=forms.HiddenInput(), initial='doorForm')
    id = forms.CharField(widget=forms.HiddenInput(), initial="empty")
    data_inspectiei = forms.CharField(initial=str(datetime.date.today().strftime("%d/%m/%Y")), required=True)
    tehnician = forms.CharField(max_length=30)
     

    lipsuri = forms.BooleanField(initial=False, required=False)
    informare = forms.BooleanField(initial=False, required=False)

class UsaRapidaForm(forms.Form):

    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField()
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100, required=False)
    formName = forms.CharField(max_length=100, widget=forms.HiddenInput(), initial='doorForm')
    id = forms.CharField(widget=forms.HiddenInput(), initial="empty")
    data_inspectiei = forms.CharField(initial=str(datetime.date.today().strftime("%d/%m/%Y")), required=True)
    tehnician = forms.CharField(max_length=30)
     

    lipsuri = forms.BooleanField(initial=False, required=False)
    informare = forms.BooleanField(initial=False, required=False)

class UsaSectionalaForm(forms.Form):

    an_fabricatie = forms.IntegerField()
    nr = forms.IntegerField()
    dimensiuni = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'0000x0000mm'}))
    tip = forms.CharField(max_length=100, required=False)
    formName = forms.CharField(max_length=100, widget=forms.HiddenInput(), initial='doorForm')
    id = forms.CharField(widget=forms.HiddenInput(), initial="empty")
    data_inspectiei = forms.CharField(initial=str(datetime.date.today().strftime("%d/%m/%Y")), required=True)
    tehnician = forms.CharField(max_length=30)
     

    lipsuri = forms.BooleanField(initial=False, required=False)
    informare = forms.BooleanField(initial=False, required=False)