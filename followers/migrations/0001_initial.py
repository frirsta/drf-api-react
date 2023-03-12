# Generated by Django 3.2.18 on 2023-03-12 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('account_followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_followed', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_following', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
                'unique_together': {('owner', 'account_followed')},
            },
        ),
    ]
