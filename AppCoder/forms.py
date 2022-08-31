from django import forms


class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    comision = forms.IntegerField()
