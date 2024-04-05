from django.contrib import admin
from .models import  blog , ContactMesssage , item 

class  blogAdmin(admin.ModelAdmin):
    list_display = ('name' , 'writer','gamename','addtime')
    search_fields = ['name','gamename']
    list_filter = ['gamename']

admin.site.register(blog,blogAdmin)

class  contactAdmin(admin.ModelAdmin):
    list_display = ('title' , 'email','detial','sendtime')
    search_fields = ['title', 'email']


admin.site.register(ContactMesssage,contactAdmin)

class  itemAdmin(admin.ModelAdmin):
    list_display = ('name' , 'price','GameName','addtime')
    search_fields = ['name','GameName']
    list_filter = ['GameName']

admin.site.register(item,itemAdmin)



