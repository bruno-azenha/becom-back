from django.shortcuts import render

def RenderHome(request):
	return render(request, 'becom_web/index.html', {})
