from django.shortcuts import render, redirect
from .models import Contact


def home(request):
    return render(request, 'index.html')


def add_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']

        Contact.objects.create(
            name=name,
            phone=phone,
            email=email,
            address=address
        )

        return redirect('view_contact')

    return redirect('home')


def view_contact(request):
    contacts = Contact.objects.all()

    return render(request, 'view.html', {
        'contacts': contacts
    })


def delete_contact(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()

    return redirect('view_contact')