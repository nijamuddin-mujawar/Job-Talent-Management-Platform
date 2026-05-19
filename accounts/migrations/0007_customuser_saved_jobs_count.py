                                                

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_profile_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='saved_jobs_count',
            field=models.IntegerField(default=0),
        ),
    ]
