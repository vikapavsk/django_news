# Generated by Django 4.1.7 on 2023-03-16 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_category_subscribers_delete_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='postCategory',
            new_name='category',
        ),
    ]