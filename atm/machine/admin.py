from django.contrib import admin

# Register your models here.
from . models import User, transactions

admin.site.register(User)