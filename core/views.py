from django.contrib.auth import get_user_model, login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.forms import ImageAdd, UserUpadate
from core.models import User, AjoutAnimal

Utilisateur = get_user_model()


def index(request):
    donnees = AjoutAnimal.objects.all()
    return render(request, 'core/index.html', locals())


def connexion(request):
    if request.method == 'POST':
        pseudo = request.POST.get('pseudo')
        passwd = request.POST.get('passwd')
        user = authenticate(
            username=pseudo,
            password=passwd
        )
        if user:
            login(request, user)
            return redirect('index')
        else:
            err = "ERRRRRRRRR LORS DE LA CONNEXION"
            return render(request, 'core/connexion.html', locals())
    return render(request, 'core/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect('index')


def inscription(request):
    if request.method == 'POST':
        pseudo = request.POST.get('pseudo')
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        passwd = request.POST.get('passwd')
        user_exist = User.objects.filter(username=pseudo)
        if user_exist:
            err = "USER EXIST"
            return render(request, 'core/inscription.html', locals())
        else:
            user = Utilisateur.objects.create_user(
                username=pseudo,
                email=email,
                first_name=prenom,
                last_name=nom,
                password=passwd
            )
            if user:
                login(request, user)
                return redirect('index')
    return render(request, 'core/inscription.html', locals())


@login_required
def add(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        form = ImageAdd(request.POST, request.FILES)
        # instance = form.save()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.proprietaire = user
            form.save()
            return redirect('index')
    else:
        form = ImageAdd()
    return render(request, 'core/ajout_image.html', locals())


def detail(request, id):
    entre = AjoutAnimal.objects.get(id=id)
    return render(request, 'core/detail.html', locals())


@login_required
def profiles(request):
    user = User.objects.get(id=request.user.id)
    publications = AjoutAnimal.objects.filter(proprietaire=user)
    return render(request, 'core/profiles.html', locals())

@login_required
def delete(request, id):
    entre = AjoutAnimal.objects.get(id=id)
    entre.delete()
    return redirect('profile')


@login_required
def edit_profile(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserUpadate(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpadate(instance=user)
    return render(request, 'core/edit_profile.html', locals())


@login_required
def edit_publication(request, id):
    entre = AjoutAnimal.objects.get(id=id)
    if request.method == 'POST':
        form = ImageAdd(request.POST, request.FILES, instance=entre)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ImageAdd(instance=entre)
    return render(request, 'core/edit_publication.html', locals())


@login_required
def delete_user(request, id):
    user = User.objects.get(id=id)
    logout(request)
    user.delete()
    return redirect('index')