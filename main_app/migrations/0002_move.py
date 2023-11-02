# Generated by Django 4.2.6 on 2023-11-02 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('move_name', models.CharField()),
                ('move_type', models.CharField(choices=[('BUG', 'Bug'), ('DRK', 'Dark'), ('DRG', 'Dragon'), ('ELC', 'Electric'), ('FRY', 'Fairy'), ('FGT', 'Fighting'), ('FIR', 'Fire'), ('FLY', 'Flying'), ('GHS', 'Ghost'), ('GRS', 'Grass'), ('GRD', 'Ground'), ('ICE', 'Ice'), ('NML', 'Normal'), ('PSN', 'Poison'), ('PSY', 'Psychic'), ('RCK', 'Rock'), ('STL', 'Steel'), ('WTR', 'Water')], max_length=3)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pokemon')),
            ],
        ),
    ]