import uuid
from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

# Create your models here.
len_xlrg = 100
len_lrg = 30
len_med = 25
len_xsml = 20
len_sml = 15
len_vsml = 10
len_uuid = 36


class User(models.Model):
    UID = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    password = models.CharField(max_length=len_med, blank=False, default=None)
    email = models.EmailField(
        max_length=254, blank=False, default=None, unique=True)
    username = models.CharField(
        max_length=len_med, blank=False, default=None, unique=True)
    contact_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contactNo = models.CharField(
        validators=[contact_regex], max_length=17, blank=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.username


class Address(models.Model):
    houseNo_flatNo = models.CharField(max_length=7, blank=False, default="")
    street = models.CharField(max_length=len_xsml, blank=False, default="")
    landmark = models.CharField(max_length=len_xsml, blank=True, default="")
    city = models.CharField(max_length=len_xsml, blank=False, default="")
    state = models.CharField(max_length=len_xsml, blank=False, default="")
    country = models.CharField(max_length=len_xsml, blank=False, default="")
    pincode = models.TextField(default="")

    class Meta:
        abstract = True

    def __str__(self):
        return self.city + " " + self.state + " " + self.country


class Individual(User, Address):
    firstName = models.CharField(max_length=len_sml, blank=False, default=None)
    middleName = models.CharField(max_length=len_sml, blank=True)
    lastName = models.CharField(max_length=len_sml, blank=False, default=None)
    profile_pic = models.FileField(blank=True, default=None, null=True)
    DOB = models.DateField()
    DOJ = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=len_sml)

    def Serialize(self):
        return {
            'UID': self.UID,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'contactNo': self.contactNo,
            'Address': {
                'houseNo': self.houseNo_flatNo,
                'street': self.street,
                'landmark': self.landmark,
                'city': self.city,
                'state': self.state,
                'country': self.country,
            },
            'name': {
                'firstName': self.firstName,
                'middleName': self.middleName,
                'lastName': self.lastName,
            },
            'profilePic': self.profile_pic.path if self.profile_pic else "None",
            'DOB': self.DOB,
            'DOJ': self.DOJ,
            'age': self.age,
            'gender': self.gender,
        }

    def SerializePartial(self):
        return {
            'UID': self.UID,
            'username': self.username,
            'email': self.email,
            'contactNo': self.contactNo,
            'name': {
                'firstName': self.firstName,
                'middleName': self.middleName,
                'lastName': self.lastName,
            },
            'profilePic': self.profile_pic.path if self.profile_pic else "None",
        }

    def __str__(self):
        return self.username


class Organisation(User, Address):
    organisationName = models.CharField(max_length=len_lrg, blank=False)
    organisationLogo = models.FileField(blank=True, default=None, null=True)
    description = models.TextField()

    def __str__(self):
        return self.organisationName + " " + self.username

    def Serialize(self):
        return {
            'UID': self.UID,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'contactNo': self.contactNo,
            'Address': {
                'houseNo': self.houseNo_flatNo,
                'street': self.street,
                'landmark': self.landmark,
                'city': self.city,
                'state': self.state,
                'country': self.country,
            },
            'name': self.organisationName,
            'logo': self.organisationLogo.path if self.organisationLogo else "None",
            'description': self.description,
        }

    def SerializePartial(self):
        return {
            'UID': self.UID,
            'username': self.username,
            'email': self.email,
            'contactNo': self.contactNo,
            'name': self.organisationName,
            'logo': self.organisationLogo.path if self.organisationLogo else "None",
        }


class Category(models.Model):
    CID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=len_xsml, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def Serialize(self):
        return {
            'CID': self.CID,
            'name': self.name
        }


class Jobs(models.Model):
    JID = models.AutoField(primary_key=True)
    CID = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=len_xsml, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Jobs'
        verbose_name_plural = 'Jobs'

    def Serialize(self):
        return {
            'JID': self.JID,
            'name': self.name
        }


class FOI(models.Model):
    UID = models.CharField(max_length=len_uuid)
    JID = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    def __str__(self):
        return self.JID.name

    class Meta:
        verbose_name = 'Field Of Interest'
        verbose_name_plural = 'Field Of Interest'


class JobsAvailable(models.Model):
    UID = models.CharField(max_length=len_uuid)
    JID = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    basePay = models.FloatField()
    timePeriodOfService = models.DurationField()
    negotiable = models.BinaryField()
    DOP = models.DateField()
    noOfRequiredPersonnel = models.PositiveIntegerField()

    def __str__(self):
        return self.UID+" "+self.JID.name

    class Meta:
        verbose_name = 'Jobs Available'
        verbose_name_plural = 'Jobs Available'


class BulkJob(models.Model):
    BID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=len_xsml)
    noOfEmployees = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Bulk Jobs'
        verbose_name_plural = 'Bulk Jobs'


class EBJ(models.Model):
    BID = models.ForeignKey(BulkJob, on_delete=models.CASCADE)
    UID = models.ForeignKey(Individual, on_delete=models.CASCADE)

    def __str__(self):
        return self.BID.title + " " + self.UID.username

    class Meta:
        verbose_name = 'Employee to Bulk Job Connector'
        verbose_name_plural = 'Employee to Bulk Job Connector'


class OBJ(models.Model):
    UID = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    BID = models.ForeignKey(BulkJob, on_delete=models.CASCADE)

    def __str__(self):
        return self.BID.title + " " + self.UID.username

    class Meta:
        verbose_name = 'Organisation to Bulk Job Connector'
        verbose_name_plural = 'Organisation to Bulk Job Connector'


class Review(models.Model):
    RID = models.AutoField(primary_key=True)
    content = models.TextField()
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    def __str__(self):
        return self.RID


class ReviewConnector(models.Model):
    RID = models.ForeignKey(Review, on_delete=models.CASCADE)
    UID = models.CharField(max_length=len_uuid)
    targetID = models.CharField(max_length=len_vsml)

    def __str__(self):
        return self.UID.username + " to " + self.targetID.username

    class Meta:
        verbose_name = 'Review Connector'
        verbose_name_plural = 'Review Connector'


class Follows(models.Model):
    UID = models.ForeignKey(Individual, on_delete=models.CASCADE)
    OrganisationID = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.UID.username + " follows " + self.OrganisationID.organisationName

    class Meta:
        verbose_name = 'Follows'
        verbose_name_plural = 'Follows'
