from rest_framework import routers
from .views import team_viewset


router=routers.DefaultRouter()
router.register('Team',team_viewset)