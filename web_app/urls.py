from django.urls import path
from web_app.views import home,privacy_policy,isn_insights,isn_platform,partnership_request,\
    our_journey,isn_insight,currier_opportunity,our_teams,isn_market_entry,apply_job,job_detail,subscription_view,\
    insight_comment,something_went_wrong,success

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
    path('subscription',subscription_view, name="subscription"),
    path('comment',insight_comment,name="insight_comment"),
    path('error',something_went_wrong,name="error"),
    path('success',success,name="success")

]

