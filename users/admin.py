from django.contrib import admin

from users.models import User, Basket, EmailVerification


admin.site.register(User)
admin.site.register(Basket)
admin.site.register(EmailVerification)
