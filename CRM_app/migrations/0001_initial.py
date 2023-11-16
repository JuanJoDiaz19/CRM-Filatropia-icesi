

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('image_link', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Allie_Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('area_description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Donation_Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('max_value', models.IntegerField()),
                ('min_value', models.IntegerField()),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Investigation_Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('objetivos', models.CharField(max_length=200, null=True)),
                ('active', models.TextField(max_length=1)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User_Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('user_type_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CRM_app.user_type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('doi', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField(null=True)),
                ('investigation_project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.investigation_project')),
            ],
        ),
        migrations.CreateModel(
            name='Practicing',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
                ('image_link', models.CharField(max_length=200, null=True)),
                ('allie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.allie')),
                ('career_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.career')),
                ('gender_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.gender')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200, null=True)),
                ('objective', models.CharField(max_length=200, null=True)),
                ('allie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.allie')),
                ('meeting_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.meeting_type')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=20)),
                ('objective', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('event_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.event_type')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('description', models.CharField(max_length=20, null=True)),
                ('allie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.allie')),
                ('donation_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.donation_type')),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('aux_email', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=20)),
                ('allie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.allie')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('contenido', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRM_app.event')),
                ('meeting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRM_app.meeting')),
            ],
        ),
        migrations.AddField(
            model_name='allie',
            name='allie_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.allie_type'),
        ),
        migrations.AddField(
            model_name='allie',
            name='area_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.area'),
        ),
        migrations.CreateModel(
            name='EventAllie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.allie')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.event')),
            ],
            options={
                'db_table': 'EVENT_ALLIE',
                'unique_together': {('event', 'allie')},
            },
        ),
        migrations.CreateModel(
            name='AllieProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.allie')),
                ('investigation_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRM_app.investigation_project')),
            ],
            options={
                'db_table': 'ALLIE_PROJECT',
                'unique_together': {('allie', 'investigation_project')},
            },
        ),
    ]
