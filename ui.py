import customtkinter as ctk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD


class TelemetryToolkitApp(TkinterDnD.DnDWrapper, ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title("Telemetry Toolkit Pro v1.1")
        self.geometry("1200x800")

        self.build_ui()

    def build_ui(self):

        # -------------------------
        # Title
        # -------------------------

        title = ctk.CTkLabel(
            self,
            text="Telemetry Toolkit Pro",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(pady=(20, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Professional Telemetry Analysis Toolkit",
            font=("Segoe UI", 16)
        )
        subtitle.pack()

        # -------------------------
        # JSON Textbox
        # -------------------------

        self.json_box = ctk.CTkTextbox(
            self,
            width=1100,
            height=520
        )

        self.json_box.pack(padx=20, pady=20, fill="both", expand=True)

        # Enable Drag & Drop

        self.json_box.drop_target_register(DND_FILES)
        self.json_box.dnd_bind("<<Drop>>", self.drop_json)

        # -------------------------
        # Buttons
        # -------------------------

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)

        self.paste_button = ctk.CTkButton(
            button_frame,
            text="Paste JSON",
            command=self.paste_json,
            width=150
        )
        self.paste_button.grid(row=0, column=0, padx=10)

        self.open_button = ctk.CTkButton(
            button_frame,
            text="Open JSON",
            command=self.open_json,
            width=150
        )
        self.open_button.grid(row=0, column=1, padx=10)

        self.convert_button = ctk.CTkButton(
            button_frame,
            text="Convert to Excel",
            width=180
        )
        self.convert_button.grid(row=0, column=2, padx=10)

        self.clear_button = ctk.CTkButton(
            button_frame,
            text="Clear",
            command=self.clear_json,
            width=150
        )
        self.clear_button.grid(row=0, column=3, padx=10)

        # -------------------------
        # Status
        # -------------------------

        self.status = ctk.CTkLabel(
            self,
            text="Ready",
            anchor="w"
        )

        self.status.pack(fill="x", padx=20, pady=(10, 20))

    # ==========================================================
    # BUTTON FUNCTIONS
    # ==========================================================

    def paste_json(self):

        try:

            clipboard = self.clipboard_get()

            self.json_box.delete("1.0", "end")
            self.json_box.insert("1.0", clipboard)

            self.status.configure(
                text="JSON pasted from clipboard."
            )

        except Exception as e:

            self.status.configure(
                text=f"Paste failed: {e}"
            )

    def open_json(self):

        filename = filedialog.askopenfilename(
            title="Open JSON File",
            filetypes=[("JSON Files", "*.json")]
        )

        if not filename:
            return

        try:

            with open(filename, "r", encoding="utf-8") as file:
                text = file.read()

            self.json_box.delete("1.0", "end")
            self.json_box.insert("1.0", text)

            self.status.configure(
                text=f"Loaded: {filename}"
            )

        except Exception as e:

            self.status.configure(
                text=f"Error: {e}"
            )

    def drop_json(self, event):

        filename = event.data.strip("{}")

        try:

            with open(filename, "r", encoding="utf-8") as file:
                text = file.read()

            self.json_box.delete("1.0", "end")
            self.json_box.insert("1.0", text)

            self.status.configure(
                text=f"Dropped: {filename}"
            )

        except Exception as e:

            self.status.configure(
                text=f"Error: {e}"
            )

    def clear_json(self):

        self.json_box.delete("1.0", "end")

        self.status.configure(
            text="Ready"
        )