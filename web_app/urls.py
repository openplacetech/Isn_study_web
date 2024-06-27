from django.urls import path
from web_app.views import home,privacy_policy,isn_insights,isn_platform,partnership_request

urlpatterns = [
    path("",home,name="home"),
    path("privacy-policy",privacy_policy,name="privacy"),
    path("insights",isn_insights,name="insights"),
    path("platform",isn_platform,name="isn_platform"),
    path("contact/<str:contact_type>",partnership_request,name="partnership_request") #partnership and us
]

