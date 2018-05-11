class Setting():
    def __init__(self):
        """ initial game setting """
        self.bg_color = (0,0,0)       # 背景顏色
        self.width =1200
        self.height=800
        self.speed_factor=1.5
        """ initial bullet """
        self.bullet_speed_factor = 15
        self.bullet_height = 5
        self.bullet_width = 3
        self.bullet_color = (230,50,50)
        self.bullet_allow = 30