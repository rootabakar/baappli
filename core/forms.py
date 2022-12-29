from django.forms import ModelForm

from core.models import AjoutAnimal, User


class ImageAdd(ModelForm):

    class Meta:
        model = AjoutAnimal
        fields = '__all__'
        exclude = ('proprietaire', )


class UserUpadate(ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]
