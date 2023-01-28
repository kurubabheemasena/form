from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def abc(request):
    if request.method=='POST':
        un=request.POST['n']
        pw=request.POST['p']
        print(un)
        print(pw)
        return HttpResponse('my name is bheema')

    return render(request,'form.html')
