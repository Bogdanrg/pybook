from rest_framework import serializers


class FilterCommentListSerializer(serializers.ListSerializer):
    """ Comment filter, parents only
    """
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """ Recursive children print
    """
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
