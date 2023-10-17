from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from email.policy import default
from tkinter.tix import Tree
from unittest.util import _MAX_LENGTH
from django.db import models
from .models import *
from django.db.models import Q
import datetime
from django.utils import timezone
import pytz
from django.core.files.storage import FileSystemStorage


import mimetypes
mimetypes.add_type("text/css",".css",True)

def home(request):
    return render(request,'home.html')

# =============================user registrations =============================
def user_reg(request):
    msg=""
    if request.POST:
        passs=request.POST["a4"]
        cpass=request.POST["a5"]
        if cpass==passs:
            if(Logintable.objects.filter(l_email=request.POST["a3"]).exists()):
                msg="Username already exist"
            else:
                obj=Usertable.objects.create(user_name=request.POST["a1"],user_lname=request.POST["a2"],user_phone="add details",user_email=request.POST["a3"],user_pass=request.POST["a4"],user_loca="add details",user_address="add details")
                obj.save()
                obj1=Logintable.objects.create(l_email=request.POST["a3"],l_pass=request.POST["a4"],l_type="user",l_status="pending")
                obj1.save()
                return HttpResponseRedirect("/login")
        else:
            msg="password mismatch"
            # print(msg)
            
    return render(request,"user_reg.html",{"msg":msg})

# =====================================login =================================

def login(request):
    msg=""
    msgg=request.GET.get('msg')
    print(msgg)
    if request.POST: 
        msg=""
        log_user=request.POST["log1"]
        log_pass=request.POST["log2"]
        request.session["unme"]=log_user
        obj=Logintable.objects.filter(Q(l_email=log_user)&Q(l_pass=log_pass))
        if obj:
            if (obj[0].l_type=="user"):
                if (obj[0].l_status=="approved"):
                
                    obj1=Usertable.objects.filter(user_email=log_user)
                    request.session["uid"]=obj1[0].userid
                    request.session["t1"]=obj1[0].user_name
                    return HttpResponseRedirect("/user_home")
            
            elif (obj[0].l_type=="admin"):
                obj1=Usertable.objects.filter(user_email=log_user)
                request.session["uid"]=obj1[0].userid
                request.session["t1"]=obj1[0].user_name
                return HttpResponseRedirect("/admin_home")
            
            elif (obj[0].l_type=="dboy"):
                if (obj[0].l_status=="approved"):
                
                    obj1=Dboytable.objects.filter(dboy_email=log_user)
                    request.session["dboyid"]=obj1[0].dboyid
                    # request.session["t1"]=obj1[0].user_name
                    return HttpResponseRedirect("/dboy_home")
            
            
        else:
            msg="invalid username and password"
            print("msg "+msg)
            # return HttpResponseRedirect("/login")
    return render(request,'login.html',{"mmm":msg})



# =====================user home =================
def user_home(request):
    return render(request,'user/user.html')
def dboy_home(request):
    return render(request,'dboy/dboy_home.html')



# =====================admin home =================
def admin_home(request):
    return render(request,'admin/admin_home.html')

# ===============================add products =============================
# def admin_add_products(request):
#     return render(request,'admin/admin_add_product.html')

def admin_add_products(request):
    uid=request.session.get('uid')
    print(uid)
    msg = ""
    msg = request.GET.get('msg')
    if request.POST:
        image = request.POST.get("Image")
        myfile = request.FILES["Image"]
        productname = request.POST.get("Product Name")
        category = request.POST.get("Category")
        stock = request.POST.get("Stock")
        price = request.POST.get("Price")
        uid=request.session["uid"]
        print(uid)
        ab = Product_table.objects.create(
                p_name=productname, p_img=myfile, p_stock=stock, p_rate=price, p_cat=category,p_date ="date",userid_id=uid)
        ab.save()    
        msg = "Added sucessfully"
    return render(request, 'Admin/admin_add_product.html',{"msg": msg})


# =======================view product= ===============================

def admin_view_product(request):
    msg = request.GET.get("msg")
    
    abc=Product_table.objects.all()
    return render(request, 'admin/admin_view_product.html',{"abc":abc,"msg":msg})


# ===============================admin delete product===========================


def delete_product(request):
    
    msg="deleted"
    id=request.GET["id"]
    abc=Product_table.objects.filter(p_id=id).delete()
    
    print(id)
    print("-----------------------------------------")
    return HttpResponseRedirect("/admin_view_product?msg="+msg)


def update_product(request):
    id=request.GET["id"]
    
    abc=Product_table.objects.filter(p_id=id)    
    if request.POST:
        a1=request.POST["a1"]
        a2=request.POST["a2"]
        a3=request.POST["a3"]
        qun = abc[0].p_stock
        # qty = request.POST["a4"]
        # print(qty)
            # Total = int(rate)*int(qty)
        upqun = int(qun)+int(a2)
        upqun = str(upqun)
        abc=Product_table.objects.filter(p_id=id).update(p_name=a1,p_stock=upqun,p_rate=a3)
        msg="updated"
        
        print(id)
        print("-----------------------------------------")
        return HttpResponseRedirect("/admin_view_product?msg="+msg)
    return render(request,"admin/updateproduct.html",{"abc":abc})


