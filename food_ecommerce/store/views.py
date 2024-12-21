from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from .models import Product, Cart, CartItem, CarouselImage, Category
from .forms import CustomUserCreationForm
from django.contrib.auth import login



def index(request):
    images = CarouselImage.objects.all()
    products = Product.objects.all()
    return render(request, 'store/index.html', {'images': images, 'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_detail.html', {'product': product})

def about(request):
    return render(request, 'store/about.html')

@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))
        cart, created = Cart.objects.get_or_create(user=request.user, active=True)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
        return JsonResponse({'success': True, 'quantity': quantity, 'product_name': product.name})
    return JsonResponse({'success': False}, status=400)

@login_required
def view_cart(request):
    cart = Cart.objects.filter(user=request.user, active=True).first()
    return render(request, 'store/cart.html', {'cart': cart})

@login_required
def update_cart(request, item_id, action):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease' and cart_item.quantity > 1:
        cart_item.quantity -= 1
    cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, item_id):
    if request.method == 'POST':
        cart = get_object_or_404(Cart, user=request.user, active=True)
        cart_item = get_object_or_404(CartItem, cart=cart, id=item_id)
        cart_item.delete()
        return redirect('cart')
    return JsonResponse({'success': False}, status=400)
    
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Signup failed.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'store/profile.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')  # Adjust based on your homepage
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'store/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('index')

from django.shortcuts import render, redirect
from django.contrib import messages

def checkout(request):
    if request.method == 'POST':
        # Process the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        # Perform any logic for placing the order

        # Add a success message
        messages.success(request, 'Your order has been placed successfully!')

        # Redirect to the same page to display the message
        return redirect('checkout')

    return render(request, 'store/checkout.html')

def feedback(request):
    if request.method == 'POST':
        # Handle feedback form submission
        # Assuming you have a Feedback model to save the feedback
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        # Save the feedback to the database
        # Feedback.objects.create(name=name, email=email, feedback=feedback)
        return HttpResponse('Thank you for your feedback!')
    return render(request, 'store/feedback.html')

def process_checkout(request):
    # Handle the actual order processing logic here
    return redirect('index')

def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')

        # Process the feedback here (e.g., save to the database)

        messages.success(request, 'Thank you for your feedback!')
        return redirect('feedback')

    return render(request, 'store/feedback.html')

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_detail.html', {'product': product})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # You can handle the data (like sending an email or saving it to the database)
        return render(request, 'store/contact.html', {'success': True})
    return render(request, 'store/contact.html')