from django.db import models

# Create your models here.

STATE_CHOICE = (
    ('Karachi','Karachi'),
    ('Lahore','Lahore'),
    ('Quetta', 'Quetta'),
    ('Islamabad', 'Islamabad'),
    ('Multan', 'Multan'),
    ('Hyderabad', 'Hyderabad'),
    ('Jamshoro', 'Jamshoro'),
    ('Shikarpur', 'Shikarpur'),
    ('Sukkur', 'Sukkur'),
    ('Larkana', 'Larkana'),
    ('Peshawar', 'Peshawar'),
    ('Sargodha', 'Sargodha'),
    ('Faisalabad', 'Faisalabad'),
    ('Rawalpindi', 'Rawalpindi'),
    ('Gujranwala', 'Gujranwala'),
    ('Sialkot', 'Sialkot'),
    ('Bahawalpur', 'Bahawalpur'),
    ('Kandhkot', 'Kandhkot'),
    ('Gujrat', 'Gujrat'),
    ('Rahim Yar Khan', 'Rahim Yar Khan'),
    ('Sahiwal', 'Sahiwal'),
    ('Nawabshah', 'Nawabshah'),
    ('Jhelum', 'Jhelum'),
    ('Jacobabad', 'Jacobabad'),
    ('Khuzdar', 'Khuzdar'),

)


class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices= STATE_CHOICE,max_length=50)
    mobile = models.PositiveIntegerField()
    email = models.EmailField(max_length = 254)
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profileimg',blank=True)
    my_file = models.ImageField(upload_to='doc', blank=True)


