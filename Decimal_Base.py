def Test_Decimal():
    assert Decimal(367,2)==101101111
    assert Decimal(9839,8)==23157
    assert Decimal(8320,16)==2080
    print("Pruebas exitosas")
def Decimal(Numero,Base):
    return Decimal_aux(Numero,Base,0,0)
def Decimal_aux(Numero,Base,Contador,Respuesta):
    if Numero==0:
        return Respuesta
    else:
        return Decimal_aux(Numero//Base,Base,Contador+1,(Numero%Base)*10**Contador+Respuesta)
Test_Decimal()
def Test_A_Decimal():
    assert A_Decimal(100101110,2)==302
    assert A_Decimal(7353,8)==3819
    assert A_Decimal(84374,16)==541556
    print("Pruebas exitosas")
def A_Decimal(Numero2,Base2):
    return A_Decimal_aux(Numero2,Base2,0,0)
def A_Decimal_aux(Numero2,Base2,Contador2,Respuesta2):
    if Numero2==0:
        return Respuesta2
    else:
        return A_Decimal_aux(Numero2//10,Base2,Contador2+1,Respuesta2+(Numero2%10)*(Base2**Contador2))
Test_A_Decimal()