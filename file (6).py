class NeonVUMeter(tk.Canvas):
    """
    Многосегментный неоновый индикатор уровня (VU Meter)
    Цвета сегментов: Зеленый -> Желтый -> Оранжевый -> Красный.
    """
    def __init__(self, parent, segments=24, width=18, height=140):
        super().__init__(parent, width=width, height=height, bg="#0a0e17", highlightthickness=0)
        self.segments = segments
        self.width = width
        self.height = height
        self.level = 0.75  # Уровень от 0.0 до 1.0
        self.draw()

    def set_level(self, val):
        self.level = max(0.0, min(1.0, val))
        self.draw()

    def draw(self):
        self.delete("all")
        w, h = self.width, self.height
        pad = 2
        seg_h = (h - (self.segments * pad)) / self.segments

        active_count = int(self.level * self.segments)

        for i in range(self.segments):
            # Индекс снизу вверх
            idx = self.segments - 1 - i
            y2 = h - (i * (seg_h + pad))
            y1 = y2 - seg_h

            # Определение цвета градиента шкалы
            ratio = i / self.segments
            if ratio < 0.6:
                base_color = "#00ff77"  # Green
                glow = "#005522"
            elif ratio < 0.8:
                base_color = "#ffdd00"  # Yellow
                glow = "#554400"
            elif ratio < 0.92:
                base_color = "#ff8800"  # Orange
                glow = "#552a00"
            else:
                base_color = "#ff1144"  # Red peak
                glow = "#550011"

            if i < active_count:
                # Включенный сегмент с ярким свечением
                self.create_rectangle(2, y1, w-2, y2, fill=base_color, outline=base_color)
            else:
                # Погашенный фоновый сегмент
                self.create_rectangle(2, y1, w-2, y2, fill="#121722", outline="#1c2436")
