from django.contrib import admin
from .models import Minigame73

# Register your models here.
@admin.register(Minigame73)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('username',)