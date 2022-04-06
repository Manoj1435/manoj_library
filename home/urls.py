from django.urls import path
from  home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student/',views.student,name='student'),
    path('signin/',views.signin,name="signin"),
    path('signup/',views.signup,name="signup"),
    path('book_library/',views.book_library,name="book_library"),
    path('show/',views.show,name="show"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
]