import tkinter as tk

class SkinCard(tk.Canvas):
    """
    Интерактивная карточка скина с превью, названием и неоновым фокусом.
    """
    def __init__(self, parent, skin_id="SKIN-1", name="NEON STAGE", is_active=False, command=None, width=95, height=75):
        super().__init__(parent, width=width, height=height, bg="#0d111a", highlightthickness=0)
        self.width = width
        self.height = height
        self.skin_id = skin_id
        self.name = name
        self.is_active = is_active
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
        if self.command:
            self.command(self.skin_id)

    def set_active(self, active):
        self.is_active = active
        self.draw()

    def draw(self):
        self.delete("all")
        w, h = self.width, self.height

        # Определение цвета рамки и фона
        if self.is_active:
            border_col = "#00d0ff"
            bg_col = "#142236"
            text_col = "#ffffff"
            glow = True
        elif self.is_hover:
            border_col = "#5075a8"
            bg_col = "#111826"
            text_col = "#d0d8e8"
            glow = False
        else:
            border_col = "#222a3d"
            bg_col = "#0e131d"
            text_col = "#7c8ca8"
            glow = False

        # Неоновое внешнее свечение при выборе
        if glow:
            self.create_rectangle(1, 1, w-1, h-1, outline="#005577", width=3)

        # Тело карточки
        self.create_rectangle(3, 3, w-3, h-3, fill=bg_col, outline=border_col, width=1.5)

        # Заглушка/превью графики скина
        self.create_rectangle(6, 6, w-6, h-26, fill="#080c14", outline="#192030")
        self.create_text(w/2, (h-20)/2, text="🎸", fill="#00d0ff" if self.is_active else "#3e4d68", font=("Segoe UI Emoji", 14))

        # Подписи ID и имени темы
        self.create_text(w/2, h-17, text=self.skin_id, fill=text_col, font=("Helvetica", 6, "bold"))
        self.create_text(w/2, h-8, text=self.name, fill=text_col, font=("Helvetica", 6))


class SkinsGalleryPanel(tk.Frame):
    """
    Модуль Skins Gallery: сетка тем оформления и управляющие кнопки Apply / Preview.
    """
    def __init__(self, parent, on_apply_callback=None):
        super().__init__(parent, bg="#101522", padx=10, pady=10, highlightbackground="#20293d", highlightthickness=1)
        self.on_apply = on_apply_callback
        self.selected_skin = "SKIN-1"
        self.cards = {}

        # 1. Заголовок и поиск
        header = tk.Frame(self, bg="#101522")
        header.pack(fill="x", pady=(0, 8))

        tk.Label(header, text="🎨 SKINS GALLERY", fg="#00d0ff", bg="#101522", font=("Helvetica", 10, "bold")).pack(side="left")

        search_box = tk.Entry(header, bg="#141a28", fg="#ffffff", insertbackground="#00d0ff",
                              font=("Helvetica", 8), width=15, relief="flat", highlightbackground="#253047", highlightthickness=1)
        search_box.insert(0, "Search Skins...")
        search_box.pack(side="right")

        # 2. Сетка скинов (4x2)
        grid_frame = tk.Frame(self, bg="#101522")
        grid_frame.pack(fill="both", expand=True)

        skins_data = [
            ("SKIN-1", "NEON STAGE"),
            ("SKIN-2", "RETRO PUNK"),
            ("SKIN-3", "DARK ROCK"),
            ("SKIN-4", "POP STYLE"),
            ("SKIN-5", "METAL CORE"),
            ("SKIN-6", "CLASSIC PUNK"),
            ("SKIN-7", "INDIE ROCK"),
            ("SKIN-8", "MINIMAL")
        ]

        for idx, (s_id, s_name) in enumerate(skins_data):
            row = idx // 4
            col = idx % 4
            card = SkinCard(grid_frame, skin_id=s_id, name=s_name,
                            is_active=(s_id == self.selected_skin), command=self._select_skin)
            card.grid(row=row, column=col, padx=3, pady=3)
            self.cards[s_id] = card

        # 3. Нижняя панель действий (Apply, Favorite, Close)
        actions = tk.Frame(self, bg="#101522")
        actions.pack(fill="x", pady=(8, 0))

        btn_fav = tk.Label(actions, text="★ Favorite", fg="#8a9ab8", bg="#151b2a",
                           font=("Helvetica", 7, "bold"), padx=6, pady=4, cursor="hand2", highlightbackground="#222c3d", highlightthickness=1)
        btn_fav.pack(side="left", padx=2)

        btn_apply = tk.Label(actions, text="✔ Apply", fg="#00d0ff", bg="#12253b",
                             font=("Helvetica", 7, "bold"), padx=10, pady=4, cursor="hand2", highlightbackground="#00d0ff", highlightthickness=1)
        btn_apply.pack(side="left", padx=2)
        btn_apply.bind("<Button-1>", lambda e: self.on_apply(self.selected_skin) if self.on_apply else None)

    def _select_skin(self, skin_id):
        self.selected_skin = skin_id
        for s_id, card in self.cards.items():
            card.set_active(s_id == skin_id)
