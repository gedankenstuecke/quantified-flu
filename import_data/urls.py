from django.urls import path

from .views import complete_fitbit, remove_fitbit, update_fitbit
from .views import authorize_oura, complete_oura, remove_oura, update_oura
from .views import authorize_googlefit, complete_googlefit, remove_googlefit, update_googlefit, garmin_dailies, authorize_garmin, complete_garmin, remove_garmin

app_name = "import_data"

urlpatterns = [
    path("complete-fitbit/", complete_fitbit, name="complete-fitbit"),
    path("remove-fitbit/", remove_fitbit, name="remove-fitbit"),
    path("update-fitbit/", update_fitbit, name="update-fitbit"),
    path("authorize-oura/", authorize_oura, name="authorize-oura"),
    path("complete-oura/", complete_oura, name="complete-oura"),
    path("remove-oura/", remove_oura, name="remove-oura"),
    path("update-oura/", update_oura, name="update-oura"),
    path('complete-googlefit/', complete_googlefit, name='complete-googlefit'),
    path('authorize-googlefit/', authorize_googlefit, name='authorize-googlefit'),
    path('update-googlefit/', update_googlefit, name='update-googlefit'),
    path('remove-googlefit/', remove_googlefit, name='remove-googlefit'),
    path('garmin/dailies/', garmin_dailies, name='garmin-dailies'),
    path('authorize-garmin/', authorize_garmin, name='authorize-garmin'),
    path('complete-garmin/<str:resource_owner_secret>/', complete_garmin, name='complete-garmin'),
    path("remove-garmin/", remove_garmin, name="remove-garmin"),

]
