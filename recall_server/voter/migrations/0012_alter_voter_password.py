
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("voter", "0011_alter_voter_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name='voter',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$720000$9yuC8frCwqmvwW4sDbaFK1$F6ERAkXknzGN8HlQ6PkLrDC+6tYOYxZ1UHMoS2NGUeM=', max_length=128),
        ),
    ]
