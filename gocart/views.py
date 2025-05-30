from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Stop, Schedule, ContactMessage

# -------------------------
# Home
# -------------------------

def home(request):
    stops = Stop.objects.all()
    return render(request, 'gocart/home.html', {'stops': stops})

# -------------------------
# Cart Search & Results
# -------------------------

def search_carts_page(request):
    stops = Stop.objects.all()
    return render(request, 'gocart/search_cart.html', {'stops': stops})

# -------------------------
# Services Views
# -------------------------

def services_view(request):
    services = [
        {
            'image': 'https://res.cloudinary.com/dmpclkrea/image/upload/v1745843951/Pic-01_hwhabw.png',
            'title': 'Gerua-Islamnagar Route',
            'description': 'Connects Gerua gate to Islamnagar residential area through central academic buildings.'
        },
        {
            'image': 'https://res.cloudinary.com/dmpclkrea/image/upload/v1745844274/pic-03_hizzk4.png',
            'title': 'Central Field Route',
            'description': 'Covers the scenic central field area, main cafeteria, and arts faculty with easy EV access.'
        },
        {
            'image': 'https://res.cloudinary.com/dmpclkrea/image/upload/v1745844274/pic-07_azogih.png',
            'title': 'Science Building Route',
            'description': 'Dedicated route for science faculty students, labs, and research centers at JU.'
        },
        {
            'image': 'https://res.cloudinary.com/dmpclkrea/image/upload/v1745844274/pic-06_mqohlb.png',
            'title': 'Library Loop',
            'description': 'Serves the main library, computer center, and nearby academic halls for study-focused rides.'
        },
        {
            'image': 'https://res.cloudinary.com/dmpclkrea/image/upload/v1745844273/pic-05_ccjvob.png',
            'title': 'Botanical Garden Route',
            'description': 'Enjoy a green ride around the JU Botanical Garden, passing scenic nature spots.'
        },
        {
            'image': 'https://res.cloudinary.com/dmpclkrea/image/upload/v1745844274/pic-08_aaxt8t.png',
            'title': 'New Market Shuttle',
            'description': 'Connects campus locations to New Market, ideal for shopping and errands.'
        },
        {
            'image': 'https://res.cloudinary.com/dmpclkrea/image/upload/v1745844276/pic-02_ru0lju.png',
            'title': 'Medical Center Route',
            'description': 'Ensuring fast EV access to the JU Medical Center for emergencies.'
        },
        {
            'image': 'https://res.cloudinary.com/dmpclkrea/image/upload/v1745844276/pic-09_db7qad.png',
            'title': 'VC Residence to Main Gate',
            'description': 'Special EV line connecting VC Residence, registrar building, and Main Gate swiftly.'
        },
        {
            'image': 'https://res.cloudinary.com/dmpclkrea/image/upload/v1745844275/pic-04_umcaea.png',
            'title': 'Full Campus Circle',
            'description': 'Complete circle covering all major points around JU campus — ideal for newcomers and tours.'
        }
    ]
    return render(request, 'gocart/services.html', {'services': services})

# -------------------------
# Pricing View
# -------------------------

def pricing_view(request):
    return render(request, 'gocart/pricing.html')


# -------------------------
# Contact Us View
# -------------------------

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        # messages.success(request, "Thank you! Your message has been sent successfully.")
        return redirect('contact')  # Refresh the page after successful submit

    return render(request, 'gocart/contact.html')


# -------------------------
# Driver Management Views
# -------------------------

@login_required
def driver_trips(request):
    # filter only schedules assigned to this driver
    qs = Schedule.objects.filter(cart__driver=request.user)
    date = request.GET.get('travel_date')
    if date:
        qs = qs.filter(travel_date=date)
    return render(request, 'gocart/driver_trips.html', {
        'trips': qs.order_by('start_time'),
    })
