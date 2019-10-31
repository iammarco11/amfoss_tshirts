from django.contrib import admin

from tshirt.models import Tshirt, User, UserProfileInfo

admin.site.register(Tshirt)
admin.site.register(UserProfileInfo)
