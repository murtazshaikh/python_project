import math

cap=int(input("Enter the capacity of the crane (in KN)"))*1000
lift=int(input("Enter the height that to be lifted"))
speed=int(input("Enter the hoisting Speed"))
classs=int(input("Enter 1 for class1 and 2 for class2"))
pi=math.pi

def DOR():     #Design of Rope
    global DL
    DL=cap*1.2    #Design load
    print("Design load is ",DL,"KN")
    #calculating no. of f150alls
    global falls
    if cap<250000:
        falls=4
    elif cap<600000:
        falls=6
    elif cap<750000:
        falls=8
    elif cap<1000000:
        falls=12
    
    print("Number of falls is",falls)

    #calculating no. of bends
    global bends
    bends=falls-1
    print("Number of bends is",bends)

    #Max load per rope
    #pulley efficiency consider as 97%
    global Fmax
    Fmax=DL/(falls*0.97)
    print("Max load per rope ",Fmax,"N")
    global Fmaxk
    Fmaxk=Fmax/10
    print(Fmaxk,"kgf/cm^2")

    #Calculating Dmin/d 
    global DminD
    DminD={1:16,2:20,3:23,4:25,5:26.5,6:28,7:30,8:31,9:32,10:33,11:34,12:35,13:36,14:37,15:37.5,16:38}
    Dmin1=0
    for i in DminD:
        if i==bends:
            Dmin1=DminD[i]
    
            print("1st Dimn/d is",Dmin1)
    
    if classs==1:
        Dmin2=15
    else:
        Dmin2=17

    print("2st Dimn/d is",Dmin2)

    Dmin=0
    if Dmin1>Dmin2:
        Dmin=Dmin1
        print("Selecting the Bigger Dmin/d value to reduce bending stress",Dmin)
    else:
        Dmin=Dmin2
        print("Selecting the Bigger Dmin/d value to reduce bending stress",Dmin)

    #Wire selection
    print("Selecting std wire rope as 6X37 as it will have more strength & risk of failure will be less")

    #Breaking Strength
    
    TS=180000  #Nominal breaking strength  9.4


    if classs==1:
        n1=4.5
        n=n1
    else:
        n1=5
        n=n1
    print("n =",n)
    print(" As per IS3177 duty factor is not considered for rope design")
    global p
    p=(Fmaxk*TS)/((TS/n)-(1/Dmin)*36000)
    print("Breaking Strength is ",p,"kgf")

    PT=round(p/1000 )  # p in tons
    print(PT,"TONS")

    STD={10:6.8,12:8.9,14:11.3,16:13.9,18:20,20:23.5,22:26.9,24:31,25:35.6,29:44.7
         ,32:55.4,35:67.1,38:79.8,41:93.5,44:108.7,48:125,51:142.2,54:160.5,57:179.8,64:221.5,70:268.2}
    
    STD1=[10,12,14,16,18,20,22,24,25,29,32,35,38,41,44,48,51,54,57,64,70]

    STD2=[7,9,11,14,20,24,27,31,36,45,55,67,80,94,109,125,142,161,180,222,268]
    for i in STD2:
        if i<=PT:
            print(STD2[i+3])
            STD2[i+3]=STD1[i+3]
            print(STD1[i+3])
            break
    global d
    d=STD1[i+3]
    FOS=p/Fmaxk

    print("FOS is",FOS)

    #Life of rope
    st=Fmaxk/((pi/4)*d**2)

    print(st,"kgf/mm**2")



    CT={130000:1.112,160000:1.06,180000:1.02}

    for i in CT:
        if i==TS:
            c=CT[i]
            print("C =",c)

    c2=0.89 
    print("c2 is ",c2)     #0.63  to 1.16
    rpd=[5,8,10,14,18,19,24,28,35,44]
    c10=[83,85,89,93,97,1,104,109,116,124]
    for i in rpd:
        if i<d:
            print("for std dia ",rpd[i+3])
            rpd[i+3]=c10[i+3]
            c1=c10[i+3]/100
            print("c1 is",c1)
            break

    m=round(100*((Dmin-8)/(12.4*c1*c2*c)))
    print("m is ",m)
    

    ZM={26:30,41:50,56:70,83:110,95:130,107:150,118:170,129:190,140:210,150:230,162:255,174:280,187:310,
        200:340,212:370,227:410,242:450,260:500,277:550,294:600,310:650,317:7000}

    for i in ZM:
        if i>m:
            z=ZM[i]*1000
            print("Z is",z)
            break

    #light duty 8hr       exception

    a=3400
    z2=3
    bt=0.4

    #rope life in months

    N=(0.4*z)/(a*bt*z2)
    print("Life of rope is",N,"months")

    if n>12:
        print("Wire rope is SAFE")

