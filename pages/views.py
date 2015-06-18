from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import models

def page(request, slug):
    page = models.Page.objects.get(slug=slug)
    return render_to_response(page.template, {'current_page':page, 'pages': models.Page.objects.filter(visible=True)})


def redirect_to_2013(request):
    return HttpResponseRedirect("http://2013.mykonosbiennale.com"+request.get_full_path())


class PageMixin(object):
    def get_context_data(self, **kwargs):
        context = super(PageMixin, self).get_context_data(**kwargs)
        context['pages'] = models.Page.objects.filter(visible=True)
        context['breadcrumbs'] = self.breadcrumbs(context)
        context['seo'] = self.seo(context)
        return context
    
    def getObject(self, context):
        return context['object']
        
    def breadcrumbs(self, context):
        pass
        
    def seo(self, context):
        object = self.getObject(context)
        return {
            'url': object.get_absolute_url(), 
            'image': 'http://mykonosbiennale.org/static/images/mykonos-biennale-logo.png'
        }
    
    
class ListMixin(PageMixin):

    def getObject(self, context):
        return context['list_object']
        
    def breadcrumbs(self, context):
        pass
    
    def seo(self, context):
        object = self.getObject(context)
        return {
            'url': '', 
            'image': 'http://mykonosbiennale.org/static/images/mykonos-biennale-logo.png'
        }