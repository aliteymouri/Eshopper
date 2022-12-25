from django.shortcuts import redirect
from django.views.generic import FormView
from Contact_us.forms import ContactForm


class ContactUs(FormView):
    template_name = 'contact_us/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        return redirect('Home:home')
