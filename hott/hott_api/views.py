from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from ipywidgets.embed import embed_minimal_html
from hott_overlays.models import Crimes, Entertainment, Events, Art, Dirtiness
import gmaps
import os
import re


class UserApi(generics.RetrieveAPIView, generics.CreateAPIView):
    permission_classes = ''  # IsAuthenticated??
    authentication_classes = (TokenAuthentication,)
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        if not pk:
            return Response(
                UserSerializer(request.user).data, status=status.HTTP_200_OK)
        return super().retrieve(request, pk)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CrimeMap(APIView):
    """Crime map view that takes in our crime data and serves the response."""

    authentication_classes = ''
    permission_classes = ''

    def get(self, request, format=None):
        """Get route for crime map."""
        gmaps.configure(api_key=os.environ.get('MAPS_API'))

        locations = []
        for each in Crimes.objects.all():
            temp = []
            temp.append(each.latitude)
            temp.append(each.longitude)
            locations.append(temp)

        heatmap_layer = gmaps.heatmap_layer(locations)

        heatmap_layer.gradient = [
            (0, 0, 0, 0.7),
            (255, 105, 180, 0.4),
            (255, 0, 0, 0.8)
        ]

        fig = gmaps.figure()

        fig.add_layer(heatmap_layer)
        embed_minimal_html('export.html', views=[fig])

        export = open('export.html').read()

        return Response(export)


class EntertainmentMap(APIView):
    """Entertainment map view that takes in our cultural centers and serves the response."""

    authentication_classes = ''
    permission_classes = ''

    def get(self, request, format=None):
        """Get route for entertainment map."""
        gmaps.configure(api_key=os.environ.get('MAPS_API'))

        locations = []
        for each in Entertainment.objects.all():
            temp = []
            p = re.compile('[()°,]')  # I know this is bad regex
            split_location = p.sub('', str(each.location)).split()
            try:
                if split_location[0] != 'None' or split_location[1] != 'None':
                    temp.append(float(split_location[0]))
                    temp.append(float(split_location[1]))
                    locations.append(temp)
            except IndexError:
                pass

        heatmap_layer = gmaps.heatmap_layer(locations)

        heatmap_layer.gradient = [
            (0, 0, 0, 0.7),
            (255, 178, 102, 0.4),
            (255, 128, 0, 0.8)
        ]

        fig = gmaps.figure()

        fig.add_layer(heatmap_layer)
        embed_minimal_html('export.html', views=[fig])

        export = open('export.html').read()

        return Response(export)


class EventMap(APIView):
    """Event map view that takes in our Event data and serves the response."""

    authentication_classes = ''
    permission_classes = ''

    def get(self, request, format=None):
        """Get route for Event map."""
        gmaps.configure(api_key=os.environ.get('MAPS_API'))

        locations = []
        for each in Events.objects.all():
            temp = []
            if each.latitude and each.longitude:
                temp.append(each.latitude)
                temp.append(each.longitude)
                locations.append(temp)

        heatmap_layer = gmaps.heatmap_layer(locations)

        heatmap_layer.gradient = [
            (0, 0, 0, 0.7),
            (255, 255, 153, 0.7),
            (255, 255, 0, 1)
        ]

        fig = gmaps.figure()

        fig.add_layer(heatmap_layer)
        embed_minimal_html('export.html', views=[fig])

        export = open('export.html').read()

        return Response(export)


class ArtMap(APIView):
    """Art map view that takes in our Art data and serves the response."""

    authentication_classes = ''
    permission_classes = ''

    def get(self, request, format=None):
        """Get route for Art map."""
        gmaps.configure(api_key=os.environ.get('MAPS_API'))

        locations = []
        for each in Art.objects.all():
            temp = []
            if each.latitude and each.longitude:
                temp.append(each.latitude)
                temp.append(each.longitude)
                locations.append(temp)

        heatmap_layer = gmaps.heatmap_layer(locations)

        heatmap_layer.gradient = [
            (0, 0, 0, 0.7),
            (0, 153, 0, 0.4),
            (102, 255, 102, 0.8)
        ]

        fig = gmaps.figure()

        fig.add_layer(heatmap_layer)
        embed_minimal_html('export.html', views=[fig])

        export = open('export.html').read()

        return Response(export)


class DirtinessMap(APIView):
    """Dirtiness map view that takes in our Dirtiness data and serves the response."""

    authentication_classes = ''
    permission_classes = ''

    def get(self, request, format=None):
        """Get route for Dirtiness map."""
        gmaps.configure(api_key=os.environ.get('MAPS_API'))

        locations = []
        for each in Dirtiness.objects.all():
            temp = []
            if each.latitude and each.longitude:
                temp.append(each.latitude)
                temp.append(each.longitude)
                locations.append(temp)

        heatmap_layer = gmaps.heatmap_layer(locations)

        heatmap_layer.gradient = [
            (0, 0, 0, 0.7),
            (255, 178, 102, 0.4),
            (102, 51, 0, 0.8)
        ]

        fig = gmaps.figure()

        fig.add_layer(heatmap_layer)
        embed_minimal_html('export.html', views=[fig])

        export = open('export.html').read()

        return Response(export)
