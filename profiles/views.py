from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, NewsletterSignup
from .forms import UserProfileForm, NewsletterSignupForm

from orders.models import Order

@ login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
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
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventoryitems') 
    else:
        form = NewsletterSignupForm()
    return render(request, 'profiles/newsletter_signup.html', {'form': form})

def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if NewsletterSignup.objects.filter(email=email).exists():
                messages.error(request, 'This email is already subscribed.')
            else:
                form.save()
                messages.success(request, 'You have successfully signed up for the newsletter.')
                return redirect('home')
    else:
        form = NewsletterSignupForm()
    return render(request, 'profiles/newsletter_signup.html', {'form': form})