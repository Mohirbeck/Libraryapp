# Generated by Django 3.2.4 on 2021-06-28 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='books',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.language'),
        ),
    ]
