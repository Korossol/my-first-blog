#from django.shortcuts import render

# Create your views here.
#def home_list(request):
   # return render(request, 'home/home_list.html', {})



from django.shortcuts import render

# Create your views here.
def home_list(request):
    return render(request, 'home/home_list.html', {})