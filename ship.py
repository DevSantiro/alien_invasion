import pygame

class Ship:
    """ Classe para gerenciar a espaçonave """

    def __init__(self, ai_game):
        """Iniciando a espaçonave e definindo as suas posições."""
        self.screen      = ai_game.screen
        self.settings    = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Sobe a Imagem.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect  = self.image.get_rect()

        # Começa cada espaçonave nova no centro inferior da tela.
        self.rect.midbottom = self.screen_rect.midbottom

        # Eixo "x" da Nave
        self.x = float(self.rect.x)

        # Flags de movimento da Nave
        self.moving_left  = False
        self.moving_right = False

    def update(self):
        """ Atualiza o movimento da Nave """

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # Atualiza o objecto de localização da Nave
        self.rect.x = self.x

    def blitme(self):
        """Desenha a espaçonave na sua localização atual"""
        self.screen.blit(self.image, self.rect)