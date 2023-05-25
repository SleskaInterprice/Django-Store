from django.contrib import admin

from users.models import Basket, EmailVerification, User

admin.site.register(User)
admin.site.register(Basket)
admin.site.register(EmailVerification)
