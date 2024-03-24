# decorators.py
'''
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

def admin_user_required(view_func):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.is_superuser,
        login_url=reverse_lazy('hidden_admin_login')
    )
    return actual_decorator(view_func)
'''