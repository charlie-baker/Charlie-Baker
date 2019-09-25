import pygame
import time
import random
import math
class character(object):
    global damagelvl
    global maxhplvl
    global speedlvl
    global aspeedlvl
    global rangelvl
    global bulletsizelvl
    global bulletspeedlvl
    def __init__(self,ID,x,y,size,rgb,currency,cc,cccount):
        self.ID = ID
        self.x = x
        self.y = y
        self.size = size
        self.rgb = rgb
        self.speed = speedlvl[0]
        self.normalspeed = speedlvl[0]
        self.xorientation = 0
        self.yorientation = 0
        self.bulletrefresh = aspeedlvl[0]
        self.bulletsize = bulletsizelvl[0]
        self.bulletspeed = bulletspeedlvl[0]
        self.bulletreach = rangelvl[0]
        self.bulletdamage = int(damagelvl[0])
        self.hitbox = (self.x, self.y, self.size, self.size)
        self.health = int(maxhplvl[0])
        self.maxhp = int(maxhplvl[0])
        self.currency = float(currency)
        self.cc = cc
        self.cccount = cccount
        self.cclength = 0
        self.severity = 0
        self.dmgbuff = True
        self.hpbuff = True
        self.spdbuff = True
        self.aspdbuff = True
        self.bulletrangebuff = True
        self.bulletcount = 100
        self.dead = False
    def drawcharacter(self,window_main):
        self.hitbox = (self.x, self.y, self.size, self.size)
        if self.dead == False:
            try:
                pygame.draw.rect(window_main,(self.rgb),(self.hitbox))
                if self.bulletcount > self.bulletrefresh:
                    pygame.draw.rect(window_main,(255,255,255),(self.x+11, self.y+11,5,5))
            except:
                pass
    def character_hit(self, dmg):
        self.health = self.health - dmg
    def CrowdControl(self, cc, CCLength,severity):
        self.cc = cc
        self.cccount = 0
        self.cclength = CCLength
        self.severity = severity
    def CCCheck(self):
        if self.cc == "slow" and self.cclength > self.cccount:
            self.speed = self.normalspeed //self.severity
        else:
            self.speed = self.normalspeed
        if self.cc == "stun" and self.cclength > self.cccount:
            self.speed = 0
    def buff(self,buff):
        if buff == "dmg":
            indexer = damagelvl.index(self.bulletdamage)
            if indexer!= 4:
                if (self.currency - buffcosts[indexer]) >=0:
                    self.bulletdamage = damagelvl[indexer+1]
                    self.currency += -buffcosts[indexer]
                    self.dmgbuff = False
        if buff == "hp":
            indexer = maxhplvl.index(self.maxhp)
            if indexer!= 4:
                if (self.currency - buffcosts[indexer]) >=0:
                    self.maxhp = maxhplvl[indexer+1]
                    self.currency += -buffcosts[indexer]
                    self.hpbuff = False
                    self.health = self.maxhp
        if buff == "speed":
            indexer = speedlvl.index(self.normalspeed)
            if indexer!= 4:
                if (self.currency - buffcosts[indexer]) >=0:
                    self.speed = speedlvl[indexer+1]
                    self.currency += -buffcosts[indexer]
                    self.spdbuff = False
                    self.normalspeed = self.speed
        if buff == "aspeed":
            indexer = aspeedlvl.index(self.bulletrefresh)
            if indexer!= 4: 
                if (self.currency - buffcosts[indexer]) >=0:
                    self.bulletrefresh = aspeedlvl[indexer+1]
                    self.bulletspeed = bulletspeedlvl[indexer + 1]
                    self.currency += -buffcosts[indexer]
                    self.aspdbuff = False
        if buff == "range":
            indexer = rangelvl.index(self.bulletreach)
            if indexer!= 4:
                if (self.currency - buffcosts[indexer]) >=0:
                    self.bulletreach = rangelvl[indexer+1]
                    self.bulletsize = bulletsizelvl[indexer + 1]
                    self.currency += -buffcosts[indexer]
                    self.bulletrangebuff = False
class projectile(object):
    def __init__ (self,x,y,radius,colour,speed,xorientation,yorientation,spawnx,spawny,distance,damage):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.xorientation = xorientation
        self.yorientation = yorientation
        self.xvel = speed * xorientation
        self.yvel = speed * yorientation
        self.spawnx = spawnx
        self.spawny = spawny
        self.distance = distance
        self.damage = int(damage)
        self.hitbox = (self.x,self.y,self.radius,self.radius)
        self.rand = random.randint(0,10000)
    def drawprojectile(self, window_main):
        self.hitbox = (int(self.x),int(self.y),int(self.radius),int(self.radius))
        pygame.draw.circle(window_main, self.colour, (int(self.x), int(self.y)), int(self.radius))   
class gelly(object):
    def __init__ (self,ID,speed,radius,r,g,b,damage,value,health,impactdeath,weight,randomelement,scarcity):
        self.ID = ID
        #deciding where it randomly spawns and what direction it will travel in:
        rand1 = random.randint(0,1)
        rand2 = random.randint(0,1)
        self.xvel = 0
        self.yvel = 0
        if rand1 == 0:
            if self.ID != 6:
                self.x = (random.randint(100+radius,1720-radius))
            else:
                self.x = (random.randint(300+radius,1420-radius))
            self.y = (1000 * rand2)    
            xorientation = 0
            if rand2 == 1:
                yorientation = -1
            else:
                yorientation = 1
        else:
            if self.ID!=6:
                self.y = (random.randint(100+radius,900-radius))
            else:
                self.y= (random.randint(400+radius,600-radius))
            self.x = (1920 * rand2)
            yorientation = 0
            if rand2 == 1:
                xorientation = -1
            else:
                xorientation = 1
        self.xvel = (speed * xorientation)
        self.yvel = (speed * yorientation)
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b
        self.colour = (r,g,b)
        self.damage = (damage)
        self.value = value
        self.maxhp = int(health)
        self.health = int(health)
        self.impactdeath = impactdeath
        self.weight = weight
        self.inside = False
        self.hitbox = (self.x,self.y,self.radius,self.radius)
        self.immunitycount = 50
        self.count = 0
        self.rand = 0
        self.gellycollisioncount = 0
        self.scarcity = scarcity
        self.randomelement = random.randint(0,randomelement)
        if self.ID == 4 or self.ID == 5:
            self.xdistance = 0
            self.ydistance = 0
    def drawenemy(self, window_main):
        self.hitbox = (self.x,self.y,self.radius,self.radius)
        try:
            pygame.draw.circle(window_main, self.colour, (self.x,self.y), self.radius)
        except:
            pass
    def enemy_hit(self, dmg):
        self.health = self.health - dmg
