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
    """
        Método que crea a un nuevo contacto en el sistema.
    Args:   
        request (Request): Request del sistema para esta función
    Returns:
        [template]: Se visualiza la pantalla inicial del sistema.
                Para ello se hace una redirección a index.html
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ContactForm()

    return render(request,'create.html',{'form': form})

def edit(request, pk, template_name='edit.html'):
    """
        Método que edita a un contacto existente en el sistema.
    Args:
        request ([type]): Request del sistema para esta función
        pk (int): identificador único para el contacto.
        template_name (str, optional): [description]. Defaults to 'edit.html'.

    Returns:
        [type]: [description]
    """
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
    """
        Método que borra a un contacto del sistema.
        Esto lo hace por la primary key del contacto en cuestión.

    Args:
        request (Request): [description]
        pk (int): Identificador del contacto
        template_name (str, optional): [description]. Defaults to 'confirm_delete.html'.

    Returns:
        [template]: Se visualiza la pantalla inicial del sistema.
                Para ello se hace una redirección a index.html
    """
    contact = get_object_or_404(Contact, pk=pk)
    if request.method=='POST':
        contact.delete()
        return redirect('index')
    return render(request, template_name, {'object':contact})