# Generated by Django 4.1.13 on 2024-03-14 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_student_class_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_level',
            field=models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV'), ('V', 'V'), ('VI', 'VI'), ('VII', 'VII'), ('VIII', 'VIII'), ('IX', 'IX'), ('X', 'X'), ('XI', 'XI'), ('XII', 'XII')], default='', max_length=5),
        ),
    ]
