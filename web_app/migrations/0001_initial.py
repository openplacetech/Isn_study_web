# Generated by Django 5.0.7 on 2024-07-29 08:18

import django.db.models.deletion
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerOpportunities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job_title', models.TextField()),
                ('job_summary', models.TextField(default='', help_text='Job summary should less then 500 character', max_length=500)),
                ('job_description', tinymce.models.HTMLField()),
                ('category', models.CharField(choices=[('ENGINEERING', 'Engineering'), ('DESIGN', 'Design')], max_length=100)),
                ('keyword', models.TextField(help_text='only for SEO write a keyword seperated by comma(,) eg: python,django,hr')),
                ('job_mode', models.CharField(choices=[('REMOTE', 'Remote'), ('ON_SITE', 'On Site'), ('HYBRID', 'Hybrid')], max_length=50)),
                ('job_type', models.CharField(choices=[('FULL_TIME', 'Full time'), ('PART_TIME', 'Part time')], max_length=50)),
                ('job_status', models.CharField(choices=[('DRAFT', 'DRAFT'), ('PUBLISHED', 'PUBLISHED'), ('PENDING', 'PENDING'), ('REVIEWING', 'REVIEWING'), ('UNPUBLISHED', 'UNPUBLISHED')], max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Career Opportunities',
                'db_table': 'CareerOpportunities',
            },
        ),
        migrations.CreateModel(
            name='ISNTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=300)),
                ('profile_image', models.ImageField(help_text='recommended size is 612x408', upload_to='team_profile')),
            ],
            options={
                'verbose_name_plural': 'Our Teams',
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='PartnershipRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('institute_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contact_person', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=200)),
                ('interested_service', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('is_accept_privacy_policy', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Partnership Request',
                'db_table': 'partnership_request',
            },
        ),
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='Privacy and Policy', max_length=200)),
                ('content', tinymce.models.HTMLField()),
                ('status', models.CharField(blank=True, choices=[('DRAFT', 'DRAFT'), ('PUBLISHED', 'PUBLISHED'), ('PENDING', 'PENDING'), ('REVIEWING', 'REVIEWING'), ('UNPUBLISHED', 'UNPUBLISHED')], max_length=200)),
            ],
            options={
                'verbose_name_plural': 'privacy policy',
                'db_table': 'privacy_policy',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(choices=[('FACEBOOK', 'FACEBOOK'), ('YOUTUBE', 'YOUTUBE'), ('LINKEDIN', 'LINKEDIN'), ('TIKTOK', 'TIKTOK'), ('TWITTER', 'TWITTER'), ('INSTAGRAM', 'INSTAGRAM')], max_length=100, unique=True)),
                ('followers', models.CharField(blank=True, default='', max_length=100)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Social Media',
                'db_table': 'social_media',
            },
        ),
        migrations.CreateModel(
            name='StudyDestinationOfNepali',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('region', models.CharField(choices=[('WEST_AFRICA', 'West Africa'), ('SOUTH_AND_CENTRAL_ASIA', 'South and Central Asia'), ('SOUTHEAST_ASIA', 'Southeast Asia'), ('MEXICO_AND_CENTRAL_AMERICA', 'Mexico and Central America'), ('SOUTH_AMERICA', 'South America')], max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('student_no', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Student Number',
                'db_table': 'NumberOfStudentStudy',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Subscribers',
                'db_table': 'Subscriber',
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(blank=True, help_text='Recommended size is 500x500', null=True, upload_to='testimonial/photo')),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
                'db_table': 'testimonial',
            },
        ),
        migrations.CreateModel(
            name='ApplyForCareer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=40)),
                ('contact_phone_type', models.CharField(blank=True, choices=[('Mobile', 'Mobile')], max_length=200, null=True)),
                ('country', models.CharField(blank=True, choices=[('AF', 'Afghanistan'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BA', 'Bosnia and Herzegovina'), ('BW', 'Botswana'), ('BR', 'Brazil'), ('BN', 'Brunei'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('CV', 'Cabo Verde'), ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CD', 'Congo, Democratic Republic of the'), ('CG', 'Congo, Republic of the'), ('CR', 'Costa Rica'), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('TL', 'East Timor (Timor-Leste)'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('SZ', 'Eswatini'), ('ET', 'Ethiopia'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GR', 'Greece'), ('GD', 'Grenada'), ('GT', 'Guatemala'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HN', 'Honduras'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KP', 'Korea, North'), ('KR', 'Korea, South'), ('XK', 'Kosovo'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('MX', 'Mexico'), ('FM', 'Micronesia'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar (Burma)'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('MK', 'North Macedonia (Macedonia)'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PL', 'Poland'), ('PT', 'Portugal'), ('QA', 'Qatar'), ('RO', 'Romania'), ('RU', 'Russia'), ('RW', 'Rwanda'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('SS', 'South Sudan'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syria'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('US', 'United States'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VA', 'Vatican City'), ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=100, null=True)),
                ('profile_link', models.URLField(blank=True, null=True)),
                ('profile_link_type', models.CharField(blank=True, max_length=100, null=True)),
                ('expected_salary', models.CharField(blank=True, max_length=200, null=True)),
                ('resume', models.FileField(upload_to='resume')),
                ('availability_or_notice_period', models.CharField(blank=True, max_length=300, null=True)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=100, null=True)),
                ('veteran_status', models.CharField(blank=True, max_length=100, null=True)),
                ('race_ethnicity', models.CharField(blank=True, max_length=100, null=True)),
                ('disability', models.CharField(blank=True, max_length=100, null=True)),
                ('legal_name', models.CharField(blank=True, max_length=100, null=True)),
                ('other_job_consider', models.BooleanField(default=False, help_text='I authorize ISN to consider me for other job opportunities for the next 36 months within ISN in addition to the specific job I am applying for.')),
                ('required_immigration_sponsorship', models.BooleanField(blank=True, default=False, help_text='Will you now or in the future require immigration sponsorship for employment with ISN?', null=True)),
                ('is_previously_employed', models.BooleanField(blank=True, default=False, help_text='Have you previously been employed by ISN?', null=True)),
                ('is_former_current_intern_or_contractor', models.BooleanField(blank=True, default=False, help_text='Are you a former/current intern or contractor?', null=True)),
                ('receive_text_message', models.BooleanField(blank=True, default=False, help_text='Do you consent to receiving text messages throughout your application process including but not limited to interview details, pre-employment screening notifications and reminders?', null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='web_app.careeropportunities')),
            ],
            options={
                'verbose_name_plural': 'Job Applications',
                'db_table': 'isn_job_application',
            },
        ),
        migrations.CreateModel(
            name='Insights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', tinymce.models.HTMLField()),
                ('cover_image', models.ImageField(help_text='Upload a cover picture. which height recommended size is 2,00x1,334 ', upload_to='blog_cover/')),
                ('keywords', models.TextField(help_text='Do not add more then five keyword this is only for SEO')),
                ('category', models.CharField(choices=[('SCIENCE_AND_TECHNOLOGY', 'Science and technology'), ('EDUCATION', 'Education'), ('IMMIGRATION', 'Immigration')], max_length=100)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ISN Insights',
                'db_table': 'Insights',
            },
        ),
        migrations.CreateModel(
            name='InsightComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('insight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_app.insights')),
            ],
            options={
                'verbose_name_plural': 'Insight Comments',
                'db_table': 'InsightComments',
            },
        ),
    ]
