# Generated by Django 4.0.4 on 2022-04-25 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_alter_moderatorinvitaion_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moderatorinvitaion',
            name='status',
            field=models.CharField(choices=[('INVITATION_STATUS_ACCETPED', 'INVITATION_STATUS_ACCETPED'), ('INVITATION_STATUS_DECLINED', 'INVITATION_STATUS_DECLINED'), ('INVITATION_STATUS_PENDING', 'INVITATION_STATUS_PENDING')], default='INVITATION_STATUS_PENDING', max_length=255),
        ),
    ]
