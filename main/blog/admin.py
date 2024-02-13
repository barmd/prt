from django.contrib import admin
from blog.models import Info, Expertise , Links , Education , Skills , Portfolio , Sertificate , Contact

@admin.register(Info)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id', 'name'] 

@admin.register(Expertise)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id', 'name'] 

@admin.register(Education)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id', 'name'] 

@admin.register(Skills)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id', 'name'] 

@admin.register(Links)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id', 'name'] 


@admin.register(Sertificate)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id', 'name'] 

@admin.register(Portfolio)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id', 'name']  


@admin.register(Contact)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    list_display_links = ['id', 'name']  
       
       
    


