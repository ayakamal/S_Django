# Generated by Django 3.2.6 on 2021-09-05 02:43

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[500, 300], upload_to='books'),
        ),
    ]
