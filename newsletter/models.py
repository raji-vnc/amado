from django.db import models

class NewsLetterSubscriber(models.Model):
    email=models.EmailField(unique=True)
    subscribed_at=models.DateField(auto_now_add=True)

    class Meta:
        ordering=["-subscribed_at"]
        verbose_name="Newsletter Subscriber"
        verbose_name_plural="Newsletter Subscribers"

    def __str__(self):
        return self.email

# Create your models here.
