import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """점수 정보를 보고하는 클래스"""

    def __init__(self, ai_game):
        """점수 관련 속성을 초기화"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 점수 정보에 쓸 폰트 세팅
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # 초기 점수 이미지를 준비
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """점수를 이미지로 렌더링"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # 점수를 화면의 오른쪽 상ㄴ단에 표시
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20 
        self.score_rect.top = 20

    def prep_high_score(self):
        """최고 점수 이미지로 렌더링"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # 최고 점수를 화면 상단 중앙에 배치
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """점수, 레벨, 남은 우주선을 화면에 그린다"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
    
    def check_high_score(self):
        """새로운 최고 점수가 있는지 체크한다"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def prep_level(self):
        """레벨을 이미지로 렌더링"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # 레벨 점수를 아래에 배치한다
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        """우주선이 얼마나 남았는지 표시"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


