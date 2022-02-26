from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.


def user_path(instance, filename):
    from random import choice
    import string

    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]

    return 'accounts/{}/{}.{}'.format(instance.user.username, pid, extension)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField('Nickname', max_length=20, unique=True)
    about = models.CharField(max_length=300, blank=True)

    GENDER_C = (
        ('N/A', 'Prefer Not to Choose'),
        ('F', 'Female'),
        ('M', 'Male'),
    )
    gender = models.CharField('Gender(Optional)',
                              max_length=25,
                              choices=GENDER_C,
                              default='N')

    picture = ProcessedImageField(upload_to=user_path,
                                  processors=[ResizeToFill(150, 150)],
                                  format='JPEG', options={'quality': 90},
                                  blank=True)

    def __str__(self):
        return self.nickname
