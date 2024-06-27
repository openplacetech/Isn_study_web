from django.shortcuts import render,redirect
from web_app.forms import PartnershipRequest
from web_app.models import Insights,Subscriber,PrivacyPolicy
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    return  render(request,"index.html")

def partnership_request(request):
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
            return redirect('contact')
    else:
        form = PartnershipRequest()
    return render(request, 'contact.html', {'form': form})

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

def isn_platform(request):
    return render(request,'isn_platform.html')


def isn_market_entry(request):
    """this is isn market entry"""

def currier_opportunity(request):
    """this is currier opportunity"""

def privacy_policy(request):
    privacy = PrivacyPolicy.objects.get(status="PUBLISHED")
    return render(request,'privacy-policy.html',{"privacy":privacy})