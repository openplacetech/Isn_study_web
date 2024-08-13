from django.shortcuts import render,redirect
from web_app.forms import PartnershipRequestForm,SubscriberForm,InsightCommentsForm,ApplyForCareerForm
from web_app.models import Insights,Subscriber,StudyDestinationOfNepali,PrivacyPolicy,CareerOpportunities,ISNTeam,Testimonials,InsightComments
from django.conf import settings
from django.core.mail import send_mail
from django.core import serializers
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Count
from web_app.constrants import DISABILITY_TYPE_CHOICES,JOB_TYPE,RACE_ETHNICITY_CHOICES,VETERAN_STATUS_CHOICES,NOTICE_PERIOD,JOB_MODE,STATUS_TYPE,COUNTRY_CHOICES,CONTACT_PHONE_TYPE,GENDER_TYPE,PROFILE_LINK_TYPE
import json


def home(request):

    insight_list = Insights.objects.order_by('-created_at')  # Fetch all items
    latest_items = insight_list[:3]
    testimonials = Testimonials.objects.all()
    map_country_list = {"country":['us']}
    return  render(request,"index.html",{"insights":latest_items,"testimonials":testimonials,"map_country_list":json.dumps(map_country_list)})

def partnership_request(request,contact_type):
    map_country_list = {"country": ['us']}
    if request.method == 'POST':
        form = PartnershipRequestForm(request.POST)
        if form.is_valid():
            partnership=form.save()
            request.session['source_url'] = "partnership"
            return redirect('success')
        else:
            print(form.errors)
            return render(request, 'error.html')
    else:
        form = PartnershipRequestForm()
    if contact_type == "us":
        return render(request, 'contact.html', {'form': form,"map_country_list":json.dumps(map_country_list)})
    elif contact_type == "partnership":
        return render(request, 'partnership.html', {'form': form})
    else:
        return render(request, 'error.html')

def isn_insights(request):
    page_number = request.GET.get('page')
    search = request.GET.get('search')
    latest_items= []
    no_of_item = 9
    if search:
        insight_list = Insights.objects.filter(title__icontains=search).order_by('-created_at')
    else:
        insight_list = Insights.objects.order_by('-created_at')  # Fetch all items
    if page_number == None or page_number == 1:
        latest_items = insight_list[:3]
        no_of_item = 6
    rest_of_items = insight_list[3:]
    paginator = Paginator(rest_of_items, no_of_item)  # Show 10 items per page
    total_pages = paginator.num_pages
    page_obj = paginator.get_page(page_number)
    return render(request,'insights.html',{"latest_items":latest_items,'total_pages':total_pages,'insights':page_obj})

def isn_insight(request,slug):
    comment_page_no = request.GET.get("comment_page")
    if comment_page_no==None:
            comment_page_no = 1
    insight = Insights.objects.get(slug=slug)
    latest = Insights.objects.exclude(id=insight.pk).order_by('-created_at')[:3]
    comment = InsightComments.objects.filter(insight=insight).order_by('-created_at')
    comment_paginator = Paginator(comment,5)
    comment_pages = comment_paginator.num_pages
    page_obj = comment_paginator.get_page(comment_page_no)
    recommendation = Insights.objects.filter(category=insight.category).exclude(id=insight.pk).order_by('-created_at')[:3]
    return render(request,'insight-detail.html',{"insight":insight,"comment_pages":comment_pages,"latest":latest,"comment":page_obj,"recommendation":recommendation})


def isn_platform(request):
    return render(request,'isn_platform.html')


def isn_market_entry(request):
    map_country_list = {"country": ['bf', 'bj', 'ci', 'cv', 'gh', 'gm', 'gn', 'gw', 'lr', 'ml', 'mr',
                                   'ne', 'ng', 'sn', 'sl', 'tg','bn', 'kh', 'id', 'la', 'my', 'mm', 'ph', 'sg',
                                   'th', 'tl', 'vn','bz', 'cr', 'sv', 'gt','hn', 'mx', 'ni', 'pa','ar', 'bo',
                                   'br', 'cl', 'co', 'ec', 'gy', 'py', 'pe', 'sr', 'uy', 've', 'in', 'af', 'tj', 'kg', 'np', 'lk', 'gf']}
    wast_africa = serializers.serialize('json',StudyDestinationOfNepali.objects.filter(region="WEST_AFRICA"))
    south_and_center_asia = serializers.serialize('json',StudyDestinationOfNepali.objects.filter(region="SOUTH_AND_CENTRAL_ASIA"))
    south_asia = serializers.serialize('json',StudyDestinationOfNepali.objects.filter(region="SOUTHEAST_ASIA"))
    mexico = serializers.serialize('json',StudyDestinationOfNepali.objects.filter(region="MEXICO_AND_CENTRAL_AMERICA"))
    south_america = serializers.serialize('json',StudyDestinationOfNepali.objects.filter(region="SOUTH_AMERICA"))
    return render(request,'market-entry.html',{"wast_africa":wast_africa,
                                               "south_and_center_asia":south_and_center_asia,
                                               "south_asia":south_asia,
                                               "mexico":mexico,
                                               "south_america":south_america,"map_country_list":json.dumps(map_country_list)})

