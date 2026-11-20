class NeonPianoKeyboard(tk.Canvas):
    """
    Клавиатура с белыми и черными клавишами, неоновой подсветкой нажатий
    и отражением света на клавишах в стиле Neon Stage.
    """
    def __init__(self, parent, octaves=3, start_octave=2, white_w=20, white_h=90, black_w=12, black_h=56):
        total_white = octaves * 7
        width = total_white * white_w
        super().__init__(parent, width=width, height=white_h + 6, bg="#080b12", highlightthickness=0)
        
        self.octaves = octaves
        self.white_w = white_w
        self.white_h = white_h
        self.black_w = black_w
        self.black_h = black_h
        self.active_keys = set()  # Множество нажатых нот
        
        # Разметка нот в октаве
        self.white_indices = [0, 2, 4, 5, 7, 9, 11]
        self.black_offsets = {1: 0, 3: 1, 6: 3, 8: 4, 10: 5} # Позиция относительно белых клавиш

        self.bind("<Button-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.draw()

    def _on_press(self, event):
        # Определение нажатой клавиши
        note = self._get_note_at(event.x, event.y)
        if note is not None:
            self.active_keys.add(note)
            self.draw()

    def _on_release(self, event):
        self.active_keys.clear()
        self.draw()

    def _get_note_at(self, x, y):
        # 1. Проверка черных клавиш (приоритет по глубине)
        if y <= self.black_h:
            for oct in range(self.octaves):
                for semi, white_idx in self.black_offsets.items():
                    bx = (oct * 7 + white_idx + 1) * self.white_w - (self.black_w / 2)
                    if bx <= x <= bx + self.black_w:
                        return oct * 12 + semi
        # 2. Проверка белых клавиш
        white_col = int(x // self.white_w)
        if 0 <= white_col < self.octaves * 7:
            oct = white_col // 7
            rel = white_col % 7
            return oct * 12 + self.white_indices[rel]
        return None

    def draw(self):
        self.delete("all")
        
        # 1. Отрисовка белых клавиш
        white_col = 0
        for oct in range(self.octaves):
            for rel in range(7):
                note = oct * 12 + self.white_indices[rel]
                x1 = white_col * self.white_w
                y1 = 2
                x2 = x1 + self.white_w
                y2 = self.white_h

                is_pressed = note in self.active_keys
                fill_color = "#18324f" if is_pressed else "#e2e8f0"
                outline_col = "#00d0ff" if is_pressed else "#64748b"

                # Корпус белой клавиши
                self.create_rectangle(x1+1, y1, x2-1, y2, fill=fill_color, outline=outline_col)
                
                # Неоновое свечение снизу активной клавиши
                if is_pressed:
                    self.create_rectangle(x1+1, y2-8, x2-1, y2, fill="#00d0ff", outline="")
                else:
                    self.create_rectangle(x1+2, y2-4, x2-2, y2, fill="#94a3b8", outline="")

                white_col += 1

        # 2. Отрисовка черных клавиш (поверх белых)
        for oct in range(self.octaves):
            for semi, white_idx in self.black_offsets.items():
                note = oct * 12 + semi
                bx = (oct * 7 + white_idx + 1) * self.white_w - (self.black_w / 2)
                is_pressed = note in self.active_keys

                fill_col = "#00d0ff" if is_pressed else "#121620"
                border_col = "#ffffff" if is_pressed else "#2d3748"

                self.create_rectangle(bx, 2, bx + self.black_w, self.black_h, fill=fill_col, outline=border_col)
                if not is_pressed:
                    # Металлическая фаска на черной клавише
                    self.create_line(bx+2, self.black_h-4, bx + self.black_w-2, self.black_h-4, fill="#3b465c")
