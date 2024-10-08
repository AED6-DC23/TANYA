# Generated by Django 4.2.15 on 2024-08-24 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratingAuthor', models.IntegerField(default=0)),
                ('authorUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryType', models.CharField(choices=[('TK', 'Танк'), ('AR', 'Хил'), ('DD', 'ДД'), ('TC', 'Торговец'), ('GD', 'Гилдмастер'), ('CG', 'Квестгивер'), ('KZ', 'Кузнец'), ('KJ', 'Кожевник'), ('ZV', 'Зельевар'), ('MZ', 'Мастер Заклинаний')], default='TC', max_length=2, verbose_name='Чей ты воин')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Дата статьи')),
                ('title', models.CharField(max_length=128, verbose_name='Поиск по названию статьи')),
                ('text', models.TextField()),
                ('rating', models.SmallIntegerField(default=0)),
                ('files', models.FileField(blank=True, upload_to='uploads/', verbose_name='Загрузи файл')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsportal.author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateComm', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsportal.post')),
            ],
        ),
    ]
