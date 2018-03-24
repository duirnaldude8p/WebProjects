from django.contrib import admin
from .models import Cat
from .models import Account
from .models import Main

admin.site.register(Cat)
admin.site.register(Account)
admin.site.register(Main)
