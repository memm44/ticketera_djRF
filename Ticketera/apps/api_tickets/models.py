from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save


class OwnerModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Responsible(models.Model):
    id = models.CharField(max_length=20, null=False, blank=False, primary_key=True)

    def __str__(self):
        return self.id


class Issuer(models.Model):
    id = models.CharField(max_length=20, null=False, blank=False, primary_key=True)

    def __str__(self):
        return self.id


class Issue(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    issue = models.CharField(max_length=50, null=False, blank=False, )
    id_issuer = models.ForeignKey(Issuer, null=False, blank=False, on_delete=models.CASCADE, related_name='issues')
    id_responsible = models.ForeignKey(Responsible, null=True, blank=True,
                                       on_delete=models.CASCADE, related_name='responsibles')
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


# pre_save.connect(receiver=get_or_create_issuer, sender=Issue)
