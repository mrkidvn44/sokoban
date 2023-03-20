import pygame
import constants as SOKOBAN

class PlayerInterface:
    def __init__(self, player, level):
        self.player = player
        self.level = level
        self.mouse_pos = (-1,-1)
        self.font_menu = pygame.font.Font('assets/fonts/FreeSansBold.ttf', 18)
        self.txtLevel = "Level 1"
        self.colorTxtLevel = SOKOBAN.BLACK
        self.txtCancel = "Undo the last move"
        self.colorTxtCancel = SOKOBAN.GREY
        self.txtReset = "Restart level"
        self.colorTxtReset = SOKOBAN.BLACK
        self.txtAutoDFS = "Auto DFS"
        self.colorTxtAutoDFS = SOKOBAN.BLACK
        self.txtAutoBFS = "Auto BFS"
        self.colorTxtAutoBSF = SOKOBAN.BLACK
        self.txtAutoUCS = "Auto UCS"
        self.colorTxtAutoUCS = SOKOBAN.BLACK
        self.txtAutoALL = "Auto ALL"
        self.colorTxtAutoALL = SOKOBAN.BLACK

    def click(self, pos_click, level, game):
        x = pos_click[0]
        y = pos_click[1]

        # Cancel last move
        if x > self.posTxtCancel[0] and x < self.posTxtCancel[0] + self.txtCancelSurface.get_width() \
         and y > self.posTxtCancel[1] and y < self.posTxtCancel[1] + self.txtCancelSurface.get_height():
            level.cancel_last_move(self.player, self)
            self.colorTxtCancel = SOKOBAN.GREY

        # Reset level
        if x > self.posTxtReset[0] and x < self.posTxtReset[0] + self.txtResetSurface.get_width() \
        and y > self.posTxtReset[1] and y < self.posTxtReset[1] + self.txtResetSurface.get_height():
            game.load_level()
            
        # Auto play DFS
        if x > self.posTxtAutoDFS[0] and x < self.posTxtAutoDFS[0] + self.txtAutoSurface.get_width() \
        and y > self.posTxtAutoDFS[1] and y < self.posTxtAutoDFS[1] + self.txtAutoSurface.get_height():
            game.auto_move_DFS()

        # Auto play BFS
        if x > self.posTxtAutoBFS[0] and x < self.posTxtAutoBFS[0] + self.txtAutoSurface.get_width() \
        and y > self.posTxtAutoBFS[1] and y < self.posTxtAutoBFS[1] + self.txtAutoSurface.get_height():
            game.auto_move_BFS()

        # Auto play UCS
        if x > self.posTxtAutoUCS[0] and x < self.posTxtAutoUCS[0] + self.txtAutoSurface.get_width() \
        and y > self.posTxtAutoUCS[1] and y < self.posTxtAutoUCS[1] + self.txtAutoSurface.get_height():
            game.auto_move_UCS()

            # Auto play UCS
        if x > self.posTxtAutoALL[0] and x < self.posTxtAutoALL[0] + self.txtAutoSurface.get_width() \
        and y > self.posTxtAutoALL[1] and y < self.posTxtAutoALL[1] + self.txtAutoSurface.get_height():
            game.auto_move_all()

    def setTxtColors(self):
        pass

    def render(self, window, level):
        self.txtLevel = "Level " + str(level)
        self.txtLevelSurface = self.font_menu.render(self.txtLevel, True, self.colorTxtLevel, SOKOBAN.WHITE)
        window.blit(self.txtLevelSurface, (10, 10))

        self.txtCancelSurface = self.font_menu.render(self.txtCancel, True, self.colorTxtCancel, SOKOBAN.WHITE)
        self.posTxtCancel = (SOKOBAN.WINDOW_WIDTH - self.txtCancelSurface.get_width() - 10, 10)
        window.blit(self.txtCancelSurface, self.posTxtCancel)

        self.txtResetSurface = self.font_menu.render(self.txtReset, True, self.colorTxtReset, SOKOBAN.WHITE)
        self.posTxtReset = ((SOKOBAN.WINDOW_WIDTH / 2) - (self.txtResetSurface.get_width() / 2), 10)
        window.blit(self.txtResetSurface, self.posTxtReset)

        self.txtAutoSurface = self.font_menu.render(self.txtAutoDFS, True, self.colorTxtAutoDFS, SOKOBAN.WHITE)
        self.posTxtAutoDFS = ((SOKOBAN.WINDOW_WIDTH - self.txtAutoSurface.get_width()) - 10, 30)
        window.blit(self.txtAutoSurface, self.posTxtAutoDFS)

        self.txtAutoSurface = self.font_menu.render(self.txtAutoBFS, True, self.colorTxtAutoBSF, SOKOBAN.WHITE)
        self.posTxtAutoBFS = ((SOKOBAN.WINDOW_WIDTH - self.txtAutoSurface.get_width()) - 10, 50)
        window.blit(self.txtAutoSurface, self.posTxtAutoBFS)

        self.txtAutoSurface = self.font_menu.render(self.txtAutoUCS, True, self.colorTxtAutoUCS, SOKOBAN.WHITE)
        self.posTxtAutoUCS = ((SOKOBAN.WINDOW_WIDTH - self.txtAutoSurface.get_width()) - 10, 70)
        window.blit(self.txtAutoSurface, self.posTxtAutoUCS)

        self.txtAutoSurface = self.font_menu.render(self.txtAutoALL, True, self.colorTxtAutoALL, SOKOBAN.WHITE)
        self.posTxtAutoALL = ((SOKOBAN.WINDOW_WIDTH - self.txtAutoSurface.get_width()) - 10, 90)
        window.blit(self.txtAutoSurface, self.posTxtAutoALL)