class arena(object):
    def __init__ (self,ID,spawnrate,value,gellyrange,difficulty):
        self.ID = ID
        self.spawnrate = spawnrate
        self.value = value
        self.gellyrange = list(gellyrange)
        self.difficulty = (1/difficulty)
        self.spawncount = 0
    def spawn(self):
        self.spawncount +=1
        if self.spawncount >= self.spawnrate:
            self.spawncount = 0
            if 1 in self.gellyrange:
                rand = random.randint(0,10)
                if rand>3:
                    enemies.append(gelly(g1[0],g1[1],g1[2],g1[3],g1[4],g1[5],g1[6],g1[7],g1[8],g1[9],g1[10],g1[11],g1[12]))
                if rand>6:
                    enemies.append(gelly(g1[0],g1[1],g1[2],g1[3],g1[4],g1[5],g1[6],g1[7],g1[8],g1[9],g1[10],g1[11],g1[12]))
                if rand==9:
                    enemies.append(gelly(g1[0],g1[1],g1[2],g1[3],g1[4],g1[5],g1[6],g1[7],g1[8],g1[9],g1[10],g1[11],g1[12]))
            if 2 in self.gellyrange:
                rand = random.randint(1,math.ceil(g2[12]*self.difficulty))
                if rand == 1:
                    enemies.append(gelly(g2[0],g2[1],g2[2],g2[3],g2[4],g2[5],g2[6],g2[7],g2[8],g2[9],g2[10],g2[11],g2[12]))
            if 3 in self.gellyrange:
                rand = random.randint(1,math.ceil(g3[12]*self.difficulty))
                if rand == 1:
                    enemies.append(gelly(g3[0],g3[1],g3[2],g3[3],g3[4],g3[5],g3[6],g3[7],g3[8],g3[9],g3[10],g3[11],g3[12]))
            if 4 in self.gellyrange:
                rand = random.randint(1,math.ceil(g4[12]*self.difficulty))
                if rand == 1:
                    enemies.append(gelly(g4[0],g4[1],g4[2],g4[3],g4[4],g4[5],g4[6],g4[7],g4[8],g4[9],g4[10],g4[11],g4[12]))
            if 5 in self.gellyrange:
                rand = random.randint(1,math.ceil(g5[12]*self.difficulty))
                if rand == 1:
                    for i in characters:
                        enemies.append(gelly(g5[0],g5[1],g5[2],g5[3],g5[4],g5[5],g5[6],g5[7],g5[8],g5[9],g5[10],g5[11],g5[12]))
            if 6 in self.gellyrange:
                rand = random.randint(1,math.ceil(g6[12]*self.difficulty))
                if rand == 1:
                    enemies.append(gelly(g6[0],g6[1],g6[2],g6[3],g6[4],g6[5],g6[6],g6[7],g6[8],g6[9],g6[10],g6[11],g6[12]))
            if 8 in self.gellyrange:
                rand = random.randint(1,math.ceil(g8[12]*self.difficulty))
                if rand == 1:
                    enemies.append(gelly(g8[0],g8[1],g8[2],g8[3],g8[4],g8[5],g8[6],g8[7],g8[8],g8[9],g8[10],g8[11],g8[12]))
def arena_check():
    global killed
    global arena_state
    global enemies
    global inter_arena
    global nextarena
    if inter_arena == True:
        message_to_screen("Press Enter For Next Arena",(220,220,220),500,900,"font2")
        if nextarena == True:
            inter_arena = False
            p1.x = 600
            p1.y = 200
            p2.x = 1300
            p2.y = 800
            if players == "1":
                p1.x = 940
                p1.y = 500
            arena_state += 1
        else:
            pass
            #upgrades are callable now as seen in draw_window()
    else:
        for i in arenas:
            if i.ID == arena_state:
                i.spawn()
                global currentarenavalue
                currentarenavalue = i.value
                if killed >= i.value:
                    nextarena = False
                    inter_arena = True
                    for i in characters:
                        i.dmgbuff = True
                        i.hpbuff = True
                        i.aspdbuff = True
                        i.spdbuff = True
                        i.bulletrangebuff = True
                    killed = 0
                    enemies = []
                    for i in characters:
                        i.health = i.maxhp
                        i.dead = False
                        i.speed = i.normalspeed
                    if players == "2":
                        p1.x = 600
                        p1.y = 200
                        p2.x = 1300
                        p2.y = 200
                    else:
                        p1.x = 940
                        p1.y = 500
