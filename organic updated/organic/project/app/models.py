from django.db import models

class Logintable(models.Model):
    lid=models.AutoField(primary_key=True)
    l_email=models.CharField(max_length=150)
    l_pass=models.CharField(max_length=50)
    l_type=models.CharField(max_length=50)
    l_status=models.CharField(max_length=50)
    

class Usertable(models.Model):
    userid = models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=100)
    user_lname=models.CharField(max_length=100)
    user_phone=models.CharField(max_length=100)
    user_address=models.CharField(max_length=100)
    user_email=models.CharField(max_length=100)
    user_pass=models.CharField(max_length=100)
    user_loca=models.CharField(max_length=100)
    user1=models.CharField(max_length=100,default="" )
    user2=models.CharField(max_length=100,default="" )  
    
    
class Product_table(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_date=models.CharField(max_length=100)
    p_name=models.CharField(max_length=100)
    p_img=models.ImageField(max_length=100)
    p_cat=models.CharField(max_length=100)
    p_stock=models.CharField(max_length=100)
    p_rate=models.CharField(max_length=100)
    userid=models.ForeignKey(Usertable,on_delete=models.CASCADE,blank=True,null=True)
    pro1=models.CharField(max_length=100,default="" )
    pro2=models.CharField(max_length=100,default="" )
    
    
class Cart_table(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cart_date=models.CharField(max_length=100)
    cart_name=models.CharField(max_length=100)
    cart_cat=models.CharField(max_length=100)
    cart_stock=models.CharField(max_length=100)
    cart_rate=models.CharField(max_length=100)
    userid=models.ForeignKey(Usertable,on_delete=models.CASCADE,blank=True,null=True)
    p_id=models.ForeignKey(Product_table,on_delete=models.CASCADE,blank=True,null=True)
    cart1=models.CharField(max_length=100,default="" )
    cart2=models.CharField(max_length=100,default="" )
    

class Feedback(models.Model):
    fid=models.AutoField(primary_key=True)
    userid=models.ForeignKey(Usertable,on_delete=models.CASCADE,blank=True,null=True)
    feed2=models.CharField(max_length=100,default="" )
    feed=models.CharField(max_length=150)
    
    
class Dboytable(models.Model):
    dboyid = models.AutoField(primary_key=True)
    dboy_name=models.CharField(max_length=100)
    dboy_lname=models.CharField(max_length=100)
    dboy_phone=models.CharField(max_length=100)
    dboy_address=models.CharField(max_length=100)
    dboy_email=models.CharField(max_length=100)
    dboy_pass=models.CharField(max_length=100)
    dboy_loca=models.CharField(max_length=100)
    dboy1=models.CharField(max_length=100,default="" )
    dboy2=models.CharField(max_length=100,default="" ) 