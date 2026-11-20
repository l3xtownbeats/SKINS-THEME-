import tkinter as tk
import math

class NeonFXButton(tk.Canvas):
    """
    FX-кнопка в точном стиле макета:
    Металлическая основа, неоновая рамка, статус ON/OFF, поддержка Hover и Active.
    """
    def __init__(self, parent, text="COMP", icon_char="∿", active=True, command=None, width=96, height=52):
        super().__init__(parent, width=width, height=height, bg="#0a0c14", highlightthickness=0)
        self.width = width
        self.height = height
        self.text = text
        self.icon_char = icon_char
        self.is_active = active
        self.is_hover = False
        self.command = command

        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_click)
        self.draw()

    def _on_enter(self, e):
        self.is_hover = True
        self.draw()

    def _on_leave(self, e):
        self.is_hover = False
        self.draw()

    def _on_click(self, e):
        self.is_active = not self.is_active
        self.draw()
        if self.command:
            self.command(self.is_active)

    def draw(self):
        self.delete("all")
        w, h = self.width, self.height

        # Выбор цветовой схемы состояния
        if self.is_active:
            bg_color = "#102235"
            border_color = "#00d0ff"
            glow_color = "#005577"
            text_color = "#ffffff"
            icon_color = "#00d0ff"
            status_text = "ON"
            status_color = "#00d0ff"
        else:
            bg_color = "#121622"
            border_color = "#00d0ff" if self.is_hover else "#252d42"
            glow_color = None
            text_color = "#8b98b0"
            icon_color = "#556480"
            status_text = "OFF"
            status_color = "#414d66"

        # Внешний ореол (неоновое свечение при активности)
        if glow_color:
            self.create_rectangle(1, 1, w-1, h-1, outline=glow_color, width=3)

        # Тело кнопки (металлическая плашка)
        self.create_rectangle(3, 3, w-3, h-3, fill=bg_color, outline=border_color, width=1.5)

        # Иконка и подписи
        self.create_text(w/2, 18, text=self.icon_char, fill=icon_color, font=("Segoe UI Symbol", 13, "bold"))
        self.create_text(w/2, 33, text=self.text, fill=text_color, font=("Helvetica", 8, "bold"))
        self.create_text(w/2, 44, text=status_text, fill=status_color, font=("Helvetica", 6, "bold"))


class NeonToggle(tk.Canvas):
    """
    Миниатюрный неоновый переключатель ON/OFF.
    """
    def __init__(self, parent, state=True, command=None, width=44, height=22):
        super().__init__(parent, width=width, height=height, bg="#0a0c14", highlightthickness=0)
        self.width = width
        self.height = height
        self.state = state
        self.command = command

        self.bind("<Button-1>", self._toggle)
        self.draw()

    def _toggle(self, e):
        self.state = not self.state
        self.draw()
        if self.command:
            self.command(self.state)

    def draw(self):
        self.delete("all")
        w, h = self.width, self.height
        r = h / 2

        if self.state:
            track_fill = "#07243a"
            border_col = "#00d0ff"
            thumb_col = "#00d0ff"
            cx = w - r - 2
        else:
            track_fill = "#141822"
            border_col = "#273044"
            thumb_col = "#4a5670"
            cx = r + 2

        # Трек
        self.create_oval(1, 1, h-1, h-1, fill=track_fill, outline=border_col)
        self.create_oval(w-h+1, 1, w-1, h-1, fill=track_fill, outline=border_col)
        self.create_rectangle(r, 1, w-r, h-1, fill=track_fill, outline=track_fill)
        self.create_line(r, 1, w-r, 1, fill=border_col)
        self.create_line(r, h-1, w-r, h-1, fill=border_col)

        # Бегунок
        tr = r - 3
        self.create_oval(cx - tr, r - tr, cx + tr, r + tr, fill=thumb_col, outline="#ffffff" if self.state else "")


class CompressorDisplay(tk.Canvas):
    """
    Координатный дисплей характеристики компрессора с неоновой сеткой и кривой.
    """
    def __init__(self, parent, width=220, height=130):
        super().__init__(parent, width=width, height=height, bg="#0b101a", highlightthickness=0)
        self.width = width
        self.height = height
        self.draw()

    def draw(self):
        self.delete("all")
        w, h = self.width, self.height

        # Металлическая окантовка окна
        self.create_rectangle(1, 1, w-1, h-1, outline="#20293d", width=1.5)

        # Сетка децибел (Grid)
        for i in range(1, 5):
            x = (w / 5) * i
            y = (h / 5) * i
            self.create_line(x, 2, x, h-2, fill="#131d2e", dash=(2, 2))
            self.create_line(2, y, w-2, y, fill="#131d2e", dash=(2, 2))

        # Кривая компрессии (Неоновая передаточная линия)
        p1 = (15, h - 15)
        p_knee = (w * 0.65, h * 0.45)
        p2 = (w - 15, h * 0.25)

        # Линия
        self.create_line(p1[0], p1[1], p_knee[0], p_knee[1], fill="#00d0ff", width=2)
        self.create_line(p_knee[0], p_knee[1], p2[0], p2[1], fill="#00d0ff", width=2)

        # Точка Knee
        self.create_oval(p_knee[0]-3, p_knee[1]-3, p_knee[0]+3, p_knee[1]+3, fill="#ffffff", outline="#00d0ff")
