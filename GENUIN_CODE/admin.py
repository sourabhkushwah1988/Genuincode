from django.contrib import admin
# 🔁 Update names below if models are renamed
from .models import Ragister, Contact, CustomUser, LoginAttempt

# 🔁 Change names if renamed
admin.site.register(Ragister)
admin.site.register(Contact)
admin.site.register(CustomUser)
admin.site.register(LoginAttempt)
