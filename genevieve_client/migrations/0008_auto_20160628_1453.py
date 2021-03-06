# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-28 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genevieve_client', '0007_genomereport_genome_file_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='genevieveuser',
            name='passed_quiz',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='genomevariant',
            name='zygosity',
            field=models.CharField(choices=[('Het', 'Heterozygous'), ('Hom', 'Homozygous'), ('Hem', 'Hemizygous')], max_length=3),
        ),
        migrations.AlterField(
            model_name='variant',
            name='chromosome',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, 'X'), (24, 'Y'), (25, 'MT')]),
        ),
    ]
