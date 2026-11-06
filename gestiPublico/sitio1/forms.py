from django import forms

from sitio1.models.properties import properties


class PropertyForm(forms.ModelForm):
    class Meta:
        model = properties
        fields = ['code', 'Address', 'Context', 'people_Id']
        labels = {
            'code': 'Código',
            'Address': 'Dirección',
            'Context': 'Contexto',
            'people_Id': 'Persona asociada (opcional)',
        }
        widgets = {
            'code': forms.TextInput(attrs={'placeholder': 'Ingrese el código'}),
            'Address': forms.TextInput(attrs={'placeholder': 'Ingrese la dirección'}),
            'Context': forms.Textarea(attrs={'placeholder': 'Ingrese el contexto', 'rows': 4}),
        }
