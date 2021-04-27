from rest_framework.routers import DefaultRouter
from .views import EmployeeViewset,ScheduleViewset

router = DefaultRouter()
router.register(r'user',EmployeeViewset)
router.register(r'schedule',ScheduleViewset)
urlpatterns = router.urls