#design of sheave and axle

def sheave_and_axle():
   
    WPD={4.8:(22,15,5,0.5,12.5,8,4,2.5,2,8,6),
         6.2:(22,15,5,0.5,12.5,8,4,2.5,2,8,6),
         8.7:(28,20,6,1,15,8,5,3,2.5,9,6),
         11:(40,30,7,1,25,10,8.5,4,3,12,8),
         13:(40,30,7,1,25,10,8.5,4,3,12,8),
         15:(40,30,7,1,25,10,8.5,4,3,12,8),
         19.5:(55,40,10,1.5,30,15,12,5,5,17,10),
         24:(65,50,10,1.5,37.5,18,14.5,5,20,15),
         28:(80,60,12,2,45,20,17,6,7,25,15),
         34.5:(90,70,15,2,55,22,20,7,8,28,20),
         39:(110,85,18,2.9,65,22,25,9,10,40,30)}
    
    for x,y in WPD.items():
        if x>d:
            d1=x
            a=y[0]
            b=y[1]
            c=y[2]
            e=y[3]
            h=y[4]
            l=y[5]
            r=y[6]
            r1=y[7]
            r2=y[8]
            r3=y[9]
            r4=y[10] 
            print("proportional diameter ",d1)
            print(a,b,c,e,h,l,r,r1,r2,r3,r4)      #proportions of sheave grooves
            break
    #design of sheave axle
    #distance between the side plate
    print(d1)
    
    Bmax = 2*Fmaxk*((90/2)+5+10+(20/2))
    print("Max bending moment is ",Bmax,"kgf-mm")
    
    print("selecting axle material C50 from PSG")
    C50=120
    print(C50,"n/mm^2")
    dxx=(Bmax/(120*(pi/32)))**(1/3)
    print("here dxx is",dxx,"mm")

    #Selection of bearing for axle

    print("Type - Spherical roller bearing")
    global fr
    fr=2*Fmaxk
    print("fr is",fr)

    print("Life in million revolution is given by")

    Lh=10000 #hrs      Assumed
    global D
    D=23*d1
    print("D is ",D)
    
    global i
    i=falls/2
    RS=i*(speed/60)
    V=RS
    print("Rope speed is",V)

    N=(V*60)/(pi*D/1000)
    print("RPM ",N)

    L10=Lmr=(N*60*Lh)/10**6
    print("life in million revolution",Lmr)
    
    print("Assuming 90% probability of survival")
     
    fa=0     #not considered
    tf=1
    s=1.2     #assumed
    x=1
    v=1       #IRR

    global P
    P=(x*fr*v)*s*tf
    print("p is ",p)
    
    k=10/3
    C=p*(L10)**(1/k)
    print("C is",C)

    bearingdict={3000:(25,"22205C"),
             4500:(30,"22206C"),
             5200:(35,"22207C"),
             6200:(40,"22208C"),
             6400:(45,"22209C"),
             6700:(50,"22210C"),
             8300:(55,"22211C"),
             10000:(60,"22212C"),
             11800:(65,"22213C"),
             12200:(70,"22214C"),
             12700:(75,"22215C"),
             15300:(80,"22216C"),
             18000:(85,"22217C"),
             20800:(90,"22218C"),
             24500:(95,"22219C"),
             27000:(100,"22220C"),
             34500:(110,"22222C"),
             40000:(120,"22224C"),
             46500:(130,"22226C"),
             53000:(140,"22228C"),
             64000:(150,"22230C"),
             73500:(160,"22232C"),
             83000:(170,"22234C"),
             88000:(180,"22236C"),
             95000:(190,"22238C"),
             108000:(200,"22240C"),
             129000:(220,"22244C"),
    }
    for x,y in bearingdict.items():
        if(x>C):
            print("Dynamic Load is ",x)
            bearing_d=y[0]
            bearing=y[1]
            print("So the bearing no is ",bearing,"and it's diameter is ",bearing_d,"mm")
            break

