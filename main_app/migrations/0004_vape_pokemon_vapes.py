# Generated by Django 4.2.6 on 2023-11-03 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_move_move_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('flavor', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pokemon',
            name='vapes',
            field=models.ManyToManyField(to='main_app.vape'),
        ),
    ]