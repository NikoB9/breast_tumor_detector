"""breast_tumor_detector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from . import views, algosViews, settings
from django.views.static import serve
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

handler404 = "breast_tumor_detector.views.handler404"
handler500 = "breast_tumor_detector.views.handler500"

urlpatterns = [
	path('', views.home, name='home'),
	path('what', views.home, name='what'),
	path('us', views.us, name='us'),
	path('detector', views.detector, name='detector'),
   path('algoSVM', views.algoSVM, name='algoSVM'),
   path('algoKNN', views.algoKNN, name='algoKNN'),
   path('algoRandomForest', views.algoRandomForest, name='algoRandomForest'),

	re_path(r'svm/(?P<kind>\d{1})$', algosViews.svm, name='svm'),
	re_path(r'randomForest$', algosViews.rf, name='rf'),
	re_path(r'knn$', algosViews.knn, name='knn'),

	re_path(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),
]  
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
