from django.shortcuts import render
from jobapp.models import hydjob,chenjob,bangjob


# Create your views here.
def home(request):
    return render(request,'home.html')

def Hydjob(request):
    job_list=hydjob.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'hydjob.html',context=my_dict)  

def Chenjob(request):
    chen_list=chenjob.objects.all()
    my_dict={'chen_list':chen_list}
    return render(request,'chenjob.html',context=my_dict)


def Bangjob(request):
    bang_list=bangjob.objects.all()
    my_dict={'bang_list':bang_list}
    return render(request,'bangjob.html',context=my_dict)    
    
