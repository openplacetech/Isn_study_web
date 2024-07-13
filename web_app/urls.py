from django.urls import path
from web_app.views import home,privacy_policy,isn_insights,isn_platform,partnership_request,\
    our_journey,isn_insight,currier_opportunity,our_teams,isn_market_entry,apply_job,job_detail

urlpatterns = [
    path("",home,name="home"),
    path("privacy-policy",privacy_policy,name="privacy"),
    path("insights",isn_insights,name="insights"),
    path("insight/<str:slug>",isn_insight,name="insight"),
    path("platform",isn_platform,name="isn_platform"),
    path("contact/<str:contact_type>",partnership_request,name="partnership_request"), #partnership and us
    path("journey",our_journey,name="our_journey"),
    path('jobs',currier_opportunity,name="currier_opportunity"),
    path('job/<str:slug>',job_detail,name='job_detail'),
    path('apply/<str:job_id>',apply_job,name="apply_job"),
    path('market-entry',isn_market_entry,name='isn_market_entry'),
    path('teams',our_teams,name='teams'),

]

