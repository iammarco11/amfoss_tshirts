from django.contrib import admin

from tshirt.models import Cart, Tshirt, User, UserProfileInfo

admin.site.register(Tshirt)
admin.site.register(Cart)
admin.site.register(UserProfileInfo)
