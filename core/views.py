from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'core/base.html')

def User(request):
    username=request.GET['username']
    print(username)
    return render(request, 'core/user.html',{'name':username})