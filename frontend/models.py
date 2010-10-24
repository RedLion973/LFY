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

    # Meta
    class Meta:
        (verbose_name, verbose_name_plural) = (u'Tag', u'Tags')

class Category(models.Model):
    # Attributes
    category = models.CharField(u'Catégorie', max_length=255, unique=True)

    # Methods
    def __unicode__(self):
        return u'%s' % (self.category)

    # Meta
    class Meta:
        (verbose_name, verbose_name_plural) = (u'Catégorie', u'Catégories')

class Article(models.Model):
    # Attributes
    title = models.CharField(u'Titre', max_length=255)
    content = models.TextField(u'Contenu')
    author = models.ForeignKey(User, verbose_name=u'Auteur')
    category = models.ForeignKey(Category, verbose_name=u'Catégorie')
    state = models.CharField(u'Etat', max_length=1, choices=STATES)
    tags = generic.GenericRelation(Tag)
    publication_date = models.DateTimeField(u'Date de Publicaton', blank=True, null=True)
    created_at = models.DateTimeField(u'Créé le', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(u'Modifié le', auto_now=True, editable=False)

    # Methods
    def __unicode__(self):
        return u'%s par %s' % (self.title, self.author)

    def state_handler(self, state):
        if state == u'1':
            self.publication_date = datetime.datetime.now()
	if state == u'2' or state == u'4':
            self.publication_date = Null
        self.state = state
	self.save()

    # Meta
    class Meta:
        (verbose_name, verbose_name_plural) = (u'Article', u'Articles')

class Comment(models.Model):
    # Attributes
    article = models.ForeignKey(Article)
    content = models.TextField(u'Contenu')
    author = models.ForeignKey(User, verbose_name=u'Auteur')
    state = models.CharField(u'Etat', max_length=1, choices=STATES)
    created_at = models.DateTimeField(u'Créé le', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(u'Modifié le', auto_now=True, editable=False)

    # Methods
    def __unicode__(self):
        return u'Commentaire de %s sur "%s"' % (self.author, self.article.title)

    def state_handler(self, state):
        self.state = state
        self.save()

    # Meta
    class Meta:
        (verbose_name, verbose_name_plural) = (u'Commentaire', u'Commentaires')

class Page(models.Model):
    # Attributes
    title = models.CharField(u'Titre', max_length=255)
    content = models.TextField(u'Contenu')
    state = models.CharField(u'Etat', max_length=1, choices=STATES)
    created_at = models.DateTimeField(u'Créée le', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(u'Modifiée le', auto_now=True, editable=False)

    # Methods
    def __unicode__(self):
        return u'%s' % (self.title)

    def state_handler(self, state):
        self.state = state
        self.save()

    # Meta
    class Meta:
        (verbose_name, verbose_name_plural) = (u'Page', u'Pages')
