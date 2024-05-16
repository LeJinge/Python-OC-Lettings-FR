from django.db import migrations


def move_lettings_data_address(apps, schema_editor):
    OldAddressModel = apps.get_model('lettings', 'Address')
    NewAddressModel = apps.get_model('lettings', 'Address')

    for old_address in OldAddressModel.objects.all():
        NewAddressModel.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )


def move_lettings_data_letting(apps, schema_editor):
    OldLettingModel = apps.get_model('lettings', 'Letting')
    NewLettingModel = apps.get_model('lettings', 'Letting')
    NewAddressModel = apps.get_model('lettings', 'Address')

    for old_letting in OldLettingModel.objects.all():
        # Récupérer l'adresse associée à l'ancienne location
        old_address = old_letting.address
        # Trouver la nouvelle adresse correspondante dans la nouvelle structure de la base de données
        new_address = NewAddressModel.objects.get(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )
        NewLettingModel.objects.create(
            title=old_letting.title,
            address=new_address,
        )


class Migration(migrations.Migration):
    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(move_lettings_data_address),
        migrations.RunPython(move_lettings_data_letting),
    ]
