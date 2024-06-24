from django import forms
from .validators import validate_yahoo_email
from .models import Guest, HotelComment, Profile
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# кастомная форма для проверки забронированной комнаты
class CheckRoomForm(forms.Form):
    room_number = forms.IntegerField()
    guest = forms.CharField(max_length=50, initial='Alice Cooper')
    hotel = forms.CharField(max_length=50, initial='Hilton Amsterdam Airport Schiphol')
    check_in_date = forms.DateTimeField()
    check_out_date = forms.DateTimeField()

# Форма AddGuestForm наследуется от модели Guest
class AddGuestForm(forms.ModelForm):

    email = forms.EmailField(validators=[validate_yahoo_email])

    class Meta:
        model = Guest
        fields: list[str] = ['first_name', 'last_name', 'age', 'sex', 'email', 'phone']

# ProfileForm, для заполнения данных гостя при добавлении, наследуется от модели Profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo', 'id_card', 'serial_number']

# Кастомная форма AddGuestForm, не наследуется от модели
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


# форма AddCommentForm связана с моделью HotelComment
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = HotelComment
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



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields: list[str] = ['username', 'email', 'password1', 'password2']


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields: list[str] = ['username', 'password']