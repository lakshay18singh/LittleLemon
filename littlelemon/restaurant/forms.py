from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Menu, Booking

class DateInput(forms.DateTimeInput):
    input_type = 'datetime'

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = '__all__'

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('Name', 'No_of_guests', 'BookingDate')
        widgets = {
            'BookingDate': forms.widgets.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *arg, **kwargs):
        self._User = kwargs.pop('user')
        super(BookingForm, self).__init__(*arg, **kwargs)

    def save(self, commit=True):
        inst = super(BookingForm, self).save(commit=False)
        inst.User = self._User
        if commit:
            inst.save()
            self.save_m2m()
        
        return inst
        

class altBooking(forms.Form):

    Id = forms.IntegerField(max_value=10)
    Name = forms.CharField(max_length=100)
    BookingDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control datetimepicker-input'}))
