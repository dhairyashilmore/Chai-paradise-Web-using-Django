from django.shortcuts import render

def all_chai_items(request):
    # Logic to retrieve and display all chai items
    
    return render(request, 'chai/all_chai.html')
