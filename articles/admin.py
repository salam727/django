from django.contrib import admin
from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug','status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(models.Category,CategoryAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','publish','status','category_to_str')
    list_filter = ('publish','status')
    search_fields = ('title','description')
    prepopulated_fields = {'slug':('title',)}

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.Category.all()])

admin.site.register(models.articles,ArticleAdmin)
