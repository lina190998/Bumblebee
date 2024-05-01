import random
import time
from time import perf_counter
from configparser import ConfigParser
# from initinterception import interception, move_to, move_relative, left_click, keydown, keyup, sleep
from initinterception import keydown, keyup, sleep














class Action:

    def __init__(self):
        self.config = ConfigParser()
        self.config.read('settings.ini')
        self.atk = self.config.get('keybind', 'attack')
        self.jump = self.config.get('keybind', 'jump')
        self.teleport = self.config.get('keybind', 'teleport')
        self.ropeconnect = self.config.get('keybind', 'ropeconnect')
        self.npc = self.config.get('keybind', 'npc')
        self.fountainkey = self.config.get('keybind', 'fountainkey')
        self.offsety=10
        self.offsetx=10
        ## for main rotation
        self.top=10.0
        self.left=10.0
        self.right=10.0
        self.btm=10.0 
        ## for stormwing map
        self.stop=29.0
        self.sleft=35.0 # 18.0 # 27.0
        self.sright=130 # 125.0 # 135.0 140.0 132.5
        self.sbtm=58.0 # 54.5
        self.runesolver=None
        self.g=None
        ## misc
        self.replaceropeconnect=False
        self.rotation_list = ['default']
        self.rotation='default'
        self.rotation_mapping = {
            'default': self.clockwise,
        }  
        self.rotation='default'

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
    
    def refreshkeybind(self):
        self.config.read('settings.ini')
        self.atk = self.config.get('keybind', 'attack')
        self.jump = self.config.get('keybind', 'jump')
        self.teleport = self.config.get('keybind', 'teleport')
        self.ropeconnect = self.config.get('keybind', 'ropeconnect')
        self.npc = self.config.get('keybind', 'npc')
        
    async def escp(self,x=31,y=101):
        keydown('esc')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def escr(self,x=31,y=101):
        keyup('esc')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)
    
    async def escpr(self,x=31,y=101):
        await self.escp()
        await self.escr()

    async def leftp(self,x=31,y=101):
        keydown('left')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def leftr(self,x=31,y=101):
        keyup('left')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def rightp(self,x=31,y=101):
        keydown('right')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def rightr(self,x=31,y=101):
        keyup('right')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def upp(self,x=31,y=101):
        keydown('up')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def upr(self,x=31,y=101):
        keyup('up')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def downp(self,x=31,y=101):
        keydown('down')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def downr(self,x=31,y=101):
        keyup('down')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def downpr(self,x=31,y=101):
        await self.downp()
        await self.downr()

    async def jumpp(self,x=31,y=101):
        keydown(self.jump)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def jumpr(self,x=31,y=101):
        keyup(self.jump)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def jumppr(self,x=31,y=101):
        await self.jumpp()
        await self.jumpr()

    ## additional patch for extra key buttons. 

    async def ep(self,x=31,y=101):
        keydown('e')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def er(self,x=31,y=101):
        keyup('e')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def rp(self,x=31,y=101):
        keydown('r')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def rr(self,x=31,y=101):
        keyup('r')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def f12p(self,x=31,y=101):
        keydown('f12')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def f12r(self,x=31,y=101):
        keyup('f12')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def bp(self,x=31,y=101):
        keydown('b')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def br(self,x=31,y=101):
        keyup('b')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)
        
    async def zp(self,x=31,y=101):
        keydown('z')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def zr(self,x=31,y=101):
        keyup('z')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)
        
    async def xp(self,x=31,y=101):
        keydown('x')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def xr(self,x=31,y=101):
        keyup('x')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)
        
    async def cp(self,x=31,y=101):
        keydown('c')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def cr(self,x=31,y=101):
        keyup('c')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)
        
    async def vp(self,x=31,y=101):
        keydown('v')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def vr(self,x=31,y=101):
        keyup('v')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)
        
    async def ap(self,x=31,y=101):
        keydown('a')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def ar(self,x=31,y=101):
        keyup('a')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)
        
    async def sp(self,x=31,y=101):
        keydown('s')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def sr(self,x=31,y=101):
        keyup('s')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)
        
    async def dp(self,x=31,y=101):
        keydown('d')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def dr(self,x=31,y=101):
        keyup('d')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)
        
    async def fp(self,x=31,y=101):
        keydown('f')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def fr(self,x=31,y=101):
        keyup('f')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def hp(self,x=31,y=101):
        keydown('h')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def hr(self,x=31,y=101):
        keyup('h')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def jp(self,x=31,y=101):
        keydown('j')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def jr(self,x=31,y=101):
        keyup('j')
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def teleportp(self,x=31,y=101):
        keydown(self.teleport)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def teleportr(self,x=31,y=101):
        keyup(self.teleport)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def attackp(self,x=31,y=101):
        keydown(self.atk)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def attackr(self,x=31,y=101):
        keyup(self.atk)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def ropeconnectp(self,x=31,y=101):
        keydown(self.ropeconnect)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def ropeconnectr(self,x=31,y=101):
        keyup(self.ropeconnect)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def ropeconnectpr(self,x=111,y=222,x2=111,y2=222):
        await self.ropeconnectp()
        await self.ropeconnectr()

    async def npcp(self,x=31,y=101):
        keydown(self.npc)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def npcr(self,x=31,y=101):
        keyup(self.npc)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def fountainp(self,x=31,y=101):
        # print(f'{self.fountainkey=}')
        keydown(self.fountainkey)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)

    async def fountainr(self,x=31,y=101):
        keyup(self.fountainkey)
        r = random.randint(x, y)
        r /= 1000
        await sleep(r)
    
    async def leftattack(self):
        print(f'leftattack')
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def rightattack(self):
        print(f'rightattack')
        await self.rightp()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def leftattackk(self):
        print(f'leftattackk')
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def rightattackk(self):
        print(f'rightattackk')
        await self.rightp()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def goleftattack(self):
        print(f'self.goleftattack')
        await self.leftp()
        await self.teleportp()
        await self.teleportr()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def goleftattackk(self):
        print(f'self.goleftattackk')
        await self.leftp()
        await self.teleportp()
        await self.teleportr()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def goattackleft(self):
        print(f'self.goattackleft')
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await self.teleportp()
        await self.teleportr()
        await self.leftr()

    async def goattackkleft(self):
        print(f'self.goattackkleft')
        await self.leftp()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.teleportp()
        await self.teleportr()
        await self.leftr()

    async def gorightattack(self):
        print(f'self.gorightattack')
        await self.rightp()
        await self.teleportp()
        await self.teleportr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def gorightattackk(self):
        print(f'self.gorightattackk')
        await self.rightp()
        await self.teleportp()
        await self.teleportr()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def goattackright(self):
        print(f'self.goattackright')
        await self.rightp()
        await self.attackp()
        await self.attackr()
        await self.teleportp()
        await self.teleportr()
        await self.rightr()

    async def goattackkright(self):
        print(f'self.goattackkright')
        await self.rightp()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await self.teleportp()
        await self.teleportr()
        await self.rightr()

    async def goupattack(self):
        print(f'goupattack')
        await sleep(.1)
        await self.upp()
        await self.teleportp()
        await self.teleportr()
        await self.upr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def goupattack_v2(self):
        print(f'goupattack_v2')
        await self.rightp()
        await self.ropeconnectp()
        await self.ropeconnectr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def goupattack_v3(self):
        print(f'goupattack_v3')
        await sleep(.1)
        await self.jumpp()
        await self.jumpr()
        await self.ropeconnectp(31,101)
        await self.ropeconnectr(31,101)
        await sleep(.333)
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def upjumpattack(self):
        print(f'upjumpattack')
        await sleep(.1)
        await self.upp()
        await self.teleportp()
        await self.teleportr()
        await self.upr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def godownattack(self):
        print(f'godownattack')
        await self.downp()
        await self.teleportp()
        await self.teleportr()
        await self.downr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)




    async def goleftattack_fjump(self):
        print(f'self.goleftattack_fjump')
        await self.leftp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.leftr()

    async def gorightattack_fjump(self):
        print(f'self.gorightattack_fjump')
        await self.rightp()
        await self.jumpp()
        await self.jumpr()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.rightr()

    async def goupattack_fjump(self): # adele upjump
        print(f'goupattack_fjump')
        await sleep(.1)
        await self.jumpp()
        await self.jumpr()
        await self.upp()
        await self.jumpp()
        await self.jumpr()
        await self.upr()
        await self.attackp()
        await self.attackr()
        await self.attackp()
        await self.attackr()
        await sleep(.1)

    async def godownattack_fjump(self):
        print(f'godownattack_fjump')
        await self.downp()    
        await self.jumpp()
        await self.jumpr()
        await self.attackp()
        await self.attackr()
        await self.downr()
        
    async def leftwalk(self,x=222,y=333):
        print(f'leftwalk')
        await self.leftp(x,y)
        await self.leftr()

    async def rightwalk(self,x=222,y=333):
        print(f'rightwalk')
        await self.rightp(x,y)
        await self.rightr()
        
    async def downjump(self):
        await self.downp()
        await self.jumpp()
        await self.jumpr()
        await self.downr()

    # polo portal hunting map rotation patch

    async def upjumpup(self):
        print(f'upjumpup')
        await self.jumpp()
        await self.jumpr()
        await self.upp()
        await self.jumpp()
        await self.jumpr()
        await self.upr()

    async def bountyhuntrotation(self):
        print(f'bountyhuntrotation')
        for i in range(5):
            await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft])()
            time.sleep(.502)
        for i in range(5):
            await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright])()
            time.sleep(.502)

    async def bountyhuntrotationv2(self): # adele flash jump
        print(f'bountyhuntrotationv2')
        for i in range(4):
            await self.goleftattack()
            time.sleep(.502)
        for i in range(4):
            await self.gorightattack()
            time.sleep(.502)

    async def castlewallrotation(self):
        print(f'castlewallrotation') 
        await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft, self.leftattack, self.rightattack, self.leftattackk, self.rightattackk])()
        time.sleep(.5)
        await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright, self.leftattack, self.rightattack, self.leftattackk, self.rightattackk])()
        time.sleep(.5)
        # await self.goleftattack()
        # time.sleep(.502)
        await self.upjumpup()
        time.sleep(.802)
        await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft, self.leftattack, self.rightattack, self.leftattackk, self.rightattackk])()
        time.sleep(.5)
        await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright, self.leftattack, self.rightattack, self.leftattackk, self.rightattackk])()
        time.sleep(.5)
        # await self.gorightattack()
        # time.sleep(.502)
        await self.downjump()
        time.sleep(.702)

    async def castlewallrotationv3(self):
        print(f'castlewallrotationv3')
        await self.leftattack()
        time.sleep(.5)
        await self.rightattack()
        time.sleep(.5)
        # await self.goleftattack()
        # time.sleep(.502)
        await self.ropeconnectpr()
        time.sleep(.802)
        await self.leftattack()
        time.sleep(.5)
        await self.rightattack()
        time.sleep(.5)
        # await self.gorightattack()
        # time.sleep(.502)
        await self.downjump()
        time.sleep(.702)

    async def castlewallrotationv2(self):
        print(f'castlewallrotationv2')
        for i in range(2):
            await self.goleftattack()
            time.sleep(.502)
        await self.ropeconnectpr()
        time.sleep(.802)
        for i in range(2):
            await self.gorightattack()
            time.sleep(.502)
        await self.downjump()
        time.sleep(.702)
        await self.attackp()
        await self.attackr()
        time.sleep(.502)

    async def stormwingrotation(self):
        print(f'stormwingrotation')
        for i in range(5):
            await self.goleftattack()
            time.sleep(.502)
        await self.ropeconnectpr()
        time.sleep(.602)
        for i in range(5):
            await self.gorightattack()
            time.sleep(.502)
        for i in range(5):
            await self.downjump()
            time.sleep(.302)

    async def stormwing(self,x,y,goleft,goright):
        if goright:
            if x > self.sright:
                if y < self.sbtm:
                    await self.godownattack()
                    time.sleep(.3)
                    await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft])()
                    time.sleep(.1)
                elif y > self.stop:
                    await self.upjumpattack()
                    time.sleep(.3)
                goright=False
                goleft=True
            else:
                await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright])()
                time.sleep(.3)
            if x < self.sleft: # only if x < left
                if y < self.sbtm:
                    await self.godownattack()
                    time.sleep(.3)
        elif goleft:
            if x < self.sleft: # only if x < left
                if y > self.stop:
                    time.sleep(.1)
                    await self.upjumpattack()
                    time.sleep(.3)
                elif y < self.stop:
                    await self.godownattack()
                    time.sleep(.3)
                    await random.choice([self.gorightattack,self.goattackright,self.gorightattackk,self.goattackkright])()
                    time.sleep(.3)
                goright=True
                goleft=False
            else:
                await random.choice([self.goleftattack,self.goattackleft,self.goleftattackk,self.goattackkleft])()
                time.sleep(.3)
            if x > self.sright: # only if x > right
                if y < self.sbtm:
                    await self.godownattack()
                    time.sleep(.3)
        return goleft,goright


    # main rotation
    #     
    async def perform_next_attack(self,x,y):
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

    # should this be remove

    

    async def default(self,x,y):
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




            
    async def leftright(self,x,y):
        if self.goleft:
            if x >= self.left-self.offsetx and x <= self.left+self.offsetx:
                await random.choice([self.goupattack])()
                if y > self.top-self.offsety and y <= self.top+self.offsety:
                    self.goright=True
                    self.goleft=False
                print(f'testing: heightdiff={y-self.top}')
            else:
                await random.choice([self.goleftattack, self.goleftattackk])()
        elif self.goright:
            if x >= self.right-self.offsetx and x <= self.right+self.offsetx:
                await random.choice([self.godownattack])()
                if y > self.btm-self.offsety and y <= self.btm+self.offsety:
                    self.goleft=True
                    self.goright=False
            else:
                await random.choice([self.gorightattack, self.gorightattackk])()
        else:
            print(f'exception coordinates .. please fix asap .. {x=} {y=}')

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
                await self.send2(code)
                await self.send3(code)
        if self.replaceropeconnect==True:
            if runonce:
                replaceropeconnecttimer0=self.now
                runonce=False
            replaceropeconnecttimer = self.now - replaceropeconnecttimer0
            if replaceropeconnecttimer > 90:
                self.replaceropeconnect=False
                runonce=True
        # self.cosmicshowerplanttimer = self.now - self.cosmicshowerplanttimer0
        # if self.cosmicshowerplanttimer > 59:
        #     self.cosmicshowerplant = True
        # self.fountaintimer = self.now - self.fountaintimer0
        # if self.fountaintimer > 59:
        #     self.fountain = True
        self.runetimer = self.now - self.runetimer0
        # if runetimer > 600: # change to 600 when haste
        if self.runetimer > 900: # change to 600 when haste
            self.checkrune = True
            # self.checkrune = False
        if self.checkrune:
            self.solverune = self.runesolver.runechecker(self.g)
        print(f'{x=} {y=} rt={self.runetimer} sr={self.solverune} ft={self.fountaintimer} gl={self.goleft} gr={self.goright}')

        if self.solverune:
            await self.runesolver.gotorune(self.g)

    # randomiser patch

    async def send2(self, code):
        keydown(code)
        r = random.randint(31, 131)
        r /= 1000
        await sleep(r)

    async def send3(self, code):
        keyup(code)
        r = random.randint(31, 131)
        r /= 1000
        await sleep(r)

    # test purpose

    async def testnpc(self):
        await self.npcp()
        await self.npcr()



