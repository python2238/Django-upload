from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.forms import userForm
def index(request):
    form = userForm()
    if request.method == 'POST':
        form = userForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1 style='color:green'>Data Saved Successfully</h1>")
    return render(request,'myapp/upload.html',{'form':form})
