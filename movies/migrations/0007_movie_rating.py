# Generated by Django 4.2.6 on 2023-10-31 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_remove_moviecomment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=3, null=True),
        ),
    ]
