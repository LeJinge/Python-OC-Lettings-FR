from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0002_move_data_to_lettings'),
    ]

    operations = [
        migrations.RunSQL("DROP TABLE IF EXISTS oc_lettings_site_address;"),
        migrations.RunSQL("DROP TABLE IF EXISTS oc_lettings_site_letting;"),
        # Ajoutez des commandes pour chaque table que vous souhaitez supprimer
    ]
