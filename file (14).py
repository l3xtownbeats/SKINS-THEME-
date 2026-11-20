class NeonStageUltimate(tk.Tk):
    """
    Полная рабочая версия интерфейса NEON STAGE MANAGER 3.0.
    """
    def __init__(self):
        super().__init__()
        self.title("NEON STAGE MANAGER 3.0 - POP PUNK GUITAR ULTIMATE")
        self.geometry("1180, 780")
        self.configure(bg="#07090f")
        self.resizable(False, False)

        self.state = AppState()

        # 1. Верхняя панель (Header Console)
        self.header = TopHeaderBar(self)
        self.header.pack(fill="x", padx=8, pady=(8, 4))

        # 2. Центральная сетка (Left: AutoChords | Center: FX Edit | Right: Amp & Settings)
        main_workspace = tk.Frame(self, bg="#07090f")
        main_workspace.pack(fill="both", expand=True, padx=8, pady=4)

        # Левая колонка: AutoChords
        left_col = tk.Frame(main_workspace, bg="#07090f")
        left_col.pack(side="left", fill="y", padx=(0, 6))

        chord_box = tk.Frame(left_col, bg="#101522", padx=8, pady=8, highlightbackground="#20293d", highlightthickness=1)
        chord_box.pack(fill="x", pady=(0, 6))
        tk.Label(chord_box, text="♫ AUTOCHORDS", fg="#00d0ff", bg="#101522", font=("Helvetica", 9, "bold")).pack(anchor="w")
        self.fretboard = AutoChordsFretboard(chord_box)
        self.fretboard.pack(pady=4)

        # Центральная колонка: FX Edit
        self.fx_edit = FXEditModule(main_workspace)
        self.fx_edit.pack(side="left", fill="both", expand=True, padx=(0, 6))

        # Правая колонка: Amp & Tone
        right_col = tk.Frame(main_workspace, bg="#07090f")
        right_col.pack(side="left", fill="y")
        self.amp_tone = AmpToneModule(right_col)
        self.amp_tone.pack(fill="x")

        # 3. Горизонтальная шина FX Chain
        self.fx_chain = FullFXChainBar(self)
        self.fx_chain.pack(fill="x", padx=8, pady=(2, 4))

        # 4. Нижняя секция: Клавиатура фортепиано
        bottom_rack = tk.Frame(self, bg="#07090f", pady=4)
        bottom_rack.pack(fill="x", padx=8, pady=(0, 8))
        self.piano = NeonPianoKeyboard(bottom_rack, octaves=5, white_w=20, white_h=80)
        self.piano.pack(anchor="center")

if __name__ == "__main__":
    app = NeonStageUltimate()
    app.mainloop()
