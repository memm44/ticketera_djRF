from django.contrib import admin
from .models import Issue, Responsible, Issuer

# Register your models here.
admin.site.register(Responsible)
admin.site.register(Issue)
admin.site.register(Issuer)