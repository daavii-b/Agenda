# Generated by Django 4.0 on 2021-12-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0004_contato_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m'),
        ),
    ]