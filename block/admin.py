from django.contrib import admin
from block.models import Author


# Register your models here.

# admin.site.register(Author)

class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','title','description')
    
    
admin.site.register(Author,AuthorAdmin)



