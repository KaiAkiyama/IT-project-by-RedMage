from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import StudyRecord
from .forms import StudyRecordForm, RegisterForm


def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        login(request, user)
        return redirect('record_list')
    return render(request, 'tracker/register.html', {'form': form})


def login_view(request):
    error = None
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('record_list')
        else:
            error = 'Invalid username or password.'
    return render(request, 'tracker/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def record_list(request):
    records = StudyRecord.objects.filter(user=request.user).order_by('-study_date')
    return render(request, 'tracker/record_list.html', {'records': records})


@login_required
def record_create(request):
    form = StudyRecordForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        record = form.save(commit=False)
        record.user = request.user
        record.save()
        return redirect('record_list')
    return render(request, 'tracker/record_form.html', {'form': form, 'action': 'Create'})


@login_required
def record_edit(request, pk):
    record = get_object_or_404(StudyRecord, pk=pk, user=request.user)
    form = StudyRecordForm(request.POST or None, instance=record)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('record_list')
    return render(request, 'tracker/record_form.html', {'form': form, 'action': 'Edit'})


@login_required
def record_delete(request, pk):
    record = get_object_or_404(StudyRecord, pk=pk, user=request.user)
    if request.method == 'POST':
        record.delete()
        return redirect('record_list')
    return render(request, 'tracker/record_confirm_delete.html', {'record': record})