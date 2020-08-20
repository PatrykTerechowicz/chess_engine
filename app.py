from sys import exit
from tkinter import *
from pathlib import Path
from gui_board import Board
import res.resource_manager


def exit_popup():
    sys.exit(0)


class App:
    def __init__(self):
        self.top_frame = Tk()
        self.top_frame.title("Chess Game")
        self.top_frame.geometry("200x100")
        self.create_main_menu()
        self.is_game_started = False

    def create_new_game(self):
        if self.is_game_started:
            self.game_already_started_popup()
            return
        new_window = Toplevel(self.top_frame)
        new_window.title("Gra człowiek kontra komputer")
        new_window.geometry("450x450")
        Board(new_window).pack(expand=YES, fill=BOTH)
        new_window.mainloop()

    def game_already_started_popup(self):
        pass

    def open_options_menu(self):
        pass

    def create_main_menu(self):
        img = PhotoImage()
        label = Label(self.top_frame)
        label['text'] = "Szachy by patryk"
        label.pack()
        Button(text="New Game", command=self.create_new_game).pack(fill=BOTH)
        Button(text="Options", command=self.open_options_menu).pack(fill=BOTH)
        Button(text="Exit", command=exit_popup).pack(fill=BOTH)

    def start(self):
        self.top_frame.mainloop()


if __name__ == '__main__':
    application = App()
    application.start()
