from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
import models

def page(request, slug):
    page = models.Page.objects.get(slug=slug)
    return render_to_response(page.template, {'current_page':page, 'pages': models.Page.objects.filter(visible=True)})



class PageMixin(object):
    def get_context_data(self, **kwargs):
        context = super(PageMixin, self).get_context_data(**kwargs)
        context['pages'] = models.Page.objects.filter(visible=True)
        context['breadcrumbs'] = self.breadcrumbs(context)
        context['seo'] = self.seo(context)
        return context
    
    def breadcrumbs(self, context):
        pass
        
    def seo(self, context):
        raise NotImplementedError()
       