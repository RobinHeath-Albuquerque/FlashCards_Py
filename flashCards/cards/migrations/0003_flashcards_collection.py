# Generated by Django 3.1.7 on 2021-05-04 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20210504_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcards',
            name='collection',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cards.collection'),
        ),
    ]
