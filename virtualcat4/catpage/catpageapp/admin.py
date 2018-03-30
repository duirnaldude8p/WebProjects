from django.contrib import admin
from .models import Cat
from .models import Account
from .models import Main
from .models import CurrentAccount
from .models import CatUniqueId

admin.site.register(Cat)
admin.site.register(Account)
admin.site.register(Main)
admin.site.register(CurrentAccount)
admin.site.register(CatUniqueId)


