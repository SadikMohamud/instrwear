from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def role_required(required_role: str):
    def decorator(view_func):
        @wraps(view_func)
        @login_required
        def _wrapped(request, *args, **kwargs):
            if getattr(request.user, "role", None) != required_role:
                messages.error(request, "Access denied.")
                return redirect("landing")
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator