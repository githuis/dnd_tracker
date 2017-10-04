# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a character name (fx. Legolas Greenleaf', max_length=100)),
                ('level', models.IntegerField()),
                ('frags', models.IntegerField(default=0)),
                ('alive', models.BooleanField(default=True)),
                ('player_super_class', models.CharField(choices=[('BB', 'Barbarian'), ('BA', 'Bard'), ('CL', 'Cleric'), ('DR', 'Druid'), ('FI', 'Fighter'), ('MO', 'Monk'), ('PA', 'Paladin'), ('RA', 'Ranger'), ('RO', 'Rogue'), ('SO', 'Sorcerer'), ('WA', 'Warlock'), ('WI', 'Wizard')], help_text='Select the main class of your character.', max_length=2)),
                ('player_sub_class', models.CharField(help_text='Enter the subclass of your character', max_length=50)),
            ],
        ),
    ]
