from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import uuid


# Create your models here.
class Article(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    
    STATUS_CHOICES = (
        (ACTIVE, 'Активна'),
        (DRAFT, 'Чернетка'),
    )
    
    
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='articles', verbose_name='Автор', default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='articles', default=1, verbose_name='Категория')
    tags = models.ManyToManyField('Tag', related_name='articles', verbose_name='Теги')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(verbose_name='URL', unique=True)
    content_preview = models.TextField(verbose_name='Превью статьи')
    content = RichTextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=DRAFT, verbose_name='Статус')
    image = models.ImageField(upload_to='articles/', verbose_name='Зображення', blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        self.slug = str(uuid.uuid4())
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
    
    
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва Категорії', unique=True)
    slug = models.SlugField(verbose_name='URL', default='', unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва тегу', unique=True)
    slug = models.SlugField(verbose_name='URL', default='', unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255, verbose_name='Ім\'я')
    email = models.EmailField(verbose_name='Email')
    content = models.TextField(verbose_name='Коментар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')

    def __str__(self):
        return f'{self.article.title} - {self.content}'
    
    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['-created_at']