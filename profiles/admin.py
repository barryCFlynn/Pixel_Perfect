from django.contrib import admin
from .models import NewsletterSignup

# Register your models here.

class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_signed_up')
    list_filter = ('date_signed_up',)
    search_fields = ('email',)


admin.site.register(NewsletterSignup, NewsletterSignupAdmin)