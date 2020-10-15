<--All about this project-->

# Hrk
1. Creating base of project...

2. creating an app for authentication purpose...
    1. urls mapping
    2. declaring functions in views
    3. creating models
    4. registring models for admin
    5. making migrations and deploying it
    6. creating superuser(username=admin, password=admin)

3. signup with registration form
    1. using csrf in form for security purpose
    2. defining action and methods in forms in 'registration.html'
    3. defining 'signUp' method in 'accounts.views' after that we can sign up in the web
    4. we are generating username for non staff user ()<<<--->>>(10)
    5. we are storing mob_no and refral code in different model

4. signin with registration form
    1. there are two ways of signing in the web - username and mob_no
    2. defining a function for signing with username and mobile
    3. authenticating with username using 'auth' model
    4. authenticating with mob_no using ()<<<--->>>(10)

5. customizing admin page
    1. creating a method in accounts/models.py which return current mobile number
        1. creating '__str__(self)' method and returning mobile number
        2. you can access this value by using 'UserDetail.objects.get(id=object_id_var)'
    2. for changing titles of site, override variables in accounts.urls.py

6. loading all html files
    1. create templates directory in src
    2. put all html files in temlates
    3. adding temlates diectory in settings.py in templates list

7. loading static files it means load all java script, css files and images files.
    1. creating a static directory
    2. create 'STATICFILES_DIRS' in setting
    3. put all js, css and images files in static directory
    4. before every static files use '/static/' because these files are present in static file
        1. provide actual url or
        2. load all static files in the html file using {%load static%}
            1. use jinja syntax in all static files like {% static 'img_dir/img_name.jpg' %}
    
8. authenticating by mobile number
    1. getting mobile number from UserDetail model
    2. checking the mobile number with user entered mobile number and iterating through it ()<<<--->>>(9)
    3. if number matched then get user from User model and 
    4. we are passing username and password in auth

9. we still don't know that how many users we have 
    1. countimng users
    2. creating a text file and set the total numbner of current user 
    3. total numbers means maximum id or id of last user
    4. every time a user created increment in it by 1
    5. if you are creating user manually then increment in templates/totaluser.txt by 1
    
10. generating username
    1. creating a function in backends.py
    2. (documents are available at accounts/backends.py)

-->future_errors
11. Solving incorrect padding error by deleting sessios object ...
        (before deployment or whenever we are facing this error)
        '''
            # deleting undetected sessions
            Session.objects.all().delete()
        '''
        ()<<<--->>>(accounts/admins.py)

12. solving this error 'TypeError: argument of type 'PosixPath' is not iterable'
    1. using pathlib
    2. documents are present here) ()<<<--->>>(
        https://adamj.eu/tech/2020/03/16/use-pathlib-in-your-django-project/
        )

13. deleting superuser before deployment 
    1. Esportz/accounts/signin.first_user with the current superuser's id
    2. due to optimizing linear search for mobile number

14. csrf verification failed (admin/...  ,  account/...)
    1. using csrf_exempt decorator

15. creating an another app for Host and join section
    1. urls mapping
    2. register the app in Esportz/settings.py
    3. creating models for join_host app
    4. register model in admin section
