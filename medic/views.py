from django.shortcuts import render
from .models import Ticket
from .forms import TicketForm
from django.utils import timezone
from django.shortcuts import redirect

# Create your views here.
def ticket_list(request):
    tickets = Ticket.objects.order_by('created_date')
    return render(request, 'medic/ticket_list.html', {'tickets': tickets})

def ticket_new(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.published_date = timezone.now()
            
            ticket.save()
            return redirect("/")
    else:
        form = TicketForm()
    return render(request, 'medic/ticket_add.html', {'form': form})