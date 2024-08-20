from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter()

router.register('api/productos', ProductViewSet, 'todos') #aqui se registra la ruta de la api
router.register('api/categorias', CategoryViewSet, 'categorias') #aqui se registra la ruta de la api
urlpatterns = router.urls