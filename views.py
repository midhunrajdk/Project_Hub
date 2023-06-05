from django.shortcuts import render


def pdash(request):
    return render(request, 'home/p_m_dashboard_base.html')
