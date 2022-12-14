from django.shortcuts import render,redirect
from .forms import ResumeForm
from .models import Resume
from django.views import View
# Create your views here.
class HomeView(View):
    def get(self,request):
        form = ResumeForm()
        candidate = Resume.objects.all()
        return render(request,"myapp/index.html",{'form':form,'candidate':candidate})
    def post(self,request):
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,"myapp/index.html",{'form':form})

class CandidateView(View):
    def get(self,request,pk):
        candidate =Resume.objects.get(pk=pk)
        return render(request,"myapp/candidate.html",{'candidate':candidate})



