# Generated by Django 4.1.3 on 2022-11-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_tag_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='projects',
            field=models.ManyToManyField(to='projects.project'),
        ),
    ]