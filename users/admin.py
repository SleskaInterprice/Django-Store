from django.contrib import admin

from users.models import EmailVerification, User

admin.site.register(User)
admin.site.register(EmailVerification)
