# Generated by Django 2.2.13 on 2020-08-01 04:07

import bestiary.models.base
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('herders', '0014_storage_conversion_stone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtifactInstance',
            fields=[
                ('slot', models.IntegerField(choices=[(1, 'Element'), (2, 'Archetype')])),
                ('element', models.CharField(blank=True, choices=[('pure', 'Pure'), ('fire', 'Fire'), ('wind', 'Wind'), ('water', 'Water'), ('light', 'Light'), ('dark', 'Dark')], max_length=6, null=True)),
                ('archetype', models.CharField(blank=True, choices=[('none', 'None'), ('attack', 'Attack'), ('hp', 'HP'), ('support', 'Support'), ('defense', 'Defense'), ('material', 'Material')], max_length=10, null=True)),
                ('quality', models.IntegerField(choices=[(0, 'Normal'), (1, 'Magic'), (2, 'Rare'), (3, 'Hero'), (4, 'Legend')], default=0)),
                ('level', models.IntegerField()),
                ('original_quality', models.IntegerField(choices=[(0, 'Normal'), (1, 'Magic'), (2, 'Rare'), (3, 'Hero'), (4, 'Legend')])),
                ('main_stat', models.IntegerField(choices=[(1, 'HP'), (3, 'ATK'), (5, 'DEF')])),
                ('main_stat_value', models.IntegerField()),
                ('effects', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, choices=[(1, 'ATK+ Proportional to Lost HP'), (2, 'DEF+ Proportional to Lost HP'), (3, 'SPD+ Proportional to Lost HP'), (4, 'SPD Under Inability'), (5, 'ATK Increased'), (6, 'DEF Increased'), (7, 'SPD Increased'), (8, 'CRI Rate Increased'), (9, 'Counterattack Damage Increased'), (10, 'Cooperative Attack Damage Increased'), (11, 'Bomb Damage Increased'), (12, 'Reflected Damage Increased'), (13, 'Crushing Hit Damage Increased'), (14, 'Damage Received Under Inability Decreased'), (15, 'Crit Damage Received Decreased'), (16, 'Life Drain Increased'), (17, 'HP When Revived Increased'), (18, 'ATB When Revived Increased'), (19, 'Damage Increased By % of HP'), (20, 'Damage Increased By % of ATK'), (21, 'Damage Increased By % of DEF'), (22, 'Damage Increased By % of SPD'), (23, 'Damage To Fire Increased'), (24, 'Damage To Water Increased'), (25, 'Damage To Wind Increased'), (26, 'Damage To Light Increased'), (27, 'Damage To Dark Increased'), (28, 'Damage From Fire Decreased'), (29, 'Damage From Water Decreased'), (30, 'Damage From Wind Decreased'), (31, 'Damage From Light Decreased'), (32, 'Damage From Dark Decreased'), (33, 'Skill 1 CRI Damage Increased'), (34, 'Skill 2 CRI Damage Increased'), (35, 'Skill 3 CRI Damage Increased'), (36, 'Skill 4 CRI Damage Increased'), (37, 'Skill 1 Recovery Increased'), (38, 'Skill 2 Recovery Increased'), (39, 'Skill 3 Recovery Increased'), (40, 'Skill 1 Accuracy Increased'), (41, 'Skill 1 Accuracy Increased'), (42, 'Skill 1 Accuracy Increased')], null=True), default=list, help_text='Bonus effect type', size=4)),
                ('effects_value', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), default=list, help_text='Bonus value of this effect', size=4)),
                ('effects_upgrade_count', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), default=list, help_text='Number of upgrades this effect received when leveling artifact', size=4)),
                ('effects_reroll_count', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), default=list, help_text='Number times this upgrades was rerolled with conversion stone', size=4)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('com2us_id', models.BigIntegerField(blank=True, null=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='herders.MonsterInstance')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herders.Summoner')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, bestiary.models.base.Quality, bestiary.models.base.Archetype, bestiary.models.base.Elements, bestiary.models.base.Stats, bestiary.models.base.Stars),
        ),
        migrations.CreateModel(
            name='ArtifactCraftInstance',
            fields=[
                ('slot', models.IntegerField(choices=[(1, 'Element'), (2, 'Archetype')])),
                ('element', models.CharField(blank=True, choices=[('pure', 'Pure'), ('fire', 'Fire'), ('wind', 'Wind'), ('water', 'Water'), ('light', 'Light'), ('dark', 'Dark')], max_length=6, null=True)),
                ('archetype', models.CharField(blank=True, choices=[('none', 'None'), ('attack', 'Attack'), ('hp', 'HP'), ('support', 'Support'), ('defense', 'Defense'), ('material', 'Material')], max_length=10, null=True)),
                ('quality', models.IntegerField(choices=[(0, 'Normal'), (1, 'Magic'), (2, 'Rare'), (3, 'Hero'), (4, 'Legend')], default=0)),
                ('effect', models.IntegerField(choices=[(1, 'ATK+ Proportional to Lost HP'), (2, 'DEF+ Proportional to Lost HP'), (3, 'SPD+ Proportional to Lost HP'), (4, 'SPD Under Inability'), (5, 'ATK Increased'), (6, 'DEF Increased'), (7, 'SPD Increased'), (8, 'CRI Rate Increased'), (9, 'Counterattack Damage Increased'), (10, 'Cooperative Attack Damage Increased'), (11, 'Bomb Damage Increased'), (12, 'Reflected Damage Increased'), (13, 'Crushing Hit Damage Increased'), (14, 'Damage Received Under Inability Decreased'), (15, 'Crit Damage Received Decreased'), (16, 'Life Drain Increased'), (17, 'HP When Revived Increased'), (18, 'ATB When Revived Increased'), (19, 'Damage Increased By % of HP'), (20, 'Damage Increased By % of ATK'), (21, 'Damage Increased By % of DEF'), (22, 'Damage Increased By % of SPD'), (23, 'Damage To Fire Increased'), (24, 'Damage To Water Increased'), (25, 'Damage To Wind Increased'), (26, 'Damage To Light Increased'), (27, 'Damage To Dark Increased'), (28, 'Damage From Fire Decreased'), (29, 'Damage From Water Decreased'), (30, 'Damage From Wind Decreased'), (31, 'Damage From Light Decreased'), (32, 'Damage From Dark Decreased'), (33, 'Skill 1 CRI Damage Increased'), (34, 'Skill 2 CRI Damage Increased'), (35, 'Skill 3 CRI Damage Increased'), (36, 'Skill 4 CRI Damage Increased'), (37, 'Skill 1 Recovery Increased'), (38, 'Skill 2 Recovery Increased'), (39, 'Skill 3 Recovery Increased'), (40, 'Skill 1 Accuracy Increased'), (41, 'Skill 1 Accuracy Increased'), (42, 'Skill 1 Accuracy Increased')])),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('com2us_id', models.BigIntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herders.Summoner')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, bestiary.models.base.Quality, bestiary.models.base.Archetype, bestiary.models.base.Elements, bestiary.models.base.Stats),
        ),
    ]
