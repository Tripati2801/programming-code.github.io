from django.shortcuts import render
from studentapp import forms

# Create your views here.
def studentinputview(request):
    form=forms.StudentForm()
    my_dict={'form':form}
    return render(request,'input.html',context=my_dict)