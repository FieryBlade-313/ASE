from rest_framework import serializers
from .models import Jobs,Category,User,Review,ReviewConnector,Follows,FOI


# Serializer for Jobs Model
class JobsSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='jobs-details',
        )

    class Meta:
        model = Jobs
        fields = ('url', 'JID', 'CID', 'name')


# Serializer for Category Model
class CategorySerializer(serializers.HyperlinkedModelSerializer):

    jobs = serializers.StringRelatedField(many=True,read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='categories-detail',
        )

    class Meta:
        model = Category
        fields = ('CID', 'url', 'name', 'jobs')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','password')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('RID','content','rating')


class ReviewConnectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewConnector
        fields = ('RID','UID','targetID')


class FollowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follows
        fields = ('UID','OrganisationID')

class FOISerializer(serializers.ModelSerializer):
    class Meta:
        model = FOI
        fields = ('UID','JID')