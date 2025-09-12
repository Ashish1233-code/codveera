from django.shortcuts import render
from cod.models import Contact

# Create your views here.

def home(request):
    


    return render(request,'home.html')

def form(request):
    if request.method == "POST":
        Name = request.POST.get("Name")
        Email = request.POST.get("Email")
        Subject = request.POST.get("Subject")
        ashu=Contact(Name=Name,Email=Email,Subject=Subject)
        ashu.save()

    return render(request,'home.html')