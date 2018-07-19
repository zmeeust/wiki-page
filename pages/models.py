from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Page(models.Model):
    """Page model definition"""
    created = models.DateTimeField(auto_now_add=True)
    current_version = models.OneToOneField('pages.Version', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return 'Wiki page - {}'.format(self.pk)

    def get_absolute_url(self):
        return reverse('page-detail',  kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created']


class Version(models.Model):
    """Version model definition"""
    title =  models.CharField(max_length=60)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    version = models.IntegerField(default=0)
    current_page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='version')

    def __str__(self):
        return 'Wiki {} page version - {}'.format(self.current_page.pk, self.version)

    class Meta:
        ordering = ['-version']


@receiver(pre_save, sender=Version)
def update_version(sender, instance, **kwargs):
    """When updating the model, the version is incremented by one"""
    instance.version += 1
