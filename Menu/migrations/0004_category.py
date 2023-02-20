# Generated by Django 3.2.3 on 2022-10-16 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0003_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('starters', 'Starters'), ('mains', 'Mains'), ('beverages', 'Beverages'), ('desserts', 'Desserts')], max_length=10)),
            ],
        ),
    ]