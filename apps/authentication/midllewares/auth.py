
from django.shortcuts import render, redirect


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.id:
            if not request.user.profile.profile_active:
                return redirect('updateprofile')

            if not request.user.profile.agent_active:
                return render(request,'accounts/account_validation.html')

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware