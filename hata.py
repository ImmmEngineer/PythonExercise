# x=10

# if x>5:
#     raise Exception("5debd büyük")

def checkPsw(psw):
    import re
    if len(psw) < 8:
        raise Exception("en az 8 karakter olsun")
    elif not re.search("[a-z]",psw):
        raise Exception("parola küçük harf içermelidir")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola büyük harf içermelidir")
    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam içermelidir")
    elif not re.search("[_@$]",psw):
        raise Exception("parola alfa numerik karakter  içermelidir")
    elif re.search("\s", psw):
        raise Exception("parola bosluk icermemelidir")
    else:
        print("Geçerli parola")

password = "12345678Ab0_ "
try:
    checkPsw(password)
except Exception as ex:
    print(ex)
else:
    print("geçerli parola")
finally:
    print("validation tamamlandi")