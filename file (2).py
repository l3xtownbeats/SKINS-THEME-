class TopHeaderBar(tk.Frame):
    """
    Верхняя системная консоль плагина:
    Логотип с короной, селектор пресетов, системный монитор и вызовы подменю.
    """
    def __init__(self, parent):
        super().__init__(parent, bg="#0e131d", padx=10, pady=6, highlightbackground="#1e293b", highlightthickness=1)
        
        # 1. Логотип
        logo_box = tk.Frame(self, bg="#0e131d")
        logo_box.pack(side="left", padx=(0, 15))
        
        tk.Label(logo_box, text="👑 PPGU", fg="#ffcc00", bg="#0e131d", font=("Helvetica", 12, "bold")).pack(side="left")
        tk.Label(logo_box, text=" | NEON STAGE", fg="#00d0ff", bg="#0e131d", font=("Helvetica", 10, "bold")).pack(side="left")

        # 2. Селектор пресетов (Preset Navigator)
        preset_box = tk.Frame(self, bg="#141a29", padx=8, pady=3, highlightbackground="#2d3748", highlightthickness=1)
        preset_box.pack(side="left", padx=10)

        tk.Label(preset_box, text="PRESET: ", fg="#64748b", bg="#141a29", font=("Helvetica", 8)).pack(side="left")
        tk.Label(preset_box, text="◀", fg="#00d0ff", bg="#141a29", font=("Helvetica", 8), cursor="hand2").pack(side="left", padx=4)
        tk.Label(preset_box, text="Pop Punk • Fast Lane", fg="#ffffff", bg="#141a29", font=("Helvetica", 9, "bold")).pack(side="left", padx=6)
        tk.Label(preset_box, text="▶", fg="#00d0ff", bg="#141a29", font=("Helvetica", 8), cursor="hand2").pack(side="left", padx=4)

        # 3. Правый блок: системные метрики и утилиты
        sys_box = tk.Frame(self, bg="#0e131d")
        sys_box.pack(side="right")

        tk.Label(sys_box, text="CPU: 3.8%  RAM: 142MB", fg="#475569", bg="#0e131d", font=("Helvetica", 8)).pack(side="left", padx=10)
        
        for name in ["SKINS", "SETTINGS", "ABOUT"]:
            btn = tk.Label(sys_box, text=name, fg="#94a3b8", bg="#141a29", font=("Helvetica", 8, "bold"),
                           padx=8, pady=3, highlightbackground="#222c3d", highlightthickness=1, cursor="hand2")
            btn.pack(side="left", padx=3)