# Design of Hook 
def design_of_hook():
    print('Design of Hook')
    DL_Tn= DL/10000
    selecting_hook={0.5:25,
                    1:35,
                    2:50,
                    3.2:63,
                    5:79,
                    8:100,
                    10:110,
                    12:125,
                    16:140,
                    20:158,
                    25:175,
                    32:190,
    }
    for x,y in selecting_hook.items():
        if(x>DL_Tn):
            print("Safe load in tonnes is ",x)
            C=y
            print("Here C is",C)
            break
    # From psg 9.11
    A=2.75*C
    print(A)
    B=1.31*C
    print(B)
    D=1.44*C
    print(D)
    E=1.25*C
    print(E)
    F=C
    print(F)
    H=0.93*C
    print(H)
    J=0.75*C
    print(J)
    K=0.92*C
    print(K)
    L=0.7*C
    print(L)
    M=0.6*C
    print(M)
    N=1.2*C
    P=0.5*C
    print(P)
    R=0.5*C
    print(R)
    U=0.3*C
    print(U)
    Z=0.12*C
    print(round(Z,2))

    bo=2*Z
    print(round(bo,2))
    h=H
    print(h)
    bi=M
    print(round(bi,2))
    ri=C/2
    print(ri)
    ro=ri+h
    print(ro)

    #From psg 6.3
    #'Cross section at 2-2'
    A=0.5*(bo+bi)*h
    print("cross section area is ",A)
    print('Cross section at 2-2')
    rn=((0.5)*(bi+bo)*(h))/((((bi*ro)-(bo-ri))/(h))*(math.log(ro/ri))-(bi-bo))
    print("rn is ",float(rn))
    R=(ri+((h*(bi+2*bo))/(3*(bi+bo))))
    print("R is ",R)
    #'Cross section at 1-1'
    print('Cross section at 1-1')

    dc= (DL/((pi/4)*150))**(1/2)
    print("here dc is ",dc)
    do=dc/0.84
    print("do is ",do)

    #'Cross section at 3-3'
    print('Cross section at 3-3')
    σs=DL/A
    print(σs)
    Mss=0.5*78.04
    if σs<Mss:
        print('It is safe')
    else:
        print('Not safe')

    #Selecting bearing for hook
    print("selecting bearing as series of 513 ")
    bearingdict={25:(51305,5000,52),
                30:(51306,6350,60),
                35:(51307,8600,68),
                40:(51308,10900,78),
                45:(51309,13800,85),
                50:(51310,16300,95),
                55:(51311,19900,105),
                60:(51312,21500,110),
                65:(51313,23100,115),
                70:(51314,27700,125),
                75:(51315,31500,135),
                80:(51316,34000,140),
                85:(51317,40800,150),
                90:(51318,40800,155),
                100:(51320,49000,170),
                110:(51322,57600,187),
                120:(51324,74000,205),
                130:(51326,84300,220),
                140:(51328,98000,235),
                150:(51330,103000,245),
                160:(51332,122500,265),
    }
    for x,y in bearingdict.items():
        if(x>do):
            print("Thread is M",x)
            bearing=y[0]
            print("selected bearing from series 513 is ",bearing)
            Cs=y[1]
            CT=Cs/1000
            print("Load is ",CT,"TONs")
            global Dbe
            Dbe=y[2]
            print("Diameter",Dbe)
            break

    if DL_Tn>CT:
        print('Safe')
    else:
        print('Not safe')

