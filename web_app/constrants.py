INTERESTED_SERVICE = (
    ("Hiring as Agent","Hiring as Agent"),
    ("Market Entry","Market Entry"),
    ("Other, Specify","Other, Specify"),
)
CONTACT_PHONE_TYPE = (
    ("Mobile","Mobile"),
)
REGION_TYPE = (
    ("WEST_AFRICA","West Africa"),
    ("SOUTH_AND_CENTRAL_ASIA","South and Central Asia"),
    ("SOUTHEAST_ASIA","Southeast Asia"),
    ("MEXICO_AND_CENTRAL_AMERICA","Mexico and Central America"),
    ("SOUTH_AMERICA","South America"),
)

GENDER_TYPE = (
    ("MALE","Male"),
    ("FEMALE","Female"),
)


RACE_ETHNICITY_CHOICES = [
    ('asian', 'Asian'),
    ('black_or_african_american', 'Black or African American'),
    ('hispanic_or_latino', 'Hispanic or Latino'),
    ('native_american_or_alaska_native', 'Native American or Alaska Native'),
    ('native_hawaiian_or_other_pacific_islander', 'Native Hawaiian or Other Pacific Islander'),
    ('white', 'White'),
    ('two_or_more_races', 'Two or More Races'),
    ('other', 'Other'),
]
DISABILITY_TYPE_CHOICES = [
    ('visual_impairment', 'Visual Impairment'),
    ('hearing_impairment', 'Hearing Impairment'),
    ('mobility_impairment', 'Mobility Impairment'),
    ('cognitive_impairment', 'Cognitive Impairment'),
    ('mental_health_condition', 'Mental Health Condition'),
    ('chronic_health_condition', 'Chronic Health Condition'),
    ('developmental_disability', 'Developmental Disability'),
    ('speech_impairment', 'Speech Impairment'),
    ('other', 'Other'),
]

JOB_TYPE=(
    ("FULL_TIME","Full time"),
    ("PART_TIME","Part time"),
)

JOB_MODE = (
    ("REMOTE","Remote"),
    ("ON_SITE","On Site"),
    ("HYBRID","Hybrid")
)

JOB_CATEGORY = (
    ("PROCESSING","Processing"),
    ("MARKETING","Marketing"),
    ("PARTNERSHIP","Partnership"),
    ("TECHNOLOGY","Technology"),
    ("OPERATIONS","Operations")
)
STATUS_TYPE = (
    ("DRAFT","DRAFT"),
    ("PUBLISHED","PUBLISHED"),
    ("PENDING","PENDING"),
    ("REVIEWING","REVIEWING"),
    ("UNPUBLISHED","UNPUBLISHED"),
)
SOCIALMEDIA_TYPE = (
    ("FACEBOOK","FACEBOOK"),
    ("YOUTUBE","YOUTUBE"),
    ("LINKEDIN","LINKEDIN"),
    ("TIKTOK","TIKTOK"),
    ("TWITTER","TWITTER"),
    ("INSTAGRAM","INSTAGRAM"),
)

PROFILE_LINK_TYPE = (
    ("FACEBOOK","Facebook"),
    ("LINKEDIN","Linkedin"),
    ("WEBSITE","Website"),
    ("YOUTUBE","Youtube"),
    ("TIKTOK","Tiktok"),
    ("TWITTER","Twitter"),
    ("INSTAGRAM","Instagram"),
)


VETERAN_STATUS_CHOICES = [
    ('military_branches', 'Veterans by military branches'),
    ('combat_war_veterans', 'Combat or war veterans'),
    ('disabled_veterans', 'Disabled veterans'),
    ('other_services', 'Veterans of services other than the armed forces'),
]

