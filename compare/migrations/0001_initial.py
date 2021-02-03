# Generated by Django 3.1.6 on 2021-02-03 02:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='password', blank=True)),
                ('document', models.FileField(upload_to='uploads/', verbose_name='document')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='uploaded_at')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
