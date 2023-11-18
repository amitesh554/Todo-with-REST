from django.shortcuts import render,redirect
from .models import Task

def home(request):
    if(request.method=='POST'):
        task=request.POST.get('form1')
        message=Task(Name=task)
        message.save()
    context=Task.objects.all()
    return render(request,'index.html',{"context":context})

    
def delete_task(request,pk):
    att=Task.objects.get(id=pk)
    att.delete()
    return redirect('/')
    
def finish_task(request,pk):
    att=Task.objects.get(id=pk)
    att.status='Finished'
    att.save()
    return redirect('/')
    
    
