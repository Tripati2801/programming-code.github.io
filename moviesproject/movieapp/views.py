from django.shortcuts import render
from movieapp.forms import MovieForm
from movieapp.models import Movie
# Create your views here.
def index(request):
    return render(request,'index.html')
def addmovie(request):
    form=MovieForm()
    if request.method=='POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'addmovie.html',{'form':form})
def listmovie(request):
    movies_list=Movie.objects.all().order_by('-rating')
    return render(request,'listmovie.html',{'movies_list':movies_list})                