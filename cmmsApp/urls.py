# In iEngApp/urls.py
from django.urls import path
from . import views

app_name = 'cmmsApp'

urlpatterns = [
    path("request-demo/", views.request_demo_view, name="request_demo"),

    # core
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("product/", views.product, name="product"),
    path("contact/", views.contact, name="contact"),
    path('contact/thanks/', views.contact_thanks, name='contact_thanks'),
    path("sitemap.xml", views.sitemap, name="sitemap"),

    # contact helpers
    path("contact/submit/", views.contact_block_submit, name="contact_submit"),
    path("contact/phone-info/", views.phone_info, name="phone_info"),
    path("contact/country-list/", views.country_list, name="country_list"),

    # solution pages
    path('services/', views.services, name='services'),
    path('neplan-electricity/', views.neplan_electricity, name='neplan_electricity'),
    path('neplan-gas-water-heating/', views.neplan_gas_water_heating, name='neplan_gas_water_heating'),
    path('neplan-anywhere/', views.neplan_anywhere, name='neplan_anywhere'),
    path('neplan-additional-solutions/', views.neplan_additional_solutions, name='neplan_additional_solutions'),
    path('neplan-integration-oem-sas/', views.neplan_integration, name='neplan_integration'),
    path('neplan-cloud/', views.neplan_cloud, name='neplan_cloud'),
    path('neplan-research/', views.neplan_research, name='neplan_research'),
    path('neplan-asset-management/', views.neplan_asset_management, name='neplan_asset_management'),

    # product namespace duplicates kept but with unique names
    path('product/neplan-electricity/', views.neplan_electricity, name='product_neplan_electricity'),
    path('product/neplan-gas-water-heating/', views.neplan_gas_water_heating, name='product_neplan_gas_water_heating'),
    path('product/neplan-anywhere/', views.neplan_anywhere, name='product_neplan_anywhere'),
    path('product/neplan-additional-solutions/', views.neplan_additional_solutions, name='product_neplan_additional_solutions'),

    # contact routes for specific pages (unique names)
    path('neplan-gas-water-heating/contact/', views.contact, name='contact_neplan_gas_water_heating'),
    path('neplan-anywhere/contact/', views.contact, name='contact_neplan_anywhere'),
    path('neplan-additional-solutions/contact/', views.contact, name='contact_neplan_additional_solutions'),
]
