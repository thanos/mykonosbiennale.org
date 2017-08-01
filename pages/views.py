import os

from bakery.views import BuildableRedirectView
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import View, ListView, DetailView

import models
from festival.models import Project


def page(request, slug):
    page = models.Page.objects.get(slug=slug)
    return render_to_response(page.template, {'current_page':page, 'pages': models.Page.objects.filter(visible=True)})

class PageView(View):
    def seo(self, context):
        current_page = context['current_page']
        return {
            'title': current_page.title,
            'description': current_page.description_155,
            'image': 'http://mykonosbiennale.org/static/images/mykonos-biennale-logo.png',
            'url': current_page.get_absolute_url(),
            'description_155': current_page.description_155,
            'description_200': current_page.description_200,
            'description_300': current_page.description_300,
        }
    def get(self, request, slug):
        page = models.Page.objects.get(slug=slug)
        self.build_path = os.path.join(slug,'index.html')
        context = {'current_page':page, 'pages': models.Page.menubar()}
        context['seo'] = self.seo(context)
        return render_to_response(page.template, context)

    # def get_context_data(self, **kwargs):
    #     context = super(PageView, self).get_context_data(**kwargs)
    #     context['seo'] = self.seo(context)
    #     return context
            
class Redirect2013View(BuildableRedirectView):
    def get(self, request):
      return HttpResponseRedirect("http://2013.mykonosbiennale.com"+request.get_full_path())




class PageMixin(object):
    def get_context_data(self, **kwargs):
        context = super(PageMixin, self).get_context_data(**kwargs)
        context.update(kwargs)
        context['pages'] = models.Page.menubar()
        context['breadcrumbs'] = self.breadcrumbs(context)
        context['seo'] = self.seo(context)
        return context

    def getObject(self, context):
        return context['object']

    def breadcrumbs(self, context):
        pass


    def seo(self, context):
        return {
            'title': object.title,
            'description': object.description_155,
            'image': 'http://mykonosbiennale.org/static/images/mykonos-biennale-logo.png',
            'url': object.get_absolute_url(),
            'description_155': object.description_155,
            'description_200': object.description_200,
            'description_300': object.description_300,
        }

    
class ListView(PageMixin, ListView):

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


class ProjectView(ListView):
    def get_project(self):
        return Project.objects.get(slug=self.kwargs['project'],
                                                     festival__year=int(self.kwargs.get('year', '2017')))
    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(project = self.get_project())
        context['breadcrumbs'] = self.breadcrumbs(context)
        return context

    def seo(self, context):
        x = super(ProjectView, self).seo(context)
        project = context.get('project')
        project__slug = self.kwargs['project']
        x.update({
            'title': '{} - {}'.format(project.festival, project.title),
            'sub_title': project.title if project else '',
            'description': 'The list of films presented in {}'.format(
                project.title if project else 'this years festival'),
            'image': 'http://mykonosbiennale.org/static/images/mykonos-biennale-logo.png',
        })
        return x

class ProjectEntryView(PageMixin, DetailView):
    def getObject(self, context):
        return context['object']
    def get_context_data(self, **kwargs):
        context =  super(ProjectEntryView, self).get_context_data(**kwargs)
        context['breadcrumbs'] = self.breadcrumbs(context)
        return context