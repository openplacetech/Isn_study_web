from django.contrib import admin
from django.urls import path,include
from web_app.views import home,privacy_policy,isn_insights

urlpatterns = [
    path("",home,name="home"),
    path("privacy-policy",privacy_policy,name="privacy"),
    path("insights",isn_insights,name="insights"),
]

