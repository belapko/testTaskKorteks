# Generated by Django 4.1.7 on 2023-02-20 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_album_title'),
        ('songs', '0002_rename_serial_number_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='serial_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ManyToManyField(related_name='songs_list', to='albums.album'),
        ),
    ]