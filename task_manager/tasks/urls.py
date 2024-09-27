from django.urls import path, include
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, signup, CategoryCreateView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('accounts/profile/', TaskListView.as_view(), name='profile'),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('signup/', signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('category/new/', CategoryCreateView.as_view(), name='category-create'),
]
