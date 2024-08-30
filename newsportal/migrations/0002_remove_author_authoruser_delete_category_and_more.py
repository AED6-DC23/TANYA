# Generated by Django 4.2.15 on 2024-08-27 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsportal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='authorUser',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='categoryType',
        ),
        migrations.RemoveField(
            model_name='post',
            name='dateCreation',
        ),
        migrations.RemoveField(
            model_name='post',
            name='rating',
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='dateMsg',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='nameCat',
            field=models.CharField(choices=[('TK', 'Танк'), ('AR', 'Хил'), ('DD', 'ДД'), ('TC', 'Торговец'), ('GD', 'Гилдмастер'), ('CG', 'Квестгивер'), ('KZ', 'Кузнец'), ('KJ', 'Кожевник'), ('ZV', 'Зельевар'), ('MZ', 'Мастер Заклинаний')], default='Tanks', max_length=64, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='files',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=128),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
