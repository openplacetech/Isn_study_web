from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_html_email():
    subject = 'Newsletter'
    text_content = 'This is the plain text version of the email.'
    html_content = '<p>This is the <strong>HTML</strong> version of the email.</p>'
    recipient_list = ['karkipramish07@gmail.com']
    email = EmailMultiAlternatives(subject, text_content, None, recipient_list)
    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=False)


def send_newsletter_to_all_subscribers(email,url,newsletter):
    subject = 'Monthly Newsletter'
    unsubscribe_link = url

        # Load and render the templates
    html_content = render_to_string('newsletter_email.html',
                                    {'newsletter':newsletter, 'unsubscribe_link': unsubscribe_link})
    # text_content = render_to_string('newsletter_email.txt',
    #                                     { 'unsubscribe_link': unsubscribe_link})
    # text_content = strip_tags(text_content)  # Strip HTML tags from text content

        # Create the email
    email = EmailMultiAlternatives(subject, None, None, email)
    email.attach_alternative(html_content, "text/html")
    email.send(fail_silently=False)

