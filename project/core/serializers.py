"""Core serializers."""

from rest_framework import serializers

from core.markdown import MarkdownField

from .models import Document


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for documents."""

    content = MarkdownField()

    class Meta:  # noqa
        model = Document
        fields = ('title', 'slug', 'content', 'url')
        extra_kwargs = {
            'url': {
                'view_name': 'api:document-detail',
                'lookup_field': 'slug',
            },
        }
