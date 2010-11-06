# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.contenttypes import generic
from LFY.frontend.models import *

class TagInline(generic.GenericTabularInline):
    model = Tag
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title'], 'classes': ['wide']}),
        (None, {'fields': ['content', 'author'], 'classes': ['wide', 'extrapretty']}),
        ('Options', {'fields': ['category','published','on_home'], 'classes': ['wide']}),
    ]
    inlines = [
        TagInline,
    ]
    change_form_template = 'admin/frontend/change_form.html'

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Page)
