from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm
from complaints.models import Complaint 

@login_required
def dashboard(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    complaints = Complaint.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'tickets': tickets,
        'complaints': complaints,
    }
    return render(request, 'dashboard.html', context)

@login_required
def view_tickets(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'view_tickets.html', {'tickets': tickets})

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('view_tickets')
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})

@login_required
def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('view_tickets')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'update_ticket.html', {'form': form})

@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == 'POST':
        ticket.delete()
        return redirect('view_tickets')
    return render(request, 'ticket_confirm_delete.html', {'ticket': ticket})

