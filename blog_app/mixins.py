from django.shortcuts import redirect
#mixins are classes that you made them one time and use it to your project many times
class LoginRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account_app:login')

        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

