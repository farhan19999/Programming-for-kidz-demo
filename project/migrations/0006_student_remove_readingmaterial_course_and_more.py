# Generated by Django 4.1.7 on 2023-02-28 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_mcq_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('school', models.CharField(max_length=50)),
                ('_class', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='readingmaterial',
            name='course',
        ),
        migrations.AlterField(
            model_name='mcq',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.course'),
        ),
        migrations.CreateModel(
            name='WeeklyModules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.course')),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.student')),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdmat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.readingmaterial')),
            ],
        ),
        migrations.AddField(
            model_name='readingmaterial',
            name='week',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.weeklymodules'),
        ),
    ]