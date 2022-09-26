from django import forms
from manager.models import UserReservations


class UserReservationsForm(forms.ModelForm):

    name = forms.CharField(
        max_length=100,
        min_length=2,
        widget=forms.TextInput(attrs={
            'type': 'text',
            'name': 'name',
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'Your Name',
            'data-rule': 'minlen:4',
            'data-msg': 'Please enter at least 4 chars',
        })
    )

    class Meta:
        model = UserReservations
        fields = ('name', 'email', 'phone', 'message')
