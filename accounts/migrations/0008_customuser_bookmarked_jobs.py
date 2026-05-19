
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customuser_saved_jobs_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bookmarked_jobs',
            field=models.IntegerField(default=0),
        ),
    ]
