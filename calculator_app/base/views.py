from django.shortcuts import render
# from django.http import HttpResponse
from .models import Calculation

from .models import Calculation

def index(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2

        calculation = Calculation(num1=num1, num2=num2, operation=operation, result=result)
        calculation.save()

        return render(request, 'base/index.html', {'result': result, 'num1': num1, 'num2' : num2, 'operation' : operation})

    return render(request, 'base/index.html')
