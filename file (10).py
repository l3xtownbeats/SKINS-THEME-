import tkinter as tk
import math

class NeonKnob(tk.Canvas):
    """
    Кастомный регулятор в стиле Neon Stage:
    Металлический корпус, индикаторная риска и круговая неоновая шкала.
    """
    def __init__(self, parent, size=60, min_val=0, max_val=100, initial=50, glow_color="#00d0ff", **kwargs):
        super().__init__(parent, width=size, height=size, bg="#10141f", highlightthickness=0, **kwargs)
        self.size = size
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial
        self.glow_color = glow_color
        
        self.bind("<B1-Motion>", self._on_drag)
        self.bind("<Button-1>", self._on_click)
        self._last_y = 0
        self.draw()

    def _on_click(self, event):
        self._last_y = event.y

    def _on_drag(self, event):
        delta = self._last_y - event.y
        self._last_y = event.y
        step = (self.max_val - self.min_val) / 100.0
        self.value = max(self.min_val, min(self.max_val, self.value + delta * step))
        self.draw()

    def draw(self):
        self.delete("all")
        cx, cy = self.size / 2, self.size / 2
        r = self.size * 0.42

        # 1. Фоновая кольцевая дуга
        self.create_arc(cx-r, cy-r, cx+r, cy+r, start=-45, extent=270,
                        style=tk.ARC, outline="#1e2538", width=4)

        # 2. Активная неоновая дуга
        ratio = (self.value - self.min_val) / (self.max_val - self.min_val)
        extent = -270 * ratio
        self.create_arc(cx-r, cy-r, cx+r, cy+r, start=225, extent=extent,
                        style=tk.ARC, outline=self.glow_color, width=4)

        # 3. Металлическая головка регулятора
        kr = r * 0.78
        self.create_oval(cx-kr, cy-kr, cx+kr, cy+kr, fill="#222838", outline="#414c66", width=2)
        self.create_oval(cx-kr+3, cy-kr+3, cx+kr-3, cy+kr-3, fill="#181d29", outline="")

        # 4. Риска положения
        angle = math.radians(225 - 270 * ratio)
        ix1 = cx + (kr * 0.3) * math.cos(angle)
        iy1 = cy - (kr * 0.3) * math.sin(angle)
        ix2 = cx + (kr * 0.85) * math.cos(angle)
        iy2 = cy - (kr * 0.85) * math.sin(angle)
        self.create_line(ix1, iy1, ix2, iy2, fill="#ffffff", width=2)
