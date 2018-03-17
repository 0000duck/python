"""
反恐精英 CS
"""

"""
战士 和 敌人
"""
class Person:
    def __init__(self, name):
        # 姓名
        self.name = name
        # 血量
        self.blood = 100

    # 给弹夹安装子弹
    def installBullet(self, clip, bullet):
        clip.savaBullets(bullet)

    # 给抢安装弹夹
    def installClip(self, gun, clip):
        gun.mountingClip(clip)

    # 持枪
    def takeGun(self, gun):
        self.gun = gun

    # 开枪射击敌人
    def fire(self, enemy):
        self.gun.shoot(enemy)

    # 掉血
    def loseBlood(self, damage):
        self.blood -= damage

    def __str__(self):
        return self.name + "剩余的血量为： " + str(self.blood)


"""
弹夹
"""
class Clip:
    def __init__(self, capacity):
        # 子弹最大容量
        self.capacity = capacity
        # 当前子弹的数量
        self.currentList = []

    # 安装子弹
    def savaBullets(self, bullet):
        # 当子弹数量小于最大容量的时候
        if len(self.currentList) < self.capacity:
            self.currentList.append(bullet)

    # 出子弹
    def shotBullet(self):
        # 判断当前弹夹中是否有子弹
        if len(self.currentList) > 0:
            bullet = self.currentList[-1]
            self.currentList.pop()
            return bullet
        else:
            return None

    # 自定义字符串
    def __str__(self):
        return "弹夹中当前的子弹数量为：" + str(len(clip.currentList)) + "/" + str(self.capacity)

"""
子弹类型
"""
class Bullet:
    def __init__(self, damage):
        # 伤害力
        self.damage = damage

    # 伤害敌人
    def hurt(self, enemy):
        enemy.loseBlood(self.damage)



"""
抢类型
"""
class Gun:
    def __init__(self):
        # 默认没有弹夹
        self.clip = None

    def __str__(self):
        if self.clip:
            return "抢当前有弹夹"
        else:
            return "抢当前没有弹夹"

    # 连接弹夹
    def mountingClip(self, clip):
        if not self.clip:
            self.clip = clip

    # 射击
    def shoot(self, enemy):
        # 弹夹出子弹
        bullet = self.clip.shotBullet()

        if bullet:
            bullet.hurt(enemy)
        else:
            print("没有子弹了， 放了空枪。。。")



"""
测试
"""
'''验证安装子弹的功能'''
# 创建一个战士
soldier = Person("战士")
# 创建一个弹夹
clip = Clip(20)
print(clip)

# 当子弹数量小于5， 添加 5 颗子弹
i = 0
while i<5:
    # 创建一个子弹
    bullet = Bullet(5)
    soldier.installBullet(clip, bullet)
    i += 1

print("--- 安装子弹之后 ---")

# 添加子弹后的弹夹的数量
print(clip)


'''验证安装弹夹的功能'''
# 创建一把枪
gun = Gun()
print(gun)

# 安装弹夹
soldier.installClip(gun, clip)
print("--- 安装弹夹之后 ---")
print(gun)


# 创建一个敌人
enemy = Person("敌人")
print(enemy)

# 士兵拿枪
soldier.takeGun(gun)

# 士兵向敌人开枪
soldier.fire(enemy)
print(clip)
print(enemy)

soldier.fire(enemy)
print(clip)
print(enemy)