from django.shortcuts import render
from world.models import World
# Create your views here.
def world(request):
    return  render(request,'world/index.html')
    post = World.objects.all()
    context={
        'post':post
    }

    return  render(request,'world/index.html',context=context)
  