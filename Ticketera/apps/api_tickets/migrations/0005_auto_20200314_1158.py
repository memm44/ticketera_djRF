# Generated by Django 2.2 on 2020-03-14 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_tickets', '0004_responsible_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issuer',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='issue',
            name='id_issuer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='api_tickets.Issuer'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='id_responsible',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsibles', to='api_tickets.Responsible'),
        ),
    ]