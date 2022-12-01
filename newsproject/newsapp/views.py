from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def moviesinfo(request):
    context={
        "head_msg":"Latest Information",
        "msg1":"Mahesh Babu is good actor",
        "msg2":" Telgu industry is best",
        "msg3":"Actors are good"
    }
    return render(request,'news.html',context)

def sportsinfo(request):
    return render(request,'news.html')

def politicsinfo(request):
    return render(request,'news.html')            