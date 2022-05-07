import uuid
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile

# Create your models here.


class Lecture(models.Model):

    INSTRUMENT = (
        ('drums', 'Drums'),
        ('piano', 'Piano'),
        ('bass',  'Bass Guitar'),
        ('guitar', ' Guitar'),
        ('sax', 'Saxophone'),
        ('percusion', 'Percusion'),
        ('singing', 'Vocal Coach'),
        ('others', 'Others'),
    )

    SKILLS = (
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advance", "Advance"),
        ("professional", "Professional"),
        ("master", "Master")
    )

    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="lectures" )
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    video = models.FileField(upload_to='videos/', blank=True, null=True, )
    image = models.FileField(upload_to='images/', null=True, blank=True, default='images/default.jpeg')
    instrument = models.CharField(max_length=100, null=True, blank=True, choices= INSTRUMENT)
    skill = models.CharField(max_length=100, null=True, blank=True, choices= SKILLS)
    price = models.IntegerField(null=True, blank=True)
    discount_price = models.FloatField(blank=True, null=True)
    totalVote = models.IntegerField(default=0, )
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


