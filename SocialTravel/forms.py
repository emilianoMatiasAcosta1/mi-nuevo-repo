from django import forms
from SocialTravel.models import Post , Futbol, Escuela

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class FutbolForm(forms.ModelForm):
    class Meta:
        model = Futbol
        fields = '__all__'        


class EscuelaForm(forms.ModelForm):
    class Meta:
        model = Escuela 
        fields = '__all__'                