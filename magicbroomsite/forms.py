from django import forms
from datetime import datetime
from django.utils import timezone
from . models import QuotationRequests, HouseInformation, SquareFeet
from localflavor.us.forms import USZipCodeField
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from . choices import *

# Set up Phone regex
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '1234445511'. Up to 15 digits allowed.")
class RequestQuotationForm(forms.ModelForm):
    """
    Form for requesting quotations
    """
    last_name = forms.CharField(
        label = "Enter Your Last Name",
        help_text = "Enter Your name here",
        widget = forms.TextInput(
            attrs = {'class': 'form-control',
            }
        ),
        error_messages = {
            'required': 'Your Last Name is required'
        }
    )
    #
    first_name = forms.CharField(
        label = "Enter Your First Name",
        help_text = "Enter Your First Name here",
        widget = forms.TextInput(
            attrs = {'class': 'form-control',
            }
        ),
        error_messages = {
            'required': 'Your First Name is required'
        }
    )
    #
    email = forms.CharField(
        label = "Enter Your Email Address",
        help_text = "Enter Your Email Address",
        widget = forms.EmailInput(
            attrs = {'class': 'form-control',
            }
        ),
        error_messages = {
            'required': 'Your Email is required'
        }
    )
    #
    telephone = forms.CharField(
        label = "Enter Your Telephone Number",
        validators = [phone_regex],
        help_text = "Enter Your Telephone",
        widget = forms.TextInput(
            attrs = {'class': 'form-control',
                'type':'tel',
            }
        ),
        error_messages = {
            'required': 'Your Telephone Number is required'
        }
    )

    address = forms.CharField(
        label = "Street Address",
        help_text = "",
        widget = forms.TextInput(
            attrs = {'class': 'form-control',
            }
        ),
        error_messages = {
            'required': 'Your Street Address is required'
        }
    )
    #
    apt_suite = forms.CharField(
        label = "Apt/Suite Number",
        help_text = "",
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'placeholder': '',
            }
        ),
        error_messages = {
            'required': 'Your Apt/Suite number is required'
        }
    )

    city = forms.CharField(
        label = "City",
        help_text = "",
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'placeholder': '',
            }
        ),
        error_messages = {
            'required': 'Your City location is required'
        }
    )
    state = forms.CharField(
        label = "State",
        required = False,
        help_text = "",
        widget = forms.Select(
            choices = state_choices,
            attrs = {'class': 'form-control', 'placeholder': '',
            }
        ),
        error_messages = {
            # 'required': 'Your State is required'
        }
    )

    referrer = forms.CharField(
        label = 'How did you hear about us?',
        initial = 'Please Select',
        required = True,
        widget = forms.Select(
            choices = referrer_choices,
            attrs = {'class':'form-control required'}
        )

    )
    # referrer = forms.Select()

    zip_code = USZipCodeField(
        widget = forms.TextInput(
            attrs = {'class': 'form-control',
            }
        ),
        error_messages = {
            'invalid': 'Please enter a valid zip code'
        }
    )
    #
    rate_home = forms.IntegerField(
        label = "Condition of your home (1-10) 10 = cleanest",
        validators=[MaxValueValidator(10), MinValueValidator(1)],
        widget = forms.NumberInput(
            attrs = {'class': 'form-control', 'placeholder': '',
            }
        ),
        error_messages = {
            'required': 'The condition of your home is required'
        }
    )
    #
    check_if_carpet = forms.BooleanField(
        label = "Check here if you have carpet",
        help_text = "",
        required = False,
        widget = forms.CheckboxInput(
            attrs = {'class': 'form-control',
            }
        ),
        error_messages = {

        }
    )

    home_info_boost = forms.CharField(
        label = "Number of Bedrooms and Bathrooms",
        # default = None,
        widget = forms.Select(
            choices = house_choices,
            attrs = {'class': 'form-control',
            },
        ),
    )

    square_feet = forms.CharField(
        label = "Square Footage",
        help_text = "",
        widget = forms.Select(
            choices = square_footage_choices,
            attrs = {'class': 'form-control', 'placeholder': '',
            }
        ),
        error_messages = {
            'required': 'Your Square Footage is required'
        }
    )

    booking_date = forms.DateField(
        # input_formats=settings.DATE_INPUT_FORMATS,
        label = "Please Select Booking Date",
        # initial = datetime.datetime.now(),
        help_text = "",
        widget = forms.TextInput(
            attrs = {'class': 'form-control', 'placeholder': ''
            }
        ),
        error_messages = {
        }
    )
    booking_time = forms.TimeField(
        label = "Please Select Booking Time",
        # initial = datetime.now,
        help_text = "",
        widget = forms.TextInput(
            attrs = {'class': 'form-control required', 'placeholder': ''
            }
        ),
        error_messages = {
        }
    )

    class Meta:
        model = QuotationRequests
        fields =  ['last_name', 'first_name', 'email','telephone', 'address',
            'apt_suite', 'city', 'state', 'zip_code', 'home_info_boost', 'service_type', 'extra_service', 'square_feet', 'rate_home',
             'check_if_carpet', 'booking_date', 'booking_time', 'referrer']
