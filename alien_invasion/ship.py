import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """우주선을 관리하는 클래스"""
    
    def __init__(self, ai_game):
        """우주선을 초기화하고 시작 위치를 결정한다"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #우주선 이미지를 불러오고 그 사각형을 가져온다
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        #우주선을 불러올 때마다 화면의 아래쪽 중앙에서 시작한다
        self.rect.midbottom = self.screen_rect.midbottom

        #우주선의 가로 위치를 나타내는 소수점 있는 값을 저장한다
        self.x = float(self.rect.x)

        # 움직임 플래그
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """움직임 플래그에 따라 우주선 위치를 업데이트"""
        # rect가 아닌 우주선의 x 값을 업데이트한다
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # self.x를 써서 rect 객체를 업데이트한다
        self.rect.x = self.x
        
    def center_ship(self):
        """우주선을 화면 하단 중앙에 배치한다"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """현재 위치에 우주선을 그린다"""
        self.screen.blit(self.image, self.rect)