from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)

#now we need to create the neccessary views, URLs and
#templates so we can display the info on the app

#first urls from config