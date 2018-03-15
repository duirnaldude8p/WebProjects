from django.contrib import admin
from .models import Cat
from .models import Cat_Comment
from .models import Comment
from .models import Account
from .models import Main
from .models import User

admin.site.register(User)
admin.site.register(Cat)
admin.site.register(Cat_Comment)
admin.site.register(Comment)
admin.site.register(Account)
admin.site.register(Main)


