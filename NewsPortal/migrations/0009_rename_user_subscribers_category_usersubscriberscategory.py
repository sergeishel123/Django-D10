# Generated by Django 4.0.3 on 2022-08-23 16:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NewsPortal', '0008_rename_category_id_user_subscribers_category_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_subscribers_Category',
            new_name='Usersubscriberscategory',
        ),
    ]