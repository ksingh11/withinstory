from tastypie.models import ApiKey
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from withinstory.app.models import UserProfile
from django.contrib.auth.models import Group
from django.template.context import RequestContext

class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'username', 'email', 'password1', 'password2')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            group = Group.objects.get(name='writers')
            username = form.cleaned_data.get('username', None)
            user = UserProfile.objects.get(username=username)
            user.groups.add(group)
            user.save()
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    
    template_data = {
        'form': form,
    }
    return render_to_response('registration/register.html', template_data, context_instance=RequestContext(request))

def get_api_key(request):
    if request.user and request.user.username:
        api = get_object_or_404(ApiKey, user__username=request.user.username)
        return HttpResponse('%s:%s' % (request.user.username, api.key))
    else:
        return HttpResponseForbidden()
