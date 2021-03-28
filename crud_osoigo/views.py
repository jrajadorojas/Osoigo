# Django
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

# Models
from crud_osoigo.models import Contact

# Forms
from crud_osoigo.form import ContactForm


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'contact_list'
    
    def get_queryset(self):
        return Contact.objects.all()

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact-detail.html'


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ContactForm()

    return render(request,'create.html',{'form': form})

def edit(request, pk, template_name='edit.html'):
    contact = Contact.objects.filter(id=pk).values_list('firstName', 
            'lastName','email','phone','address','description')[0]
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, 
        {
            'form':form,
            'contact': contact,
        }
    )

def delete(request, pk, template_name='confirm_delete.html'):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object':contact})