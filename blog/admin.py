from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    pass
    # fields = "__all__"

admin.site.register(Post, PostAdmin)
