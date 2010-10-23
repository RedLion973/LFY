# -*- coding: utf-8 -*-

from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

STATES = (
    (u'1', u'Publié'),
    (u'2', u'Non publié'),
    (u'3', u'Home'),
    (u'4', u'Corbeille')
)

class Tag(models.Model):
    # Attributes
    word = models.SlugField(u'Mot', max_length=255)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
   
    # Methods
    def __unicode__(self):
        return u'%s' % (self.word)

class Article(models.Model):
    # Attributes
    title = models.CharField(u'Titre', max_length=255)
    content = models.TextField(u'Content')
    author = models.ForeignKey(User, verbose_name=u'Auteur')
    state = models.CharField(u'Etat', max_length=1, choices=STATES)
    tags = generic.GenericRelation(Tag)
    created_at = models.DateTimeField(u'Crée le', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(u'Modifié le', auto_now=True, editable=False)
