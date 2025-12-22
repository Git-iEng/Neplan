# In iEngApp/urls.py
from django.urls import path
from . import views
from .views import contact_section
app_name = 'cmmsApp'
from .views import request_demo_view

urlpatterns = [
      path("request-demo/", views.request_demo_view, name="request_demo"),
    # path("contact-thanks/", views.thanks_view, name="contact_thanks"),  # if you add a separate thanks view for demo
    path('', views.home, name='home'),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
   

    # path('contact/', views.contact, name='contact'),
    # path("contacts/", views.contact_section, name="contact_section"),
path("product/", views.product, name="product"),
   path("contact/", views.contact, name="contact"),
    path('about/', views.about, name='about'),
    # path('contacts/', views.contact_section, name='contact_section'),
    path('contact/thanks/', views.contact_thanks, name='contact_thanks'),
       path("sitemap.xml", views.sitemap, name="sitemap"),
    # More URLs
     # --- NEW: consulting block form + helper ---
    path("contact/submit/", views.contact_block_submit, name="contact_submit"),
    path("contact/phone-info/", views.phone_info, name="phone_info"),
    path('neplan-electricity/', views.neplan_electricity, name='neplan-electricity'),
     path('neplan-gas-water-heating/', views.neplan_gas_water_heating, name='neplan-gas-water-heating'),

     path('product/neplan-electricity/', views.neplan_electricity, name='neplan-electricity'),
     path('product/neplan-gas-water-heating/', views.neplan_gas_water_heating, name='neplan-gas-water-heating'),
    path("contact/country-list/", views.country_list, name="country_list"),
path('neplan-anywhere/', views.neplan_anywhere, name='neplan_anywhere'),
path('services/', views.services, name='services'),
path('neplan-additional-solutions/', views.neplan_additional_solutions, name='neplan_additional_solutions'),

path('neplan-integration-oem-sas/', views.neplan_integration, name='neplan_integration'),
path('neplan-cloud/', views.neplan_cloud, name='neplan_cloud'),
path('neplan-research/', views.neplan_research, name='neplan_research'),


path('product/neplan-anywhere/', views.neplan_anywhere, name='neplan_anywhere'),
path('neplan-asset-management/', views.neplan_asset_management, name='neplan_asset_management'),

path('product/neplan-additional-solutions/', views.neplan_additional_solutions, name='neplan_additional_solutions'),
    # contact section
    path('contact/', views.contact, name='contact'),
    path('neplan-gas-water-heating/contact/', views.contact, name='contact'),
    path('neplan-anywhere/contact/', views.contact, name='contact'),
      path('neplan-additional-solutions/contact/', views.contact, name='contact'),

]
