from django.db import models

class Setting(models.Model):
    banner_title=models.CharField(max_length=200)
    banner_content=models.TextField()
    banner_image=models.ImageField(upload_to='setting_images/')

    category_title=models.CharField(max_length=100)
    category_icon=models.CharField(max_length=100)

    introduction_title=models.CharField(max_length=100)
    introduction_content=models.TextField()
    introduction_image=models.ImageField(upload_to='category_images/')
    name=models.CharField(max_length=100)
    profession=models.CharField(max_length=100)


    job_title=models.CharField(max_length=100)
    job_content=models.TextField()

    job2_title=models.CharField(max_length=100)
    job2_content=models.TextField()
    users=models.IntegerField(default=0)
    jobs=models.IntegerField(default=0)
    video=models.FileField(upload_to='setting_files/')


    recent_title=models.CharField(max_length=100)
    recent_content=models.TextField()

    customer_title=models.CharField(max_length=100)

    over_title=models.CharField(max_length=100)
    over_content=models.TextField()

#about

    about_title=models.CharField(max_length=100)
    service_title=models.CharField(max_length=100)


# job detail
    
    job_detail=models.CharField(max_length=100)
    similar_title=models.CharField(max_length=100)
    similar_text=models.TextField()

#contact

    contact_title=models.CharField(max_length=100)
    message_title=models.CharField(max_length=100)

    def __str__(self):
        return self.job_title
    


class Job(models.Model):
    FULL_TIME = 'Full time'
    PART_TIME = 'Part time'
    FREELANCE = 'Freelance'

    JOB_TYPE_CHOICES = [
        (FULL_TIME, 'Tam ştat'),
        (PART_TIME, 'Yarim ştat'),
        (FREELANCE, 'Frilanser'),
    ]

    JUNIOR = 'Junior'
    MID = 'Middle'
    SENIOR = 'Senior'
    LEVEL_CHOICES = [
        (JUNIOR, 'Junior'),
        (MID, 'Mid-Level'),
        (SENIOR, 'Senior'),
    ]
    name=models.CharField(max_length=100)
    icon=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    price=models.IntegerField(default=0)
    level=level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default=JUNIOR,
    )
    
    job_type= models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES,
        default=FULL_TIME,
    )

    
    def __str__(self):
        return self.name
   

class Recent_jobs(models.Model):

    FULL_TIME = 'Full time'
    PART_TIME = 'Part time'
    FREELANCE = 'Freelance'

    JOB_TYPE_CHOICES = [
        (FULL_TIME, 'Tam ştat'),
        (PART_TIME, 'Yarim ştat'),
        (FREELANCE, 'Frilanser'),
    ]

    JUNIOR = 'Junior'
    MID = 'Middle'
    SENIOR = 'Senior'
    LEVEL_CHOICES = [
        (JUNIOR, 'Junior'),
        (MID, 'Mid-Level'),
        (SENIOR, 'Senior'),
    ]

    company=models.CharField(max_length=100)
    image=models.ImageField(upload_to='job_images/')
    name=models.CharField(max_length=100)
    icon=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    price=models.IntegerField(default=0)
    level=level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default=JUNIOR,
    )
    
    job_type= models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES,
        default=FULL_TIME,
    )

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    SALES_MANAGER = 'Sales Manager'
    TECHNICAL_LEADER = 'Tech Leader'
    DEV_OPS = 'DevOps'
    PRODUCT_MANAGER = 'Product Manager' 

    PROFESSION_CHOICES = [
        (SALES_MANAGER, 'Sales Manager'),
        (TECHNICAL_LEADER, 'Technical Leader'),
        (DEV_OPS, 'DevOps'),
        (PRODUCT_MANAGER, 'Product Manager'), 
    ]

    name=models.CharField(max_length=100)
    stars=models.IntegerField(default=0)
    content=models.TextField()
    image=models.ImageField(upload_to='customer_images/')
    profession= profession = models.CharField(
        max_length=20,
        choices=PROFESSION_CHOICES,
        default=DEV_OPS,  
    )

    def __str__(self):
        return self.name
    

class Service(models.Model):
    name=models.CharField(max_length=100)
    icon=models.CharField(max_length=100)
    content=models.TextField()

    def __str__(self):
        return self.name
    

class Jobdetail(models.Model):
    FULL_TIME = 'Full time'
    PART_TIME = 'Part time'
    FREELANCE = 'Freelance'

    JOB_TYPE_CHOICES = [
        (FULL_TIME, 'Tam ştat'),
        (PART_TIME, 'Yarim ştat'),
        (FREELANCE, 'Frilanser'),
    ]

    JUNIOR = 'Junior'
    MID = 'Middle'
    SENIOR = 'Senior'
    LEVEL_CHOICES = [
        (JUNIOR, 'Junior'),
        (MID, 'Mid-Level'),
        (SENIOR, 'Senior'),
    ]
    head_title=models.CharField(max_length=100)
    main_title=models.CharField(max_length=100)
    main_content=models.TextField()
    role_title=models.CharField(max_length=100)
    role_content=models.TextField()
    requirement_title=models.CharField(max_length=100)
    requirement_content=models.TextField()
    
    location=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    price=models.IntegerField(default=0)
    level=level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default=JUNIOR,
    )
    
    job_type= models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES,
        default=FULL_TIME,
    )

    def __str__(self):
        return self.head_title
    

class Contact(models.Model):
    icon=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    content=models.TextField()

    def __str__(self):
        return self.title
    



    