# Generated by Django 4.2.2 on 2024-05-12 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=30)),
                ('rating', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='feedback_images/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pets.product')),
            ],
        ),
    ]