def Key_presses():
    global pausehalt
    global nextarena
    global pause
    pausehalt += 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        if pausehalt > 50:
            pausehalt = 0
            if pause == False:
                pause = True
            else:
                pause = False
    if pause == False:
        p1.CCCheck()
        p2.CCCheck()
        if keys[pygame.K_a] and p1.x > 100 + p1.speed:
            p1.x = p1.x - p1.speed
            p1.xorientation = -1
        if keys[pygame.K_d] and p1.x < 1820 - p1.speed - p1.size:
            p1.x = p1.x + p1.speed
            p1.xorientation = 1
        if keys[pygame.K_w] and p1.y > 100 + p1.speed:
            p1.y = p1.y - p1.speed
            p1.yorientation = -1
        if keys[pygame.K_s] and p1.y < 900 - p1.speed - p1.size:
            p1.y = p1.y + p1.speed
            p1.yorientation = 1
        if keys[pygame.K_w] == False and keys[pygame.K_s] == False:
            p1.yorientation = 0
        if keys[pygame.K_a] == False and keys[pygame.K_d] == False:
            p1.xorientation = 0
        if keys[pygame.K_LEFT] and p2.x > 100 + p2.speed:
            p2.x = p2.x - p2.speed
            p2.xorientation = -1
        if keys[pygame.K_RIGHT] and p2.x < 1820 - p2.speed - p2.size:
            p2.x = p2.x + p2.speed
            p2.xorientation = 1
        if keys[pygame.K_UP] and p2.y > 100 + p2.speed:
            p2.y = p2.y - p2.speed
            p2.yorientation = -1
        if keys[pygame.K_DOWN] and p2.y < 900 - p2.speed - p2.size:
            p2.y = p2.y + p2.speed
            p2.yorientation = 1
        if keys[pygame.K_UP] == False and keys[pygame.K_DOWN] == False:
            p2.yorientation = 0
        if keys[pygame.K_LEFT] == False and keys[pygame.K_RIGHT] == False:
            p2.xorientation = 0
        if keys[pygame.K_RETURN]:
            nextarena = True
        if p1.cc != "stun" or p1.cclength < p1.cccount:
            if keys[pygame.K_SPACE] and p1.dead == False:
                if (p1.xorientation != 0 or p1.yorientation != 0) and p1.bulletcount > p1.bulletrefresh:
                    bulletsone.append(projectile(p1.x + p1.size //2, p1.y + p1.size //2, p1.bulletsize,(200,100,100),p1.bulletspeed,p1.xorientation,p1.yorientation,p1.x,p1.y,p1.bulletreach, p1.bulletdamage))
                    p1.bulletcount = 0
        if players == "2":
            if p2.cc != "stun" or p2.cclength < p2.cccount:
                if keys[pygame.K_KP_ENTER] and p2.dead == False:
                    if (p2.xorientation != 0 or p2.yorientation != 0) and p2.bulletcount > p2.bulletrefresh:
                        bulletstwo.append(projectile(p2.x + p2.size //2, p2.y + p2.size//2, p2.bulletsize,(130,130,200),p2.bulletspeed,p2.xorientation,p2.yorientation,p2.x,p2.y,p2.bulletreach,p2.bulletdamage))
                        p2.bulletcount = 0
        p1.bulletcount += 1
        p2.bulletcount += 1
        p1.cccount += 1
        p2.cccount += 1
def hit_enemies():
    global killed
    for bullet in bulletsone:
        bullet.drawprojectile(window_main)
        for enemy in enemies:
            if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                    bullet.damage = bullet.damage - enemy.health
                    enemy.enemy_hit(bullet.damage + enemy.health)
                if bullet.damage <=0:
                    try:
                        bulletsone.pop(bulletsone.index(bullet))
                    except:
                        pass
                if enemy.health <=0:
                    killed+= enemy.value
                    enemies.pop(enemies.index(enemy))
                    if p2.dead == True:
                        p1.currency += enemy.value/2
                        p2.currency += enemy.value/2
                    else:
                        p1.currency += enemy.value
                    if enemy.ID == 8:
                            a = math.ceil(enemy.radius/10)
                            for b in range(a):
                               spawned = gelly(g4[0],g4[1],g4[2],g4[3],g4[4],g4[5],g4[6],g4[7],g4[8],g4[9],g4[10],g4[11],g4[12])
                               spawned.x = enemy.x + 18*b
                               spawned.y = enemy.y - 18*b
                               enemies.append(spawned)
                    if enemy.ID == 6:
                        slowzone = gelly(g7[0],g7[1],g7[2],g7[3],g7[4],g7[5],g7[6],g7[7],g7[8],g7[9],g7[10],g7[11],g7[12])
                        slowzone.x = enemy.x
                        slowzone.y = enemy.y
                        enemies.append(slowzone)
    if players == "2":
        for bullet in bulletstwo:
            bullet.drawprojectile(window_main)
            for enemy in enemies:
                if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                    if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                        bullet.damage = bullet.damage - enemy.health
                        enemy.enemy_hit(bullet.damage + enemy.health)
                    if bullet.damage <=0:
                        try:
                            bulletstwo.pop(bulletstwo.index(bullet))
                        except:
                            pass
                    if enemy.health <=0:
                        killed += enemy.value
                        enemies.pop(enemies.index(enemy))
                        if p1.dead == True:
                            p1.currency += enemy.value/2
                            p2.currency += enemy.value/2
                        else:
                            p2.currency += enemy.value
                        if enemy.ID == 8:
                            a = math.ceil(enemy.radius/10)
                            for b in range(a):
                               spawned = gelly(g4[0],g4[1],g4[2],g4[3],g4[4],g4[5],g4[6],g4[7],g4[8],g4[9],g4[10],g4[11],g4[12])
                               spawned.x = enemy.x + 18*b
                               spawned.y = enemy.y - 18*b
                               enemies.append(spawned)
                        if enemy.ID == 6:
                            slowzone = gelly(g7[0],g7[1],g7[2],g7[3],g7[4],g7[5],g7[6],g7[7],g7[8],g7[9],g7[10],g7[11],g7[12])
                            slowzone.x = enemy.x
                            slowzone.y = enemy.y
                            enemies.append(slowzone)
def hit_character():
    global killed
    global gelly4_hit_timer
    for i in characters:
        if i.dead == False:
            for enemy in enemies:
                enemy.immunitycount += 1
                if ((i.x + i.size) in range (enemy.x - enemy.radius,enemy.x + enemy.radius) or i.x in range (enemy.x - enemy.radius, enemy.x + enemy.radius)):
                   if (i.y + i.size) in range (enemy.y - enemy.radius, enemy.y+enemy.radius) or (i.y) in range (enemy.y - enemy.radius, enemy.y + enemy.radius):
                        if enemy.immunitycount > 50 and enemy.ID != 7:
                            i.character_hit(enemy.damage)
                            if enemy.ID == 1:
                                i.CrowdControl("stun", 50, 0)
                            if enemy.ID == 2:
                                i.CrowdControl("slow",100, 2)
                            if enemy.ID == 3:
                                i.CrowdControl("stun", 100, 0)
                            if enemy.ID == 4:
                                gelly4_hit_timer = 0
                            if enemy.ID == 5:
                                i.CrowdControl("slow", 40,0.5)
                            if enemy.ID == 6:
                                i.CrowdControl("slow", 20,4)
                            if enemy.ID == 8:
                               a = math.ceil(enemy.radius/10)
                               for b in range(a):
                                   gelly4_hit_timer = 0
                                   spawned = gelly(g4[0],g4[1],g4[2],g4[3],g4[4],g4[5],g4[6],g4[7],g4[8],g4[9],g4[10],g4[11],g4[12])
                                   spawned.x = enemy.x + 18*b
                                   spawned.y = enemy.y - 18*b
                                   enemies.append(spawned)
                            if enemy.impactdeath == True:
                                killed += enemy.value
                                enemies.pop(enemies.index(enemy))
                                if enemy.ID == 6:
                                    slowzone = gelly(g7[0],g7[1],g7[2],g7[3],g7[4],g7[5],g7[6],g7[7],g7[8],g7[9],g7[10],g7[11],g7[12])
                                    slowzone.x = enemy.x
                                    slowzone.y = enemy.y
                                    enemies.append(slowzone)
                            else:
                                enemy.xvel = enemy.xvel * -1
                                enemy.yvel = enemy.yvel * -1
                                enemy.immunitycount = 0
                        elif enemy.immunitycount>20 and enemy.ID == 7:
                            i.character_hit(enemy.damage)
                            i.CrowdControl("slow", 20,4)
                            enemy.immunitycount = 0
def gelly_movement():
    global killed
    global gelly4_hit_timer
    global gelly4_accelerator
    gelly4_hit_timer += 1
    gelly4_accelerator = 2
    if gelly4_hit_timer in range(50,150):
        gelly4_accelerator = 3
    if gelly4_hit_timer in range(150,200):
        gelly4_accelerator = 4
    if gelly4_hit_timer in range(200,250):
        gelly4_accelerator = 5
    if gelly4_hit_timer >=250:
        gelly4_accelerator = 6
    for enemy in enemies:
        enemy.count += 1
        if enemy.ID == 1 or enemy.ID == 3:
            enemy.x = enemy.x + enemy.xvel
            enemy.y = enemy.y + enemy.yvel
            if enemy.x  not in range (0,2000) or enemy.y not in range (0, 1100):
                enemies.pop(enemies.index(enemy))
                killed += enemy.value
        if enemy.ID == 2:
            if enemy.inside == False:
                if enemy.x in range (100,1820) and enemy.y in range (100,900):
                    enemy.inside = True
            if enemy.xvel > 25:
                enemy.xvel = 25
            if enemy.xvel < -25:
                enemy.xvel = -25
            if enemy.yvel > 25:
                enemy.yvel = 25
            if enemy.yvel < -25:
                enemy.yvel = -25
            if enemy.inside == True:
                if enemy.x + enemy.xvel < 100 or enemy.x + enemy.xvel > 1820:
                    enemy.xvel = round(enemy.xvel * -1.3)
                if enemy.y + enemy.yvel < 100 or enemy.y + enemy.yvel > 900:
                    enemy.yvel = round(enemy.yvel * -1.1)
            if enemy.xvel == 0 and enemy.randomelement == 1:
                enemy.xvel = 1
            if enemy.xvel == 0 and enemy.randomelement == 0:
                enemy.xvel = -1
            if enemy.yvel == 0 and enemy.randomelement == 1:
                enemy.yvel = 1
            if enemy.yvel == 0 and enemy.randomelement == 0:
                enemy.yvel = -1
            enemy.x += enemy.xvel
            enemy.y += enemy.yvel
        if enemy.ID == 3:
            if enemy.xvel == 0:
                if enemy.yvel<0:
                    enemy.yvel = math.floor(-enemy.health/3.5)
                else:
                    enemy.yvel = math.ceil(enemy.health/3.5)
            else:
                if enemy.xvel <0:
                    enemy.xvel = math.floor(-enemy.health/2)
                else:
                   enemy.xvel = math.ceil(enemy.health/2) 
            enemy.x+= enemy.xvel
            enemy.y+= enemy.yvel    
        if enemy.ID == 4:
            if enemy.x in range (100,1820) and enemy.y in range (100,900):
                enemy.inside = True
            if enemy.inside == True:
                if players == "1" or enemy.randomelement == 0:
                    enemy.xdistance = (enemy.x - p1.x)
                    enemy.ydistance = (enemy.y - p1.y)
                    if players == "2" and p1.dead == True:
                        enemy.xdistance = (enemy.x - p2.x)
                        enemy.ydistance = (enemy.y - p2.y)
                if (players == "2") and (enemy.randomelement == 1):
                    enemy.xdistance = (enemy.x - p2.x)
                    enemy.ydistance = (enemy.y - p2.y)
                    if p2.dead == True:
                        enemy.xdistance = (enemy.x - p1.x)
                        enemy.ydistance = (enemy.y - p1.y)           
                enemy.colour = (252 - 17*gelly4_accelerator,50,135 + 20 * gelly4_accelerator)
                enemy.cap = math.ceil(5/gelly4_accelerator)
                if enemy.count > gelly4_accelerator:
                    enemy.count = 0
                    if enemy.xdistance > 0:
                        enemy.xvel = enemy.xvel - enemy.cap
                    if enemy.xdistance < 0:
                        enemy.xvel = enemy.xvel + enemy.cap
                    if enemy.ydistance > 0:
                        enemy.yvel = enemy.yvel - enemy.cap
                    if enemy.ydistance < 0:
                        enemy.yvel = enemy.yvel + enemy.cap
                if enemy.xvel > 10*enemy.cap:
                    enemy.xvel = 10*enemy.cap
                if enemy.xvel < -10*enemy.cap:
                    enemy.xvel = -10*enemy.cap
                if enemy.yvel > 10*enemy.cap:
                    enemy.yvel = 10*enemy.cap
                if enemy.yvel < -10*enemy.cap:
                    enemy.yvel = -10*enemy.cap
                if enemy.x + enemy.xvel < 100 or enemy.x + enemy.xvel > 1820:
                    enemy.xvel = (enemy.xvel * -1)
                if enemy.y + enemy.yvel < 100 or enemy.y + enemy.yvel > 900:
                    enemy.yvel = (enemy.yvel * -1)
            enemy.x += enemy.xvel
            enemy.y += enemy.yvel
        if enemy.ID == 5:
            if enemy.x in range (100,1820) and enemy.y in range (100,900):
                enemy.inside = True
            if enemy.inside == True:
                if players == "2":
                    if abs(p1.x - enemy.x + p1.y - enemy.y) < abs(p2.x - enemy.x + p2.y - enemy.y):
                        enemy.xdistance = p1.x - enemy.x
                        px = p1.x
                        enemy.ydistance = p1.y - enemy.y
                        py = p1.y
                    else:
                        enemy.xdistance = p2.x - enemy.x
                        px = p2.x
                        enemy.ydistance = p2.y - enemy.y
                        py = p2.y
                else:
                    enemy.xdistance = p1.x - enemy.x
                    px = p1.x
                    enemy.ydistance = p1.y - enemy.y
                    py = p1.y
                if enemy.count > 4:
                    enemy.count = 0
                    if ((enemy.xdistance * enemy.xdistance) + (enemy.ydistance * enemy.ydistance)) < 50000:
                        if enemy.x > px:
                            enemy.xvel += 1
                        if enemy.x < px:
                            enemy.xvel += -1
                        if enemy.y > py:
                            enemy.yvel += 1
                        if enemy.y < py:
                            enemy.yvel += -1
                if enemy.xvel > 11:
                    enemy.xvel = 11
                if enemy.xvel < -11:
                    enemy.xvel = -11
                if enemy.yvel > 11:
                    enemy.yvel = 11
                if enemy.yvel < -11:
                    enemy.yvel = -11
                if enemy.x + enemy.xvel < 100 or enemy.x + enemy.xvel > 1820:
                    enemy.xvel = (enemy.xvel * -1)
                if enemy.y + enemy.yvel < 100 or enemy.y + enemy.yvel > 900:
                    enemy.yvel = (enemy.yvel * -1)
            enemy.x += enemy.xvel
            enemy.y += enemy.yvel
        if enemy.ID == 6:
            if enemy.inside == False:
                if enemy.x in range (100,1820) and enemy.y in range (100,900):
                    enemy.inside = True 
            if enemy.inside == True:
                if enemy.x + enemy.xvel < 100 or enemy.x + enemy.xvel > 1820:
                    enemy.xvel = round(enemy.xvel * -1)
                if enemy.y + enemy.yvel < 100 or enemy.y + enemy.yvel > 900:
                    enemy.yvel = round(enemy.yvel * -1)
            if enemy.xvel == 0 and enemy.randomelement == 1:
                enemy.xvel = enemy.yvel
            if enemy.xvel == 0 and enemy.randomelement == 0:
                enemy.xvel = -enemy.yvel
            if enemy.yvel == 0 and enemy.randomelement == 1:
                enemy.yvel = enemy.xvel
            if enemy.yvel == 0 and enemy.randomelement == 0:
                enemy.yvel = -enemy.xvel
            enemy.x += enemy.xvel
            enemy.y += enemy.yvel
        if enemy.ID == 7:
            if enemy.count > 1000:
                enemies.pop(enemies.index(enemy))
        if enemy.ID == 8:
            if enemy.x in range (100,1820) and enemy.y in range (100,900):
                enemy.inside = True
            if enemy.inside == True:
                if players == "2":
                    if ((p1.x - enemy.x)*(p1.x - enemy.x) + (p1.y - enemy.y)*(p1.y - enemy.y)) < ((p2.x - enemy.x)*(p2.x - enemy.x) +(p2.y - enemy.y)*(p2.y - enemy.y)):
                        enemy.xdistance = p1.x - enemy.x
                        px = p1.x
                        enemy.ydistance = p1.y - enemy.y
                        py = p1.y
                    else:
                        enemy.xdistance = p2.x - enemy.x
                        px = p2.x
                        enemy.ydistance = p2.y - enemy.y
                        py = p2.y
                else:
                    enemy.xdistance = p1.x - enemy.x
                    px = p1.x
                    enemy.ydistance = p1.y - enemy.y
                    py = p1.y
                if enemy.radius < 22:
                    enemy.weight = 2
                if enemy.radius in range(22,30):
                    enemy.weight = 3
                if enemy.radius >=30:
                    enemy.weight = 4
                if enemy.radius >= 60:
                    enemies.pop(enemies.index(enemy))
                    killed+= enemy.value
                    a = math.ceil(enemy.radius/10)
                    gelly4_hit_timer = 0
                    for b in range(a):
                        spawned = gelly(g4[0],g4[1],g4[2],g4[3],g4[4],g4[5],g4[6],g4[7],g4[8],g4[9],g4[10],g4[11],g4[12])
                        spawned.x = enemy.x + 18*b
                        spawned.y = enemy.y - 18*b
                        enemies.append(spawned)
                enemy.damage = math.floor(0.2*enemy.radius)            
                if enemy.radius < 30:
                    if enemy.count > math.floor(0.2*enemy.radius):
                        enemy.count = 0
                        if ((enemy.xdistance * enemy.xdistance) + (enemy.ydistance * enemy.ydistance)) < 200000:
                            if enemy.x > px:
                                enemy.xvel += 1
                            if enemy.x < px:
                                enemy.xvel += -1
                            if enemy.y > py:
                                enemy.yvel += 1
                            if enemy.y < py:
                                enemy.yvel += -1
                else:
                    if enemy.count > math.ceil(0.3*enemy.radius):
                        enemy.count = 0
                        if enemy.xdistance > 0:
                            enemy.xvel = enemy.xvel + 1
                        if enemy.xdistance < 0:
                            enemy.xvel = enemy.xvel - 1
                        if enemy.ydistance > 0:
                            enemy.yvel = enemy.yvel + 1
                        if enemy.ydistance < 0:
                            enemy.yvel = enemy.yvel - 1   
                enemy.cap  = math.ceil(150/enemy.radius)
                if enemy.xvel > enemy.cap:
                    enemy.xvel = enemy.cap
                if enemy.xvel < -enemy.cap:
                    enemy.xvel = -enemy.cap
                if enemy.yvel > enemy.cap:
                    enemy.yvel = enemy.cap
                if enemy.yvel < -enemy.cap:
                    enemy.yvel = -enemy.cap
                if enemy.x + enemy.xvel < 100 or enemy.x + enemy.xvel > 1820:
                    enemy.xvel = (enemy.xvel * -1)
                if enemy.y + enemy.yvel < 100 or enemy.y + enemy.yvel > 900:
                    enemy.yvel = (enemy.yvel * -1)     
            enemy.x += enemy.xvel
            enemy.y += enemy.yvel   
def gelly_collision():
    global killed
    global gelly4_hit_timer 
    for enemy in enemies:
        enemy.gellycollisioncount+=1
        if enemy.ID != 7:
            for enemy2 in enemies:
                if enemy2.ID != 8 or enemy.ID != 8:
                    if enemy2.ID != 7  and enemy != enemy2:
                        if enemy.y - enemy.radius < enemy2.hitbox[1]- enemy2.hitbox[3] and enemy.y + enemy.radius > enemy2.hitbox[1] - enemy2.hitbox[3]:
                            if enemy.x + enemy.radius > enemy2.hitbox[0]-enemy2.hitbox[2] and enemy.x < enemy2.hitbox[0] + enemy2.hitbox[2]:
                                if enemy.weight > enemy2.weight:
                                    if enemy2.ID != 4:
                                        killed += enemy2.value
                                        enemies.pop(enemies.index(enemy2))
                                    else:
                                        if enemy2.gellycollisioncount > 10:
                                            killed += enemy2.value
                                            enemies.pop(enemies.index(enemy2))
                                    if enemy.ID == 8:
                                        enemy.radius += 5
                                        enemy.maxhp += 1
                                        enemy.health += 1
                                    if enemy2.ID == 6:
                                        slowzone = gelly(g7[0],g7[1],g7[2],g7[3],g7[4],g7[5],g7[6],g7[7],g7[8],g7[9],g7[10],g7[11],g7[12])
                                        slowzone.x = enemy2.x
                                        slowzone.y = enemy2.y
                                        enemies.append(slowzone)
                                    if enemy2.ID == 8:
                                        a = math.ceil(enemy.radius/10)
                                        for b in range(a):
                                            spawned = gelly(g4[0],g4[1],g4[2],g4[3],g4[4],g4[5],g4[6],g4[7],g4[8],g4[9],g4[10],g4[11],g4[12])
                                            spawned.x = enemy.x + 18*b
                                            spawned.y = enemy.y - 18*b
                                            enemies.append(spawned)
                                elif (enemy.weight == enemy2.weight) and (enemy.gellycollisioncount>25):
                                    enemy.xvel = -enemy.xvel
                                    enemy.yvel = -enemy.yvel
                                    enemy2.xvel = -enemy2.xvel
                                    enemy2.yvel = -enemy2.yvel
                                    enemy.gellycollisioncount = 0
                                    enemy2.gellycollisioncount = 0
def Draw_window():
    global currentarenavalue
    global killed
    global main_menu
    global pause
    global end_message
    window_main.fill((0,0,0))
    pygame.draw.rect(window_main,(30,0,30),(100,100,1720,800))
    for enemy in enemies:
        if enemy.ID == 7:
            enemies.pop(enemies.index(enemy))
            enemies.insert(0,enemy)
    for enemy in enemies:
        enemy.drawenemy(window_main)
    if main_menu == False:
        if inter_arena == False:
            message_to_screen(str(arena_state),(75,75,75), 910, 430,"font3")
            pygame.draw.rect(window_main,(2,255,191),(100,960,(killed/currentarenavalue * 1820),15))
        else:
            upgrades()
        if pause == False:
            arena_check()
            Bullet_movement()
            gelly_collision()
            gelly_movement()
            hit_enemies()
            hit_character()
            damage_check()
        for i in characters:
            i.drawcharacter(window_main)
            if i.ID == 1:
                message_to_screen(str(math.floor(i.currency)), i.rgb, 50, 50, "font1")
            else:
                message_to_screen(str(math.floor(i.currency)), i.rgb, 1800, 50, "font1")
        if run == False:
            if end_message == "Gellies Defeated":
                message_colour = (0, 235, 130)
                pos = 500
            else:
                message_colour = (255,50,50)
                pos = 660
            message_to_screen(end_message,message_colour, pos,100, "font3")
    else:
        if controls == False:
            message_to_screen("Gelly",(0, 235, 130),760,100,"font3")
            message_to_screen("One Player", (50,255,50), 280,400, "font4")
            button(300,450, 100,100,(150,150,150),(50,255,50),"1player")
            message_to_screen("Two Players", (50,100,255), 670,400, "font4")
            button(700,450, 100,100,(150,150,150),(50,100,255),"2player")
            message_to_screen("Controls and Tips", (243, 255, 20), 1040,400, "font4")
            button(1100,450,100,100,(150,150,150),(243, 255, 20),"controls")
            message_to_screen("Quit", (255,50,50), 1520,400, "font4")
            button(1500,450,100,100,(150,150,150),(255,50,50),"exit")
            message_to_screen("Difficulty:", (255,255,255),820,600, "font4")
            message_to_screen(difficulty, (255,255,255),960,600,"font4")
            button(500,750,100,100,(0,150,0),(0,255,0),"Easy")
            button(900,750,100,100,(0,0,150),(0,0,255),"Medium")
            button(1300,750,100,100,(150,0,0),(255,0,0),"Hard")
        else:
            button(880,850,100,100,(150,150,150),(255,255,255),"main menu")
            message_to_screen("Main Menu", (255,255,255),860,800,"font4")
            message_to_screen("Player 1 Controls: Press WASD To Move                     Press SPACE To Shoot", (200,100,0),150,200, "font4")
            message_to_screen("Player 2 Controls: Press ARROW KEYS To Move      Press NUMBER PAD ENTER To Shoot", (0,150,200),150,300,"font4")
            message_to_screen("Press Escape to Pause", (0, 255, 166),150,400,"font4")
            message_to_screen("Tips: Each upgrade can be bought between arenas, on 5 seperate occasions for increasing effect.",(200, 200, 200),150,500,"font4")
            message_to_screen("You shoot while moving, in the direction you are moving when enough time since your last attack has passed",(200, 200, 200),150,600,"font4")
            message_to_screen("The Red Gelly heals you if you can catch it!", (200,200,200),150,700, "font4")
    if pause == True and main_menu == False:
        message_to_screen("Press escape to resume game", (255,255,255),600,100,"font1")
    pygame.display.update()
def Bullet_movement():
    for bullet in bulletsone:
        if bullet.x < 1820 - bullet.radius and bullet.x > 100 + bullet.radius and abs(bullet.x - bullet.spawnx) < bullet.distance:
            bullet.x = bullet.x + bullet.xvel
        else:
            bulletsone.pop(bulletsone.index(bullet))

        if  bullet.y < 900 - bullet.radius and bullet.y > 100 + bullet.radius and abs(bullet.y - bullet.spawny) < bullet.distance:
            bullet.y = bullet.y + bullet.yvel
        else:
            try:
                bulletsone.pop(bulletsone.index(bullet))
            except:
                pass
    if players == "2":
        for bullet in bulletstwo:
            if bullet.x < 1820 - bullet.radius and bullet.x > 100 + bullet.radius and abs(bullet.x - bullet.spawnx) < bullet.distance:
                bullet.x = bullet.x + bullet.xvel
            else:
                bulletstwo.pop(bulletstwo.index(bullet))
            if bullet.y < 900 - bullet.radius and bullet.y > 100 + bullet.radius and abs(bullet.y - bullet.spawny) < bullet.distance:
                bullet.y = bullet.y + bullet.yvel
            else:
                try:
                    bulletstwo.pop(bulletstwo.index(bullet))
                except:
                    pass
def damage_check():
    global run
    global arena_state
    global inter_arena
    global end_message
    p1hpleft = (p1.health/p1.maxhp)
    p2hpleft = (p2.health/p2.maxhp)
    deadcount = 0
    if arena_state == 10 and inter_arena == True:
        run = False
        end_message = "Gellies Defeated"
    for i in characters:
        if i.health <=0:
            i.dead = True
            deadcount += 1
        if i.health > i.maxhp:
            i.health = i.maxhp
        if i.cclength > i.cccount:
            if i.ID == 1:
                i.rgb = (220*p1hpleft,120*p1hpleft,150*p1hpleft)
            if i.ID == 2:
                i.rgb = (150*p2hpleft,170*p2hpleft,220*p2hpleft)
        else:
            if i.ID == 1:
                i.rgb = (200*p1hpleft+20,100*p1hpleft+20,0)
            if i.ID == 2:
                i.rgb = (0,150*p2hpleft+20,200*p2hpleft+20)
        if deadcount == len(characters):
            run = False
            end_message = "You Lose"
    for enemy in enemies:
        if enemy.ID!= 4:
            hpleft = (enemy.health/enemy.maxhp)
            enemy.colour = (math.floor(enemy.r*hpleft),math.floor(enemy.g*hpleft),math.floor(enemy.b*hpleft))
def upgrades():
    message_to_screen("Upgrades cost: 6, 25, 100, 300 per level",(80, 80, 80),670,500,"font4")
    if players == "1":
        if p1.dmgbuff == True and p1.bulletdamage<damagelvl[4]:
            message_to_screen("Damage",(200,0,0),200,100,"font4")
            pygame.draw.circle(window_main,(200,0,0),(260,150),15)
            if p1.x in range (235,285) and p1.y in range (120,160):
                p1.buff("dmg")
        if p1.hpbuff == True and p1.maxhp < maxhplvl[4]:
            message_to_screen("Max Health",(0,200,0),500,100,"font4")
            pygame.draw.circle(window_main,(0,200,0),(560,150),15)
            if p1.x in range (535,585) and p1.y in range (120,160):
                p1.buff("hp")
        if p1.spdbuff == True and p1.normalspeed < speedlvl[4]:
            message_to_screen("Movement Speed",(0,0,200),800,100,"font4")
            pygame.draw.circle(window_main,(0,0,200),(860,150),15)
            if p1.x in range (835,885) and p1.y in range (120,160):
                p1.buff("speed")
        if p1.aspdbuff == True and  p1.bulletrefresh > aspeedlvl[4]:
            message_to_screen("Attack Speed",(255,255,255),1100,100,"font4")
            pygame.draw.circle(window_main,(255,255,255),(1160,150),15)
            if p1.x in range (1135,1185) and p1.y in range (120,160):
                p1.buff("aspeed")
        if p1.bulletrangebuff == True and p1.bulletreach < rangelvl[4]:
            message_to_screen("Attack Range",(255,255,0),1400,100,"font4")
            pygame.draw.circle(window_main,(255,255,0),(1460,150),15)
            if p1.x in range (1435,1485) and p1.y in range (120,160):
                p1.buff("range")
    elif players == "2":
        if p1.dmgbuff == True or p2.dmgbuff == True:
            message_to_screen("Damage",(200,0,0),260,100,"font4")
            pygame.draw.circle(window_main,(200,0,0),(260,150),15)
            if p1.x in range (235,285) and p1.y in range (120,160) and p1.dmgbuff == True:
                p1.buff("dmg")
            if p2.x in range (235,285) and p2.y in range (120,160) and p2.dmgbuff == True:
                p2.buff("dmg")
        if p1.hpbuff == True or p2.hpbuff == True:
            message_to_screen("Max Health",(0,200,0),560,100,"font4")
            pygame.draw.circle(window_main,(0,200,0),(560,150),15)
            if p1.x in range (535,585) and p1.y in range (120,160) and p1.hpbuff == True:
                p1.buff("hp")
            if p2.x in range (535,585) and p2.y in range (120,160) and p2.hpbuff == True:
                p2.buff("hp")
        if p1.spdbuff == True or p2.spdbuff == True:
            message_to_screen("Movement Speed",(0,0,200),860,100,"font4")
            pygame.draw.circle(window_main,(0,0,200),(860,150),15)
            if p1.x in range (835,885) and p1.y in range (120,160 ) and  p1.spdbuff == True:
                p1.buff("speed")
            if p2.x in range (835,885) and p2.y in range (120,160) and p2.spdbuff == True:
                p2.buff("speed")
        if p1.aspdbuff == True or p2.aspdbuff == True:
            message_to_screen("Attack Speed",(255,255,255),1160,100,"font4")
            pygame.draw.circle(window_main,(255,255,255),(1160,150),15)
            if p1.x in range (1135,1185) and p1.y in range (120,160) and p1.aspdbuff == True:
                p1.buff("aspeed")
            if p2.x in range (1135,1185) and p2.y in range (120,160) and p2.aspdbuff == True:
                p2.buff("aspeed")
        if p1.bulletrangebuff == True or p2.bulletrangebuff == True:
            message_to_screen("Attack Range",(255,255,0),1460,100,"font4")
            pygame.draw.circle(window_main,(255,255,0),(1460,150),15)
            if p1.x in range (1435,1485) and p1.y in range (120,160) and p1.bulletrangebuff == True:
                p1.buff("range")
            if p2.x in range (1435,1485) and p2.y in range (120,160) and p2.bulletrangebuff == True:
                p2.buff("range")
def message_to_screen(msg,colour,x,y,font):
    try:
        if font == "font1":
            screen_text = font1.render(msg, True, colour)
        elif font == "font2":
            screen_text = font2.render(msg, True, colour)
        elif font == "font3":
            screen_text = font3.render(msg, True, colour)
        elif font == "font4":
            screen_text = font4.render(msg, True, colour)
        window_main.blit(screen_text, [x,y])
    except:
        pass
def button (x,y,width,height,off_colour,on_colour,action):
    global players
    global restart
    global main_menu
    global run
    global characters
    global controls
    global difficulty
    mousepos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mousepos[0] > x and y + height > mousepos[1] > y:
        pygame.draw.rect(window_main, on_colour, (x,y,width,height))
        if click[0] == 1:
            if action == "controls":
                controls = True
            elif action == "exit":
                message_to_screen("Quitting Gelly", (255,50,50),150,100,"font1")
                pygame.display.update()
                run = False
                restart = False
            elif action == "1player":
                players = "1"
                characters = [p1]
                main_menu = False
                p1.x = 930
                p1.y = 500
                if difficulty == "Easy":
                    enemies.append(gelly(g1[0],g1[1],g1[2],g1[3],g1[4],g1[5],g1[6],g1[7],g1[8],g1[9],g1[10],g1[11],g1[12]))
                if difficulty == "Medium":
                    enemies.append(gelly(g4[0],g4[1],g4[2],g4[3],g4[4],g4[5],g4[6],g4[7],g4[8],g4[9],g4[10],g4[11],g4[12]))
                if difficulty == "Hard":
                    enemies.append(gelly(g6[0],g6[1],g6[2],g6[3],g6[4],g6[5],g6[6],g6[7],g6[8],g6[9],g6[10],g6[11],g6[12]))
                difficulty_control()
            elif action == "2player":
                if difficulty == "Easy":
                    enemies.append(gelly(g1[0],g1[1],g1[2],g1[3],g1[4],g1[5],g1[6],g1[7],g1[8],g1[9],g1[10],g1[11],g1[12]))
                if difficulty == "Medium":
                    enemies.append(gelly(g4[0],g4[1],g4[2],g4[3],g4[4],g4[5],g4[6],g4[7],g4[8],g4[9],g4[10],g4[11],g4[12]))
                if difficulty == "Hard":
                    enemies.append(gelly(g6[0],g6[1],g6[2],g6[3],g6[4],g6[5],g6[6],g6[7],g6[8],g6[9],g6[10],g6[11],g6[12]))
                players = "2"
                characters = [p1,p2]
                main_menu = False
                difficulty_control()
                for arena in arenas:
                    arena.value = arena.value*2
                    arena.spawnrate = math.ceil(arena.spawnrate/1.8)
            elif action == "main menu":
                controls = False
            elif action == "Easy":
                difficulty = "Easy"
            elif action == "Medium":
                difficulty = "Medium"
            elif action == "Hard":
                difficulty = "Hard"
            difficulty_control()
    else:
        pygame.draw.rect(window_main, off_colour, (x,y,width,height))
def difficulty_control():
    global difficulty
    global arenas
    if difficulty == "Easy":
        diffactor = 0.7
    elif difficulty == "Medium":
        diffactor = 1
    elif difficulty == "Hard":
        diffactor = 1.5
    arenas = [arena(1,60,25,[1],1), arena(2,75,65,[1,4,5],3*diffactor), arena(3,55,100,[1,2,5],1.5*diffactor), arena(4,70,120,[1,2,4,5],1.25*diffactor), arena(5,35,125,[1,3],3), arena(6,50,150,[1,2,5,6],1.75*diffactor), arena(7,35,500,[1,8],1.5*diffactor),
          arena(8,50,400,[1,5,4,6],1.75*diffactor), arena(9,2,1500,[3],4 + 2*diffactor), arena(10,40,800,[1,2,3,4,5,6,8],1 + diffactor)]
pygame.init()
g1 = [1,4,15,0,200,0,0,2,1,False,1,1,5] #green
g2 = [2,8,21,230,230,200,4,10,3,False,3,1,12] #white
g3 = [3,2,30,245,225,0,9,30,7,True,4,1,25] #yellow
g4 = [4,5,10,150,50,255,3,6,1,True,1,1,7] #purple
g5 = [5,3,15,200,0,60,-5,0,1,True,1,1,40] #red
g6 = [6,6,21,0,191,255,1,15,3,True,2,1,15] # light blue
g7 = [7,0,90,0,0,255,1,0,20,False,1,1,0] #deep blue, non spawnable
g8 = [8,5,11,255,128,0,5,25,4,True, 1, 1, 37] #Orange
buffcosts = [6,25,100,300]
damagelvl = [1,2,3,5,8]
bulletsizelvl = [20,22,26,32,40]
maxhplvl = [10,15,21,27,35]
speedlvl = [4,5,7,10,14]
aspeedlvl = [110,85,60,35,10]
rangelvl = [200,275,400,575,800]
bulletspeedlvl = [13,17,24,33,45]
font1 = pygame.font.SysFont("comicsans", 60, True, False)
font2 = pygame.font.SysFont("impact",80,False,False)
font3 = pygame.font.SysFont("inkfree",120,True,False)
font4 = pygame.font.SysFont("cambria",30,False,False)
difficulty = "Medium"
restart = True
while restart == True:
    pygame.init()
    p1 = (character(1,600,200,27,(200,100,0),0,"",0))
    p2 = (character(2,1300,800,27,(0,150,200),0,"",0))
    window_main = pygame.display.set_mode((1920,1000))
    pygame.display.set_caption("Gelly")
    iteration_rate = 15
    bulletsone = []
    bulletstwo = []
    enemies = []
    killed = 0
    controls = False
    players = "1"
    playerloop = True
    inter_arena = False
    main_menu = True
    arena_state = 1
    currentarenavalue = 1
    gelly4_hit_timer = 200
    run = True
    pause = True
    pausehalt = 100
    while run == True:
        pygame.time.delay(iteration_rate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                restart = False
                run = False
                end_message = "Quitting Gelly"
        Key_presses()
        Draw_window()
    time.sleep(2)
pygame.quit()
