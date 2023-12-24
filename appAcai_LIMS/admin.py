from django.contrib import admin
from . models import Library

# Register your models here.


class LibraryAdmin(admin.ModelAdmin):
  list_display = ("Publisher", "Author", "Title","PageCount", "Category", "ShelfLocation","PublishedDate", "IsInstock", "DateCheckedOut",)

admin.site.register(Library, LibraryAdmin)

