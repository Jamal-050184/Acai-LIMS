from rest_framework import serializers
from appAcai_LIMS.models import Library


class LibrarySerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Library
            fields = ('Publisher', 'Author', 'Title', 'PageCount', 'Category', 'ShelfLocation', 'PublishedDate', 'IsInstock', 'DateCheckedOut')

