class AutoChordsFretboard(tk.Canvas):
    """
    Индикатор гитарного грифа с точками зажатия струн (Chord Diagram) в неоновом стиле.
    """
    def __init__(self, parent, width=130, height=110):
        super().__init__(parent, width=width, height=height, bg="#0d121c", highlightthickness=0)
        self.width = width
        self.height = height
        self.draw()

    def draw(self, chord_name="A Maj", frets=[0, 0, 2, 2, 2, 0]):
        self.delete("all")
        w, h = self.width, self.height
        
        # Заголовок аккорда
        self.create_text(w/2, 14, text=chord_name, fill="#00d0ff", font=("Helvetica", 11, "bold"))
        
        # Сетка грифа (6 струн, 4 лада)
        gx1, gy1 = 20, 30
        gx2, gy2 = w - 20, h - 14
        num_strings = 6
        num_frets = 4
        
        dx = (gx2 - gx1) / (num_strings - 1)
        dy = (gy2 - gy1) / num_frets

        # Нулевой порожек (Nut)
        self.create_line(gx1, gy1, gx2, gy1, fill="#4a5568", width=3)

        # Ладовые проволоки
        for i in range(1, num_frets + 1):
            y = gy1 + i * dy
            self.create_line(gx1, y, gx2, y, fill="#222c3d", width=1)

        # Струны
        for i in range(num_strings):
            x = gx1 + i * dx
            self.create_line(x, gy1, x, gy2, fill="#334155", width=1.2)

        # Точки зажатия (Dots)
        for string_idx, fret in enumerate(frets):
            x = gx1 + string_idx * dx
            if fret > 0:
                y = gy1 + (fret - 0.5) * dy
                # Неоновая светящаяся точка
                self.create_oval(x-4, y-4, x+4, y+4, fill="#00d0ff", outline="#ffffff", width=1)
            elif fret == 0:
                # Открытая струна 'O'
                self.create_text(x, gy1 - 6, text="○", fill="#64748b", font=("Helvetica", 7))
