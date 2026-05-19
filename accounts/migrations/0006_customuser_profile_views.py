                                                

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_customuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_views',
            field=models.IntegerField(default=0),
        ),
    ]
