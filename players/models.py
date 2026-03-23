from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=128, verbose_name="Никнейм")
    steam_id = models.CharField(max_length=64, unique=True, verbose_name="Steam ID")
    games_played = models.IntegerField(default=0, verbose_name="Игр сыграно")
    wins = models.IntegerField(default=0, verbose_name="Побед")

    def winrate(self):
        if self.games_played == 0:
            return 0
        return round(self.wins / self.games_played * 100, 2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"
        db_table = "players"
