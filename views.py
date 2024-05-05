from django.shortcuts import render
from app.models import Person
def first(request):
    return render(request,"index.html")
def submit(request):
    myper =Person()
    if request.method=="POST":   
        name=request.POST.get('Name')
        email=request.POST.get("email")
        passw =request.POST.get("pass")
        if name=="" and email=="" and passw=="":
            return render(request,"index.html",{"page":"none"})
        else:
             myper.Name=name
             myper.Email=email
             myper.Password=passw
             myper.save()
             return render(request,"index.html")
def delete(request):
    if request.method=="POST":
        delete_val=request.POST.get('delname')
        if Person.objects.filter(Name=delete_val).exists():
                persontodel=Person.objects.get(Name=delete_val)
                persontodel.delete()
                return render(request,"index.html")
            
def modify(request):
    if request.method=="POST":
        newmail=request.POST.get('newemail')
        newpass=request.POST.get('newpassword')
        
        data_you_want_to_mod=request.POST.get('moddata')
        if Person.objects.filter(Name=data_you_want_to_mod).exists():
            moddata=Person.objects.get(Name=data_you_want_to_mod)
            moddata.Email=newmail
            moddata.Password=newpass
            moddata.save()
            return render(request,'index.html')
          
def showall(request):
    if request.method=="POST":
        allperson =Person.objects.all()
    
    return render(request,"index.html",{"showpeople":allperson})                 