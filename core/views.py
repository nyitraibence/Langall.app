from django.shortcuts import render, redirect
from django.http import HttpResponse
# for email sending feature
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.core.mail import EmailMessage
# !!! for using "User" this is necessary:
from django.contrib.auth import get_user_model
# for signals:
from .signals import new_user_activation


def homepage(request):
    user_count = get_user_model().objects.all().count()
    teacher_count = get_user_model().objects.filter(is_teacher='True').count()
    return render(request, 'homepage.html',{'num_users' : user_count, 'num_teachers' : teacher_count})

def profile(request):
    if request.user.is_authenticated:
        content={
            "person" : request.user,
            "form" : CustomUserChangeForm(instance=request.user),
            "has_fb_flag" : False
        }
            
        person = request.user
        if(person.social_auth.exists()):
            persons_facebook = person.social_auth.get(provider="facebook")
            content.update({
                "profile_url" : persons_facebook.extra_data['profile_url'],
                "profile_pic_url" : persons_facebook.extra_data['picture']['data']['url'],
                "has_fb_flag" : True
            })
        
        if request.method == 'POST':
            update_form = CustomUserChangeForm(request.POST, instance=request.user)
            if update_form.is_valid():
                update_form.save()
                message="Sikeresen frissítetted! ✔️"
                content.update({"message" : message})
                return render(request, 'profile.html', content)
        else:
            return render(request, 'profile.html', content)
    else:
        return redirect('login')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Langall regisztráció aktiválás'
            message = render_to_string('email/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.content_subtype = "html"          # important addition for html email to render !
            email.send()
            return render(request, 'verify_register.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        new_user_activation.send(sender=user)                                       # signal for welcome mail sending
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')   # important to add the backend !!!
        return redirect('homepage')
    else:
        return render(request, 'registration/invalid_registration_link.html')


def new_social(request):
    return render(request, 'new_social_user.html')











# ================= only created for testing hrad-to-reach urls' templates ===============================================
def tester(request):

    return render(request, 'my404.html')