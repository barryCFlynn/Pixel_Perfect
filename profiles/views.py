from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import UserProfile, NewsletterSignup
from .forms import UserProfileForm, NewsletterSignupForm

from orders.models import Order


@login_required
def profile(request):
    """
    Display the user's profile.

    Retrieves the user's profile based on the request's user object. Handles
    POST requests to update the profile using UserProfileForm. Renders the
    'profiles/profile.html' template with the form and user's orders.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: Rendered template with form and orders context.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    Display a past order confirmation.

    Retrieves the order with the given order_number using get_object_or_404.
    Displays an informational message about the order. Renders the
    'orders/order_success.html' template with the order details.

    Parameters:
    request (HttpRequest): The HTTP request object.
    order_number (str): The unique order number to retrieve.

    Returns:
    HttpResponse: Rendered template with order context.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'orders/order_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def newsletter_signup(request):
    """
    Handle newsletter signup form submission.

    Displays and processes the newsletter signup form. Validates the form
    data and saves the subscription if valid. Sends a confirmation email
    upon successful signup. Renders 'profiles/newsletter_signup.html' with
    the form.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: Rendered template with form context or redirect to 'home'.
    """
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if NewsletterSignup.objects.filter(email=email).exists():
                messages.error(request, 'This email is already subscribed.')
            else:
                form.save()
                messages.success(request,
                    'You have successfully signed up for the newsletter.')
                subject = render_to_string(
                    'emails/newsletter_signup_subject.txt'
                ).strip()
                message = render_to_string(
                    'emails/newsletter_signup_body.txt',
                    {'email': email}
                )
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False
                )
                return redirect('home')
    else:
        form = NewsletterSignupForm()

    return render(request, 'profiles/newsletter_signup.html', {'form': form})
