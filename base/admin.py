from django.contrib import admin

# Register your models here.
from base.models import Topic
from base.models import Topic, Entry


admin.site.register(Topic)
admin.site.register(Entry)