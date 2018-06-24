from django.contrib import admin
from .models import Cat
from .models import Profile
from .models import Main
from .models import Comment


admin.site.register(Cat)
admin.site.register(Profile)
admin.site.register(Main)
admin.site.register(Comment)

# Register your models here.
