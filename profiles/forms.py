from django import forms
from .models import UserProfile, NewsletterSignup


class UserProfileForm(forms.ModelForm):
    """
    Form for editing user profile information.

    This form customizes field widgets, placeholders, and classes for the
    UserProfile model fields. It excludes the 'user' field from direct user
    modification.

    Attributes:
    - Meta: Specifies the model (UserProfile) and excludes the 'user' field.

    Methods:
    - __init__: Initializes the form with custom placeholders, autofocus,
      and classes for fields, and removes auto-generated labels.
    """
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on the first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False


class NewsletterSignupForm(forms.ModelForm):
    """
    Form for subscribing to the newsletter.

    This form allows users to enter their email address to subscribe to
    the newsletter.

    Attributes:
    - Meta: Specifies the model (NewsletterSignup) and includes the 'email' field.

    """
    class Meta:
        model = NewsletterSignup
        fields = ['email']
