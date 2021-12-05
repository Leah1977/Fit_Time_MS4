from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Review
from .forms import ReviewForm
from products.models import Product
from profiles.models import UserProfile


# # A view to render the all reviews template
# def all_reviews(request):
#     """ A view to show all reviews """

#     reviews = Review.objects.all()
#     direction = None

#     context = {
#         'reviews': reviews,
#         'search_term': query,
#         'current_categories': categories,
#         'current_sorting': current_sorting,
#     }

#     reviews = Review.objects.filter(user=request.user).order_by('-id')

#     return render(request, 'user/reviews.html', {'reviews': reviews})


# # A view to render the product detail template
# def product_detail(request, product_id):
#     """ A view to show individual product details """

#     product = get_object_or_404(Product, pk=product_id)

#     context = {
#         'product': product,
#     }

#     return render(request, 'products/product_detail.html', context)


# A view to render the add review template

# if request.method == 'POST':
#     form = ProductForm(request.POST, request.FILES)
#     if form.is_valid():
#         product = form.save()
#         messages.success(request, "Successfully added product!")
#         return redirect(reverse('product_detail', args=[product.id]))
#     else:
#         messages.error(request, 'Failed to add product. \
#             Please ensure the form is valid')
# else:
#     form = ProductForm()

# template = 'products/add_product.html'
# context = {
#     'form': form,
# }

# return render(request, template, context)

@login_required
def add_review(request, product_id):
    """ Add a review to a product """
    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            comment = request.POST['comment']
            rating = request.POST['rating']
            review = Review.objects.create(
                user=user,
                product=get_object_or_404(Product, pk=product_id),
                title=title,
                comment=comment,
                rating=rating)
            messages.success(request, "Successfully added review!")
            return redirect(reverse(
                'product_detail',
                args=[product.id]
            ))
        else:
            messages.error(request, 'Failed to add review. \
                Please ensure the form is valid')
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


# A view to render the edit review template
@login_required
def edit_review(request, review_id):
    """ Edit a review """
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(
            request.POST, request.FILES,
            instance=review
            )
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated review!")
            return redirect(
                reverse(
                'product_detail',
                 args=(review.product.id)))
        else:
            messages.error(request, 'Failed to edit review. \
                Please ensure the form is valid')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing review for {product.name}')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'product': review.product,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a product review """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('product_detail', args=(review.product.id)))
