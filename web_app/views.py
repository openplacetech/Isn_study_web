from django.shortcuts import render,redirect
from web_app.forms import PartnershipRequest
from web_app.models import Insights,Subscriber,PrivacyPolicy,CurrierOpportunities,ISNTeam
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    insight_list = Insights.objects.order_by('-created_at')  # Fetch all items
    latest_items = insight_list[:3]
    return  render(request,"index.html",{"insights":latest_items})

def partnership_request(request,contact_type):
    if request.method == 'POST':
        form = PartnershipRequest(request.POST)
        if form.is_valid():
            partnership=form.save()
            # send_mail(
            #     subject=contact.subject,
            #     message=contact.message,
            #     from_email=contact.email,
            #     recipient_list=[settings.CONTACT_EMAIL],
            # )
            return redirect('partnership_request')
    else:
        form = PartnershipRequest()
    if contact_type == "us":
        return render(request, 'contact.html', {'form': form})
    elif contact_type == "partnership":
        return render(request, 'partnership.html', {'form': form})
    else:
        return render(request, 'error.html')

def isn_insights(request):
    page_number = request.GET.get('page')
    latest_items= []
    no_of_item = 9
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
    insight = Insights.objects.get(slug=slug)
    latest = Insights.objects.order_by('-created_at')[:3]
    return render(request,'insight-detail.html',{"insight":insight,"latest":latest})


def isn_platform(request):
    return render(request,'isn_platform.html')


def isn_market_entry(request):
    """this is isn market entry"""

def currier_opportunity(request):
    # page_number = request.GET.get('page')
    opportunity = CurrierOpportunities.objects.all()
    return render(request,'open-jobs.html',{'opportunity':opportunity})


def privacy_policy(request):
    privacy = PrivacyPolicy.objects.get(status="PUBLISHED")
    return render(request,'privacy-policy.html',{"privacy":privacy})

def our_journey(request):
    return render(request,'journey.html')

def our_teams(request):
    page_number = request.GET.get('page')
    latest_items = []
    no_of_item = 9
    team = ISNTeam.objects.order_by('-created_at')  # Fetch all items
    paginator = Paginator(team, no_of_item)  # Show 10 items per page
    total_pages = paginator.num_pages
    page_obj = paginator.get_page(page_number)
    return render(request,'team.html',{'teams':team,"page":total_pages})