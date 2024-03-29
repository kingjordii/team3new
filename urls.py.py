from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('games/', views.games_view, name='games'),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    # Paths for math game challenges
    path('static_math_challenge/', views.static_math_challenge, name='static_math_challenge'),
    path('algebra_challenge/', views.algebra_challenge, name='algebra_challenge'),
    path('geometry_challenge/', views.geometry_challenge, name='geometry_challenge'),
    path('trigonometry_challenge/', views.trigonometry_challenge, name='trigonometry_challenge'),
    path('probability_challenge/', views.probability_challenge, name='probability_challenge'),
]
