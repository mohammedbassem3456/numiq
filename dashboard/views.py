from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    data = {
        'total_revenue': 45230,
        'total_orders': 312,
        'net_profit': 28400,
        'shipping_cost': 8200,
        'returns': 3100,
        'ad_spend': 5530,
        'daily_sales': [1200, 1800, 950, 2100, 1650, 2800, 3200],
        'days': ['السبت', 'الأحد', 'الاثنين', 'الثلاثاء', 'الأربعاء', 'الخميس', 'الجمعة'],
    }
    return render(request, 'dashboard/home.html', data)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    
    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control'})
    
    return render(request, 'dashboard/register.html', {'form': form})