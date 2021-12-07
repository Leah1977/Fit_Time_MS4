from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
    """ allow a user to write a review on a Product """

    RATING_OPTIONS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    user = models.ForeignKey(
        UserProfile,
        related_name='reviews',
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews',
    )

    title = models.CharField(max_length=254)
    comment = models.TextField(default=0, blank=True, null=False)
    rating = models.IntegerField(default=0, choices=RATING_OPTIONS)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
