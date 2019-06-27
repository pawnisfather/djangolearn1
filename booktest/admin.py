from django.contrib import admin

from .models import *


class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 2


# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'b_title', 'b_pub_date']
    list_filter = ['b_pub_date']
    search_fields = ['b_title']
    list_per_page = 5
    fieldsets = [
        ('base', {'fields': ['b_title']}),
        ('more', {'fields': ['b_pub_date']}),

    ]
    inlines = [HeroInfoInline, ]


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)
