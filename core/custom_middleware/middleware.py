from django.shortcuts import redirect,render


class CustomMiddleware(object):
    def view_auth(self,request):
        if not request.user.profile.profile_active:
            return redirect('updateprofile')
        if not request.user.profile.agent_active:
            return render(request,'accounts/account_validaton.html')
