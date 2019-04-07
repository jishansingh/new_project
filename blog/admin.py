from django.contrib import admin
from .models import blog,url_post,topic,product,called,visited
# Register your models here.

admin.site.register(blog)
admin.site.register(url_post)
admin.site.register(topic)
admin.site.register(product)
admin.site.register(called)
admin.site.register(visited)