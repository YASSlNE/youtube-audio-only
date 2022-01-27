from django import forms
from django.forms import ModelForm
class ClientForm(forms.Form):
    yurl=forms.CharField(label='Youtube video URL ',max_length=100,widget=forms.TextInput(attrs={'class':'input-group-text btncls'}))
# class AuthorForm(forms.Form):
#     class Meta:
#         # model = Author
#         fields = ['name', 'title', 'birth_date']