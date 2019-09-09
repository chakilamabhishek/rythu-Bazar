from django.db.models import Count, Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from rythubazarapp.forms import AddCrop
from rythubazarapp.models import *
from django.urls import resolve
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class DisplayInventory(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request):
        my_dict=farmer.objects.all()
        print("="*20)
        print(my_dict)
        print("="*20)
        return render(request, template_name="inventoryitems.html",
                          context={
                              'my_dict': my_dict,
                              'no_of_items':len(my_dict)
                          })
class AddINventory(LoginRequiredMixin,View):
    login_url = '/login/'

    def get(self, request):
        addinvetory = AddCrop()
        return render(request, template_name="farmerpage.html",
                          context={
                              'form':addinvetory
                          })
    def post(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login_app')

        # if resolve(request.path_info).url_name == 'delete_college':
        #     College.objects.get(pk=kwargs.get('pk')).delete()
        #     return HttpResponseRedirect('/colleges')
        #
        # if resolve(request.path_info).url_name == 'edit_college':
        #     college = College.objects.get(pk=kwargs.get('pk'))
        #     form = AddCollege(request.POST, instance=college)
        #     if form.is_valid():
        #         form.save()
        #         return HttpResponseRedirect('/colleges')

        form = AddCrop(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.farmername=request.user
            form.save()
            return HttpResponseRedirect('/home/')
        else:
            return render(request, template_name="farmerpage.html",
                          context={
                              'form': form,
                          })
