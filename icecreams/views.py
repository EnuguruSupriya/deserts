from django.shortcuts import render
def func(request,no,cost):
    return render(request,'index.html',{'result':obj})

def func2(required):
    res=menu.objects.all()
    if request.method=="POST":
        sno=request.POST.get('sno')
        new_flovour=request.POST.get('fav')
        result=Menu.ojects.get(id=sno)
        result.flovour=new_flovour
        result.save()
        res=Menu.object.all()
        return render(request,'update.html',{"res"=result})