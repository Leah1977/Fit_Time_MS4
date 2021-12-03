from django.contrib import admin
from .models import ProductReview


# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product',
        'user',
        'rating',
        'date_posted',
    )

admin.site.register(ProductReview)
