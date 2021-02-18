from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

app_name='snippets'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

# explicit ViewSets based view version==================================================
# from django.urls import path
# from rest_framework import renderers
# from rest_framework.urlpatterns import format_suffix_patterns
#
# from snippets.views import SnippetViewSet, UserViewSet, api_root
#
#
# app_name='snippets'
#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])

# class based views version==============================================================
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views
# 
# app_name='snippets'
# urlpatterns = [
#     path('', views.api_root),
#
#     path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
#     path('snippets/<int:pk>/highlite/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
#
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

# function base views version
# from django.urls import path
# from snippets import views
#
#
# app_name='snippets'
# # urlpatterns = [
# #     path('', views.snippet_list, 'snippet-list'),
# #     path('<int:pk>/', views.snippet_detail, 'snippet-detail'),
# # ]