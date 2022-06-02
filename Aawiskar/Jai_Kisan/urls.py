from django.urls import path
from Jai_Kisan import views
from django.contrib import messages
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    # path('', views.index),
    path('', views.ProductView.as_view(), name="home"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("search/", views.search, name="Search"),
    path('venderregistration/', views.VenderRegistrationView.as_view(), name="venderregistration"),
    path('farmerregistration/',views.FarmerRegistrationView.as_view(),name='farmerregistration'),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('venderaddproduct/', views.vender_add_product, name='vender-add-product'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('checkout/', views.checkout, name='checkout'),
    path('address/', views.address, name='address'),
    path('booked/', views.Booked_placed, name='booked'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('farmer/', views.farmer, name='farmer'),
    path('farmserv/',views.farmserv,name='farmserv'), 
    path('booking/',views.booking,name='booking'),
    path('vendor/',views.vendor, name='vendor'),
    path('amigo/',views.amigo,name='amigo'),
    path('farmer/transport/',views.transport,name='transport'),
    path('tracter/', views.tracter, name='tracter'),
    path('tracter/<slug:data>', views.tracter, name='tracterdata'),
    path('drones/', views.drones, name='drones'),
    path('drones/<slug:data>', views.drones, name='dronesdata'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='Jai_Kisan/login.html', authentication_form=LoginForm)
         , name='login'),
#     path('accounts/login/', auth_views.LoginView.as_view(template_name='Jai_Kisan/vendorlogin.html', authentication_form=LoginForm)
     # , name='venderlogin'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/',
         auth_views.PasswordChangeView.as_view(template_name='Jai_Kisan/passwordchange.html', form_class=MyPasswordChangeForm,
                                               success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='Jai_Kisan/passwordchangedone.html'),
         name='passwordchangedone'),

    path("password-reset/",
         auth_views.PasswordResetView.as_view(template_name='Jai_Kisan/password_reset.html', form_class=MyPasswordResetForm),
         name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='Jai_Kisan/password_reset_done.html'),
         name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(template_name='Jai_Kisan/password_reset_confirm.html',
                                                     form_class=MySetPasswordForm), name="password_reset_confirm"),
    path("password-reset-complete/",
         auth_views.PasswordResetCompleteView.as_view(template_name='Jai_Kisan/password_reset_complete.html'),
         name="password_reset_complete"),

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
