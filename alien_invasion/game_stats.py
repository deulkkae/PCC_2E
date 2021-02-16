class GameStats:
    """외계인 침공 게임 기록 저장"""

    def __init__(self, ai_game):
        """기록 초기화"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 게임은 비활성화 상태에서 시작
        self.game_active = False

        # 최고 점수는 리셋하면 안 됨
        self.high_score = 0

    def reset_stats(self):
        """게임을 진행하는 동안 바뀔 수 있도록 기록 초기화"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
