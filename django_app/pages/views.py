from django.shortcuts import render, redirect

from .models import (
    Banner, InternetPlan, Combo, Service, SelfServiceItem,
    AppPromo, MegaEnergiaHome, EnergyHero, EnergySavings,
    EnergyFeature, EnergyStep, TrackingHero, TrackingFeature,
    TrackingBenefit, TrackingCTA, BlogPost,
)


def home(request):
    return render(request, 'pages/home.html', {
        'banners': Banner.objects.filter(page='home', is_active=True),
        'plans': InternetPlan.objects.filter(page='home', is_active=True).prefetch_related('features'),
        'combos': Combo.objects.all(),
        'services': Service.objects.all(),
        'self_service_items': SelfServiceItem.objects.all(),
        'app_promo': AppPromo.objects.filter(page='home').first(),
        'mega_energia': MegaEnergiaHome.load(),
    })


def energia(request):
    return render(request, 'pages/energia.html', {
        'hero': EnergyHero.load(),
        'savings': EnergySavings.load(),
        'features': EnergyFeature.objects.all(),
        'steps': EnergyStep.objects.all(),
    })


def rastreamento(request):
    return render(request, 'pages/rastreamento.html', {
        'hero': TrackingHero.load(),
        'features': TrackingFeature.objects.all(),
        'benefits': TrackingBenefit.objects.all(),
        'app_promo': AppPromo.objects.filter(page='rastreamento').first(),
        'cta': TrackingCTA.load(),
    })


def algar(request):
    return render(request, 'pages/algar.html', {
        'banners': Banner.objects.filter(page='algar', is_active=True),
        'plans': InternetPlan.objects.filter(page='algar', is_active=True).prefetch_related('features'),
        'self_service_items': SelfServiceItem.objects.all(),
        'app_promo': AppPromo.objects.filter(page='algar').first(),
        'blog_posts': BlogPost.objects.all(),
    })


def lojas(request):
    return redirect('https://megalinktelecom.com.br/lojas')
