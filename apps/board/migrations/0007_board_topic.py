# Generated by Django 4.0.4 on 2022-04-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_alter_moderatorinvitaion_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='topic',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
