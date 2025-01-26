from django.urls import path,include
from .views import registerPage,loginPage,homePage,roomPage,signout,deleteMessage,updateProfile
from .views import CustomUserViewSet,UserMessagesViewSet,listingCreation
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('userDetails', CustomUserViewSet, basename='userDetails')
router.register('messages', UserMessagesViewSet, basename='userMessages')

urlpatterns=[
    path('api',include(router.urls)),
    path('register/',registerPage,name="register"),
    path('login/',loginPage,name="login"),
    path('',homePage,name="home"),
    path('room/<str:pk>/', roomPage, name="room"),
    path('logout/',signout,name='signout'),
    path('delete/<str:pk>/',deleteMessage,name='delete'),
    path('userProfile/',updateProfile,name='updateProfile'),
    path('listing/',listingCreation,name='listing'),

]
