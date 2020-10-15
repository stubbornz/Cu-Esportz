from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, auth
from accounts.models import UserDetail
from . import backends
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def home(request):
    return HttpResponse("Home Page")

@csrf_exempt
def registration(request):
    return render(request, 'registration.html')
@csrf_exempt
def signIn(request):
    # fetching data from registration form
    if request.method == 'POST':
        user_mob = request.POST.get('user_mob')  # username/mobile number
        password = request.POST['password']

        # sign in with username
        user = auth.authenticate(username=user_mob, password=password)
        if user is not None:      # log in done
            auth.login(request, user)
            return render(request, 'join_Host.html')
        
        # signin with mobile number
        else: 
            with open('templates/totaluser.txt', 'r') as file:
                total = file.read()
                total_user = int(total)
            # get mobile number of user
            first_user = 1
            for ids in range(first_user, total_user + 1):
                try:
                    obj = UserDetail.objects.get(id=ids)
                except:
                    obj = ""
                mob_no = str(obj)

                # matching mob_no
                if mob_no == user_mob:
                    name = User.objects.get(id=ids)   # get username of the given id
                    username = str(name)
                    
                    user = auth.authenticate(username=username, password=password)
                    if user is not None:
                        auth.login(request, user)
                        return render(request, 'join_host.html')

                    else: return HttpResponse("password incorrect")

    return HttpResponse("user not found")


@csrf_exempt
def signUp(request):
    if request.method == 'POST':
        # extracting data from registration form
        name = request.POST['name']
        email = request.POST['email']
        mob_no = request.POST['mob']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        ref_code = request.POST['reffral_code']

        # checking password mismatch
        if password2 == password1:
            password = password1
        else: return HttpResponse("password does not match with previous password")

        # generate username
        username = backends.generateUserName(name=name)

        # pushing data in data base using User and UserDetail model
        user = User.objects.create_user(username=username, first_name=name, password=password, email=email)
        user.save()
        user_detatil = UserDetail(user=user, mob_no=mob_no, ref_code=ref_code)
        user_detatil.save()


        with open('templates/totaluser.txt', 'r') as file:
            total = file.read()
            count = int(total)

        # we are checking here that data is pushed or not
        if user is not None:
            if user_detatil is not None:
                count += 1
                with open('templates/totaluser.txt', 'w') as file:
                    file.write(str(count))
                return render(request, 'registration.html')
            else: return HttpResponse("Data is not saved in data base in UserDetail model")
        else: return HttpResponse("Data is not saved in data base in User Model")

    return HttpResponse("signing up failed")
