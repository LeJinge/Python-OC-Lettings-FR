from django.db import migrations


def move_profiles_data(apps, schema_editor):
    # Remplacez 'Profile' par le nom exact du modèle utilisé dans oc_lettings_site
    OldProfileModel = apps.get_model('profiles', 'Profile')
    NewProfileModel = apps.get_model('profiles', 'Profile')

    for old_profile in OldProfileModel.objects.all():
        NewProfileModel.objects.create(
            user=old_profile.user,
            favorite_city=old_profile.favorite_city,
        )


class Migration(migrations.Migration):
    dependencies = [
        ('profiles', '0001_initial'),  # Dépend de la première migration qui crée la structure de la table
    ]

    operations = [
        migrations.RunPython(move_profiles_data),
    ]
