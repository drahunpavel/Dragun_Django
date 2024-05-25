from django import forms
from .validators import validate_yahoo_email
from .models import Guest, HotelComment
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.formfields import PhoneNumberField

class CheckRoomForm(forms.Form):
    room_number = forms.IntegerField()
    guest = forms.CharField(max_length=50, initial='Alice Cooper')
    hotel = forms.CharField(max_length=50, initial='Hotel_Hotel')
    check_in_date = forms.DateTimeField()
    check_out_date = forms.DateTimeField()

#* Форма AddGuestForm наследуется от модели
class AddGuestForm(forms.ModelForm):

    email = forms.EmailField(validators=[validate_yahoo_email])

    class Meta:
        model = Guest
        fields: list[str] = ['first_name', 'last_name', 'age', 'sex', 'email', 'phone']

#* Форма AddGuestForm не наследуется от модели
class AddGuestForm2(forms.Form):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField(validators=[
        MaxValueValidator(90),
        MinValueValidator(18)
    ])
    sex = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    email = forms.EmailField(validators=[validate_yahoo_email])
    phone = PhoneNumberField()




#* форма AddCommentForm связана с моделью HotelComment
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


