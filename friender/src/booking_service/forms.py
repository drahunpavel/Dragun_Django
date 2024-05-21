from django import forms
from .validators import validate_yahoo_email
from .models import Guest


class CheckRoomForm(forms.Form):
    room_number = forms.IntegerField()
    guest = forms.CharField(max_length=50, initial='Alice Cooper')
    hotel = forms.CharField(max_length=50, initial='Hotel_Hotel')
    # details = forms.CharField(max_length=200, initial='Default Details')
    check_in_date = forms.DateTimeField()
    check_out_date = forms.DateTimeField()

class AddGuestForm(forms.ModelForm):

    email = forms.EmailField(validators=[validate_yahoo_email])
    
    class Meta:
        model = Guest
        fields: list[str] = ['first_name', 'last_name', 'age', 'sex', 'email', 'phone']

