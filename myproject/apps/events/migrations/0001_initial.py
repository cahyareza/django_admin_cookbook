# Generated by Django 3.2.12 on 2022-03-25 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('participating_heroes', models.ManyToManyField(to='entities.Hero')),
                ('participating_villains', models.ManyToManyField(to='entities.Villain')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('years_ago', models.PositiveIntegerField()),
                ('epic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.epic')),
            ],
        ),
        migrations.CreateModel(
            name='EventVillain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.villain')),
            ],
        ),
        migrations.CreateModel(
            name='EventHero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_primary', models.BooleanField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entities.hero')),
            ],
        ),
    ]
