from rest_framework.routers import SimpleRouter

from .views import (
    CategoriaViewSet,
    CidadeViewSet,
    ModalidadeEntregaViewSet,
    UnidadeViewSet,
)

router = SimpleRouter()
router.register('cidades', CidadeViewSet)
router.register('unidades', UnidadeViewSet)
router.register('categorias', CategoriaViewSet)
router.register('modalidade-entrega', ModalidadeEntregaViewSet)

urlpatterns = router.urls