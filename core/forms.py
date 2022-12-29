from django.forms import ModelForm

from core.models import AjoutAnimal


class ImageAdd(ModelForm):

    class Meta:
        model = AjoutAnimal
        fields = '__all__'
        exclude = ('proprietaire', )