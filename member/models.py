from django.db import models
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Expertise(models.Model):
    """Bidang keahlian supervisor"""
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)


class Member(models.Model):
    """Pengganti User, include student dan supervisor"""
    LEVEL_CHOICES = (('st', 'mahasiswa'), ('sp', 'pembimbing'))
    STATUS_CHOICES = (('a', 'aktif'), ('b', 'banned'), ('n', 'nonaktif'))

    # username = models.CharField(max_length=50, unique=True)
    # password = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    nim = models.CharField(max_length=20, null=True, blank=True)
    npp = models.CharField(max_length=20, null=True, blank=True)
    # name = models.CharField(max_length=50)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    # email = models.CharField(max_length=200)
    expertise = models.ManyToManyField(Expertise, blank=True)
    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    status = models.CharField(max_length=1, default='a', choices=STATUS_CHOICES)
    supervisor = models.ForeignKey("self", null=True, blank=True)

    def __str__(self):
        return self.user.username

    # def save(self, *args, **kwargs):
    #     self.set_password()
    #     super(Member, self).save(*args, **kwargs)

    # def set_password(self):
    #     hasher = PBKDF2PasswordHasher()
    #     self.password = hasher.encode(password=self.password,
    #                                   salt='asdfa3u45tje*UKJ&*TYGH*&HBJK',
    #                                   iterations=20)[-44:]

    # def check_password(self, inp_password):
    #     hasher = PBKDF2PasswordHasher()
    #     return (self.password == hasher.encode(password=inp_password,
    #                                            salt='asdfa3u45tje*UKJ&*TYGH*&HBJK',
    #                                            iterations=20)[-44:])


# class MemberToken(models.Model):
#     """Token untuk login"""
#     member = models.ForeignKey(Member)
#     token = models.CharField(max_length=20)
#     status = models.CharField(max_length=1)

#     @staticmethod
#     def create_token(member):
#         token = get_random_string(length=20)
#         while MemberToken.objects.filter(token=token).count() > 0:
#             token = get_random_string(length=20)

#         MemberToken.objects.create(member=member, token=token, status='a')
#         return token
    