from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from main.models import *

# Create your views here.

def index(request):
	works = Work.objects.all().order_by('?')[:6]
	context = {"works": works}
	return render(request, "main/index.html", context)


def about(request):
	context = {}
	return render(request, "main/about.html", {})

def work(request):
	works = Work.objects.all().order_by('-pub_date')
	context = {"works": works}
	return render(request, "main/work.html", context)


def team(request):
	teams = Team.objects.all().order_by('-pub_date')
	context = {"teams": teams}
	return render(request, "main/team.html", context)



def contact(request):

	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')

		contact_model = ContactModel.objects.create(name=name, email=email, phone=phone, message=message)
		contact_model.save()

		response = "We will get back to you shortly!"

		context = {"response": response}
		return render(request, "main/contact.html", context)

	else:

	
		response = ""

		context = {"response": response}
		return render(request, "main/contact.html", context)




def DMSignUpView(request):

	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		about = request.POST.get('about')
		why = request.POST.get('why')
		address = request.POST.get('address')

		dm = DigitalMarketer.objects.create(name=name, email=email, phone=phone, about=about, address=address, why=why)
		dm.save()

		response = "Data Submitted!, Await our response(Within 24hrs)"

		context = {"response": response}
		return render(request, "main/dm_sign_up.html", context)

	else:

	
		response = ""

		context = {"response": response}
		return render(request, "main/dm_sign_up.html", context)



