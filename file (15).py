"""
NEON STAGE MANAGER 3.0 - UI ASSET LOADER & CONTROLLER ENGINE
Target Framework: Python 3.8+ / Tkinter + Pillow (PIL)
Strict reference: Approved PPGU / Neon Stage Mockup
"""

import tkinter as tk
from PIL import Image, ImageTk
import json
import math

class SpriteSheetLoader:
    """Универсальный нарезчик спрайт-листов на отдельные кадры"""
    @staticmethod
    def slice_horizontal(image_path, frame_w, frame_h, total_frames, y_offset=0, x_offset=0):
        sheet = Image.open(image_path).convert("RGBA")
        frames = []
        for i in range(total_frames):
            box = (x_offset + i * frame_w, y_offset, x_offset + (i + 1) * frame_w, y_offset + frame_h)
            frames.append(sheet.crop(box))
        return frames

    @staticmethod
    def slice_grid(image_path, cell_w, cell_h, cols, rows, start_x=0, start_y=0):
        sheet = Image.open(image_path).convert("RGBA")
        grid = []
        for r in range(rows):
            row_frames = []
            for c in range(cols):
                box = (start_x + c * cell_w, start_y + r * cell_h,
                       start_x + (c + 1) * cell_w, start_y + (r + 1) * cell_h)
                row_frames.append(sheet.crop(box))
            grid.append(row_frames)
        return grid


class NeonKnob(tk.Canvas):
    """
    Интерактивный поворотный регулятор на основе спрайт-листа (11 кадров: 0% - 100%).
    Управление: зажать левую кнопку мыши и тянуть вверх/вниз для изменения значения.
    """
    def __init__(self, parent, frames, default_val=0.5, name="KNOB", command=None, size=(120, 120)):
        super().__init__(parent, width=size[0], height=size[1] + 25, bg="#12141A", highlightthickness=0)
        self.raw_frames = frames
        self.tk_frames = [ImageTk.PhotoImage(f.resize(size, Image.Resampling.LANCZOS)) for f in frames]
        self.num_frames = len(frames)
        self.value = default_val  # 0.0 to 1.0
        self.command = command
        self.name = name
        self.size = size

        self.last_y = 0
        self.bind("<Button-1>", self._on_press)
        self.bind("<B1-Motion>", self._on_drag)

        self._render()

    def _render(self):
        self.delete("all")
        frame_idx = int(round(self.value * (self.num_frames - 1)))
        frame_idx = max(0, min(self.num_frames - 1, frame_idx))
        
        # Отрисовка ручки
        self.create_image(self.size[0] // 2, self.size[1] // 2, image=self.tk_frames[frame_idx])
        # Текстовый заголовок
        self.create_text(self.size[0] // 2, self.size[1] + 10, text=self.name, fill="#8892B0", font=("Arial", 9, "bold"))

    def _on_press(self, event):
        self.last_y = event.y

    def _on_drag(self, event):
        delta = self.last_y - event.y
        self.last_y = event.y
        # Чувствительность регулятора
        self.value = max(0.0, min(1.0, self.value + delta * 0.008))
        self._render()
        if self.command:
            self.command(self.value)


class NeonButton(tk.Canvas):
    """
    Модульная кнопка с 5 состояниями: Normal, Hover, Pressed, Active (Glow), Disabled
    """
    def __init__(self, parent, state_images, command=None, size=(140, 60), is_toggle=True):
        super().__init__(parent, width=size[0], height=size[1], bg="#12141A", highlightthickness=0)
        # state_images: dict {'normal', 'hover', 'pressed', 'active', 'disabled'}
        self.tk_states = {k: ImageTk.PhotoImage(v.resize(size, Image.Resampling.LANCZOS)) for k, v in state_images.items()}
        self.is_active = False
        self.is_toggle = is_toggle
        self.command = command
        self.current_state = "normal"

        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

        self._render()

    def _render(self):
        self.delete("all")
        img = self.tk_states.get(self.current_state, self.tk_states["normal"])
        self.create_image(self.winfo_reqwidth() // 2, self.winfo_reqheight() // 2, image=img)

    def _on_enter(self, e):
        if not self.is_active:
            self.current_state = "hover"
            self._render()

    def _on_leave(self, e):
        self.current_state = "active" if self.is_active else "normal"
        self._render()

    def _on_press(self, e):
        self.current_state = "pressed"
        self._render()

    def _on_release(self, e):
        if self.is_toggle:
            self.is_active = not self.is_active
            self.current_state = "active" if self.is_active else "normal"
        else:
            self.current_state = "normal"
        self._render()
        if self.command:
            self.command(self.is_active)


class NeonRadar(tk.Canvas):
    """Анимированный круговой радар Auto Discover на основе спрайта (8 кадров)"""
    def __init__(self, parent, frames, size=(100, 100), fps=12):
        super().__init__(parent, width=size[0], height=size[1], bg="#12141A", highlightthickness=0)
        self.tk_frames = [ImageTk.PhotoImage(f.resize(size, Image.Resampling.LANCZOS)) for f in frames]
        self.current_frame = 0
        self.delay_ms = int(1000 / fps)
        self.is_running = True
        self._animate()

    def _animate(self):
        if not self.is_running:
            return
        self.delete("all")
        self.create_image(self.winfo_reqwidth() // 2, self.winfo_reqheight() // 2, image=self.tk_frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.tk_frames)
        self.after(self.delay_ms, self._animate)
