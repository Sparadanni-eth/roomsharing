# Generated by Django 3.0.12 on 2021-03-21 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0003_auto_20210321_1826"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomamenity",
            name="amenity",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="roomamenities_of_amenity",
                related_query_name="roomamenity_of_aptitude",
                to="rooms.Amenity",
            ),
        ),
    ]
