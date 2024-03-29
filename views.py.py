from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged In!')
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request,"home.html")

def games_view(request):
    return render(request, 'games.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out...')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You Have Successfully Registered!')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, "register.html", {'form': form})

# Static Math Challenge view
def static_math_challenge(request):
    context = {
        'question': "Compute the derivative of the function f(x) = 3x^2 + 2x + 1.",
        'option_a': "6x + 2",
        'option_b': "3x^2",
        'option_c': "6x^2 + 2",
        'option_d': "9x + 2",
    }
    return render(request, 'static_math_challenge.html', context)

# Algebra Challenge view
def algebra_challenge(request):
    context = {
        'question': "Solve for x: 3x + 5 = 14",
        'option_a': "x = 3",
        'option_b': "x = -3",
        'option_c': "x = 9",
        'option_d': "x = -9",
    }
    return render(request, 'algebra_challenge.html', context)

# Geometry Challenge view
def geometry_challenge(request):
    context = {
        'question': "What is the area of a triangle with base 8 cm and height 5 cm?",
        'option_a': "20 cm²",
        'option_b': "40 cm²",
        'option_c': "18 cm²",
        'option_d': "25 cm²",
    }
    return render(request, 'geometry_challenge.html', context)

# Trigonometry Challenge view
def trigonometry_challenge(request):
    context = {
        'question': "Calculate cos(θ) if sin(θ) = 0.5 and θ is in the first quadrant.",
        'option_a': "cos(θ) = 0.866",
        'option_b': "cos(θ) = 0.5",
        'option_c': "cos(θ) = 0.707",
        'option_d': "cos(θ) = 0.4",
    }
    return render(request, 'trigonometry_challenge.html', context)

# Probability Challenge view
def probability_challenge(request):
    context = {
        'question': "What is the probability of rolling an even number on a six-sided die?",
        'option_a': "1/6",
        'option_b': "1/3",
        'option_c': "1/2",
        'option_d': "2/3",
    }
    return render(request, 'probability_challenge.html', context)