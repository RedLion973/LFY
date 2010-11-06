# -*- coding: utf-8 -*-

import datetime
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.comments.moderation import CommentModerator, moderator
from django.template.defaultfilters import slugify

TODAY = datetime.datetime.today()

class Tag(models.Model):
    # Attributes
    word = models.CharField(u'Mot', max_length=255)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')
   
    # Methods
    def __unicode__(self):
        return u'%s' % (self.word)

    def save(self, *args, **kwargs):
        self.word = slugify(self.word)
        super(Tag, self).save(*args, **kwargs)

    # Meta
    class Meta:
        (verbose_name, verbose_name_plural) = (u'Tag', u'Tags')

class Category(models.Model):
    # Attributes
    name = models.CharField(u'Nom de la Catégorie', max_length=255, unique=True)
    parent_category = models.ForeignKey('self', verbose_name=u'Catégorie-mère', null=True, blank=True)

    # Methods
    def __unicode__(self):
        return u'%s' % (self.name)

    # Meta
    class Meta:
        (verbose_name, verbose_name_plural) = (u'Catégorie', u'Catégories')

class Article(models.Model):
    # Attributes
    title = models.CharField(u'Titre', max_length=255)
    content = models.TextField(u'Contenu')
    author = models.ForeignKey(User, verbose_name=u'Auteur')
    category = models.ForeignKey(Category, verbose_name=u'Catégorie')
    tags = generic.GenericRelation(Tag)
    published = models.BooleanField(u'Publié', default=0)
    publication_date = models.DateTimeField(u'Date de Publicaton', editable=False, blank=True, null=True)
    on_home = models.BooleanField(u'Sur la Home Page', default=0)
    enable_comments = models.BooleanField(u'Activer les Commentaires')
    created_at = models.DateTimeField(u'Créé le', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(u'Modifié le', auto_now=True, editable=False)

    # Methods
    def __unicode__(self):
        return u'%s par %s' % (self.title, self.author)

    def is_published(self):
        return self.published == 1 and True or False

    def is_on_home(self):
        return self.on_home == 1 and True or False

    def save(self, *args, **kwargs):
        if self.is_published:
            self.publication_date = TODAY
        else:
            self.publication_date = None
        super(Article, self).save(*args, **kwargs)

    # Meta
    class Meta:
        (verbose_name, verbose_name_plural) = (u'Article', u'Articles')

class Page(models.Model):
    # Attributes
    title = models.CharField(u'Titre', max_length=255)
    content = models.TextField(u'Contenu')
    published = models.BooleanField(u'Publié', default=0)
    publication_date = models.DateTimeField(u'Date de Publicaton', editable=False, blank=True, null=True)
    created_at = models.DateTimeField(u'Créée le', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(u'Modifiée le', auto_now=True, editable=False)

    # Methods
    def __unicode__(self):
        return u'%s' % (self.title)

    def is_published(self):
        return self.published == 1 and True or False

    def save(self, *args, **kwargs):
        if self.is_published:
            self.publication_date = TODAY
        else:
            self.publication_date = None
        super(Page, self).save(*args, **kwargs)

    # Meta
    class Meta:
        (verbose_name, verbose_name_plural) = (u'Page', u'Pages')

class ArticleModerator(CommentModerator):
    email_notification = True
    enable_field = 'enable_comments'

moderator.register(Article, ArticleModerator)

