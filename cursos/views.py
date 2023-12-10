from django.shortcuts import render, redirect
from .models import Curso
from datetime import datetime

def listar_cursos(request):
    nome_filtrar = request.Get.get('nome_filtrar')
    cursos = Curso.objects.all()
    return render(request, 'listar_cursos.html', {'cursos':cursos})

def criar_curso(request):
    if request.method == "GET":
        status = request.GET.get('status')

        return render(request, 'criar_cursos.html',{'status': status})

    elif request.method == "POST":
        nome_digitado= request.POST.get('nome')
        carga_horaria_digitada= request.POST.get('carga_horaria')

        curso = Curso(
            nome = nome_digitado,
            carga_horaria = carga_horaria_digitada,
            data_de_criação = datetime.now()

        ) 

        curso.save()

        return redirect('/curso/criar_curso/?status=1')
    

