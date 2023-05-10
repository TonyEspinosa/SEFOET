from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import *
from .forms import fm_proveedor

# Create your views here.
@login_required(login_url='u_usr_login')
def v_prov(request):
    qProvTodo = m_proveedor.objects.all()
    context = {'prov':qProvTodo}
    return render(request, 'prov_list.html', context)

@login_required(login_url='u_usr_login')
def v_prov_new(request):
    form = fm_proveedor()
    if request.method == 'POST':
        form = fm_proveedor(request.POST)
        if form.is_valid():
            form.save()
            return redirect('u_prov_list') 
    context = {'form':form}
    # qProvID = m_proveedor.objects.get(id_proveedor = pk_prov)
    # context = {'prov':qProvID}
    return render(request, 'prov_new.html', context)

#@login_required(login_url='u_usr_login')
def v_prov_upd(request, pk_prov):
    pass
#    qProvID = m_proveedor.objects.get(id_proveedor = pk_prov)
#    form = fm_proveedor(instance = qProvID)
#    context = {'form':form}
#    return render(request, 'prov_new.html', context)

#@login_required(login_url='u_usr_login')
def v_prov_del(request, pk_prov):
    pass
#    qProvID = m_proveedor.objects.get(id_proveedor = pk_prov)

#    if request.method == "POST":
#        qProvID.delete()
#        return redirect('u_prov_list')
        
#    context = {'item':qProvID}
#    return render(request, 'prov_del.html', context)
