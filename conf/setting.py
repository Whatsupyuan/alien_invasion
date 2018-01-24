class Setting():
    def __init__(self):
        self.width = 800
        self.height = 500
        # 背景颜色
        self.backgroudColor = (230,230,230)
        # 飞船的移动速度，越大越快
        self.ship_speed_factor = 1

        # bullet
        self.bullet_width = 3
        # 子弹移动速度
        self.bullet_speed_factor = 1

        self.bullet_height = 15
        self.bullet_color = 60,60,60
        # 允许的bullet数量,game中最多可以使用的子弹
        self.bullets_allowed = 3