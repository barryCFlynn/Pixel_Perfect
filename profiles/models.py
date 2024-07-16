from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for storing additional information related to users.

    This model extends the default User model provided by Django to include 
    fields for maintaining default delivery information and order history.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        help_text='The user associated with this profile.'
    )
    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text='The default phone number of the user.'
    )
    default_street_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        help_text='The first line of the user\'s street address.'
    )
    default_street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        help_text='The second line of the user\'s street address (optional).'
    )
    default_town_or_city = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        help_text='The town or city of the user\'s address.'
    )
    default_county = models.CharField(
        max_length=80,
        null=True,
        blank=True,
        help_text='The county or region of the user\'s address.'
    )
    default_postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        help_text='The postcode or ZIP code of the user\'s address.'
    )
    default_country = CountryField(
        blank_label='Country',
        null=True,
        blank=True,
        help_text='The country of the user\'s address.'
    )
    
    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile associated with the User instance.

    If a new User instance is created, a corresponding UserProfile instance
    is also created. For existing users, the UserProfile instance is simply
    saved.

    Parameters:
    sender (class): The model class that sends the signal (User).
    instance (User): The instance of the User model being saved.
    created (bool): Boolean indicating whether the instance was created.
    **kwargs: Additional keyword arguments.

    Returns:
    None
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()


class NewsletterSignup(models.Model):
    """
    Model representing an email address signed up for a newsletter.

    Attributes:
    - email (EmailField): The email address of the subscriber (unique).
    - date_signed_up (DateTimeField): The date and time when the email was
    signed up.

    Methods:
    - __str__: Returns the email address as the string representation of the
    model instance.
    """
    email = models.EmailField(unique=True)
    date_signed_up = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
