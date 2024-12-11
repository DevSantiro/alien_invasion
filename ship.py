import pygame


class Ship:
    """ Classe para gerenciar a espaçonave """

    def __init__(self, ai_game):
        """Iniciando a espaçonave e definindo as suas posições."""
        self.screen      = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Sobe a Imagem.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect  = self.image.get_rect()

        # Começa cada espaçonave nova no centro inferior da tela.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Desenha a espaçonave na sua localização atual"""
        self.screen.blit(self.image, self.rect)