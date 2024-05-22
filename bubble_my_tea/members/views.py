from django.db import connection
from django.shortcuts import render, redirect
from operator import itemgetter
from django.contrib import messages
from . import forms
from .models import Products
from datetime import datetime
import bcrypt
import jwt

#allows users to go to designate homepage depending on their token and role
def homepage(request):
    if request.session.get('token') is None:
        return render(request, 'homepage.html', getAllProducts())
    else:
        user_id = getUserIdFromToken(request)
        admin = getuserAdminValue(user_id)[0][0]
        if admin == 0:
            return render(request, 'client.html', getAllProducts())
        else:
            return render(request, 'admin.html', getAllProducts())

#allows user to log in and create a token
def login(request):
    cursor = connection.cursor()
    cursor2 = connection.cursor()
    sqlQuery = "SELECT email FROM users"
    sqlQuery2 = "SELECT password FROM users"
    cursor.execute(sqlQuery)
    cursor2.execute(sqlQuery2)
    emails=[]
    passwords=[]
    for i in cursor:
        emails.append(i)
    for j in cursor2:
        passwords.append(j)
    res = list(map(itemgetter(0), emails))
    res2 = list(map(itemgetter(0), passwords))
    form = forms.LoginForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            for i in range(0, len(res)):
                if res[i]==email and bcrypt.checkpw(bytes(password.encode('utf-8')), bytes(res2[i].encode('utf-8'))):
                    user_id = getUserId(email)
                    jwt_obj= {
                        'user_id': user_id[0],
                    }
                    token = jwt.encode(jwt_obj, 'secret', algorithm='HS256')
                    request.session['token'] = token
                    request.session.save()
                    return redirect('/')
                    break
                elif res[i]==email and bcrypt.checkpw(bytes(password.encode('utf-8')), bytes(res2[i].encode('utf-8'))) == False:
                    messages.info(request, "Mauvais email ou password!")
                    return redirect('/login')
                elif i == len(res) - 1:
                    messages.info(request, "Utilisateur n'existe pas")
                    return redirect('/login')
                render(request, 'homepage.html')
        else:
            messages.info(request, "Remplissez les champs!")
            return redirect('/login')
    return render(request, 'login.html')

#allows user to register and insert their data in th database 
def register(request):
    cursor = connection.cursor()
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            firstname= data['firstname']
            lastname= data['lastname']
            email= data['email']
            username= data['username']
            password= data['password']
            address= data['address']
            admin = data['admin']
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            sqlQuery = "SELECT email FROM users"
            cursor.execute(sqlQuery)
            emails=[]
            for i in cursor:
                emails.append(i)
            res = list(map(itemgetter(0), emails))
            for i in range(0, len(res)):
                if res[i]==email:
                    messages.error(request, 'Utilisateur existe déjà!')
                    return redirect('/register')
                    break
            cursor.execute(
                "INSERT INTO users (firstname, lastname, email, username, password, address, admin, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (firstname, lastname, email, username, hashed_password, address, admin, datetime.now(), datetime.now())
            )
            messages.success(request, 'Compte créé avec succès!')
            return redirect('login')
        else:
            messages.error(request, 'Le formulaire est invalide. Veuillez corriger les erreurs.')
    else:
        form = forms.RegisterForm()
    return render(request, 'register.html', {'form': form})

#allows client users to go to their profile page
def profilePage(request):
    user_id = getUserIdFromToken(request)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchall()
    context = {
        'result': user,
    }
    return render(request, 'profile.html', context)

#function that gets user id from their email
def getUserId(email):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
    row = cursor.fetchone()
    return row

#allows users to see their past orders
def orders(request):
    user_id = getUserIdFromToken(request)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM products as p JOIN orders as o ON p.id=o.product_id JOIN users as u ON o.user_id=u.id WHERE u.id=%s", (user_id,))
    products = cursor.fetchall()
    orders_list = products
    context = {
        'result': orders_list,
    }
    return render(request, 'orders.html', context)

#function for mysql queries
def my_custom_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchall()
    return row

#function that gets all products from the database and puts them in an object
def getAllProducts():
    result = my_custom_sql("SELECT * FROM products;")
    result_list = result
    context = {
        'result': result_list,
    }
    return context

#function that returns the role of the user on connexion
def getuserAdminValue(id):
    cursor = connection.cursor()
    cursor.execute("SELECT admin FROM users WHERE id=%s", (id,))
    row = cursor.fetchall()
    adminValue = row
    return adminValue

#function that gets user id with their token
def getUserIdFromToken(request):
    token = request.session.get('token')
    decode_token = jwt.decode(token, 'secret', algorithms=["HS256"])
    return decode_token['user_id']

#allows users to logout and destroy their token
def logout(request):
    del request.session['token']
    return redirect('/login')

#allows users to update their data
def updateUser(request):
    if request.session.get('token') is None:
        return redirect('/')
    else:
        form = forms.UpdateForm(request.POST)
        user_id = getUserIdFromToken(request)
        if request.method == "POST":
            if form.is_valid():
                data = form.cleaned_data
                username= data['username']
                password= data['password']
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                address= data['address']
                cursor = connection.cursor()
                cursor.execute("UPDATE users SET username = %s, password = %s, address = %s WHERE id = %s", (username, hashed_password, address, user_id))
                return redirect('profile')
        return render(request, 'updateUser.html')

#allows admin to add new bubbleteas to their database
def addBubbletea(request):
    if request.session.get('token') is None:
        return redirect('/')
    else:
        user_id = getUserIdFromToken(request)
        admin = getuserAdminValue(user_id)[0][0]
        if admin == 0:
            return render(request, 'client.html', getAllProducts())
        else:
            cursor = connection.cursor()
            if request.method == "POST":
                form = forms.ProductsForm(request.POST)
                if form.is_valid():
                    data = form.cleaned_data
                    name= data['name']
                    description= data['description']
                    price= data['price']
                    extras= data['extras']
                    
                    if name and description and price and extras:
                        try:
                            price = float(price)
                            if price <= 0:
                                print("Le prix doit être un nombre positif.")
                        except:
                            return redirect('addBubbletea')
                    cursor.execute("INSERT INTO products (name, description, price, extras) VALUES (%s, %s, %s, %s)",(name, description, price, extras))
                    messages.success(request, 'Bubbletea ajouté !')
                    return redirect('/')
                else:
                    messages.error(request, "L'ajout du bubbletea a échoué !")
            else:
                form = forms.ProductsForm()
            return render(request, "addBubbletea.html", {'form': form})

#mysql query to delete product
# def deleteBubbletea(request):
#     form = forms.DeleteProductsForm(request.POST)
#     if form.is_valid() == False:
#         data = form.cleaned_data
#         print(data)
#         products = getAllProducts()
#         print(products.0)
#         for product in products.result:
#             if product_name == product[1]:
#                 cursor = connection.cursor()
#                 cursor.execute("DELETE * FROM products WHERE name = %s", (product_name,))
#     else:
#         print("no")
#     return redirect('/')