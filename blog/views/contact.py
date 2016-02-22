from blog.models import Menu
from django.shortcuts import render
from django.template import RequestContext
import json
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import urllib.request
from dns.resolver import query
from dns.exception import DNSException


from django.conf import settings


def main(request):
    error = None
    success = None
    if request.POST:
        contact_text = request.POST.get("contact-text")
        contact_email = request.POST.get("contact-email")
        g_rc_response = request.POST.get("g-recaptcha-response")
        url = "https://www.google.com/recaptcha/api/siteverify?secret=%s&response=%s" % (settings.RECAPTCHA_SECRET_KEY, g_rc_response)
        resp = urllib.request.urlopen(url)
        js = json.loads(resp.read().decode("utf-8"))
        if js['success']:
            if check_address(contact_email):
                try:
                    send_email(contact_text, contact_email)
                    contact_text = ""
                    contact_email = ""
                    success = "Twoja wiadomość została wysłana"
                except Exception:
                    error = "Błąd wysyłania wiadomości, spróbuj później"
            else:
                error = "Niepoprawny adres email"
        else:
            error = "Udowodnij, że jesteś człowiekiem"
    return render(request, 'blog/contact/main.html', {
        'success': success,
        'error': error,
        'contact_text': contact_text,
        'contact_email': contact_email,
        'context_instance': RequestContext(request),
        'menu': Menu.options()
    })

def check_address(address):
    parts = address.split("@")
    if len(parts) != 2:
        return False
    try:
        query(parts[1], 'MX') #sprawdzamy wpis dns
    except DNSException:
        return False
    return True

def send_email(content, address):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Wiadomość z aplikacji od %s" % address
    msg['From'] = address
    msg['To'] = settings.NOREPLY_TARGET
    text = "Hej, z naszej marchewkowej strony odezwał się %s i zostawił wiadomość\n\n%s\n\nPozdrawiam, marchewa." % (address, content)
    html = """
<html><head></head><body>
    <h3>Hej, z naszej marchewkowej strony odezwał się %s i zostawił wiadomość</h3>
    <br><br><p>%s<p>
    <br><br><b>Pozdrawiam, </b>
    <img src="https://codecarrots-koszalin.herokuapp.com/static/img/cc.jpg" width="40px">
  </body></html>
""" % (address, remove_tags(content))
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(settings.NOREPLY_ACCOUNT, settings.NOREPLY_PASSWORD)
    server.sendmail(address, settings.NOREPLY_TARGET, msg.as_string())
    server.quit()


def remove_tags(text):
    return re.compile(r'<[^>]+>').sub('', text)