# from django.shortcuts import render,redirect
# from web_app.forms import ContactForm
# # from django.conf import settings
# # from django.core.mail import send_mail
# # Create your views here.
#
# def index(request):
#     return  render(request,"index.html")
#
# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             contact=form.save()
#             # send_mail(
#             #     subject=contact.subject,
#             #     message=contact.message,
#             #     from_email=contact.email,
#             #     recipient_list=[settings.CONTACT_EMAIL],
#             # )
#             return redirect('contact')
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})
#
# def isn_insights(request):
#     """this is isn insights"""
#
# def isn_platform(request):
#     """isn platform"""
#
#
# def isn_market_entry(request):
#     """this is isn market entry"""
#
# def currier_opportunity(request):
#     """this is currier opportunity"""