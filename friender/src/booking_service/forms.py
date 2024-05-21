from django import forms
from .validators import validate_yahoo_email
from .models import Guest, HotelComment


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


class AddCommentForm(forms.ModelForm):
    # guest = forms.CharField(label='Your Name', max_length=100)

    class Meta:
        model = HotelComment
        # fields: list[str] = ['guest', 'text']
        fields: list[str] = ['text']
        label: dict[str, str] = {
            'text': 'Message'
        }
        widgets: dict[str, forms.Textarea] = {
            'text': forms.Textarea(attrs={'cols': 40, 'rows': 4}),
        }
        # field_order: list[str] = ['guest', 'text'] # упорядочивание полей в форме

    # вариант через инициализацию
    # def __init__(self, *args, **kwargs):
    #     super(AddCommentForm, self).__init__(*args, **kwargs)
    #     self.fields['text'].widget = forms.Textarea(attrs={'rows': 4, 'cols': 40})