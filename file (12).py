class NeonCheckBox(tk.Canvas):
    """
    Неоновый чекбокс с галочкой.
    """
    def __init__(self, parent, text="", checked=True, command=None, size=16):
        super().__init__(parent, width=size + 140, height=size + 4, bg="#101522", highlightthickness=0)
        self.size = size
        self.text = text
        self.checked = checked
        self.command = command

        self.bind("<Button-1>", self._toggle)
        self.draw()

    def _toggle(self, e):
        self.checked = not self.checked
        self.draw()
        if self.command:
            self.command(self.checked)

    def draw(self):
        self.delete("all")
        s = self.size
        # Квадрат чекбокса
        box_bg = "#0f2336" if self.checked else "#131824"
        border_col = "#00d0ff" if self.checked else "#2a354c"
        
        self.create_rectangle(2, 2, s+2, s+2, fill=box_bg, outline=border_col, width=1.5)

        # Галочка
        if self.checked:
            self.create_line(4, s/2 + 2, s/2 + 1, s, fill="#00d0ff", width=2)
            self.create_line(s/2 + 1, s, s, 4, fill="#00d0ff", width=2)

        # Подпись
        self.create_text(s + 12, s/2 + 2, text=self.text, fill="#c0cce0", font=("Helvetica", 8), anchor="w")


class SettingsModule(tk.Frame):
    """
    Панель настроек (General, Audio, MIDI, GUI, Buffer Size, ECO Profile).
    """
    def __init__(self, parent):
        super().__init__(parent, bg="#101522", padx=12, pady=10, highlightbackground="#20293d", highlightthickness=1)

        # 1. Заголовок с табами
        header = tk.Frame(self, bg="#101522")
        header.pack(fill="x", pady=(0, 10))

        tk.Label(header, text="⚙ SETTINGS", fg="#00d0ff", bg="#101522", font=("Helvetica", 10, "bold")).pack(side="left", padx=(0, 10))

        for tab_name, active in [("General", True), ("Audio", False), ("MIDI", False), ("GUI", False)]:
            t_col = "#ffffff" if active else "#6b7c99"
            t_bg = "#19283d" if active else "#141926"
            t_bd = "#00d0ff" if active else "#252e42"
            tab = tk.Label(header, text=tab_name, fg=t_col, bg=t_bg, font=("Helvetica", 7, "bold"),
                           padx=6, pady=2, highlightbackground=t_bd, highlightthickness=1, cursor="hand2")
            tab.pack(side="left", padx=2)

        # 2. Опции чекбоксов
        body = tk.Frame(self, bg="#101522")
        body.pack(fill="both", expand=True)

        left_opts = tk.Frame(body, bg="#101522")
        left_opts.pack(side="left", fill="y", padx=(0, 15))

        NeonCheckBox(left_opts, text="Enable MIDI Learn", checked=True).pack(anchor="w", pady=2)
        NeonCheckBox(left_opts, text="Enable Tooltips", checked=True).pack(anchor="w", pady=2)
        NeonCheckBox(left_opts, text="Auto Save Presets", checked=True).pack(anchor="w", pady=2)
        NeonCheckBox(left_opts, text="High Quality Graphics", checked=True).pack(anchor="w", pady=2)

        # 3. Параметры выпадающих списков
        right_opts = tk.Frame(body, bg="#101522")
        right_opts.pack(side="left", fill="both", expand=True)

        self._add_dropdown_row(right_opts, "UI Scale", "100%")
        self._add_dropdown_row(right_opts, "Buffer Size", "512")
        self._add_dropdown_row(right_opts, "ECO Profile", "Normal")

        # 4. Кнопка сброса
        reset_btn = tk.Label(self, text="↺ Reset to Default", fg="#7889a8", bg="#131926",
                             font=("Helvetica", 7, "bold"), pady=4, highlightbackground="#252f44", highlightthickness=1, cursor="hand2")
        reset_btn.pack(fill="x", pady=(10, 0))

    def _add_dropdown_row(self, parent, label_text, val_text):
        row = tk.Frame(parent, bg="#101522")
        row.pack(fill="x", pady=2)
        tk.Label(row, text=label_text, fg="#8b9bb8", bg="#101522", font=("Helvetica", 7)).pack(side="left")
        val = tk.Label(row, text=f"{val_text} ▾", fg="#00d0ff", bg="#141a29", font=("Helvetica", 7, "bold"),
                       padx=6, pady=2, highlightbackground="#253047", highlightthickness=1)
        val.pack(side="right")
