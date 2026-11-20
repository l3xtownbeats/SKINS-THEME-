class FullFXChainBar(tk.Frame):
    """
    Горизонтальная шина эффектов:
    Compressor -> EQ -> Distortion -> Chorus -> Delay -> Reverb -> Cabinet IR
    """
    def __init__(self, parent):
        super().__init__(parent, bg="#0e131e", padx=6, pady=6, highlightbackground="#1e273a", highlightthickness=1)

        tk.Label(self, text="FX CHAIN", fg="#00d0ff", bg="#0e131e", font=("Helvetica", 9, "bold")).pack(side="left", padx=8)

        effects = [
            ("COMP", "∿", True),
            ("EQ", "ılı", True),
            ("DIST", "⚡", True),
            ("CHORUS", "≈", False),
            ("DELAY", "🕒", False),
            ("REVERB", "⬡", True),
            ("CABINET", "⧈", True)
        ]

        self.buttons = []
        for name, icon, act in effects:
            btn = NeonFXButton(self, text=name, icon_char=icon, active=act, width=82, height=46)
            btn.pack(side="left", padx=3)
            self.buttons.append(btn)