# admin view user============================================

def admin_view_user(request):
    msg = request.GET.get("msg")
    
    abc=Usertable.objects.filter(user1="")
    # edf=Logintable.objects.all()
    return render(request, 'admin/view_user.html',{"abc":abc,"msg":msg})

def delete_user(request):
    
    msg="deleted"
    id=request.GET["id"]
    abc=Usertable.objects.filter(userid=id).delete()
    
    print(id)
    print("-----------------------------------------")
    return HttpResponseRedirect("/admin_view_user?msg="+msg)

def approve_user(request):
    
    msg="Approved"
    id=request.GET["id"]
    
    
    abc=Usertable.objects.filter(userid=id)
    qun = abc[0].user_email
    edf=Logintable.objects.filter(l_email=qun).update(l_status="approved")
    data=Usertable.objects.filter(userid=id).update(user1="approved")
    
    
    
    print(id)
    print("-----------------------------------------")
    return HttpResponseRedirect("/admin_view_user?msg="+msg)
# ===============================user veiw product=========================================

def user_view_product(request):
    msg = request.GET.get("msg")
    uid=request.session['uid']
    
    
    abc=Product_table.objects.all()
    current_date = datetime.date.today()
    current_time = timezone.now()
    current_time = timezone.now() 
    timezone_India = pytz.timezone('Asia/Kolkata') 
    India_time = current_time.astimezone(timezone_India) 

    # id=request.GET["id"]
    if request.POST:
        addadd=Usertable.objects.filter(userid=uid)
        a1=request.POST["a1"]
        a2=request.POST["a2"]
        # a3=request.POST["a3"]
        obc=Product_table.objects.filter(p_id=a1)  
        qun = obc[0].p_stock
        rate=obc[0].p_rate
        
      
        upqun = int(qun)-int(a2)
        total=int(rate)*int(a2)
        ad=addadd[0].user_address
        print(ad)
        b="add details"
        if ad==b:
            msg=""
            return HttpResponseRedirect("/update_profile?msg="+msg)
            
        else:
            if upqun>0:
                upqun = str(upqun)
                total=str(total)
                abcd=Product_table.objects.filter(p_id=a1).update(p_stock=upqun)
                obj=Cart_table.objects.create(p_id_id=a1, cart_stock=a2,cart_date=India_time,cart_rate=total,userid_id=uid,cart_name="user",cart_cat="booked")
                obj.save
                print("============================",upqun)
                print(total)
                print(India_time)
                print(uid)
                msg="added to user cart"
                
            else:
                msg="item out of stock"
    # return HttpResponseRedirect("/admin_view_user?msg="+msg)
    return render(request, 'user/view_product.html',{"abc":abc,"msg":msg})


def updateprofile(request):
    uid=request.session['uid']
    
    
    if request.POST:
        a1=request.POST["a1"]
        a2=request.POST["a2"]
        a3=request.POST["a3"]
        addadd=Usertable.objects.filter(userid=uid).update(user_phone=a1,user_address=a2,user_loca=a3)
        
        msg="Profile updated"
        return HttpResponseRedirect("/user_view_product?msg="+msg)
    
    return render(request, 'user/update_profile.html')

# useer view history===================================================================
def view_history(request):
    msg=""
    uid=request.session['uid']

    abc=Cart_table.objects.filter(userid_id=uid,cart_cat="paid")
    print(uid)
    print(uid)
    print(abc)
    if request.POST:
        abc=Cart_table.objects.filter(userid_id=uid).delete()
        msg="moved to trash"

    
    return render(request, 'user/view_booked_history.html',{"abc":abc,"msg":msg})

def booked_pro(request):
    msg=""
    btn=""
    uid=request.session['uid']

    abc=Cart_table.objects.filter(userid_id=uid,cart_cat="booked")
    return render(request, 'user/booked_pro.html',{"abc":abc,"msg":msg})




# =========================useradd products =========================
def user_add_products(request):
    uid=request.session.get('uid')
    print(uid)
    msg = ""
    msg = request.GET.get('msg')
    if request.POST:
        image = request.POST.get("Image")
        myfile = request.FILES["Image"]
        productname = request.POST.get("Product Name")
        category = request.POST.get("Category")
        stock = request.POST.get("Stock")
        price = request.POST.get("Price")
        uid=request.session["uid"]
        print(uid)
        ab = Product_table.objects.create(
                p_name=productname, p_img=myfile, p_stock=stock, p_rate=price, p_cat=category,p_date ="date",userid_id=uid)
        ab.save()    
        msg = "Added sucessfully"
    return render(request, 'user/user_add_product.html',{"msg": msg})


# =======================view product= ===============================

def u_view_product(request):
    msg = request.GET.get("msg")
    
    abc=Product_table.objects.all()
    return render(request, 'admin/admin_view_product.html',{"abc":abc,"msg":msg})


