from django.urls import path
from web_app.views import home,privacy_policy,isn_insights,isn_platform,partnership_request,our_journey,isn_insight,currier_opportunity

urlpatterns = [
    path("",home,name="home"),
    path("privacy-policy",privacy_policy,name="privacy"),
    path("insights",isn_insights,name="insights"),
    path("insight/<str:slug>",isn_insight,name="insight"),
    path("platform",isn_platform,name="isn_platform"),
    path("contact/<str:contact_type>",partnership_request,name="partnership_request"), #partnership and us
    path("journey",our_journey,name="our_journey"),
    path('jobs',currier_opportunity,name="currier_opportunity")
]

