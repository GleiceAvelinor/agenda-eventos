from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event

@login_required
def lista_eventos(request):
    if request.method == "POST":
        title = request.POST.get('title')
        date = request.POST.get('date')
        description = request.POST.get('description', '')

        if title and date:
            Event.objects.create(
                title=title,
                date=date,
                description=description,
                user=request.user
            )
            messages.success(request, "Evento agendado com sucesso!")
            return redirect('lista_eventos')
        
        messages.error(request, "Preencha o título e a data para criar o evento.")

   
    data_filtro = request.GET.get('q_data')
    termo_busca = request.GET.get('q')

    eventos = Event.objects.filter(user=request.user)

    if termo_busca:
        eventos = eventos.filter(title__icontains=termo_busca)

    if data_filtro:
        eventos = eventos.filter(date__date=data_filtro)

    eventos = eventos.order_by('date')

    return render(request, 'agenda.html', {'eventos': eventos})


@login_required
def deletar_evento(request, id):
    evento = get_object_or_404(Event, id=id, user=request.user)
    evento.delete()
    messages.success(request, "Evento removido com sucesso!")
    return redirect('lista_eventos')