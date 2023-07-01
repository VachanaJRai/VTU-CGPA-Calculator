from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request, 'calculator/index.html')

def calculate_sgpa(request):
    grades={
        'O':10, 'A+':9, 'A':8, 'B+':7, 'B':6, 'C':5, 'P':4, 'F':0, 'Ab':0, 'I':0
    }
    total_credits=0
    total_points=0

    for i in range(1,9):
        credit=int(request.POST[f'credit_{i}'])
        grade=request.POST[f'grade_{i}']
        total_credits+=credit
        total_points+=credit*grades[grade]

    sgpa=total_points/total_credits

    return render(request, 'calculator/sgpa.html',{'sgpa':sgpa})

def calculate_cgpa(request):
    grades={
        'O':10, 'A+':9, 'A':8, 'B+':7, 'B':6, 'C':5, 'P':4, 'F':0, 'Ab':0, 'I':0
    }
    total_credits=0
    total_points=0

    for i in range(1,9):
        credit=int(request.POST[f'credit_{i}'])
        grade=request.POST[f'grade_{i}']
        total_credits+=credit
        total_points+=credit*grades[grade]

    cgpa=total_points/total_credits

    return render(request, 'calculator/cgpa.html',{'cgpa':cgpa})