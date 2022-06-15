

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from .forms import LoginForm, SignUpForm, UserForm, ProfileForm
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from .models import Profile
from .tokens import account_activation_token


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                if User.objects.filter(username=username):
                    msg = "User is not active"
                else:
                    msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your CMS account.'
            message = render_to_string('accounts/account_activation_email_template.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            # return HttpResponse('Please confirm your email address to complete the registration')
            success = True
            return render(request, "accounts/verify_email.html", {"msg": to_email, "success": success})

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        usr = request.POST.get("insurance_company", None)
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            form_obj = profile_form.save(commit=False)
            form_obj.profile_active = True
            form_obj.save()
            query=Profile.objects.filter(insurance_company=usr).first()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profile')
        else:
            return render(request,'accounts/account_validation.html')
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'home/settings.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def activate(request, uidb64, token,backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user,backend)
        # return redirect('home')
        success = True
        return render(request, "accounts/account_activated.html", {"success": success})
    else:
        success = False
        return render(request, "accounts/invalid_email_verification_link.html", {"success": success})

