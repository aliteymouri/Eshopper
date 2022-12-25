from django import forms

from Contact_us.models import Message


class ContactForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput({'class': "form-control", "placeholder": "email"}),
    )
    subject = forms.CharField(
        widget=forms.TextInput({'class': "form-control", "placeholder": "subject"}),
    )
    text = forms.CharField(required=True,
                           widget=forms.Textarea({'class': "form-control", "placeholder": "message", }),
                           )

    class Meta:
        model = Message
        fields = "__all__"
