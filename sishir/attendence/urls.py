from django.urls import path
from .import views

urlpatterns=[
    path('',views.homepage,name='homepage'),
    # path('add',views.add,name='add')
    path('registrations/',views.registrations,name='registrations'),
    # path('',views.create_dataset,name='create dataset')
    # path('capture_photo/', views.capture_photo, name='capture_photo')
    path('registrations/takephoto/',views.capture_photo)
]


