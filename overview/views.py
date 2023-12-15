from django.shortcuts import render, get_object_or_404
from .models import loans, items
from datetime import datetime

def index(request):

    if 'back' in request.POST:
        data = request.POST
        pk = data.get("back")
        loan_save = get_object_or_404(loans, pk=pk)
        loan_save.loan_is_finished = True
        loan_save.item_id.item_state = 0
        items_save = loan_save.item_id
        items_save.item_state = 0 #0 = ready pujcit, 1 = zapujceno, 2 = cekani na potvrzeni o delsi pujcku
        items_save.save()
        loan_save.save()
    
    if 'confirm' in request.POST:
        data = request.POST
        pk = data.get("confirm")

        loan_save = get_object_or_404(loans, pk=pk)
        loan_save.loan_is_finished = False
        loan_save.item_id.item_state = 1
        loan_save.date_on_loan = datetime.now()

        items_save = loan_save.item_id
        items_save.item_state = 1 #0 = ready pujcit, 1 = zapujceno, 2 = cekani na potvrzeni o delsi pujcku
        items_save.save()
        loan_save.save()
    
    
    loan = [get_object_or_404(loans, pk=1)]
    for x in range (2, loans.objects.count() + 1):
        loan.append(get_object_or_404(loans, pk=x))
    
    context = {
        "loans": loan,
    }

    return render(request, 'test.html', context)
