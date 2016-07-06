from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.recipe_list, name='recipe_list'),
    url(r'^recipe/(?P<recipe_title>\d+)/$', views.recipe_details, name='recipe_details'),
    url(r'^NewRecipe/$', views.recipe_add, name='recipe_add'),
    url(r'^recipe/(?P<pk>\d+)/edit/$', views.recipe_edit, name='recipe_edit'),
    url(r'^test_hero', views.test_hero, name='test_hero'),
]