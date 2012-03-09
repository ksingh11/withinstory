from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication, Authentication
from tastypie.authorization import DjangoAuthorization, Authorization
from withinstory.app.models import UserProfile, Story


class CustomAuthentication(ApiKeyAuthentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        else:
            return super(CustomAuthentication, self).is_authenticated(request,
                **kwargs)


class CustomAuthorization(DjangoAuthorization):
    def apply_limits(self, request, object_list):
        if request.method != 'GET' and object_list and type(object_list[0]) == Story:
            object_list = object_list.filter(author__username=request.user.username)
        return object_list


class UserProfileResource(ModelResource):
    class Meta:
        queryset = UserProfile.objects.all()
        fields = ['name', 'username']


class StoryResource(ModelResource):
    author = fields.ForeignKey(UserProfileResource, 'author')
    
    class Meta:
        queryset = Story.objects.all()
        authentication = CustomAuthentication()
        authorization = CustomAuthorization()
