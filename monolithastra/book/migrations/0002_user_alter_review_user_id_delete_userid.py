# Generated by Django 4.0.5 on 2022-06-22 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=25)),
                ('date_of_birth', models.DateField()),
                ('reviews', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.review')),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.user'),
        ),
        migrations.DeleteModel(
            name='Userid',
        ),
    ]
