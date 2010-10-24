# -*- coding: utf-8 -*-

from django.contrib import admin
from LFY.frontend.models import *
from django import forms

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title'], 'classes': ['wide']}),
        (None, {'fields': ['content', 'author'], 'classes': ['wide', 'extrapretty']}),
        ('Options', {'fields': ['category','state'], 'classes': ['wide']}),
    ]
    change_form_template = 'admin/frontend/change_form.html'

admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Page)