def design_of_ropedrum():

    print("Diameter of pulley is ",D,"mm")
    
    wallthickness=((0.02*D)+0.8)
    print("wallthickness W:",wallthickness,"mm")

    Df=(D+6*d)
    print("flange diameter Df:",Df,"mm")

    Di=D-2*wallthickness
    print("Internal diameter Di:",Di,"mm")

    stdgroove={4.8:(3.5,7,2),
               6.2:(4,8,2),
               8.7:(5,11,3),
               11:(7,13,3),
               13:(8,15,4),
               15:(9,17,5),
               19.5:(11.5,22,5),
               24:(13.5,27,6),
               28:(15.5,31,8),
               34.5:(19,38,10),
               39:(21,42,12)
    }
    for x,y in stdgroove.items():
        if(x>d):
            ford=x
            print("for selected std diameter :",ford,"mm")
            r1=y[0]
            s1=y[1]
            c1=y[2]
            print("r1:",r1,"mm")
            print("s1:",s1,"mm")
            print("c1:",c1,"mm")
            break
    
    z1=round(((lift*i*1000)/(pi*D))+2)
    print("number of turns on drum z1:",z1)

    global l1
    global L
    l1=z1*s1
    L=((((2*lift*2*1000)/(pi*D))+12)*s1)+l1
    print("Length of drum is L:",L,"mm")

    print("finding stress in drum")
    print("selecting material for drum GCI25 from PSG 1.4")

    st=250  #n/mm^2
    FOS=3   #assume
    tau=125   #n/mm^2
    scr=500  #n/mm^2

    bearingStress = (8*fr*10*L*D)/((math.pow(D,4)-math.pow(Di,4))*pi)
    print("BearingStress: ", bearingStress)

    if(bearingStress<st):
        print("In brearing stress Drum is safe")
    else:
        print("In brearing stress Drum is not safe")

    crushingStress = fr*10/(wallthickness*s1)
    print("CrushingStress: ",crushingStress)

    if(crushingStress<scr):
        print("In crushing stress Drum is safe")
    else:
        print("In crushing stress Drum is not safe")
 
    global mt
    mt = fr*10*((Di+ford)/2)
    print("mt",mt)

    shearStress = (16*mt*D)/(3.14*(math.pow(D,4)-math.pow(Di,4)))
    print("Shear Stress: ",shearStress)

    if(shearStress<tau):
        print("In shear stress Drum is safe")
    else:
        print("In shear stress Drum is not safe")

    totalNormalStress = math.sqrt((bearingStress**2)+(crushingStress**2))
    print("Total Normal Stress: ",totalNormalStress)

    combinedEquivalentStress = math.sqrt((totalNormalStress**2)+(4*(shearStress**2)))
    print("Combined Equivalent Stress: ", combinedEquivalentStress)

    if(combinedEquivalentStress<st):
        print("In combined Equivalent stress Drum is safe")
    else:
        print("In combined Equivalent stress Drum is not safe")

