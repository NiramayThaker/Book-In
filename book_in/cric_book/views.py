from django.shortcuts import render, HttpResponse


# Create your views here.
def cric_home(request):
	return render(request, "cric_book/cric_home.html")
