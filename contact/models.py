from django.db import models

class Contact(models.Model):
    """ allow a user to Contact us with a message """

    name = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    message = models.TextField(default=0, blank=True, null=False)
    email = models.EmailField(required=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