NOTICE_PERIOD = (
    ('Immediate','Immediate'),
    ('1 week','1 week'),
    ('2 weeks','2 week'),
    ('1 month','1 month'),
    ('More than 1 month','More than 1 month'),
)
INSIGHTS_CATEGORY = (
    ("TRENDS","Trends"),
    ("CASE_STUDY","Case Study"),
    ("INFORMATICS","Informatics")
)
COUNTRY_CHOICES = [
    ('AF', 'Afghanistan'),
    ('AL', 'Albania'),
    ('DZ', 'Algeria'),
    ('AD', 'Andorra'),
    ('AO', 'Angola'),
    ('AG', 'Antigua and Barbuda'),
    ('AR', 'Argentina'),
    ('AM', 'Armenia'),
    ('AU', 'Australia'),
    ('AT', 'Austria'),
    ('AZ', 'Azerbaijan'),
    ('BS', 'Bahamas'),
    ('BH', 'Bahrain'),
    ('BD', 'Bangladesh'),
    ('BB', 'Barbados'),
    ('BY', 'Belarus'),
    ('BE', 'Belgium'),
    ('BZ', 'Belize'),
    ('BJ', 'Benin'),
    ('BT', 'Bhutan'),
    ('BO', 'Bolivia'),
    ('BA', 'Bosnia and Herzegovina'),
    ('BW', 'Botswana'),
    ('BR', 'Brazil'),
    ('BN', 'Brunei'),
    ('BG', 'Bulgaria'),
    ('BF', 'Burkina Faso'),
    ('BI', 'Burundi'),
    ('CV', 'Cabo Verde'),
    ('KH', 'Cambodia'),
    ('CM', 'Cameroon'),
    ('CA', 'Canada'),
    ('CF', 'Central African Republic'),
    ('TD', 'Chad'),
    ('CL', 'Chile'),
    ('CN', 'China'),
    ('CO', 'Colombia'),
    ('KM', 'Comoros'),
    ('CD', 'Congo, Democratic Republic of the'),
    ('CG', 'Congo, Republic of the'),
    ('CR', 'Costa Rica'),
    ('HR', 'Croatia'),
    ('CU', 'Cuba'),
    ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'),
    ('DK', 'Denmark'),
    ('DJ', 'Djibouti'),
    ('DM', 'Dominica'),
    ('DO', 'Dominican Republic'),
    ('TL', 'East Timor (Timor-Leste)'),
    ('EC', 'Ecuador'),
    ('EG', 'Egypt'),
    ('SV', 'El Salvador'),
    ('GQ', 'Equatorial Guinea'),
    ('ER', 'Eritrea'),
    ('EE', 'Estonia'),
    ('SZ', 'Eswatini'),
    ('ET', 'Ethiopia'),
    ('FJ', 'Fiji'),
    ('FI', 'Finland'),
    ('FR', 'France'),
    ('GA', 'Gabon'),
    ('GM', 'Gambia'),
    ('GE', 'Georgia'),
    ('DE', 'Germany'),
    ('GH', 'Ghana'),
    ('GR', 'Greece'),
    ('GD', 'Grenada'),
    ('GT', 'Guatemala'),
    ('GN', 'Guinea'),
    ('GW', 'Guinea-Bissau'),
    ('GY', 'Guyana'),
    ('HT', 'Haiti'),
    ('HN', 'Honduras'),
    ('HU', 'Hungary'),
    ('IS', 'Iceland'),
    ('IN', 'India'),
    ('ID', 'Indonesia'),
    ('IR', 'Iran'),
    ('IQ', 'Iraq'),
    ('IE', 'Ireland'),
    ('IL', 'Israel'),
    ('IT', 'Italy'),
    ('JM', 'Jamaica'),
    ('JP', 'Japan'),
    ('JO', 'Jordan'),
    ('KZ', 'Kazakhstan'),
    ('KE', 'Kenya'),
    ('KI', 'Kiribati'),
    ('KP', 'Korea, North'),
    ('KR', 'Korea, South'),
    ('XK', 'Kosovo'),
    ('KW', 'Kuwait'),
    ('KG', 'Kyrgyzstan'),
    ('LA', 'Laos'),
    ('LV', 'Latvia'),
    ('LB', 'Lebanon'),
    ('LS', 'Lesotho'),
    ('LR', 'Liberia'),
    ('LY', 'Libya'),
    ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'),
    ('LU', 'Luxembourg'),
    ('MG', 'Madagascar'),
    ('MW', 'Malawi'),
    ('MY', 'Malaysia'),
    ('MV', 'Maldives'),
    ('ML', 'Mali'),
    ('MT', 'Malta'),
    ('MH', 'Marshall Islands'),
    ('MR', 'Mauritania'),
    ('MU', 'Mauritius'),
    ('MX', 'Mexico'),
    ('FM', 'Micronesia'),
    ('MD', 'Moldova'),
    ('MC', 'Monaco'),
    ('MN', 'Mongolia'),
    ('ME', 'Montenegro'),
    ('MA', 'Morocco'),
    ('MZ', 'Mozambique'),
    ('MM', 'Myanmar (Burma)'),
    ('NA', 'Namibia'),
    ('NR', 'Nauru'),
    ('NP', 'Nepal'),
    ('NL', 'Netherlands'),
    ('NZ', 'New Zealand'),
    ('NI', 'Nicaragua'),
    ('NE', 'Niger'),
    ('NG', 'Nigeria'),
    ('MK', 'North Macedonia (Macedonia)'),
    ('NO', 'Norway'),
    ('OM', 'Oman'),
    ('PK', 'Pakistan'),
    ('PW', 'Palau'),
    ('PA', 'Panama'),
    ('PG', 'Papua New Guinea'),
    ('PY', 'Paraguay'),
    ('PE', 'Peru'),
    ('PH', 'Philippines'),
    ('PL', 'Poland'),
    ('PT', 'Portugal'),
    ('QA', 'Qatar'),
    ('RO', 'Romania'),
    ('RU', 'Russia'),
    ('RW', 'Rwanda'),
    ('KN', 'Saint Kitts and Nevis'),
    ('LC', 'Saint Lucia'),
    ('VC', 'Saint Vincent and the Grenadines'),
    ('WS', 'Samoa'),
    ('SM', 'San Marino'),
    ('ST', 'Sao Tome and Principe'),
    ('SA', 'Saudi Arabia'),
    ('SN', 'Senegal'),
    ('RS', 'Serbia'),
    ('SC', 'Seychelles'),
    ('SL', 'Sierra Leone'),
    ('SG', 'Singapore'),
    ('SK', 'Slovakia'),
    ('SI', 'Slovenia'),
    ('SB', 'Solomon Islands'),
    ('SO', 'Somalia'),
    ('ZA', 'South Africa'),
    ('SS', 'South Sudan'),
    ('ES', 'Spain'),
    ('LK', 'Sri Lanka'),
    ('SD', 'Sudan'),
    ('SR', 'Suriname'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('SY', 'Syria'),
    ('TW', 'Taiwan'),
    ('TJ', 'Tajikistan'),
    ('TZ', 'Tanzania'),
    ('TH', 'Thailand'),
    ('TL', 'Timor-Leste'),
    ('TG', 'Togo'),
    ('TO', 'Tonga'),
    ('TT', 'Trinidad and Tobago'),
    ('TN', 'Tunisia'),
    ('TR', 'Turkey'),
    ('TM', 'Turkmenistan'),
    ('TV', 'Tuvalu'),
    ('UG', 'Uganda'),
    ('UA', 'Ukraine'),
    ('AE', 'United Arab Emirates'),
    ('GB', 'United Kingdom'),
    ('US', 'United States'),
    ('UY', 'Uruguay'),
    ('UZ', 'Uzbekistan'),
    ('VU', 'Vanuatu'),
    ('VA', 'Vatican City'),
    ('VE', 'Venezuela'),
    ('VN', 'Vietnam'),
    ('YE', 'Yemen'),
    ('ZM', 'Zambia'),
    ('ZW', 'Zimbabwe'),
]

currencies = [
    {'country': 'United States', 'currency_code': 'USD', 'currency_name': 'United States Dollar'},
    {'country': 'Eurozone', 'currency_code': 'EUR', 'currency_name': 'Euro'},
    {'country': 'United Kingdom', 'currency_code': 'GBP', 'currency_name': 'British Pound Sterling'},
    {'country': 'Japan', 'currency_code': 'JPY', 'currency_name': 'Japanese Yen'},
    {'country': 'Australia', 'currency_code': 'AUD', 'currency_name': 'Australian Dollar'},
    {'country': 'Canada', 'currency_code': 'CAD', 'currency_name': 'Canadian Dollar'},
    {'country': 'Switzerland', 'currency_code': 'CHF', 'currency_name': 'Swiss Franc'},
    {'country': 'China', 'currency_code': 'CNY', 'currency_name': 'Chinese Yuan'},
    {'country': 'Sweden', 'currency_code': 'SEK', 'currency_name': 'Swedish Krona'},
    {'country': 'New Zealand', 'currency_code': 'NZD', 'currency_name': 'New Zealand Dollar'},
    {'country': 'India', 'currency_code': 'INR', 'currency_name': 'Indian Rupee'},
    {'country': 'Russia', 'currency_code': 'RUB', 'currency_name': 'Russian Ruble'},
    {'country': 'Brazil', 'currency_code': 'BRL', 'currency_name': 'Brazilian Real'},
    {'country': 'South Africa', 'currency_code': 'ZAR', 'currency_name': 'South African Rand'},
    {'country': 'Singapore', 'currency_code': 'SGD', 'currency_name': 'Singapore Dollar'},
    {'country': 'Hong Kong', 'currency_code': 'HKD', 'currency_name': 'Hong Kong Dollar'},
    {'country': 'Mexico', 'currency_code': 'MXN', 'currency_name': 'Mexican Peso'},
    {'country': 'Norway', 'currency_code': 'NOK', 'currency_name': 'Norwegian Krone'},
    {'country': 'South Korea', 'currency_code': 'KRW', 'currency_name': 'South Korean Won'},
    {'country': 'Turkey', 'currency_code': 'TRY', 'currency_name': 'Turkish Lira'},
    {'country': 'Indonesia', 'currency_code': 'IDR', 'currency_name': 'Indonesian Rupiah'},
    {'country': 'Poland', 'currency_code': 'PLN', 'currency_name': 'Polish Zloty'},
    {'country': 'Thailand', 'currency_code': 'THB', 'currency_name': 'Thai Baht'},
    {'country': 'Taiwan', 'currency_code': 'TWD', 'currency_name': 'New Taiwan Dollar'},
    {'country': 'Malaysia', 'currency_code': 'MYR', 'currency_name': 'Malaysian Ringgit'},
    {'country': 'Philippines', 'currency_code': 'PHP', 'currency_name': 'Philippine Peso'},
    {'country': 'Vietnam', 'currency_code': 'VND', 'currency_name': 'Vietnamese Dong'},
    {'country': 'Czech Republic', 'currency_code': 'CZK', 'currency_name': 'Czech Koruna'},
    {'country': 'Hungary', 'currency_code': 'HUF', 'currency_name': 'Hungarian Forint'},
    {'country': 'Israel', 'currency_code': 'ILS', 'currency_name': 'Israeli New Shekel'},
    {'country': 'Saudi Arabia', 'currency_code': 'SAR', 'currency_name': 'Saudi Riyal'},
    {'country': 'United Arab Emirates', 'currency_code': 'AED', 'currency_name': 'United Arab Emirates Dirham'},
    {'country': 'Colombia', 'currency_code': 'COP', 'currency_name': 'Colombian Peso'},
    {'country': 'Chile', 'currency_code': 'CLP', 'currency_name': 'Chilean Peso'},
    {'country': 'Peru', 'currency_code': 'PEN', 'currency_name': 'Peruvian Nuevo Sol'},
    {'country': 'Argentina', 'currency_code': 'ARS', 'currency_name': 'Argentine Peso'},
    {'country': 'Pakistan', 'currency_code': 'PKR', 'currency_name': 'Pakistani Rupee'},
    {'country': 'Bangladesh', 'currency_code': 'BDT', 'currency_name': 'Bangladeshi Taka'},
    {'country': 'Sri Lanka', 'currency_code': 'LKR', 'currency_name': 'Sri Lankan Rupee'},
    {'country': 'Nepal', 'currency_code': 'NPR', 'currency_name': 'Nepalese Rupee'},
    {'country': 'Kazakhstan', 'currency_code': 'KZT', 'currency_name': 'Kazakhstani Tenge'},
    {'country': 'Oman', 'currency_code': 'OMR', 'currency_name': 'Omani Rial'},
    {'country': 'Qatar', 'currency_code': 'QAR', 'currency_name': 'Qatari Rial'},
    {'country': 'Kuwait', 'currency_code': 'KWD', 'currency_name': 'Kuwaiti Dinar'},
    {'country': 'Bahrain', 'currency_code': 'BHD', 'currency_name': 'Bahraini Dinar'},
    {'country': 'Jordan', 'currency_code': 'JOD', 'currency_name': 'Jordanian Dinar'},
    {'country': 'Lebanon', 'currency_code': 'LBP', 'currency_name': 'Lebanese Pound'},
    {'country': 'Armenia', 'currency_code': 'AMD', 'currency_name': 'Armenian Dram'},
    {'country': 'Georgia', 'currency_code': 'GEL', 'currency_name': 'Georgian Lari'},
    {'country': 'Iceland', 'currency_code': 'ISK', 'currency_name': 'Icelandic Króna'},
    {'country': 'Mauritius', 'currency_code': 'MUR', 'currency_name': 'Mauritian Rupee'},
    {'country': 'Botswana', 'currency_code': 'BWP', 'currency_name': 'Botswana Pula'},
    {'country': 'Ghana', 'currency_code': 'GHS', 'currency_name': 'Ghanaian Cedi'},
    {'country': 'Ethiopia', 'currency_code': 'ETB', 'currency_name': 'Ethiopian Birr'},
    {'country': 'Angola', 'currency_code': 'AOA', 'currency_name': 'Angolan Kwanza'},
    {'country': 'Uganda', 'currency_code': 'UGX', 'currency_name': 'Ugandan Shilling'},
    {'country': 'Tanzania', 'currency_code': 'TZS', 'currency_name': 'Tanzanian Shilling'},
    {'country': 'Zambia', 'currency_code': 'ZMW', 'currency_name': 'Zambian Kwacha'},
    {'country': 'Malawi', 'currency_code': 'MWK', 'currency_name': 'Malawian Kwacha'},
    {'country': 'Sierra Leone', 'currency_code': 'SLL', 'currency_name': 'Sierra Leonean Leone'},
    {'country': 'Liberia', 'currency_code': 'LRD', 'currency_name': 'Liberian Dollar'},
    {'country': 'South Sudan', 'currency_code': 'SSP', 'currency_name': 'South Sudanese Pound'}
]
