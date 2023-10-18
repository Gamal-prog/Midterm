from django.views.generic import DetailView
from django.shortcuts import redirect

def list_contacts(request):
    return render(request, 'blog/list_contact.html', {'blog':'contact'})

class PostDetail(DetailView):
    model = UserContacts
    template_name = 'blog/detail_contacts.html'
    context_object_name = 'contact'