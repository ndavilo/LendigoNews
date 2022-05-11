from django.urls import path
from .views import UserRegisterView, UserEditView, DeleteUserView, Password_ChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('edit_settings/', UserEditView.as_view(), name = 'edit_settings'),
    path('password/', Password_ChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success/', views.password_success, name='password_success'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
    path('<int:pk>/profile/delete', DeleteUserView.as_view(), name='deleteuser'),

]