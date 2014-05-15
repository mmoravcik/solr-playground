from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, blank=True)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    PENDING, PUBLISHED = 1, 2
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (PUBLISHED, 'Rejected'),
        (PUBLISHED, 'Published'),
    )

    title = models.CharField(max_length=128, blank=True)
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=PENDING)
    date_created = models.DateTimeField()
    highlighted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title