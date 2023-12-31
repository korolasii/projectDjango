# Generated by Django 4.2.2 on 2023-08-16 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField(default=0, verbose_name='Сума замовлення')),
                ('first_name', models.CharField(max_length=255, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=255, verbose_name='Прізвище')),
                ('email', models.EmailField(max_length=254, verbose_name='Електронна пошта')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефон')),
                ('address', models.CharField(max_length=255, verbose_name='Адреса')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='Коментарі')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('status', models.CharField(blank=True, choices=[('in_progress', 'В обробці'), ('waiting_for_payment', 'Очікується оплата'), ('in_delivery', 'Відправлено'), ('completed', 'Завершено'), ('canceled', 'Скасовано')], default='in_progress', max_length=100, null=True, verbose_name='Статус')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Ціна')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Кількість')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='order.order', verbose_name='Замовлення')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.games', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар замовлення',
                'verbose_name_plural': 'Товари замовлення',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.games', verbose_name='Товар')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Кількість')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.games', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
        ),
    ]
