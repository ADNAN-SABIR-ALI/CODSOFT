from django.shortcuts import render
from .models import Calculation

def index(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        operation = request.POST['operation']

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            error_message = "Please enter valid numbers"
            return render(request, 'base/index.html', {'error_message': error_message})

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                error_message = "Cannot divide by zero"
                return render(request, 'base/index.html', {'error_message': error_message})
            result = num1 / num2

        calculation = Calculation(num1=num1, num2=num2, operation=operation, result=result)
        calculation.save()

        return render(request, 'base/index.html', {'result': result, 'num1': num1, 'num2': num2, 'operation': operation})

    return render(request, 'base/index.html')

