from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Ecosystem, Animal
from .forms import EcosystemForm, AnimalForm
from accounts.models import StudentProgress


def ecosystem_list(request):
    ecosystems = Ecosystem.objects.all()
    
    # Filtering
    region_filter = request.GET.get('region')
    era_filter = request.GET.get('era')
    search_query = request.GET.get('search')
    species_filter = request.GET.get('species')
    
    if region_filter:
        ecosystems = ecosystems.filter(region=region_filter)
    if era_filter:
        ecosystems = ecosystems.filter(era=era_filter)
    if search_query:
        ecosystems = ecosystems.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(vegetation__icontains=search_query)
        )
    if species_filter:
        # Filter by species type in animals
        ecosystems = ecosystems.filter(animals__species_type=species_filter).distinct()
    
    paginator = Paginator(ecosystems, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'ecosystem/list.html', {
        'page_obj': page_obj,
        'region_filter': region_filter,
        'era_filter': era_filter,
        'search_query': search_query,
        'species_filter': species_filter,
    })


def ecosystem_detail(request, pk):
    ecosystem = get_object_or_404(Ecosystem, pk=pk)
    animals = ecosystem.animals.all()
    
    # Track student visit
    if request.user.is_authenticated and request.user.is_student_user():
        progress, created = StudentProgress.objects.get_or_create(
            student=request.user,
            ecosystem=ecosystem,
            defaults={'completed': False}
        )
        if not created:
            progress.time_spent_minutes += 1
            progress.save()
    
    # Filter animals by type if requested
    species_type_filter = request.GET.get('species_type')
    if species_type_filter:
        animals = animals.filter(species_type=species_type_filter)
    
    existing_species = animals.filter(species_type='existing')
    extinct_species = animals.filter(species_type='extinct')
    
    return render(request, 'ecosystem/detail.html', {
        'ecosystem': ecosystem,
        'animals': animals,
        'existing_species': existing_species,
        'extinct_species': extinct_species,
        'species_type_filter': species_type_filter,
    })


@login_required
def ecosystem_create(request):
    if not (request.user.is_admin_user() or request.user.is_teacher_user()):
        messages.error(request, 'You do not have permission to create ecosystems.')
        return redirect('ecosystem:list')
    
    if request.method == 'POST':
        form = EcosystemForm(request.POST, request.FILES)
        if form.is_valid():
            ecosystem = form.save(commit=False)
            ecosystem.created_by = request.user
            ecosystem.save()
            messages.success(request, 'Ecosystem created successfully!')
            return redirect('ecosystem:detail', pk=ecosystem.pk)
    else:
        form = EcosystemForm()
    return render(request, 'ecosystem/form.html', {'form': form, 'action': 'Create'})


@login_required
def ecosystem_update(request, pk):
    ecosystem = get_object_or_404(Ecosystem, pk=pk)
    if not (request.user.is_admin_user() or request.user == ecosystem.created_by):
        messages.error(request, 'You do not have permission to edit this ecosystem.')
        return redirect('ecosystem:detail', pk=pk)
    
    if request.method == 'POST':
        form = EcosystemForm(request.POST, request.FILES, instance=ecosystem)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ecosystem updated successfully!')
            return redirect('ecosystem:detail', pk=ecosystem.pk)
    else:
        form = EcosystemForm(instance=ecosystem)
    return render(request, 'ecosystem/form.html', {'form': form, 'action': 'Update', 'ecosystem': ecosystem})


@login_required
def ecosystem_delete(request, pk):
    ecosystem = get_object_or_404(Ecosystem, pk=pk)
    if not (request.user.is_admin_user() or request.user == ecosystem.created_by):
        messages.error(request, 'You do not have permission to delete this ecosystem.')
        return redirect('ecosystem:detail', pk=pk)
    
    if request.method == 'POST':
        ecosystem.delete()
        messages.success(request, 'Ecosystem deleted successfully!')
        return redirect('ecosystem:list')
    return render(request, 'ecosystem/delete.html', {'ecosystem': ecosystem})


@login_required
def animal_create(request, ecosystem_pk):
    ecosystem = get_object_or_404(Ecosystem, pk=ecosystem_pk)
    if not (request.user.is_admin_user() or request.user.is_teacher_user()):
        messages.error(request, 'You do not have permission to create animals.')
        return redirect('ecosystem:detail', pk=ecosystem_pk)
    
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.ecosystem = ecosystem
            animal.save()
            messages.success(request, 'Animal created successfully!')
            return redirect('ecosystem:detail', pk=ecosystem_pk)
    else:
        form = AnimalForm()
    return render(request, 'ecosystem/animal_form.html', {'form': form, 'ecosystem': ecosystem})


@login_required
def animal_update(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if not (request.user.is_admin_user() or request.user.is_teacher_user()):
        messages.error(request, 'You do not have permission to edit this animal.')
        return redirect('ecosystem:detail', pk=animal.ecosystem.pk)
    
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            form.save()
            messages.success(request, 'Animal updated successfully!')
            return redirect('ecosystem:detail', pk=animal.ecosystem.pk)
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'ecosystem/animal_form.html', {'form': form, 'animal': animal, 'ecosystem': animal.ecosystem})


@login_required
def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    ecosystem_pk = animal.ecosystem.pk
    if not (request.user.is_admin_user() or request.user.is_teacher_user()):
        messages.error(request, 'You do not have permission to delete this animal.')
        return redirect('ecosystem:detail', pk=ecosystem_pk)
    
    if request.method == 'POST':
        animal.delete()
        messages.success(request, 'Animal deleted successfully!')
        return redirect('ecosystem:detail', pk=ecosystem_pk)
    return render(request, 'ecosystem/animal_delete.html', {'animal': animal})
