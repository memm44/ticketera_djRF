from django.db import models
from django.conf import settings


class OwnerModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Responsible(OwnerModel):
    id = models.CharField(max_length=20, null=False, blank=False, primary_key=True)

    def __str__(self):
        return self.id


class Issue(OwnerModel):
    id = models.AutoField(auto_created=True, primary_key=True)
    issue = models.CharField(max_length=50, null=False, blank=False, )
    id_issuer = models.CharField(max_length=20, null=False, blank=False, unique=True)
    id_responsible = models.ForeignKey(Responsible, null=True, blank=True,
                                       on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id_issuer)
