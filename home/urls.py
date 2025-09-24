from django.urls import path
from .views import MenuCategoryListView, MenuItemSearchViewSet


menu_item_update = MenuItemVewSet.as_view({
    'put': 'update',
})


menu_item_search = MenuItemSearchViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    path('categories/', MenuCategoryListView.as_view(), name='menu-categories'),
    path('menu-item/<int:pk>/', menu_item_update, name='menu-item-update'),
    path('menu-items/search/', menu_item_search, name='menu-item-search'),
]
