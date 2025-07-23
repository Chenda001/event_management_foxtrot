
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
        ('venue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venue.space'),
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
    ]
