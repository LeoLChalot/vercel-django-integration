# Generated by Django 5.1.2 on 2024-11-15 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0026_delete_uploadedimage'),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='custom_cover_image',
            field=models.ForeignKey(blank=True, help_text='Sélectionnez une image qui sera utilisée comme couverture pour cet article.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Cover Image'),
        ),
    ]
