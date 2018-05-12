"""API routers."""
from rest_framework import routers

from core import views as core_views
from showcase_site import views as showcase_site_views

app_name = 'api'

# Register API routes here

router = routers.DefaultRouter(trailing_slash=True)

# Showcase site views
router.register('articles', showcase_site_views.ArticleViewSet)
router.register('categories', showcase_site_views.CategoryViewSet)
router.register('testimonies', showcase_site_views.TestimonyViewSet)
router.register('keyfigures', showcase_site_views.KeyFigureViewSet)
router.register('partners', showcase_site_views.PartnerViewSet)
router.register('actions', showcase_site_views.ActionViewSet)

# Core views
router.register('documents', core_views.DocumentViewSet)

urlpatterns = router.urls
