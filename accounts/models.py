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
    follow_set = models.ManyToManyField('self', # referring itself
                                       blank=True, # following nobody yet
                                       through='Follow', # middleware
                                       symmetrical=False,) 

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
    
    @property
    def get_follower(self):
        return [i.from_user for i in self.follower_user.all()]
    
    @property
    def get_following(self):
        return [i.to_user for i in self.follow_user.all()]
    
    @property
    def follower_count(self):
        return len(self.get_follower)
    
    @property
    def following_count(self):
        return len(self.get_following)
    
        
    def is_follower(self, user):
        return user in self.get_follower
    
    def is_following(self, user):
        return user in self.get_following
    
    

class Follow(models.Model):
    from_user = models.ForeignKey(Profile, related_name='follow_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(Profile, related_name='follower_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): ## instance tracking
        return "{} Follows {}".format(self.from_user, self.to_user)
    
    class Meta:
        unique_together = (
            ('from_user', 'to_user')        
        )
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
