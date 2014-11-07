from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse, HttpResponse

# Create your views here.

class IndexView(View):
	template = 'valscrape/index.html'
	def get(self, request):
		return render(request, self.template)