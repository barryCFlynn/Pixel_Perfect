from django.contrib import admin
from .models import NewsletterSignup

# Register your models here.


class NewsletterSignupAdmin(admin.ModelAdmin):
    """
    Admin configuration for the NewsletterSignup model.

    This admin class specifies how the NewsletterSignup model is displayed
    and filtered in the Django admin interface.

    Attributes:
    - list_display: Specifies the fields to display in the list view of
      NewsletterSignup instances.
    - list_filter: Specifies the fields to use for filtering in the admin
      interface based on date_signed_up.
    - search_fields: Specifies the fields to search for in the admin
      interface based on email.
    """
    list_display = ('email', 'date_signed_up')
    list_filter = ('date_signed_up',)
    search_fields = ('email',)


admin.site.register(NewsletterSignup, NewsletterSignupAdmin)
