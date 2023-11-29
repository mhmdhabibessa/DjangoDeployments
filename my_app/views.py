from django.shortcuts import render ,HttpResponse,redirect
from .models import Movie,Category,Actor,User,MovieForm
from django.contrib import messages
import bcrypt
# from somewhere import handle_uploaded_file

def upload_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.image_file = form.cleaned_data['image_file']
            movie.save()
            return redirect('success_page')  # Replace 'success_page' with the actual URL or view name you want to redirect to after successful upload
    else:
        form = MovieForm()

    return render(request, 'upload_movie.html', {'form': form})


# Create your views here.
def index(request):
    context = {
        "movies" : Movie.objects.all(),
        "actors_movie" : Movie.objects.all(),
        "category" : Category.objects.all(),
        "actors" : Actor.objects.all()
    }
    return render(request,"index.html",context)

def categoryForm(request):
    return render(request,"category-form.html")

def ActorForm(request):
    return render(request,"form_actor.html")

def createCategory(request):
    Category.objects.create(name=request.POST['name'])
    return redirect('/')
    
def formMovie(request):
    data =  {
        "categories" : Category.objects.all() 
    }
    return render(request,"form_movie.html",data)
def createActor(request):
    Actor.objects.create(name=request.POST['name'],age=request.POST['age'])
    return redirect('/')

def createMovie(request):
    errors = Movie.objects.basic_validator(request.POST)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie successfully created")
            return redirect('/')
        else:
            for key, value in errors.items():
                        messages.error(request,value, extra_tags= key)
            return redirect('/create-movie')
    else :
        form = MovieForm()
    return render(request, 'create_movie.html', {'form': form})

    # errors = Movie.objects.basic_validator(request.POST)
    # if len(errors) > 0 :
    #     for key,value in errors.items():
    #         messages.error(request,value)
    #     return redirect ('/create-movie')
    
    # else :
    #     category_id = int(request.POST['category'])
    #     Movie.objects.create(
    #                         title=request.POST['title'],
    #                         release_date = "2023-11-19 12:00:00",
    #                         duration= 200,
    #                         description=request.POST['description'],
    #                         image = request.POST['image'],
    #                         category = Category.objects.get(id=category_id) 
    #                         )
    #     messages.success(request, "Movie successfully updated")
    #     return redirect('/')

def addActorToMove(request):
    
    
    actor_id = request.POST['actor_id']
    movie_id = request.POST['movie_id']
    thisMovie = Movie.objects.get(id=movie_id)
    thisActor = Actor.objects.get(id=actor_id)    
    thisMovie.actors.add(thisActor)	
    return redirect('/')

def createuserForm(request):
    return render(request,"form-user.html")

def createUser(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for tag, error in errors.items():
            messages.error(request, error)
        return redirect('/create-user-form')
    else:
        password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=password_hash)
        return redirect('/')