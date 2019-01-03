from django.shortcuts import render
from hello.models import Hello
# Create your views here.

#GET hello/
def hello(request):
    #ORM==>Object Relation MApping 
    # Python Code <=>SQL
    post = Hello.objects.all()
    context={
        'post':post
    }

    return  render(request,'hello/index.html',context=context)
  