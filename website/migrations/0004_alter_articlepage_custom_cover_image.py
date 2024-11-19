# Generated by Django 5.1.2 on 2024-11-15 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_media', '0002_initial'),
        ('website', '0003_alter_articlepage_custom_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='custom_cover_image',
            field=models.ForeignKey(blank=True, help_text='Choisissez une image de couverture pour cet article.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='custom_media.customimage', verbose_name='Cover Image'),
        ),
    ]