import random
import time
from time import perf_counter
# from configparser import ConfigParser
from action import Action
from initinterception import sleep








class Soulmaster(Action):

    def __init__(self):
        super().__init__()
        self.offsety=5
        self.offsetx=15
        self.goleft=True
        self.goright=False
        self.randomlist = ['3', '4', 'n', 'r', 't', 'a', 'g', 'f1', 'f2',]
        self.x2exptimer0=0
        self.x2exptimer=0
        self.x2exp=True
        self.x2exp30mtimer0=0
        self.x2exp30mtimer=0
        self.x2exp30m=True
        self.frenzytimer0=0
        self.frenzytimer=0
        self.frenzy=True
        self.lucidtimer0=0
        self.lucidtimer=0
        self.lucid=True
        self.cosmicshowerplanttimer0=0
        self.cosmicshowerplanttimer=0
        self.cosmicshowerplant=True
        self.fountaintimer0=0
        self.fountaintimer=0
        self.fountain=True
        self.cctimer0=0
        self.cctimer=3600
        self.cc=False
        self.randommtimer0=0
        self.randommtimer=0
        self.runetimer0=0
        self.runetimer=0
        self.checkrune=True
        self.solverune=True
        self.now=0  
        self.rotation_list = ['default', 'limen1-7', 'limen1-4', 'pfrenzy', 'castlegate_2', 'LBtLDoor', 'x2exp', 'x2exp30m']
        self.rotation='default'
        self.rotation_mapping = {
            'default': self.clockwise,
            'limen1-7': self.limen1_7,
            'limen1-4': self.limen1_4,
            'castlegate_2': self.castlegate_2,
            'LBtLDoor' : self.LBtLDoor,
            'pfrenzy': self.pfrenzy,
            'px2exp': self.px2exp,
            'px2exp30m': self.px2exp30m,
        }

    def define(self):
        pass

    def setup(self,runesolver,g,rotation):
        if runesolver is not None:
            self.runesolver=runesolver
        if rotation is not None:
            self.rotation=rotation
        if g is not None:
            self.g=g
        
    async def perform_next_attack(self, x, y):
        # await self.limen1_7(x,y)
        # await self.clockwise(x,y)
        print(f'{self.rotation=}')
        await self.rotation_mapping[self.rotation](x,y)
        
    def get_rotation_list(self):
        return self.rotation_list
        
    def set_rotation(self, rotation):
        self.rotation = rotation
        print(f'{self.rotation=}')
    
    async def cccheck(self):
        while self.cc == True:
            if self.cc:
                await sleep(.4)
                await random.choice([self.cchannel])()
            self.cc=False
            print('changing channels')
            self.cctimer0=perf_counter()
            await sleep(.72)
    
    async def cchannel(self):
        time.sleep(5) #number of seconds to stop hitting. If your class has auto hitting skills adjust for longer
        await self.f8p() #press change channel hotkey
        await self.f8r() #release change channel hotkey
        await self.rightp()
        await self.rightr()
        await self.enterp()
        await self.enterr()
        await self.enterp()
        await self.enterr()
        time.sleep(1)

    # basic 4x direction movement (goleft, goright, gooup, godown)
    async def goleftattack(self):
        print(f'goleftattack')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def goleftattack2(self):
        print(f'goleftattack2')
        await self.leftp()
        await self.jumpp(222,388)
        await self.jumpr(3,11)    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def goleftattack3(self):
        print(f'goleftattack3')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()
        await self.leftr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()

    async def goleftattack4(self):
        print(f'goleftattack4')
        await self.leftp()
        await self.leftr()
        await self.jumpp(222,388)
        await self.jumpr(3,11)    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()

    async def gorightattack(self):
        print(f'gorightattack')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def gorightattack2(self):
        print(f'gorightattack2')
        await self.rightp()
        await self.jumpp(222,388)
        await self.jumpr(3,11)
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def gorightattack3(self):
        print(f'gorightattack3')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()
        await self.rightr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()

    async def gorightattack4(self):
        print(f'gorightattack4')
        await self.rightp()
        await self.rightr() 
        await self.jumpp(222,388)
        await self.jumpr(3,11)
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()   

    async def upjumpfacerightattack(self):
        print(f'upjumpfacerightattack')
        await sleep(.1)
        await self.upp()
        await self.jumpp(31,101)
        await self.jumpr(31,101)  
        await self.jumpp(31,101)
        await self.jumpr(31,101)
        await self.upr()
        await self.rightp()
        await self.rightr()
        await self.rightp()
        await self.rightr()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def upjumpfaceleftattack(self):
        print(f'upjumpfaceleftattack')
        await sleep(.1)
        await self.leftp()
        await self.upp()
        await self.jumpp(31,101)
        await self.jumpr(31,101)  
        await self.jumpp(31,101)
        await self.jumpr(31,101)
        await self.leftr()
        await self.upr()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def upjumpattack(self):
        print(f'upjumpattack')
        await sleep(.1)
        await self.upp()
        await self.jumpp(31,101)
        await self.jumpr(31,101)  
        await self.jumpp(31,101)
        await self.jumpr(31,101)
        await self.upr()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def goupattack(self): # adele upjump
        print(f'goupattack')
        await sleep(.1)
        await self.jumpp()
        await self.jumpr()
        await self.ropeconnectp(31,101)
        await self.ropeconnectr(31,101)
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.leftr()
        await sleep(.1)

    async def goupattack2(self): # adele upjump
        print(f'goupattack2')
        await sleep(.1)
        await self.jumpp()
        await self.jumpr()
        await self.ropeconnectp(31,101)
        await self.ropeconnectr(31,101)
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await self.leftr()
        await sleep(.1)

    async def goupattack3(self): # adele upjump
        print(f'goupattack3')
        await sleep(.1)
        await self.leftp()
        await self.jumpp()
        await self.jumpr()
        await self.leftr()
        await self.ropeconnectp(31,101)
        await self.ropeconnectr(31,101)
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def godownattack(self):
        print(f'godownattack')
        await self.downp()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.downr()

    async def godownattackleft(self):
        print(f'godownattackleft')
        await self.downp()    
        await self.jumpp()
        await self.jumpr()
        await self.downr()
        await self.leftp()
        await self.leftr()
        await self.attackp()
        await self.attackr()

    async def godownattackright(self):
        print(f'godownattackright')
        await self.downp()    
        await self.jumpp()
        await self.jumpr()
        await self.downr()
        await self.rightp()
        await self.rightr()
        await self.attackp()
        await self.attackr()

    # variation of 4 basic movement to make sequence more randomise.
    async def goleftattackk(self):
        print(f'goleftattackk')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.leftr()
        
    async def goattackleft(self):
        print(f'goattackleft')
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await sleep(.5)
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.leftr()

    async def goattackkleft(self):
        print(f'goattackleft')
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.5)
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.leftr()
    
    async def gorightattackk(self):
        print(f'gorightattackk')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.rightr()
    
    async def goattackright(self):
        print(f'goattackright')
        await self.rightp()
        await self.attackp()
        await self.attackr()
        await sleep(.5)
        await self.jumpp()
        await self.jumpr()  
        await self.jumpp()
        await self.jumpr()
        await self.rightr()

    async def goattackkright(self):
        print(f'goattackkright')
        await self.rightp()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.5)
        await self.jumpp()
        await self.jumpr()  
        await self.jumpp()
        await self.jumpr()
        await self.rightr()
        
    async def stormwing(self,x,y,goleft,goright):
        if goright:
            if y < self.top:
                await self.godownattack()
                time.sleep(.3)
            elif y > self.top:
                await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright])()
            if x > self.right:
                await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft])()
                time.sleep(.1)
                goright=False
                goleft=True
        elif goleft:
            if y < self.top:
                await self.godownattack()
                time.sleep(.3)
            elif y > self.top:
                await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft])()
                time.sleep(.1)
            if x < self.left: # only if x < left
                await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright])()
                time.sleep(.1)
                goright=True
                goleft=False
        return goleft,goright

    # soul master actions patch for limen 1-7
    
    async def rightupjump(self):
        print(f'rightupjump')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()
        await self.rightr(3,11)
        await self.upp()
        await self.jumpp()
        await self.jumpr()
        await self.upr()
        time.sleep(.1)

    async def leftupjump(self):
        print(f'leftupjump')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()
        await self.leftr(3,11)
        await self.upp()
        await self.jumpp()
        await self.jumpr()
        await self.upr()
        time.sleep(.1)

    async def rightjumpattack(self):
        print(f'rightjumpattack')
        await self.rightp()
        await self.jumpp(131,211)
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def jumpropeconnectpr(self,x=111,y=222,x2=111,y2=222):
        await self.ropeconnectp(x,y)
        await self.ropeconnectr(x2,y2)

    async def ropeconnectpr(self,x=111,y=222,x2=111,y2=222):
        await self.ropeconnectp(x,y)
        await self.ropeconnectr(x2,y2)

    async def lucidpr(self):
        r = random.randint(2,4)
        for i in range(r):
            await self.rp(101,177)
            await self.rr()

    async def cosmicshower(self):
        r = random.randint(2,4)
        for i in range(r):
            await self.ep(101,177)
            await self.er()

    async def faceleftfountain(self):
        await self.leftp()
        await self.leftr()
        await self.fountainp()
        await self.fountainr()
        time.sleep(.1)

    async def facerightfountain(self):
        await self.rightp()
        await self.rightr()
        await self.fountainp()
        await self.fountainr()
        time.sleep(.1)

    async def walkleft(self,distance=1):
        print(f'walkleft for {distance=}')
        x=int(distance*88)
        y=int(distance*144)
        await self.leftp(x,y)
        await self.leftr()
        # if distance <= 2:
        #     await self.leftp(distance*388,distance*444)
        #     await self.leftr()
        # elif distance <= 4:
        #     await self.leftp(distance*388,distance*444)
        #     await self.leftr()
        # elif distance <= 6:
        #     await self.leftp(distance*388,distance*444)
        #     await self.leftr()
        # elif distance <= 8:
        #     await self.leftp(distance*388,distance*444)
        #     await self.leftr()
        # else:
        #     await self.leftp(distance*388,distance*444) # calculate sleep time according to distance. 
        #     await self.leftr()
            
    async def walkright(self,distance=1):
        print(f'walkright for {distance=}')
        x=int(distance*88)
        y=int(distance*144)
        await self.rightp(x,y)
        await self.rightr()
        # if distance <= 2:
        #     await self.rightp(x,y)
        #     await self.rightr()
        # elif distance <= 4:
        #     await self.rightp(distance*388,distance*444)
        #     await self.rightr()
        # elif distance <= 6:
        #     await self.rightp(distance*388,distance*444)
        #     await self.rightr()
        # elif distance <= 8:
        #     await self.rightp(distance*388,distance*444)
        #     await self.rightr()
        # else:
        #     await self.rightp(distance*388,distance*444) # calculate sleep time according to distance. 
        #     await self.rightr()



    async def pfrenzy(self,x,y):
        if self.frenzy:
            time.sleep(.4)
            print(f'frenzy pressed. ')
            await self.f12p()
            await self.f12r()
            time.sleep(.1)
        else:
            time.sleep(1)
    
    async def px2exp(self,x,y):
        if self.x2exp:
            time.sleep(.9)
            print(f'x2 exp 15m pressed. ')
            await self.hp()
            await self.hr()
            time.sleep(.1)
        else:
            time.sleep(1)
    
    async def px2exp30m(self,x,y):
        if self.x2exp30m:
            time.sleep(.9)
            print(f'x2 exp 30m pressed. ')
            await self.jp()
            await self.jr()
            time.sleep(.1)
        else:
            time.sleep(1)

        self.now = perf_counter()
        # self.randommtimer = self.now - self.randommtimer0
        # if self.randommtimer > 15:
        #     self.randommtimer0 = self.now
        #     # p = random.randint(0, len(self.randomlist)-1)
        #     code = random.choice(self.randomlist)
        #     if code is not None:
        #         print(f'randomiser {code=}')
        #         await self.send2(code)
        #         await self.send3(code)
        # if self.replaceropeconnect==True:
        #     if runonce:
        #         replaceropeconnecttimer0=self.now
        #         runonce=False
        #     replaceropeconnecttimer = self.now - replaceropeconnecttimer0
        #     if replaceropeconnecttimer > 90:
        #         self.replaceropeconnect=False
        #         runonce=True
        # # self.cosmicshowerplanttimer = self.now - self.cosmicshowerplanttimer0
        # # if self.cosmicshowerplanttimer > 59:
        # #     self.cosmicshowerplant = True
        # # self.fountaintimer = self.now - self.fountaintimer0
        # # if self.fountaintimer > 59:
        # #     self.fountain = True
        self.x2exptimer = self.now - self.x2exptimer0
        if self.x2exptimer > 960:
            self.x2exp=True
        self.x2exp30mtimer = self.now - self.x2exp30mtimer0
        if self.x2exp30mtimer > 1860:
            self.x2exp30m=True

        self.frenzytimer = self.now - self.frenzytimer0
        if self.frenzytimer > 120:
            self.frenzy=True
        # self.runetimer = self.now - self.runetimer0
        # # if runetimer > 600: # change to 600 when haste
        # if self.runetimer > 900: # change to 600 when haste
        #     self.checkrune = True
        #     # self.checkrune = False
        # if self.checkrune:
        #     self.solverune = self.runesolver.runechecker(self.g)
        # print(f'{x=} {y=} rt={self.runetimer} sr={self.solverune} ft={self.fountaintimer} gl={self.goleft} gr={self.goright}')
        print(f'{x=} {y=} {self.frenzytimer=}')
        print(f'{x=} {y=} {self.x2exptimer=}')
        print(f'{x=} {y=} {self.x2exp30mtimer=}')
        # if self.solverune:
        #     await self.runesolver.gotorune(self.g)

    async def LBtLDoor(self,x,y):
        if y <= 13.5:
            await random.choice([self.godownattack, self.godownattackleft, self.godownattackright])()
        elif y > 13.5 and y <= 27.5:
            if x >= 66.5 and x <= 94.5:
                await random.choice([self.godownattack, self.godownattackleft, self.godownattackright])()
            elif x > 94.5 and x < 97.5: #ladder
                await random.choice([self.goleftattack, self.goleftattack2, self.goleftattack3, self.goleftattack4])()
            elif x >= 97.5 and x <= 131.5:
                if self.fountain:
                    if x >= 97.5 and x < 111.5:
                        await random.choice([self.walkright])(111.5-x)
                    elif x >= 111.5 and x <= 117.5:
                        await random.choice([self.facerightfountain])()
                        self.fountain=False
                        self.fountaintimer0=perf_counter()
                    elif x > 117.5 and x <= 131.5:
                        await random.choice([self.walkleft])(x-111.5)
                else:
                    await random.choice([self.goleftattack, self.goleftattack2, self.goleftattack3, self.goleftattack4])()
            elif x > 131.5 and x <= 205.5:
                await random.choice([self.goleftattack, self.goleftattack2, self.goleftattack3, self.goleftattack4])()
        elif y > 27.5 and y <= 40.5:
            if x >= 155.5:
                await random.choice([self.goupattack, self.goupattack2, self.goupattack3])()
            elif x > 94.5 and x < 155.5:
                await random.choice([self.goleftattack, self.goleftattack2, self.goleftattack3, self.goleftattack4])()
            elif x >= 66.5 and x <= 94.5:
                if self.cosmicshowerplant:
                    if x >= 66.5 and x < 77.5:
                        await random.choice([self.walkright])(77.5-x)
                    elif x >= 77.5 and x <= 83.5:
                        await random.choice([self.cosmicshower])()
                        self.cosmicshowerplant=False
                        self.cosmicshowerplanttimer0=perf_counter()
                    elif x > 83.5 and x <= 94.5:
                        await random.choice([self.walkleft])(x-83.5)            
                else:
                    await random.choice([self.godownattack, self.godownattackleft, self.godownattackright])()
        elif y > 40.5 and y <= 54.5:
            if x >= 59.5 and x < 155.5:
                await random.choice([self.gorightattack, self.gorightattack2, self.gorightattack3, self.gorightattack4])()
            elif x >= 155.5 and x <= 189.5:
                await random.choice([self.goupattack, self.goupattack2, self.goupattack3])()
            elif x > 189.5:
                await random.choice([self.goleftattack, self.goleftattack2, self.goleftattack3, self.goleftattack4])()
        else:
            print(f'this coordinates not yet plan .. ')

        self.now = perf_counter()

        self.randommtimer = self.now - self.randommtimer0
        if self.randommtimer > 15:
            self.randommtimer0 = self.now
            code = random.choice(self.randomlist)
            if code is not None:
                print(f'randomiser {code=}')
                time.sleep(.4)
                await self.send2(code)
                await self.send3(code)
                time.sleep(.1)
        
        self.x2exptimer = self.now - self.x2exptimer0
        if self.x2exptimer > 960:
            time.sleep(.9)
            print(f'x2 exp pressed. ')
            await self.hp()
            await self.hr()
            time.sleep(.1)
            self.x2exptimer0=self.now

        self.x2exp30mtimer = self.now - self.x2exp30mtimer0
        if self.x2exp30mtimer > 1860:
            time.sleep(.9)
            print(f'x2 exp 30m pressed. ')
            await self.jp()
            await self.jr()
            time.sleep(.1)
            self.x2exp30mtimer0=self.now

        self.frenzytimer = self.now - self.frenzytimer0
        if self.frenzytimer > 120:
            time.sleep(.4)
            print(f'frenzy pressed. ')
            await self.f12p()
            await self.f12r()
            time.sleep(.1)
            self.frenzytimer0=self.now

        self.cosmicshowerplanttimer = self.now - self.cosmicshowerplanttimer0
        if self.cosmicshowerplanttimer > 59:
            self.cosmicshowerplant = True

        self.fountaintimer = self.now - self.fountaintimer0
        if self.fountaintimer > 59:
            self.fountain = True

        self.runetimer = self.now - self.runetimer0
        if self.runetimer > 900:
            self.checkrune = True
        if self.checkrune:
            self.solverune = self.runesolver.runechecker(self.g)

        print(f'{x=} {y=} rt={self.runetimer} sr={self.solverune} ft={self.fountaintimer} gl={self.goleft} gr={self.goright}')

        if self.solverune:
            await self.runesolver.gotorune(self.g)
        else:
            pass


    async def limen1_7(self,x,y):    
        if y > 34.5 and y <= 47.5:
            if x > 84.5 and x <= 120.5:
                if self.cosmicshowerplant:
                    if x >= 102.5 and x <= 104.5:
                        await random.choice([self.jumpropeconnectpr])(x2=999,y2=1222)
                        time.sleep(.1)
                        await random.choice([self.cosmicshower])()
                    elif x < 102.5:
                        await random.choice([self.rightupjump])()
                        return
                    elif x > 104.5:
                        await random.choice([self.leftupjump])()
                        return
                    else:
                        print(f'if ever character stucked at this point, assign an action. {x=} {y=}')
                    self.cosmicshowerplant=False
                    self.cosmicshowerplanttimer0=perf_counter()
                    return
                else:
                    pass
            if self.goleft:
                if x > 57.5:
                    await random.choice([self.goleftattack, self.goleftattack2, self.goleftattack3, self.goleftattack4])()
                else:
                    if self.fountain:
                        await random.choice([self.goupattack, self.goupattack2, self.goupattack3])()
                    self.goright=True
                    self.goleft=False
            elif self.goright:
                if x < 140.5:
                    await random.choice([self.gorightattack, self.gorightattack2, self.gorightattack3, self.gorightattack4])()
                else:
                    await random.choice([self.goleftattack, self.goleftattack2, self.goleftattack3, self.goleftattack4])()
                    self.goright=False
                    self.goleft=True
        else:
            if x >= 28.5 and x <= 57.5:
                if y > 18.5 and y <= 29.5:
                    if self.fountain:
                        if x >= 37.5 and x <= 38.5:
                            await random.choice([self.facerightfountain])()
                        elif x >= 53.5 and x <= 57.5:
                            await random.choice([self.faceleftfountain])()
                        elif x > 38.5 and x <= 45.5:
                            await random.choice([self.walkleft])(x-38.5)
                            time.sleep(.1)
                            await random.choice([self.facerightfountain])()
                        elif x > 45.5 and x < 53.5:
                            await random.choice([self.walkright])(53.5-x)
                            time.sleep(.1)
                            await random.choice([self.faceleftfountain])()
                        elif x < 37.5:
                            await random.choice([self.walkright])(37.5-x)
                            time.sleep(.1)
                            await random.choice([self.facerightfountain])()
                        else:
                            print(f'if ever character stucked at this point, assign an action. {x=} {y=}')
                        self.fountain=False
                        self.fountaintimer0=perf_counter()
                    else:
                        await random.choice([self.gorightattack, self.gorightattack2, self.gorightattack3, self.gorightattack4])()
                elif y <= 18.5:
                    await random.choice([self.gorightattack, self.gorightattack2, self.gorightattack3, self.gorightattack4])()
                else:
                    print(f'if ever character stucked at this point, assign an action. {x=} {y=}')
            elif x > 57.5 and x <= 84.5:
                await random.choice([self.gorightattack, self.gorightattack2, self.gorightattack3, self.gorightattack4])()
            elif x > 84.5 and x <= 120.5:
                if y <= 23.5:
                    if self.cosmicshowerplant:
                        if x >= 102.5 and x <= 104.5:
                            await random.choice([self.cosmicshower])()
                        elif x < 102.5:
                            await random.choice([self.walkright])(102.5-x)
                            time.sleep(.1)
                            await random.choice([self.cosmicshower])()
                        elif x > 104.5:
                            await random.choice([self.walkleft])(x-104.5)
                            time.sleep(.1)
                            await random.choice([self.cosmicshower])()
                        else:
                            print(f'if ever character stucked at this point, assign an action. {x=} {y=}')
                        self.cosmicshowerplant=False
                        self.cosmicshowerplanttimer0=perf_counter()
                    else:
                        await random.choice([self.godownattack])()
                else:
                    await random.choice([self.gorightattack, self.gorightattack2, self.gorightattack3, self.gorightattack4])()
            elif x > 120.5 and x <= 165.5:
                if y <= 28.5:
                    if x >= 138.5 and x <= 142.5:
                        await random.choice([self.goleftattack, self.goleftattack2, self.goleftattack3, self.goleftattack4])()
                    else:
                        await random.choice([self.godownattack])()
                else:
                    print(f'if ever character stucked at this point, assign an action. {x=} {y=}')

        self.now = perf_counter()
        self.randommtimer = self.now - self.randommtimer0
        if self.randommtimer > 15:
            self.randommtimer0 = self.now
            code = random.choice(self.randomlist)
            if code is not None:
                print(f'randomiser {code=}')
                time.sleep(.4)
                await self.send2(code)
                await self.send3(code)
                time.sleep(.1)
        self.frenzytimer = self.now - self.frenzytimer0
        if self.frenzytimer > 120:
            time.sleep(.4)
            print(f'frenzy pressed. ')
            await self.f12p()
            await self.f12r()
            time.sleep(.1)
            self.frenzytimer0=self.now
        self.x2exptimer = self.now - self.x2exptimer0
        if self.x2exptimer > 960:
            time.sleep(.9)
            print(f'x2 exp pressed. ')
            await self.hp()
            await self.hr()
            time.sleep(.1)
            self.x2exptimer0=self.now
            
        self.x2exp30mtimer = self.now - self.x2exp30mtimer0
        if self.x2exp30mtimer > 1860:
            time.sleep(.9)
            print(f'x2 exp 30m pressed. ')
            await self.jp()
            await self.jr()
            time.sleep(.1)
            self.x2exp30mtimer0=self.now

        self.cosmicshowerplanttimer = self.now - self.cosmicshowerplanttimer0
        if self.cosmicshowerplanttimer > 59:
            self.cosmicshowerplant = True
        self.fountaintimer = self.now - self.fountaintimer0
        if self.fountaintimer > 59:
            self.fountain = True
        self.runetimer = self.now - self.runetimer0
        if self.runetimer > 900:
            self.checkrune = True
        if self.checkrune:
            self.solverune = self.runesolver.runechecker(self.g)
        print(f'{x=} {y=} rt={self.runetimer} sr={self.solverune} ft={self.fountaintimer} gl={self.goleft} gr={self.goright}')

        if self.solverune:
            await self.runesolver.gotorune(self.g)
        else:
            pass

    async def limen1_4(self,x,y):    
        if y >= 51.5 and y <= 67.5:
            if x >= 138.5 and x <= 172.5:
                if self.cosmicshowerplant:
                    if x >= 153.5 and x <= 157.5:
                        await random.choice([self.jumpropeconnectpr])(x2=999,y2=1222)
                        time.sleep(.1)
                        await random.choice([self.cosmicshower])()
                    elif x < 153.5:
                        await random.choice([self.rightupjump])()
                        return
                    elif x > 157.5:
                        await random.choice([self.leftupjump])()
                        return
                    else: # should be no else case here
                        print(f'if ever character stucked at this point, assign an action. {x=} {y=}')
                    self.cosmicshowerplant=False
                    self.cosmicshowerplanttimer0=perf_counter()
                    return # done, go next loop. 
                else:
                    pass # do nothing, proceed to check goleft goright
            if self.goleft:
                if x > 57.5:
                    await random.choice([self.goleftattack, self.goleftattack2, self.goleftattack3, self.goleftattack4])()
                    self.goright=True
                    self.goleft=False
            elif self.goright:
                if x < 130.5:
                    await random.choice([self.gorightattack, self.gorightattack2, self.gorightattack3, self.gorightattack4])()
                else:
                    await random.choice([self.goleftattack, self.goleftattack2, self.goleftattack3, self.goleftattack4])()
                    self.goright=False
                    self.goleft=True
        elif x >= 138.5 and x <= 172.5:
            if y >= 34.5 and y <= 51.5:
                if self.cosmicshowerplant:
                    if x >= 153.5 and x <= 157.5:
                        await random.choice([self.cosmicshower])()
                    elif x < 153.5:
                        await random.choice([self.walkright])(153.5-x)
                        time.sleep(.1)
                        await random.choice([self.cosmicshower])()
                    elif x > 157.5:
                        await random.choice([self.walkleft])(x-157.5)
                        time.sleep(.1)
                        await random.choice([self.cosmicshower])()
                    else: # should be no else case here
                        print(f'if ever character stucked at this point, assign an action. {x=} {y=}')
                    self.cosmicshowerplant=False
                    self.cosmicshowerplanttimer0=perf_counter()
                else:
                    await random.choice([self.godownattack])()
        elif y < 57.5:
            await random.choice([self.godownattack])()
        else: # should be no else case here
            print(f'if ever character stucked at this point, assign an action. {x=} {y=}')
        self.now = perf_counter()
        self.randommtimer = self.now - self.randommtimer0
        if self.randommtimer > 15:
            self.randommtimer0 = self.now
            # p = random.randint(0, len(self.randomlist)-1)
            code = random.choice(self.randomlist)
            if code is not None:
                print(f'randomiser {code=}')
                time.sleep(.4)
                await self.send2(code)
                await self.send3(code)
                time.sleep(.1)
        self.frenzytimer = self.now - self.frenzytimer0
        if self.frenzytimer > 120:
            time.sleep(.4)
            print(f'frenzy pressed. ')
            await self.f12p()
            await self.f12r()
            time.sleep(.1)
            self.frenzytimer0=self.now
        self.x2exptimer = self.now - self.x2exptimer0
        if self.x2exptimer > 960:
            time.sleep(.9)
            print(f'x2 exp pressed. ')
            await self.hp()
            await self.hr()
            time.sleep(.1)
            self.x2exptimer0=self.now
        self.x2exp30mtimer = self.now - self.x2exp30mtimer0
        if self.x2exp30mtimer > 1860:
            time.sleep(.9)
            print(f'x2 exp 30m pressed. ')
            await self.jp()
            await self.jr()
            time.sleep(.1)
            self.x2exp30mtimer0=self.now
        self.cosmicshowerplanttimer = self.now - self.cosmicshowerplanttimer0
        if self.cosmicshowerplanttimer > 59:
            self.cosmicshowerplant = True
        self.fountaintimer = self.now - self.fountaintimer0
        if self.fountaintimer > 59:
            self.fountain = True
        # if self.replaceropeconnect==True:
        #     if runonce:
        #         replaceropeconnecttimer0=self.now
        #         runonce=False
        #     replaceropeconnecttimer = self.now - replaceropeconnecttimer0
        #     if replaceropeconnecttimer > 90:
        #         self.replaceropeconnect=False
        #         runonce=True
        # polocheckertimer = self.now - self.polocheckertimer0
        # if polocheckertimer > 90:
        #     self.pausepolochecker=False
        self.runetimer = self.now - self.runetimer0
        # if runetimer > 600: # change to 600 when haste
        if self.runetimer > 900: # change to 600 when haste
            self.checkrune = True
            # self.checkrune = False
        if self.checkrune:
            self.solverune = self.runesolver.runechecker(self.g)
        # print(f'{x=} {y=} {statuetimer=} {fountaintimer=}, {runetimer=}, {cctimer=}')
        print(f'{x=} {y=} rt={self.runetimer} sr={self.solverune} ft={self.fountaintimer} gl={self.goleft} gr={self.goright}')
        # print(f'{x=} {y=} {self.runetimer} {self.solverune} | {self.left}, {self.top}, {self.right}, {self.btm} | {self.left1}, {self.top1}, {self.right1}, {self.btm1}')
        # print(f'{x=}, {y=} | {left=}, {top=}, {right=}, {btm=} | {left1=}, {top1=}, {right1=}, {btm1=}')

        if self.solverune:
            await self.runesolver.gotorune(self.g)
        # elif self.polochecker:
        #     if self.whitedotoccur:
        #         if not await self.polocheckerfunc(self.gotoportal):
        #             self.replaceropeconnect=True
        #         self.whitedotoccur=False
        #     else:
        #         await self.polocheckerfunc(self.gotoportal)
        else:
            pass



    async def castlegate_2(self,x,y):
        #line 1
        if y <= 21.5:
            await random.choice([self.godownattack])()
        #line 2
        elif y > 21.5 and y <= 34.5:
            #40.5 la ben trai cung line 2
            if x >= 40.5 and x < 80.5:
                await random.choice([self.gorightattack, self.gorightattack2])()
            #Erda 80.5 +- 5
            elif x >= 80.5 and x <= 90.5:
                if self.fountain:
                    if x >= 80.5 and x < 82.5:
                        await random.choice([self.walkright])(85.5-x)
                    elif x >= 82.5 and x <= 88.5:
                        await random.choice([self.facerightfountain])()
                        self.fountain=False
                        self.fountaintimer0=perf_counter()
                    elif x > 88.5 and x <= 90.5:
                        await random.choice([self.walkleft])(x-85.5)
                else:
                    await random.choice([self.gorightattack, self.gorightattack2])()
            elif x > 71.5 and x < 116.5:
                await random.choice([self.gorightattack, self.gorightattack2])()
            #Cosmis 121.5 +-5
            elif x >= 116.5 and x <= 126.5:
                if self.cosmicshowerplant:
                    if x >= 116.5 and x < 118.5:
                        await random.choice([self.walkright])(121.5-x)
                    elif x >= 118.5 and x <= 124.5:
                        await random.choice([self.cosmicshower])()
                        self.cosmicshowerplant=False
                        self.cosmicshowerplanttimer0=perf_counter()
                    elif x > 124.5 and x <= 126.5:
                        await random.choice([self.walkleft])(x-121.5)
                else:
                    await random.choice([self.gorightattack, self.gorightattack2])()
            elif x > 126.5 and x < 142.5:
                await random.choice([self.gorightattack, self.gorightattack2])()
            elif x >= 142.5 and x <= 162.5:
                await random.choice([self.godownattackleft])()
        #line 3
        elif y > 34.5 and y <= 48.5:
            if x >= 40.5 and x < 80.5:
                await random.choice([self.goupattack, self.goupattack2, self.goupattack3])()
            #lucidsoul 147.5 +-5
            elif x >= 142.5 and x <= 152.5:
                if self.lucid:
                    if x >= 142.5 and x < 144.5:
                        await random.choice([self.walkright])(147.5-x)
                    elif x >= 144.5 and x <= 150.5:
                        await random.choice([self.lucidpr])()
                        self.lucid=False
                        self.lucidtimer0=perf_counter()
                    elif x > 150.5 and x <= 152.5:
                        await random.choice([self.walkleft])(x-147.5)
                else:
                    await random.choice([self.godownattack])()
            elif x > 152.5 and x <= 165.5:
                await random.choice([self.godownattack])()
            else:
                await random.choice([self.goleftattack, self.goleftattack2])()
        #line 4
        elif y > 48.5 and y <= 61.5:
            if x < 40.5:
                await random.choice([self.gorightattack, self.gorightattack2])()
            elif x >= 40.5 and x <69.5:
                await random.choice([self.goupattack, self.goupattack2, self.goupattack3])()
            elif x > 69.5 and x <= 174.5:
                await random.choice([self.goleftattack, self.goleftattack2])()            
        else:
            print(f'this coordinates not yet plan .. ')

        await self.post_perform_action(x,y)


        self.now = perf_counter()
        self.randommtimer = self.now - self.randommtimer0
        if self.randommtimer > 15:
            self.randommtimer0 = self.now
            # p = random.randint(0, len(self.randomlist)-1)
            code = random.choice(self.randomlist)
            if code is not None:
                print(f'randomiser {code=}')
                time.sleep(.4)
                await self.send2(code)
                await self.send3(code)
                time.sleep(.1)
        self.frenzytimer = self.now - self.frenzytimer0
        if self.frenzytimer > 120:
            time.sleep(.4)
            print(f'frenzy pressed. ')
            await self.f12p()
            await self.f12r()
            time.sleep(.1)
            self.frenzytimer0=self.now
        self.x2exp30mtimer = self.now - self.x2exp30mtimer0
        if self.x2exp30mtimer > 1860:
            time.sleep(.9)
            print(f'x2 exp 30m pressed. ')
            await self.jp()
            await self.jr()
            time.sleep(.1)
            self.x2exp30mtimer0=self.now
        self.cosmicshowerplanttimer = self.now - self.cosmicshowerplanttimer0
        if self.cosmicshowerplanttimer > 59:
            self.cosmicshowerplant = True
        self.fountaintimer = self.now - self.fountaintimer0
        if self.fountaintimer > 59:
            self.fountain = True
        # if self.replaceropeconnect==True:
        #     if runonce:
        #         replaceropeconnecttimer0=self.now
        #         runonce=False
        #     replaceropeconnecttimer = self.now - replaceropeconnecttimer0
        #     if replaceropeconnecttimer > 90:
        #         self.replaceropeconnect=False
        #         runonce=True
        # polocheckertimer = self.now - self.polocheckertimer0
        # if polocheckertimer > 90:
        #     self.pausepolochecker=False
        self.runetimer = self.now - self.runetimer0
        # if runetimer > 600: # change to 600 when haste
        if self.runetimer > 900: # change to 600 when haste
            self.checkrune = True
            # self.checkrune = False
        if self.checkrune:
            self.solverune = self.runesolver.runechecker(self.g)
        # print(f'{x=} {y=} {statuetimer=} {fountaintimer=}, {runetimer=}, {cctimer=}')
        print(f'{x=} {y=} rt={self.runetimer} sr={self.solverune} ft={self.fountaintimer} gl={self.goleft} gr={self.goright}')
        # print(f'{x=} {y=} {self.runetimer} {self.solverune} | {self.left}, {self.top}, {self.right}, {self.btm} | {self.left1}, {self.top1}, {self.right1}, {self.btm1}')
        # print(f'{x=}, {y=} | {left=}, {top=}, {right=}, {btm=} | {left1=}, {top1=}, {right1=}, {btm1=}')

        if self.solverune:
            await self.runesolver.gotorune(self.g)
        # elif self.polochecker:
        #     if self.whitedotoccur:
        #         if not await self.polocheckerfunc(self.gotoportal):
        #             self.replaceropeconnect=True
        #         self.whitedotoccur=False
        #     else:
        #         await self.polocheckerfunc(self.gotoportal)
        else:
            pass





    async def clockwise(self,x,y):
        await random.choice([self.cccheck])()
        #changechannel timer
        self.cctimer = self.now - self.cctimer0
        if self.cctimer > 3599:
            self.cc = True
        if y > self.top and (y > self.btm-self.offsety and y <= self.btm+self.offsety):
            if x > self.left+self.offsetx:
                if x < self.left+self.offsetx+5:
                    await random.choice([self.leftwalk])()
                else:
                    await random.choice([self.goleftattack, self.goleftattackk])()
            elif x < self.left-self.offsetx:
                if x > self.left-self.offsetx-5:
                    await random.choice([self.rightwalk])()
                else:
                    await random.choice([self.gorightattack, self.gorightattackk])()
            elif x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                if self.replaceropeconnect:
                    await random.choice([self.goupattack_v3])()
                else:
                    await random.choice([self.goupattack])()
        elif y <= self.top+self.offsety and y > self.top-self.offsety:
            if x < self.right-self.offsetx:
                await random.choice([self.gorightattack, self.gorightattackk])()
            elif x > self.right+self.offsetx:
                await random.choice([self.goleftattack, self.goleftattackk])()
            elif x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                await random.choice([self.godownattack])()
        elif y > self.top and not (y > self.btm-self.offsety and y <= self.btm+self.offsety):
            if x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                if self.replaceropeconnect:
                    await random.choice([self.goupattack_v3])()
                else:
                    await random.choice([self.goupattack])()
            elif x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                await random.choice([self.godownattack])()
            else:
                if x < ((self.right-self.left)/2):
                    if self.replaceropeconnect:
                        await random.choice([self.goupattack_v3])()
                    else:
                        await random.choice([self.goupattack])()
                elif x >= ((self.right-self.left)/2):
                    await random.choice([self.godownattack])()
        else:
            await random.choice([self.godownattack])()

        await self.post_perform_action(x,y)













        
    async def post_perform_action(self,x,y):
        self.now = perf_counter()
        self.randommtimer = self.now - self.randommtimer0
        if self.randommtimer > 15:
            self.randommtimer0 = self.now
            # p = random.randint(0, len(self.randomlist)-1)
            code = random.choice(self.randomlist)
            if code is not None:
                print(f'randomiser {code=}')
                time.sleep(.4)
                await self.send2(code)
                await self.send3(code)
                time.sleep(.1)
        self.frenzytimer = self.now - self.frenzytimer0
        if self.frenzytimer > 120:
            time.sleep(.4)
            print(f'frenzy pressed. ')
            await self.f12p()
            await self.f12r()
            time.sleep(.1)
            self.frenzytimer0=self.now
        self.lucidtimer = self.now - self.lucidtimer0
        if self.lucidtimer > 59:
            self.lucidplant = True
        self.cosmicshowerplanttimer = self.now - self.cosmicshowerplanttimer0
        if self.cosmicshowerplanttimer > 59:
            self.cosmicshowerplant = True
        self.fountaintimer = self.now - self.fountaintimer0
        if self.fountaintimer > 59:
            self.fountain = True
        # if self.replaceropeconnect==True:
        #     if runonce:
        #         replaceropeconnecttimer0=self.now
        #         runonce=False
        #     replaceropeconnecttimer = self.now - replaceropeconnecttimer0
        #     if replaceropeconnecttimer > 90:
        #         self.replaceropeconnect=False
        #         runonce=True
        # polocheckertimer = self.now - self.polocheckertimer0
        # if polocheckertimer > 90:
        #     self.pausepolochecker=False
        self.runetimer = self.now - self.runetimer0
        # if runetimer > 600: # change to 600 when haste
        if self.runetimer > 900: # change to 600 when haste
            self.checkrune = True
            # self.checkrune = False
        if self.checkrune:
            self.solverune = self.runesolver.runechecker(self.g)
        # print(f'{x=} {y=} {statuetimer=} {fountaintimer=}, {runetimer=}, {cctimer=}')
        print(f'{x=} {y=} rt={self.runetimer} sr={self.solverune} ft={self.fountaintimer} gl={self.goleft} gr={self.goright}')
        # print(f'{x=} {y=} {self.runetimer} {self.solverune} | {self.left}, {self.top}, {self.right}, {self.btm} | {self.left1}, {self.top1}, {self.right1}, {self.btm1}')
        # print(f'{x=}, {y=} | {left=}, {top=}, {right=}, {btm=} | {left1=}, {top1=}, {right1=}, {btm1=}')

        if self.solverune:
            await self.runesolver.gotorune(self.g)
        # elif self.polochecker:
        #     if self.whitedotoccur:
        #         if not await self.polocheckerfunc(self.gotoportal):
        #             self.replaceropeconnect=True
        #         self.whitedotoccur=False
        #     else:
        #         await self.polocheckerfunc(self.gotoportal)
        else:
            pass