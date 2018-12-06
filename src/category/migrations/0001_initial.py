# Generated by Django 2.1.2 on 2018-12-06 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
        ('context', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='The date and time when this object was created.')),
                ('updated', models.DateTimeField(auto_now=True, help_text='The date and time when this object was last updated.')),
                ('name', models.CharField(help_text='The name of this Category. Must be unique within the Team.', max_length=100)),
                ('slug', models.SlugField(help_text='The slug for this Category. Must be unique within the Team.')),
                ('description', models.TextField(help_text='The description of this category. Markdown is supported.')),
                ('weight', models.IntegerField(default=10, help_text='Change the weight of a Category to change sorting. Heavier Categories sink to the bottom. Categories with the same weight are sorted by name.')),
                ('requires_context', models.BooleanField(default=True, help_text='Check to make it mandatory to pick a Context for Reviews of Items in this Category.')),
                ('default_context', models.ForeignKey(blank=True, help_text='The default Context for new Reviews for Items in this Category. Leave blank to have no default.', null=True, on_delete=django.db.models.deletion.PROTECT, to='context.Context')),
                ('team', models.ForeignKey(help_text='The Team to which this Category belongs', on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='team.Team')),
            ],
            options={
                'ordering': ['weight', 'name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('name', 'team'), ('slug', 'team')},
        ),
    ]
