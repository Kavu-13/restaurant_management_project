from django.urls import path
from .views import MenuCategoryListView


menu_item_update = MenuItemVewSet.as_view({
    'put': 'update',
})
urlpatterns = [
    path('categories/', MenuCategoryListView.as_view(), name='menu-categories'),
    path('menu-item/<int:pk>/', menu_item_update, name='menu-item-update'),
]
