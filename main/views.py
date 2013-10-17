from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.core.files.images import get_image_dimensions
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.core.urlresolvers import reverse
from django.db.models import Max

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_protect, requires_csrf_token


def main_view(request):
    print request

    t = loader.get_template("main.html")
    c = RequestContext(request, {
        "request": request
    })

    return HttpResponse(t.render(c))


