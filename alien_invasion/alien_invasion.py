import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """게임 전체의 자원과 동작을 관리하는 클래스"""
    
    def __init__(self):
        """게임을 초기화하고 게임 자원을 생성합니다"""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("외계인 침공!!")
        
        # 게임 기록을 저장할 인스턴스를 만든다
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
        # 배경색을 설정한다
        # self.bg_color = (230, 230, 230)

        self.play_button = Button(self, "Play")
        
    def run_game(self):
        """게임의 메인 루프를 시작합니다"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """키 입력과 마우스 이벤트에 반응한다"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """플레이어가 플레이를 클릭하면 새 게임을 시작한다"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._new_setting()
    
    def _new_setting(self): # 와랄라랄라 내가 새로 만든 함수!!
        """게임을 다시 세팅"""
        # 게임 세팅을 리셋합니다
        self.settings.initialize_dynamic_settings()

        # 게임 기록을 리셋합니다
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # 남아 있는 외계인과 탄환을 제거
        self.aliens.empty()
        self.bullets.empty()

        # 새 함대를 만들고 우주선 배치
        self._create_fleet()
        self.ship.center_ship()

        # 마우스 커서를 숨긴다
        pygame.mouse.set_visible(False)

    def _check_keydown_event(self, event):
        """키 입력에 반응합니다"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p: 
            self._new_setting()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """새 탄환을 생성하고 bullets 그룹에 추가한다"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """탄환 위치를 업데이트하고 사라진 탄환을 제거한다"""
        # 탄환 위치 업데이트
        self.bullets.update()

        # 사라진 탄환 제거
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets)) # 탄환이 실제로 삭제되는지 그냥 확인하기 위해서. 무한 반복되므로 이거 포함하면 엄청 느려짐

        self._check_bullet_alien_collisions()
                
    def _check_bullet_alien_collisions(self):
        """탄환과 외계인의 충돌에 반응한다"""
        # 외계인을 맞힌 탄환이 있는지 체크한다
        # 맞힌 탄환이 있으면 그 탄환과 외계인을 제거한다
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)    

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # 남아 있는 탄환을 파괴하고 새 함대를 만든다
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # 레벨 올리기
            self.stats.level += 1
            self.sb.prep_level()

    def _create_fleet(self):
        """외계인 함대를 만든다"""
        # 외계인 하나를 만들고 한 줄에 몇 개가 들어갈지 정한다
        # 외계인 사이의 공간은 외계인 하나의 너비다
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # 화면 높이에 맞는 외계인 줄 수 결정
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)
        
        # 외계인 함대를 만든다
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                    self._create_alien(alien_number, row_number)
            
    def _create_alien(self, alien_number, row_number):
        """외계인을 만들고 줄에 배치한다"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien.rect.height + 2 * alien.rect.height * row_number
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """외계인이 경계에 닿았다면 그에 맞게 반응한다"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """함대 전체를 아래로 내리고 방향을 바꿉니다"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """함대가 경계에 닿으면 함대에 속한 외계인의 위치를 업데이트한다"""
        self._check_fleet_edges()
        self.aliens.update()

        # 외계인과 우주선이 충돌했는지 확인
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 화면 아래쪽에 닿은 외계인이 있는지 체크
        self._check_aliens_bottom()

    def _ship_hit(self):
        """우주선이 외계인과 충돌했을 때 반응한다"""
        if self.stats.ships_left > 0:
            # ship_left를 줄이고 점수판을 업데이트한다.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # 남아 있는 외계인과 탄환을 제거한다
            self.aliens.empty()
            self.bullets.empty()

            # 새 함대를 만들고 우주선을 배치한다
            self._create_fleet()
            self.ship.center_ship()

            # 일시 정지
            sleep(0.5)
        else: 
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """화면 아래쪽에 닿은 외계인이 있는지 체크합니다"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_screen(self):
        """화면에 이미지를 업데이트하고 새 화면을 그립니다"""
        # 루프의 반복마다 화면을 다시 그린다
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen) # draw() 메서드는 요소를 그릴 서피스를 매개변수로 받는다

        # 점수 정보를 그린다
        self.sb.show_score()

        # 게임이 비활성 상태이면 플레이 버튼을 그린다
        if not self.stats.game_active:
            self.play_button.draw_button()

        # 가장 최근에 그려진 화면을 표시한다
        pygame.display.flip()

if __name__ == '__main__':
    # 게임 인스턴스를 만들고 게임을 실행
    ai = AlienInvasion()
    ai.run_game()