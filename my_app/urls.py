from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    	   
    path('category-form', views.categoryForm),	   
    path('form-actor', views.ActorForm),	   
    path('create-category', views.createCategory),	   
    path('create-movie', views.formMovie),	   
    path('store-actor-on-database', views.createActor),	   
    path('store-movie-on-database', views.createMovie),	   
    path('add-actor-to-move', views.addActorToMove),	   
    path('create-user-form', views.createuserForm),	   
    path('create_user', views.createUser),	   
    path('remove-actore-from-movie/<int:actor_id>/<int:movie_id>', views.removeActroFromMovie),	   
    path ('search/' , views.Serach_Request), 

]
