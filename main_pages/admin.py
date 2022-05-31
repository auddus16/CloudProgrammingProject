from django.contrib import admin

from .models import Menu, Category, Order


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )} # slug 필드에서는 name 값을 그대로 넣어주세요. 뒤에 튜플 형태로 넣은 거 유의

class MenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

# Register your models here.
admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
