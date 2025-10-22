from rest_framework_nested import routers
from accounts.views.auth import AuthViewSet
from catalog.views import (
    CategoryViewSet,
    ProductViewSet,
    ProductImageViewSet,
    AttributeViewSet,
    AttributeValueViewSet,
    ProductAttributeViewSet,
    VariantViewSet,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register("auth", AuthViewSet, basename="auth")

# catalog
router.register("catalog/categories", CategoryViewSet, basename="catalog-category")
router.register("catalog/products", ProductViewSet, basename="catalog-product")
router.register("catalog/images", ProductImageViewSet, basename="catalog-image")
router.register("catalog/attributes", AttributeViewSet, basename="catalog-attribute")
router.register("catalog/attribute-values", AttributeValueViewSet, basename="catalog-attribute-value")
router.register("catalog/product-attributes", ProductAttributeViewSet, basename="catalog-product-attribute")
router.register("catalog/variants", VariantViewSet, basename="catalog-variant")

urlpatterns = [*router.urls]
