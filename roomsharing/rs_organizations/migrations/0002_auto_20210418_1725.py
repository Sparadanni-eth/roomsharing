# Generated by Django 3.0.12 on 2021-04-18 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rs_organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='contact_person',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact Person'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(max_length=4000, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Telephone'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Website'),
        ),
        migrations.CreateModel(
            name='OrganizationalAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_address_line', models.CharField(blank=True, max_length=200, null=True, verbose_name='Additional Address Line')),
                ('street', models.CharField(blank=True, max_length=200, null=True, verbose_name='Street')),
                ('street_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='Street Number')),
                ('zip_code', models.CharField(blank=True, max_length=200, null=True, verbose_name='ZIP Code')),
                ('city', models.CharField(blank=True, max_length=200, null=True, verbose_name='City')),
                ('country', models.IntegerField(choices=[(1, 'Germany')], default=1, verbose_name='Country')),
                ('long', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Longitude')),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Latitude')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizationaladdresses_of_organization', related_query_name='organizationaladdress_of_organization', to='rs_organizations.Organization')),
            ],
        ),
    ]
