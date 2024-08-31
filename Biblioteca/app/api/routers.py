from rest_framework.routers import DefaultRouter
from ..Libros.views import *
from ..Status.views import *

router = DefaultRouter()

router.register(r'Libros', LibrosViewset, basename='Libros')
router.register(r'Status', StatusViewset, basename='Status')


urlpatterns = router.urls