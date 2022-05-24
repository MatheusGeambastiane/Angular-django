#Django
from django.contrib import admin
from django.urls import path, include
#Myapps
from clinica.views import ExamViewSet
#3rd Party
from rest_framework import routers, serializers 


admin.site.site_title = 'Administração'
admin.site.index_title = 'Administração Medicar'
admin.site.site_header = 'Medicar'



router = routers.DefaultRouter()

router.register(r'Exames', ExamViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
    ]
