from django import forms
from django.forms import widgets
from app2.tasks import send_review_email_task

class ReviewForm(forms.Form):
    name = forms.CharField(
        label='Firstname', max_length=50, min_length=4, widget=forms.TextInput(
            attrs={
                'class': 'form-control-mb3', 'placeholder': 'Firtsname', 'id':'form-firstname'
            }
        )
    )
    email = forms.EmailField(
         max_length=250, widget=forms.TextInput(
            attrs={
                'class': 'form-control-mb3', 'placeholder': 'E-mail', 'id':'form-email'
            }   
         )
    )
    review = forms.CharField(
        label='Review', widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': '5'
            }
        )
    )

    def send_email(self):
        send_review_email_task.delay(
        self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['review'])