from django.contrib import admin
from .models import * 
# Register your models here.


admin.site.register(User)
admin.site.register(BloodExpert) 
admin.site.register(Lab)
admin.site.register(TimeService)