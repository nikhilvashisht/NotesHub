# Generated by Django 4.2.7 on 2023-12-14 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("storage", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("name", models.CharField(max_length=225)),
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name="file",
            name="author",
        ),
        migrations.AddField(
            model_name="file",
            name="user_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="storage.user",
            ),
        ),
    ]