from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect

from saidia_app.forms import *
from saidia_app.models import *
from saidia_app.cipher import *
from saidia_app.error_list import *

# Create your views here.

def add_orphanage(request):
    # one can only access this view if they have logged in
    # otherwiser an error status with the 404 code will be raised
    if "user" in request.session:
        user_id = request.session["user"]

        # checks if manager is adding a new orphanage
        if request.method == "POST":
            # TODO: ADD CODE TO ADD NEW ORPHANAGE TO THE SYSTEM
            user = User.objects.get(id = user_id)
            manager = Manager.objects.get(user = user)

            # extract data from orphanage_form
            orphanage_form = OrphanageForm(request.POST)
            if orphanage_form.is_valid():
                # get orphanage name
                orph_name = orphanage_form.cleaned_data['name']
                # get capacity
                orph_cap = orphanage_form.cleaned_data['capacity']
                # get location
                orph_loc = orphanage_form.cleaned_data['location']
                # get x-coordinate and y_coordinate
                x_coord = orphanage_form.cleaned_data['x_coordinate']
                y_coord = orphanage_form.cleaned_data['y_coordinate']

                # create model object and save it
                orphanage = Orphanage(
                    name = orph_name,
                    manager = manager,
                    capacity = orph_cap,
                    location = orph_loc,
                    x_coordinate = x_coord,
                    y_coordinate = y_coord
                )
                orphanage.save()
            return redirect('saidia_app:manage')
        else:
            orphanage_form = OrphanageForm()
            return render(request, 'saidia_app/add_orphanage.html',{
                "orphanage_form": orphanage_form,
            })
    return redirect("saidia_app:error", 400)

def add_need(request, oph):
    # one can only add need if they
    # are logged in.
    # otherwise, error is returned
    if 'user' in request.session:
        if request.method == "POST":
            oph_need_form = OphNeedsForm(request.POST)
            # validate form data
            if oph_need_form.is_valid():
                orphanage = Orphanage.objects.get(id = oph) #get orphanage with specified id
                need = oph_need_form.cleaned_data["needs"][0]
                orphanage.needs.add(need.id)
                return redirect("saidia_app:add_need",oph)

        # perform in GET method
        oph_need_form = OphNeedsForm()
        needs = Orphanage.objects.get(id = oph).needs.all()

        return render(request, "saidia_app/add_need.html", {
            "oph_need_form": oph_need_form,
            "orph_id":oph,
            "orph_needs": needs
        })
    else:
        return redirect("saidia_app:error", 400)

def error(request, error_id):
    message = errors.get_error(error_id)

    return render(request, "saidia_app/error.html", {
        "message": message
    })

def get_coord(request):
    # get location id
    if request.method == "POST":
        location_id = request.POST['id']
        location = Location.objects.get(id = location_id)
        print(location.x_coordinate)

    body = {
        "x": location.x_coordinate,
        "y": location.y_coordinate
    }
    data = {
        'head': 'locationCoordinates',
        'body': body
    }
    return JsonResponse(data)

def index(request):
    orphanages = Orphanage.objects.all()
    if request.method == "POST":
        if "orphanage" in request.POST:
            orphanages = Orphanage.objects.filter(name__icontains = request.POST["orphanage"])
            return render(request, "saidia_app/index.html",{
                "orphanages": orphanages
            })


         # coordinates of the donor
         # remember them for subsequent calls
        coordinates = {
            "lat": request.POST["lat"],
            "lng": request.POST["lon"]
        }
        request.session["coord"] = coordinates 

        # feedback to ajax request
        data = {
            'head': 'close_orphanages',
            'body': 'success'
        }
        return JsonResponse(data)

    return render(request, "saidia_app/index.html",{
        "orphanages": orphanages
    })

def login(request):
    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        auth_form = AuthForm(request.POST)

        # validates form
        if user_form.is_valid() and auth_form.is_valid():
            email = user_form.cleaned_data['email']

            # get user with specified email
            # if exist, validate password otherwise return error
            user = User.objects.filter(email = email)
            if user.count() != 0:
                user = user[0]
                password = Manager.objects.filter(
                    user = user,
                    password = encrypt(auth_form.cleaned_data['password'])
                )

                # if a record with specified user and password returns
                # redirect to management page
                if password.count() != 0:
                    # create session for the user
                    request.session["user"] = user.id
                    return redirect('saidia_app:manage')

        # eror if invalid data
        error = "invalid credentials"

        return render(request, "saidia_app/login.html",{
            "user_form": user_form,
            "auth_form": auth_form,
            "error": error
        })
    else:
        user_form = LoginForm()
        auth_form = AuthForm()
        return render(request, "saidia_app/login.html",{
            "user_form": user_form,
            "auth_form": auth_form
        })

def logout(request):
    request.session.pop("user")
    return redirect("saidia_app:index")

def manage(request):
    if "user" in request.session:
        # get list of orphanages for the manager in session.
        user_id =  request.session["user"] #get user id from session
        user = User.objects.get(id = user_id) #get user with specified id
        manager = Manager.objects.get(user = user) #get the id of the manager
        orphanages = Orphanage.objects.filter(manager = manager) # get orphanages manaaged by this specific manager

        return render(request, "saidia_app/manage.html",{
            "manager": request.session["user"],
            "orphanages": orphanages
        })
    return redirect("saidia_app:error", 403)

def orphanage(request, orph_id):
    orphanage = Orphanage.objects.get(id = orph_id)

    # TODO: when method is POST
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            message = review_form.cleaned_data['message']
        else:
            # TODO: fix redirect
            return redirect("saidia_app:error", 404)
        if 'user' in request.session:
            user_id = request.session['user']

            # create and save review
            review  = Review(
                user = User.objects.get(id =user_id),
                orphanage = Orphanage.objects.get(id = orph_id),
                message = message
            )
            review.save()
        else:
            return redirect("saidia_app:error", 400)

    reviews = Review.objects.filter(orphanage = orph_id)
    review_form = ReviewForm()
    return render(request, "saidia_app/orphanage.html", {
        "orphanage": orphanage,
        "review_form": review_form,
        "reviews": reviews
    })

def register(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        auth_form = AuthForm(request.POST)

        # save user object if valid
        if user_form.is_valid():
            user = user_form.save()

            if auth_form.is_valid():
                # use user object to create Manager object
                # password is hashed first before encryption
                password = encrypt(auth_form.cleaned_data['password'])

                manager =  Manager(user = user, password=password)
                manager.save()

                #create session for the user
                request.session["user"] = user.id

                # Manager has successfully been created
                # redirect to the management page

                return redirect('saidia_app:manage')
    else:
        user_form = RegisterForm()
        auth_form = AuthForm()
    return render(request, "saidia_app/register.html",{
        "user_form": user_form,
        "auth_form": auth_form
    })

def remove_need(request, orph_id, need_id):
    # one can only remove need if
    # session is established
    if 'user' in request.session:
        user_id = request.session['user']

        # delete the need from the orphanage
        orphanage = Orphanage.objects.get(id = orph_id)
        need = Needs.objects.get(id = need_id)
        orphanage.needs.remove(need)
        return redirect("saidia_app:add_need",orph_id)

    return redirect("saidia_app:index")

def remove_orphanage(request, orph_id):
    if 'user' in request.session:
        user_id = request.session['user']

        # delete the orphanage
        Orphanage.objects.get(id = orph_id).delete()
    return redirect('saidia_app:manage')
