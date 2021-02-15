from django.contrib import admin
from .models import Article, Social, Message, AboutMe

# Register your models here.
admin.site.register(Article)
admin.site.register(Social)
admin.site.register(Message)
admin.site.register(AboutMe)
