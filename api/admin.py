from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(FacebookRoom)
admin.site.register(AmazonRoom)
admin.site.register(GoogleRoom)
admin.site.register(NetflixRoom)
admin.site.register(HuluRoom)