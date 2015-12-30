# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from braces.views import LoginRequiredMixin

from commonrepo.elos.models import ELO
from commonrepo.groups.models import Group

from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user = User.objects.get(username=self.kwargs['username'])

        # Count Friends and Followers
        context['friends_count'] = user.userprofile.friends.all().count()
        context['followers_count'] = user.followed_by.all().count()
        context['following_count'] = user.userprofile.follows.all().count()
        context['has_followed'] = user.userprofile.follows.filter(username=self.request.user.username)

        # ELOs
        context['elo_count'] = ELO.objects.filter(author=user).count()
        context['elo_list'] = ELO.objects.filter(author=user).filter(is_public=1)

        # Groups
        context['group_count'] = Group.objects.filter(creator=user).count()

        return context


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        # Basic user information
        'id', 'username', 'organization', 'education', 'url', 'phone', 'address', 'language', 'area', 'about',
        # Social informaion
        'social_facebook', 'social_google', 'social_linkedin', 'social_twitter',
        # Extend user information
        'teaching_category', 'teaching_subject_area',
        # Preferences
        'elo_similarity_threshold']

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"
