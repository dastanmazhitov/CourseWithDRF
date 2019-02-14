from django.db import models
'''
class Category(models.Model):
    name=models.CharField(max_length=40)
    imgpath=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    logo=models.CharField(max_length=1000)

    def __str__(self):
        return self.address


class Branch(models.Model):
    course=models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE,null=True)
    latitude = models.CharField(max_length=250)
    longitude = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    
    def __str__(self):
        return self.address



class Contact(models.Model):
    CHOISES = (
    (1, "PHONE"),
    (2, "FACEBOOK"),
    (3, "EMAIL"),
    )
    course = models.ForeignKey(Course, related_name='contacts',on_delete=models.CASCADE, null=True)
    type = models.IntegerField(choices=CHOISES, default=1)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value
!!!
'''
class Category(models.Model):
    name = models.CharField(max_length=30)
    imgpath = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Branch(models.Model):
    course = models.ForeignKey(Course, related_name='branches',on_delete=models.CASCADE, null=True)
    latitude = models.CharField(max_length=1000)
    longitude = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)

    def __str__(self):
        return self.address


class Contact(models.Model):
    CHOISES = (
    (1, "PHONE"),
    (2, "FACEBOOK"),
    (3, "EMAIL"),
    )
    course = models.ForeignKey(Course, related_name='contacts',on_delete=models.CASCADE, null=True)
    type = models.IntegerField(choices=CHOISES, default=1)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value
