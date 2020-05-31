# Generated by Django 3.0.4 on 2020-05-31 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(default='default.jpeg', upload_to='product_pics')),
                ('description', models.TextField()),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
