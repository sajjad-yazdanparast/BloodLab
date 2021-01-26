# Generated by Django 3.0.7 on 2021-01-26 15:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('end_point', models.URLField()),
                ('api_key', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('sex', models.BooleanField()),
                ('phone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='phone number length must be 11', regex='^\\w{11}$')])),
            ],
        ),
        migrations.CreateModel(
            name='BloodExpert',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.User')),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Lab')),
            ],
            bases=('user.user',),
        ),
        migrations.CreateModel(
            name='TimeService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('stime', models.TimeField()),
                ('etime', models.TimeField()),
                ('evailable', models.BooleanField()),
                ('expert_snn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.BloodExpert')),
            ],
            options={
                'unique_together': {('expert_snn', 'date', 'stime', 'etime')},
            },
        ),
    ]
