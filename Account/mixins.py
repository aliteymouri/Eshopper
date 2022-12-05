from django.shortcuts import redirect


class RequiredLoginMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('Account:sign_in')
        return super().dispatch(request, *args, **kwargs)


class AuthenticatedMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("Home:home")
        return super().dispatch(request, *args, **kwargs)
