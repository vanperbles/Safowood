# Generated by Django 2.2.10 on 2020-02-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GuestUser',
            new_name='GuestEmail',
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='Phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fullname',
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
