from new_user.forms import AdminUserAddForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


class AuthorView(FormView):
    template_name = 'login.html'
    form_class = AdminUserAddForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.save()
        return super(AuthorView, self).form_valid(form)


class ThanksView(TemplateView):
    template_name = 'thanks.html'

    def get_context_data(self, **kwargs):
        context = super(ThanksView, self).get_context_data(**kwargs)

        return context
