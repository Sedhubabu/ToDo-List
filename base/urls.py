from django.urls import path
from .views import TaskList, TaskDetail ,TaskCreateView , TaskUpdate , TaskDelete , CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('Register/', RegisterPage.as_view(), name='Register'),
    path('', TaskList.as_view(), name='tasklist'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/create/', TaskCreateView.as_view(), name='task-create'),
    path('task-Update/<int:pk>/', TaskUpdate.as_view(), name='task-Update'),
    path('task-Delete/<int:pk>/', TaskDelete.as_view(), name='task-Delete'),

]
