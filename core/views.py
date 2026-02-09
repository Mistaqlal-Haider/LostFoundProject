from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Item
from .forms import ItemForm

def item_list(request):
    # 1. Get ONLY APPROVED items
    # (We added .filter(is_approved=True) here)
    items = Item.objects.filter(is_approved=True).order_by('-date_reported')

    # 2. Count ONLY APPROVED items for the dashboard
    total_lost = Item.objects.filter(status='LOST', is_approved=True).count()
    total_found = Item.objects.filter(status='FOUND', is_approved=True).count()

    # 3. Search Logic
    query = request.GET.get('q')
    if query:
        items = items.filter(Q(title__icontains=query) | Q(location__icontains=query))
    
    # 4. Filter Logic
    status_filter = request.GET.get('status')
    if status_filter:
        items = items.filter(status=status_filter)

    context = {
        'items': items, 
        'query': query if query else '',
        'selected_status': status_filter if status_filter else '',
        'total_lost': total_lost,
        'total_found': total_found
    }
    return render(request, 'core/item_list.html', context)

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            # Force is_approved to False just in case
            item = form.save(commit=False)
            item.is_approved = False
            item.save()
            
            # Redirect to the "Pending" page instead of the Home page
            return render(request, 'core/pending_approval.html')
    else:
        form = ItemForm()
    return render(request, 'core/add_item.html', {'form': form})

# These functions remain the same
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return redirect('item_list')

def mark_returned(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.status = 'RETURNED'
        item.save()
        return redirect('item_list')
    return redirect('item_list')