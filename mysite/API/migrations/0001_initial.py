# Generated by Django 5.1.4 on 2024-12-23 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(default='', max_length=100)),
                ('telephone', models.CharField(blank=True, default=None, max_length=200)),
                ('schoolemail', models.EmailField(blank=True, default=None, max_length=254)),
                ('schooladdress', models.TextField(default='', max_length=100)),
                ('postal_address', models.CharField(blank=True, default=None, max_length=100)),
                ('website', models.TextField(default=None, max_length=100)),
                ('slogan', models.CharField(blank=True, default=None, max_length=200)),
                ('type_of_school', models.CharField(blank=True, choices=[('Primary', 'Primary School'), ('Secondary', 'Secondary School'), ('Combined', 'Combined School'), ('Vocational', 'Vocational School'), ('Other', 'Other School')], max_length=200)),
                ('umalusi', models.CharField(blank=True, choices=[('DBE', 'The Department of Basic Education (DBE)'), ('IEB', 'The Independent Examination Board (IEB)'), ('SACAI', 'The South African Comprehensive Assessment Institute (SACAI)')], max_length=200)),
                ('province', models.CharField(choices=[('Limpopo', 'Limpopo'), ('Free State', 'Free State'), ('Gauteng', 'Gauteng'), ('North West', 'North West'), ('KwaZulu-Natal', 'KwaZulu-Natal'), ('Mpumalanga', 'Mpumalanga'), ('Eastern Cape', 'Eastern Cape'), ('Northern Cape', 'Northern Cape'), ('Western Cape', 'Western Cape')], max_length=50, null=True)),
                ('district', models.CharField(choices=[('Alfred Nzo District', 'Alfred Nzo District'), ('amajuba', 'Amajuba District'), ('amathole', 'Amathole District'), ('bojanala platinum', 'Bojanala Platinum District'), ('buffalo city', 'Buffalo City Metropolitan '), ('capa winelands', 'Cape Winelands District'), ('capricorn', 'Capricorn District'), ('central karoo', 'Central Karoo District'), ('chris hani', 'Chris Hani District '), ('city of cape town', 'City of Cape Town Metropolitan'), ('city of johannesburg', 'City of Johannesburg Metropolitan'), ('city of tshwane', 'City of Tshwane Metropolitan'), ('dr kenneth kaunda', 'Dr Kenneth Kaunda District'), ('dr ruth segomotsi mompati', 'Dr Ruth Segomotsi Mompati District '), ('ehlanzeni', 'Ehlanzeni District '), ('ekurhuleni', 'Ekurhuleni Metropolitan '), ('ethekwini', 'eThekwini Metropolitan '), ('fezile dabi', 'Fezile Dabi District '), ('frances baard', 'Frances Baard District '), ('garden route', 'Garden Route District '), ('gert sibande', 'Gert Sibande District '), ('harry gwala', 'Harry Gwala District '), ('ilembe', 'iLembe District'), ('joe gqabi', 'Joe Gqabi District'), ('john taolo gaetsewe', 'John Taolo Gaetsewe District'), ('king cetshwayo', 'King Cetshwayo District '), ('lejweleputswa', 'Lejweleputswa District '), ('mangaung', 'Mangaung Metropolitan '), ('mopani', 'Mopani District'), ('namakwa', 'Namakwa District'), ('nelson mandela bay', 'Nelson Mandela Bay Metropolitan'), ('ngaka modiri molema', 'Ngaka Modiri Molema District '), ('nkangala', 'Nkangala District '), ('or tambo', 'OR Tambo District '), ('overberg', 'Overberg District'), ('pixley ka seme', 'Pixley ka Seme District '), ('sarah baartman', 'Sarah Baartman District '), ('sedibeng', 'Sedibeng District '), ('sekhukhune', 'Sekhukhune District'), ('thabo mofutsanyana', 'Thabo Mofutsanyana District '), ('ugu', 'Ugu District'), ('umgungundlovu', 'uMgungundlovu District'), ('umkhanyakude', 'uMkhanyakude District '), ('umzinyathi', 'uMzinyathi District '), ('uthukela', 'uThukela District'), ('vhembe', 'Vhembe District'), ('waterberg', 'Waterberg District'), ('west coast', 'West Coast District '), ('west rand', 'West Rand District '), ('xhariep', 'Xhariep District '), ('zf mgcawu', 'ZF Mgcawu District '), ('zululand', 'Zululand District')], default='', max_length=200)),
                ('circuit', models.CharField(choices=[('Soutpansberg East', 'Soutpansberg East Circuit'), ('Kgakotlou ', 'Kgakotlou '), ('Lebowakgomo', 'Lebowakgomo'), ('Mankweng ', 'Mankweng '), ('Pietersburg ', 'Pietersburg '), ('Seshego ', 'Seshego '), ('Bochum East ', 'Bochum East '), ('Potgietersrus', 'Potgietersrus')], default='', max_length=200)),
                ('curriculum', models.CharField(blank=True, choices=[('CAPS', 'CAPS curriculum'), ('Cambridge', 'Cambridge curriculum')], max_length=100)),
                ('grade_levels', models.CharField(blank=True, max_length=100)),
                ('accreditation', models.CharField(blank=True, max_length=100)),
                ('local_municipality', models.CharField(blank=True, max_length=100)),
                ('urban_rural', models.CharField(blank=True, max_length=100)),
                ('ward_id', models.CharField(blank=True, max_length=100)),
                ('Eei_district', models.CharField(blank=True, max_length=100)),
                ('emis_number', models.CharField(blank=True, max_length=100)),
                ('examination_number', models.CharField(blank=True, max_length=100)),
                ('examination_centre', models.CharField(blank=True, max_length=100)),
                ('persal_paypoint_number', models.CharField(blank=True, max_length=100)),
                ('persal_component_number', models.CharField(blank=True, max_length=100)),
                ('name_of_principal', models.CharField(blank=True, max_length=100)),
                ('number_of_teachers', models.CharField(blank=True, max_length=100)),
                ('number_of_learners', models.CharField(blank=True, max_length=100)),
                ('section_21', models.CharField(choices=[('Section 21 (Self Reliant)', 'Self Reliant: Yes'), ('Section 21 (Self Reliant)', 'Self Reliant: No')], default=None, max_length=100)),
                ('school_fees', models.CharField(default=None, max_length=100)),
                ('quintile_Level', models.CharField(choices=[('Quintile 1', 'Q1'), ('Quintile 2', 'Q2'), ('Quintile 3', 'Q3'), ('Quintile 4', 'Q4'), ('Quintile 5', 'Q5')], default=None, max_length=100)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/schoolprofile/')),
                ('image1', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/schoolprofile/')),
                ('history', models.CharField(blank=True, max_length=200)),
                ('mission', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'school profile',
            },
        ),
    ]