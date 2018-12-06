# Generated by Django 2.1.2 on 2018-12-06 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time when this object was created.')),
                ('updated', models.DateTimeField(auto_now=True, help_text='The date and time when this object was last updated.')),
                ('name', models.CharField(help_text='The name of this Context. Must be unique within the Team.', max_length=100)),
                ('slug', models.SlugField(help_text='The slug for this Context. Must be unique within the Team.')),
                ('description', models.TextField(help_text='The description of this context. Markdown is supported.')),
                ('team', models.ForeignKey(help_text='The Team to which this Context belongs', on_delete=django.db.models.deletion.PROTECT, related_name='contexts', to='team.Team')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='context',
            unique_together={('name', 'team'), ('slug', 'team')},
        ),
    ]
