from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

from tasks.license import activate_license
from tasks.models import License

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return self.request.user.get_absolute_url()  # type: ignore [union-attr]

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        if self.request.user.is_superuser:
            return reverse("home")
        elif self.request.user.is_staff:
            try:
                slicense = License.objects.latest("id")
            except License.DoesNotExist:
                slicense = None
            if not slicense:
                return reverse("tasks:license")
            else:
                try:
                    valid, msg = activate_license(slicense.license_id, slicense.key)
                except:
                    return reverse("tasks:license")
                if valid:
                    return reverse("home")
        else:
            return reverse(
                "users:detail", kwargs={"username": self.request.user.username}
            )


user_redirect_view = UserRedirectView.as_view()
