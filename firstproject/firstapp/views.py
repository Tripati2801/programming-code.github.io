from django.shortcuts import render

# Create your views here.
def home(request):
    marks=[123,33,44,55,66]
    context={
        'marks':marks,
        'name':'Tripati'
    }
    return render(request,'index.html',context)

