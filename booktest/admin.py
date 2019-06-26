from django.contrib import admin

from .models import *


# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'b_title', 'b_pub_date']
    list_filter = ['b_pub_date']
    search_fields = ['b_title']
    fieldsets = [
        ('base', {'fields': ['b_title']}),
        ('more', {'fields': ['b_pub_date']}),

    ]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
