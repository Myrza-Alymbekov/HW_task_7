from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


from account import views as acc_view
from shop import views as shop_view

acc_router = DefaultRouter()
acc_router.register('register', acc_view.ProfileListAPIView)


shop_router = DefaultRouter()
shop_router.register('category', shop_view.CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/auth/token/', obtain_auth_token),


    path('api/account/', include(acc_router.urls)),
    path('api/shop/', include(shop_router.urls)),

    path('api/shop/category/<int:category_id>/item/', shop_view.ItemListCreateAPIView.as_view()),
    path('api/shop/category/<int:category_id>/item/<int:pk>/', shop_view.ItemRetrieveUpdateDestroy.as_view()),
    path('api/shop/category/<int:category_id>/item/<int:item_id>/order/', shop_view.OrderListCreateAPIView.as_view()),
    path('api/shop/category/<int:category_id>/item/<int:item_id>/order/<int:pk>/', shop_view.OrderRetrieveUpdateDestroy.as_view()),

]