def career_opportunity(request):
    # page_number = request.GET.get('page')
    category_grouping = CareerOpportunities.objects.values('category').annotate(count=Count('category')).order_by('category')
    result = []
    JOB_TYPE_DICT = dict(JOB_TYPE)
    JOB_STATUS_DICT = dict(STATUS_TYPE)
    JOB_MODE_DICT = dict(JOB_MODE)
    for group in category_grouping:
        jobs = list(CareerOpportunities.objects.filter(category=group['category']).values('job_title', 'job_summary',
                                                                                           'job_mode', 'job_type',
                                                                                           'job_status', 'slug'))
        for job in jobs:
            job['job_type'] = JOB_TYPE_DICT.get(job['job_type'], job['job_type'])
            job['job_mode'] = JOB_MODE_DICT.get(job['job_mode'],job['job_mode'])
            job['job_status'] = JOB_STATUS_DICT.get(job['job_status'],job['job_status'])
        result.append({
            'category': group['category'],
            'jobs':jobs
        })
    return render(request,'open-jobs.html',{'opportunity':json.dumps(result)})

def job_detail(request,slug):
    job = CareerOpportunities.objects.get(slug=slug)
    recommendation = CareerOpportunities.objects.filter(Q(category=job.category)|Q(job_mode=job.job_mode)|Q(job_status=job.job_status)).exclude(id=job.pk)[:3]

    return render(request,'job-detail.html',{'job':job,"recommendation":recommendation})

def privacy_policy(request):
    privacy = PrivacyPolicy.objects.get(status="PUBLISHED")
    return render(request,'privacy-policy.html',{"privacy":privacy})

def our_journey(request):
    return render(request,'journey.html')

def our_teams(request):
    page_number = request.GET.get('page')
    no_of_item = 9
    team = ISNTeam.objects.order_by('created_at')
    paginator = Paginator(team, no_of_item)
    total_pages = paginator.num_pages
    page_obj = paginator.get_page(page_number)
    return render(request,'team.html',{'teams':page_obj,"page":total_pages})

def apply_job(request,job_id):
    referer = request.META.get('HTTP_REFERER', '/')
    try:
        job = CareerOpportunities.objects.get(pk=job_id)
        if request.method == "POST":
            form = ApplyForCareerForm(request.POST,request.FILES)
            if form.is_valid():
                application = form.save(commit=False)
                application.job = job
                application.save()
            else:
                print("********",form.errors)
            path = '/job/{}'.format(job.slug)
            return redirect("success")
        else:
            context = {
                'country': COUNTRY_CHOICES,
                'phone_type':CONTACT_PHONE_TYPE,
                'gender_type':GENDER_TYPE,
                "profile_link":PROFILE_LINK_TYPE,
                'notice_period':NOTICE_PERIOD,
                'veteran_status':VETERAN_STATUS_CHOICES,
                'gender':GENDER_TYPE,
                'race_eth':RACE_ETHNICITY_CHOICES,
                'disability':DISABILITY_TYPE_CHOICES,
                "job":job
            }
            return render(request,'job_apply.html',context)
    except CareerOpportunities.DoesNotExist:
        return redirect(referer)

def subscription_view(request):
    if request.method == "POST":
        form  = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect("error")
        return redirect("success")

def insight_comment(request):
    referer = request.META.get('HTTP_REFERER', '/')
    if request.method == "POST":
        form  = InsightCommentsForm(request.POST)
        id = request.POST.get('id')
        try:
            insight=Insights.objects.get(pk=id)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.insight = insight
                form.save()
            else:
                print(form.errors)
        except Insights.DoesNotExist:
            return redirect(referer)
    return redirect(referer)

def something_went_wrong(request):
    return render(request,'error.html')

def success(request):
    source_url = request.session.get('source_url', None)
    if source_url=="partnership":
        return render(request,'partnership_success.html')
    return render(request,'success.html')