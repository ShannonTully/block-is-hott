from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DetailView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class CrimeView(TemplateView):
    """Class view for library."""

    template_name = 'crime.html'


class ArtView(TemplateView):
    """Class view for library."""

    template_name = 'art.html'


class EventView(TemplateView):
    """Class view for library."""

    template_name = 'events.html'


class EntertainmentView(TemplateView):
    """Class view for library."""

    template_name = 'entertainment.html'


class DirtinessView(TemplateView):
    """Class view for library."""

    template_name = 'dirtiness.html'
    # context_object_name = 'crime'
    # login_url = reverse_lazy('auth_login')

    # def get(self, *args, **kwargs):
    #     """Get username."""
    #     if kwargs:
    #         return super().get(*args, **kwargs)

    #     else:
    #         kwargs.update({'username': self.request.user.username})
    #         kwargs.update({'owner': True})

    #     return super().get(*args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     """Get and return context data for library."""
    #     context = super().get_context_data(**kwargs)

    #     photos = Photo.objects.filter(user__username=context['username'])
    #     albums = Album.objects.filter(user__username=context['username'])

    #     context['albums'] = albums
    #     context['photos'] = photos
    #     return context
