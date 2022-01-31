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
            if('=' in url):
                getid=url.split('=')[1]
            else:
                getid=url.split('/')[3]
            mp3=f'<iframe src="https://www.yt-download.org/api/button/mp3/{getid}" width="100%" height="100px" scrolling="no" style="border:none;"></iframe>'
        # print("mqlskdjfqsdmlk")
            return render(request,'index.html',context={'form':c,'streamurl':streamurl,'title':k.title, 'mp3download':mp3})
    return render(request,'index.html',context={'form':c})