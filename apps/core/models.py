from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# Create your models here.


class Heros(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва Персонажу', unique=True)
    slug = models.SlugField(verbose_name='URL', default='', unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажі'
        
class Cells(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва Комірки', unique=True)
    slug = models.SlugField(verbose_name='URL', default='', unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Комірка'
        verbose_name_plural = 'Комірки'
        
class Raritys(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва Комірки', unique=True)
    slug = models.SlugField(verbose_name='URL', default='', unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Рідкісність'
        verbose_name_plural = 'Рідкісність'
        
 
 
class Games(models.Model):

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='game', verbose_name='Автор', default=1)
    name_item = models.CharField(max_length=255, verbose_name='Назва товару')
    heros = models.ForeignKey(Heros, related_name='game', on_delete=models.SET_NULL, null=True, blank=True)
    raritys = models.ForeignKey(Raritys, related_name='game', on_delete=models.SET_NULL, null=True, blank=True)
    cells = models.ForeignKey(Cells, related_name='game', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(verbose_name='Кількість', default=0)
    price = models.DecimalField(verbose_name='Ціна', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    slug = models.SlugField(verbose_name='URL', unique=True)
    image = models.ImageField(upload_to='articles/', verbose_name='Зображення', blank=True, null=True)
    
    def __str__(self):
        return f'{self.name_item}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.price}-{self.name_item}-{self.quantity}")
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ['-created_at']
 
    
class Comment(models.Model):
    article = models.ForeignKey(Games, on_delete=models.CASCADE, related_name='comments')
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
        

        