import sys 
import pygame

from settings import Settings
from ship     import Ship

class AlienInvasion:
    """ Classe geral do Projeto para Inicialização """

    def __init__(self):
        """ Inicia o jogo e cria os parametros iniciais """
        pygame.init()

        # Iniciando o objeto de Configurações
        self.settings = Settings()

        # Inicando o Relógio para auxiliar nos Frames
        self.clock = pygame.time.Clock() 

        # Iniciando as configurações da Tela
        self.screen = pygame.display.set_mode(
            (
                self.settings.screen_width, 
                self.settings.screen_height
            )
        )

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(ai_game=self)


    def __check_events(self):
        """ Observa Eventos do Teclado e do Mouse """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.__check_keydown_events(event=event)

            elif event.type == pygame.KEYUP:
                self.__check_keyup_events(event=event)

    def __check_keydown_events(self, event):
        """ Função para verificar os eventos de Keydown """
        if event.key in [pygame.K_RIGHT,  pygame.K_d]:
            self.ship.moving_right = True
        
        elif event.key in [pygame.K_LEFT,  pygame.K_a]:
            self.ship.moving_left = True

        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def __check_keyup_events(self, event):
        """ Função para verificar os eventos de Keyup """
        if event.key in [pygame.K_RIGHT,  pygame.K_d]:
            self.ship.moving_right = False
        
        elif event.key in [pygame.K_LEFT,  pygame.K_a]:
            self.ship.moving_left = False

    def __update_screen(self):
        """ Redesenhando a tela a cada iteração """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Deixa a tela mais recente visivel
        pygame.display.flip()

    def run_game(self):
        """ Inicia o Loop principal do jogo """
        while True:
            self.__check_events()
            self.ship.update()
            self.__update_screen()
            self.clock.tick(60)


if __name__ == "__main__":
    # Cria uma instancia do Jogo
    game = AlienInvasion()
    game.run_game()
