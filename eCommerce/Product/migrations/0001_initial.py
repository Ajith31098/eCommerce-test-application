# Generated by Django 4.1 on 2023-02-09 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=25)),
                ('product_code', models.CharField(max_length=100)),
                ('product_dimension', models.JSONField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('stock', models.PositiveIntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='Product.category')),
                ('employee', models.ForeignKey(blank=True, null=True,
                 on_delete=django.db.models.deletion.SET_NULL, to='Seller.employee')),
                ('seller', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='Seller.company')),
            ],
            options={
                'ordering': ['product_code'],
                'unique_together': {('product_code', 'employee')},
            },
        ),
    ]