def design_of_shaftdrum():

    maxBending = fr*10*((L- l1)/2)
    print("maximum bending : ", maxBending, "N.mm")

    print("maximum torque : ", mt)
    
    equivalentTorque = (maxBending**2 + mt**2)**(1/2)
    print("equivalent Torque : " ,equivalentTorque)

    print("Assuiming shaft material as C45")
    tau=50
    print("therefore tau is ",tau)


    d = ((equivalentTorque*16)/(math.pi * tau))**(1/3)
    print("initial diameter is ",d)

    print('selecting bearing Spherical Roller type')
    
    N = 10.37
    Lh= 10000
    K = 10/3

    Lmr=(N*60*Lh)/10**6
    print("life in million rev is ",Lmr,"mr")

    print("Assuming 90% probability of survival")
    L10=Lmr


    C = (L10**(1/K)) * P
    print("Dynamic capacity : ", C, "kgf")

    bearingdict={3000:(25,"22205C"),
             4500:(30,"22206C"),
             5200:(35,"22207C"),
             6200:(40,"22208C"),
             6400:(45,"22209C"),
             6700:(50,"22210C"),
             8300:(55,"22211C"),
             10000:(60,"22212C"),
             11800:(65,"22213C"),
             12200:(70,"22214C"),
             12700:(75,"22215C"),
             15300:(80,"22216C"),
             18000:(85,"22217C"),
             20800:(90,"22218C"),
             24500:(95,"22219C"),
             27000:(100,"22220C"),
             34500:(110,"22222C"),
             40000:(120,"22224C"),
             46500:(130,"22226C"),
             53000:(140,"22228C"),
             64000:(150,"22230C"),
             73500:(160,"22232C"),
             83000:(170,"22234C"),
             88000:(180,"22236C"),
             95000:(190,"22238C"),
             108000:(200,"22240C"),
             129000:(220,"22244C"),
    }
    for x,y in bearingdict.items():
        if(x>C):
            print("Dynamic Load is ",x)
            bearing_d=y[0]
            bearing=y[1]
            print("So the bearing no is ",bearing,"and it's diameter is ",bearing_d,"mm")
            break

def design_of_crosspiece():
    l = 200
    S1 = 10
    S = 20
    bendingStress = 120
    efficiency = 0.97
    v = 12/60


    L = l + (2*S1) + (2*(S/2))
    print("length:", L, "mm")

    B = 1.5*Dbe
    print("B: ", B, "mm")

    bendingMoment = ((DL/2)*((L/2) - (Dbe/4))) 
    print("MBmax: ", bendingMoment,"N/mm")

    Z = bendingMoment/bendingStress
    print("Z: ", Z)

    H = math.sqrt((Z/19.25))
    print("H: ",H, "mm")

    #Increasing 20% we get
    H = H*1.2
    print("After increasing 20%: ", H, "mm")

    #Turnnion pin diameter fail due to bearing failure
    dt = DL/(2*0.6*bendingStress*S)
    print("Turnnion pin diameter: ", dt,"mm")

    #now check for shear failure for turnnion pin
    shearStress = (DL*2)/(math.pi * math.pow(dt,2))
    print("shearStress: ",shearStress,"N/mm^2")

    permissibleShearStress = 0.5*bendingStress
    print("permissibleShearStress:", permissibleShearStress,"N/mm^2")

    if shearStress<permissibleShearStress:
        print("Shear stress is less than Permissible Shear Stress hence safe")
    else:
        print("Shear stress is less than Permissible Shear Stress hence unsafe")

    #Checking the turnnion pin in bending
    Mb = (DL/2)*(S1 + S/2)
    print("Mb",Mb, "N.mm")

    Z1 = (math.pi/32) * math.pow(dt,3)
    print("Z1",Z1)

    bendingStress1 = Mb/Z1
    print("bendingStress1:",bendingStress1,"N/mm^2")

    permissibleBendingStress =120

    if bendingStress1<permissibleBendingStress:
        print("Bending stress is less than Permissible Bending Stress hence safe")
    else:
        print("Bending stress is less than Permissible Bending Stress hence unsafe")

def motor_selection():

    P=((DL/1000)/0.97)*(speed/60)
    print("Power required :",P,"KW")


DOR()
sheave_and_axle()
design_of_hook()
design_of_ropedrum()
design_of_shaftdrum()
design_of_crosspiece()
motor_selection()
