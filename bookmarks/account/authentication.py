from django.contrib.auth.models import User
from .models import Profile





#The user credentials will be checked using ModelBackend,
# and if no user is returned, the credentials
#will be checked using EmailAuthBackend.
class EmailAuthBackend:
    def authenticate(self,request,username=None,password=None):
        try:
            user = User.objects.get(email=username) #Bu userdaaa email bo`ssaa
            if user.check_password(password):# tekshiradi va hashlidi
                return user #va user qaytardi
            return None #user ichida email usernaame bo`sa NOne qaytaaradi
        except (User.DoesNotExist,User.MultipleObjectsReturned): #agar user topilmasa bergam emaial adrisaa xatolik beradi
            #DoesNotExist ishlidi,MultipleObjectsReturned-bu esa agar ko`p user topilsa bir xill email foydalangan ,
            return None #yoki hec nima qaytarmidi

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)#user_id oladi
        except User.DoesNotExist: #xatolik qaytaradi
            return None #yoki hec nima qaytarmaydi


def create_profile(backend,user,*args,**kwargs):
    Profile.objects.get_or_create(user=user)


