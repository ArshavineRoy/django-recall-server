# Generated by Django 5.0.6 on 2024-09-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voter', '0016_alter_voter_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$dWOl4fjCUjwpCHy0NgjG80$zkKwkYmz56bpAyJVRCqI/7hkyJvomrNczBXgvm7fd1E=', max_length=128),
        ),
    ]