from django.shortcuts import render

import datetime
import xlwt

from .models import *

# Create your views here.
#@login_required(login_url='u_usr_login')
def v_cat(request):
    qCatTodo = m_categoria.objects.all()
    context = {'cat':qCatTodo}
    m_categoria.setColorCategory()
    return render(request, 'cat_list.html', context)

#@login_required(login_url='u_usr_login')
def v_cat_new(request):
    pass
#    form = fm_categoria()
#    if request.method == 'POST':
        # Imprimir en línea de comandos cuando sea un POST
        #print('Printing POST:', request.POST) 
#        form = fm_categoria(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('u_cat_list') 
#    context = {'form':form}
    #qCatID = m_c-ategoria.objects.get(id_categoria = pk_cat)
    #context = {'cat':qCatID}
#    return render(request, 'cat_new.html', context)

#@login_required(login_url='u_usr_login')
def v_cat_upd(request, pk_cat):
    pass
#    qCatID = m_categoria.objects.get(id_categoria = pk_cat)
#    form = fm_categoria(instance = qCatID)
#    context = {'form':form}
#    return render(request, 'cat_new.html', context)

#@login_required(login_url='u_usr_login')
def v_cat_del(request, pk_cat):
    pass
#    qCatID = m_categoria.objects.get(id_categoria = pk_cat)

#    if request.method == "POST":
#        qCatID.delete()
#        return redirect('u_cat_list')
        
#    context = {'item':qCatID}
#    return render(request, 'cat_del.html', context)

#@login_required(login_url='u_usr_login')
def v_export_excel(request):
    pass
#    response = HttpResponse(content_type='application/ms-excel')
#    response['Content-Disposition'] = 'attachment; filename=Categoria' + \
#        str(datetime.datetime.now()) + '.xls'
    
#    wb = xlwt.Workbook(encoding='utf-8')
#    ws = wb.add_sheet('Categoria')
#    row_num = 0
#    font_style = xlwt.XFStyle()
#    font_style.font.bold = True

#    columns = ['Nombre', 'Descripcion']

#    for col_num in range(len(columns)):
#        ws.write(row_num, col_num, columns[col_num], font_style)
    
#    font_style = xlwt.XFStyle()
    ##font_style.font.bold = False

#    rows = m_categoria.objects.all().values_list('nombre', 'descripcion')

#    for row in rows:
#        row_num+=1

#        for col_num in range(len(row)):
#            ws.write(row_num, col_num, str(row[col_num]), font_style)

#    wb.save(response)

#    return response