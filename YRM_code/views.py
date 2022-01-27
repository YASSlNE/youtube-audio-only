from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ClientForm
import pafy
# Create your views here.
def index(request):
    c=ClientForm()
    # k=AuthorForm()
    if(request.method=='POST'):
        form=ClientForm(request.POST)
        if(form.is_valid()):
            url=form.cleaned_data['yurl']
            k=pafy.new(url)
            aud=k.getbestaudio()
            streamurl=aud.url
        # print("mqlskdjfqsdmlk")
            return render(request,'index.html',context={'form':c,'streamurl':streamurl,'title':k.title})
    return render(request,'index.html',context={'form':c})