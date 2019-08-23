from django import forms
from .models import Receta


class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('titulo',)

    titulo = forms.CharField(
        label='Título',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Introducir Título'
        })
    )
        # descripcion = forms.CharField(
        #     label='Descripción',
        #     widget=forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter Description'
        #     })
        # )