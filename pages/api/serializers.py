from rest_framework import serializers

from pages.models import Page, Version


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ('id', 'created', 'current_version')


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = ('id', 'title', 'text', 'created', 'version', 'current_page')
