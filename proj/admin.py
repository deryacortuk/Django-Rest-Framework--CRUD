from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    class Meta:
        model = Article
    fields = ["title", "slug","content"]

# Register your models here.
