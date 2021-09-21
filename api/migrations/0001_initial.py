from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name='satwikan',
                          email='satwik@gmail.com',
                          is_staff=True,
                          is_superuser=True,
                          phone="987654321",
                          gender="Male"
                          )
        
        user.set_password("password")
        user.save()
        
    dependencies = [
        
    ]
    operations = [
        migrations.RunPython(seed_data),
    ]
