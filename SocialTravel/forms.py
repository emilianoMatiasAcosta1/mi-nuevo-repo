from django import forms
from SocialTravel.models import Post , Futbol

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class FutbolForm(forms.ModelForm):
    class Meta:
        model = Futbol
        fields = '__all__'        