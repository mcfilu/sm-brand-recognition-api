from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Campaign(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.IntegerField()

    def __str__(self):
        return self.name

class CampaingHints(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/campaigns/hints/')
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True, blank=True)

class Influencers(models.Model):
    username = models.CharField(max_length=50)
    instagram_link = models.URLField(_("link to the "), max_length=200)
    profile_image = models.ImageField(upload_to='images/influencers/profile_images/')
    campaing = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Posts(models.Model):
    post_image = models.ImageField(upload_to='images/influencers/post_images/')
    post_image_processed = models.ImageField(upload_to='images/influencers/post_images/processed/', null=True, blank=True)
    post_link = models.URLField(_("link to the "), max_length=200)
    post_description = models.CharField(max_length=2200)
    post_sentiment = models.DecimalField(_("sentiment of the post"), max_digits=6, decimal_places=5, null=True, blank=True)
    post_subjectivity = models.DecimalField(_("subjectivity of the post"), max_digits=6, decimal_places=5, null=True, blank=True)
    influencer = models.ForeignKey(Influencers, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_link

class Comments(models.Model):
    comment = models.CharField(max_length=2200)
    sentiment = models.DecimalField(_("sentiment of the comment"), max_digits=6, decimal_places=5, null=True, blank=True)
    subjectivity = models.DecimalField(_("subjectivity of the comment"), max_digits=6, decimal_places=5, null=True, blank=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