# ===============================admin delete product===========================


def u_delete_product(request):
    
    msg="deleted"
    id=request.GET["id"]
    abc=Product_table.objects.filter(p_id=id).delete()
    
    print(id)
    print("-----------------------------------------")
    return HttpResponseRedirect("/admin_view_product?msg="+msg)


def u_update_product(request):
    id=request.GET["id"]
    
    abc=Product_table.objects.filter(p_id=id)    
    if request.POST:
        a1=request.POST["a1"]
        a2=request.POST["a2"]
        a3=request.POST["a3"]
        qun = abc[0].p_stock
        # qty = request.POST["a4"]
        # print(qty)
            # Total = int(rate)*int(qty)
        upqun = int(qun)+int(a2)
        upqun = str(upqun)
        abc=Product_table.objects.filter(p_id=id).update(p_name=a1,p_stock=upqun,p_rate=a3)
        msg="updated"
        
        print(id)
        print("-----------------------------------------")
        return HttpResponseRedirect("/admin_view_product?msg="+msg)
    return render(request,"admin/updateproduct.html",{"abc":abc})

def payment(request):
    uid=request.session.get('uid')
    
    
    total = 0
    abc = Cart_table.objects.filter(cart_cat="booked",userid_id=uid)
    for i in abc:
        total += int(i.cart_rate)
    print(total)
    if request.POST:
        obj=Cart_table.objects.filter(userid_id=uid).update(cart_cat="paid")
    return render(request,"user/payment.html",{"total":total})

def admin_booked_pro(request):
   
    msg=""
    uid=request.session['uid']

    abc=Cart_table.objects.all()
    print(uid)
    print(uid)
    print(abc)
    if request.POST:
        abc=Cart_table.objects.filter(userid_id=uid).delete()
        msg="moved to trash"

    
    return render(request, 'admin/admin_booked_pro.html',{"abc":abc,"msg":msg})

def feedback(request):
    abc=Feedback.objects.all()
    
    if request.POST:
        msg=""
        uid=request.session['uid']
        typ=request.session['t1']
        a1=request.POST["a1"]
        
        print(typ)
        if typ=="admin":
            ghi=Feedback.objects.create(feed=a1,userid_id=uid) 
            msg="added to feedback"
            return HttpResponseRedirect("/admin_home?msg="+msg)
        else:
            ghi=Feedback.objects.create(feed=a1,userid_id=uid)
            msg="added to feedback"
            
            return HttpResponseRedirect("/user_home?msg="+msg)

    return render(request, 'admin/admin_feedback.html',{"abc":abc})


# =============================delivery boy registrations =============================
def dboy_reg(request):
    msg=""
    if request.POST:
        passs=request.POST["a4"]
        cpass=request.POST["a5"]
        if cpass==passs:
            if(Logintable.objects.filter(l_email=request.POST["a3"]).exists()):
                msg="Username already exist"
            else:
                obj=Dboytable.objects.create(dboy_name=request.POST["a1"],dboy_lname=request.POST["a2"],dboy_phone="add details",dboy_email=request.POST["a3"],dboy_pass=request.POST["a4"],dboy_loca="add details",dboy_address="add details")
                obj.save()
                obj1=Logintable.objects.create(l_email=request.POST["a3"],l_pass=request.POST["a4"],l_type="dboy",l_status="pending")
                obj1.save()
                return HttpResponseRedirect("/login")
        else:
            msg="password mismatch"
            # print(msg)
            
    return render(request,"dboy_reg.html",{"msg":msg})

def admin_view_dboy(request):
    msg = request.GET.get("msg")
    
    abc=Dboytable.objects.filter(dboy1="")
    # edf=Logintable.objects.all()
    return render(request, 'admin/view_dboy.html',{"abc":abc,"msg":msg})

def delete_dboy(request):
    
    msg="deleted"
    id=request.GET["id"]
    abc=Dboytable.objects.filter(dboyid=id).delete()
    
    print(id)
    print("-----------------------------------------")
    return HttpResponseRedirect("/admin_view_dboy?msg="+msg)

def approve_dboy(request):
    
    msg="Approved"
    id=request.GET["id"]
    
    
    abc=Dboytable.objects.filter(dboyid=id)
    qun = abc[0].dboy_email
    edf=Logintable.objects.filter(l_email=qun).update(l_status="approved")
    data=Dboytable.objects.filter(dboyid=id).update(dboy1="approved")
    
    
    
    print(id)
    print("-----------------------------------------")
    return HttpResponseRedirect("/admin_view_dboy?msg="+msg)

def dboy_booked_pro(request):
   
    msg=""
    # id=""
    # id=request.GET["id"]
    dboyid=request.session['dboyid']
    abc=Cart_table.objects.filter(cart_cat="paid")
    if request.POST:
        a1=request.POST["a1"]
        abo=Cart_table.objects.filter(userid_id=a1).update(cart_cat="delivered")
        msg="Updated"

    
    return render(request, 'dboy/dboy_view_order.html',{"abc":abc,"msg":msg})