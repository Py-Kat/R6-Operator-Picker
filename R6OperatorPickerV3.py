import tkinter as tk
from random import choice

# MAIN WINDOW
window = tk.Tk()
window.title("R6 Operator Picker! v3.0!")
window.geometry("1280x720")
window.resizable(True, True)
window.configure(bg="black")
default_color = "grey"


# COMMANDS
def choose_attacker():
    attacker = choice([
        "Glaz",
        "Fuze",
        "IQ",
        "Blitz",
        "Twitch",
        "Montagne",
        "Thermite",
        "Ash",
        "Thatcher",
        "Sledge",
        "Buck",
        "Blackbeard",
        "Capitão",
        "Hibana",
        "Jackal",
        "Ying",
        "Zofia",
        "Dokkaebi",
        "Finka",
        "Lion",
        "Maverick",
        "Nomad",
        "Gridlock",
        "Nøkk",
        "Amaru",
        "Kali",
        "Iana",
        "Ace",
        "Zero",
        "Flores",
        "Osa",
        "Sens",
        "Grim",
        "Brava",
        "Ram",
        "Deimos",
        "Striker",
        "Rauora"
    ])
    global default_color
    default_color = "red"
    op_label.config(fg=default_color)
    random_operator.set(f"YOUR ATTACKER IS: \n\n{attacker} !")
    return


def choose_defender():
    defender = choice([
        "Kapkan",
        "Tachanka",
        "Bandit",
        "Jäger",
        "Rook",
        "Doc",
        "Pulse",
        "Castle",
        "Smoke",
        "Mute",
        "Frost",
        "Valkyrie",
        "Caveira",
        "Echo",
        "Mira",
        "Lesion",
        "Ela",
        "Vigil",
        "Alibi",
        "Maestro",
        "Clash",
        "Kaid",
        "Mozzie",
        "Warden",
        "Goyo",
        "Wamai",
        "Oryx",
        "Melusi",
        "Aruni",
        "Thunderbird",
        "Thorn",
        "Azami",
        "Solis",
        "Fenrir",
        "Tubarão",
        "Sentry",
        "Skopós",
        "Denari"
    ])
    global default_color
    default_color = "blue"
    op_label.config(fg=default_color)
    random_operator.set(f"YOUR DEFENDER IS: \n\n{defender} !")
    return


def reset_text():
    global default_color
    default_color = "grey"
    op_label.config(fg=default_color)
    random_operator.set("Press a button!")
    return


def show_changelogs():
    changelog_window = tk.Toplevel(window)
    changelog_window.title("R6 Operator Picker ChangeLogs!")
    changelog_window.geometry("840x420")
    changelog_window.resizable(False, False)
    changelog_window.configure(bg="black")
    changes_label = tk.Label(
        changelog_window,
        text=
        """
        v1.0 - First Version Done! - 7/19/25
        \n\nv1.0.1 - Made code more readable and reformatted some text! - 8/21/25
        \n\nv2.0 - Completely rewrote the script and added more text styling with colorama! - 8/22/25
        \n\nv3.0 - Completely rewrote the script again to instead use a full GUI with tkinter! - 9/17/25""",
        font=("Helvetica", 14),
    )
    changes_label.config(
        bg="black",
        fg="purple"
    )
    changes_label.place(
        relx=0.5,
        rely=0.05,
        anchor="n"
    )
    info_label = tk.Label(
        changelog_window,
        text=
        """
        Please report any issues you encounter or suggestions you have in the GitHub repository.
        \nOr message directly on Discord @helvetika! ( May need to request first! )""",
        font=("Helvetica", 10),
    )
    info_label.config(
        bg="black",
        fg="red"
    )
    info_label.place(
        relx=0.5,
        rely=0.85,
        anchor="s"
    )
    close_logs_button = tk.Button(
        changelog_window,
        text="Close Changelogs",
        command=changelog_window.destroy,
        font=("Helvetica", 14),
    )
    close_logs_button.config(
        activebackground="red",
        activeforeground="black",
        bg="grey",
        fg="red"
    )
    close_logs_button.place(
        relx=0.975,
        rely=0.975,
        anchor="se"
    )


# BUTTONS

# Random Operator
random_operator = tk.StringVar(
    value="Press a button!"
)
op_label = tk.Label(
    window,
    textvariable=random_operator,
    font=("Helvetica", 40)
)
op_label.config(
    bg="black",
    fg=default_color
)
op_label.place(
    relx=0.5,
    rely=0.25,
    anchor="center"
)

#Choose Attacker
random_attacker = tk.Button(
    window,
    text="Random Attacker",
    command=choose_attacker,
    font=("Helvetica", 28)
)
random_attacker.config(
    activebackground="black",
    activeforeground="red",
    bg="red",
    fg="black"
)
random_attacker.place(
    relx=0.25,
    rely=0.6,
    anchor="center"
)

# Choose Defender
random_defender = tk.Button(
    window,
    text="Random Defender",
    command=choose_defender,
    font=("Helvetica", 28)
)
random_defender.config(
    activebackground="black",
    activeforeground="blue",
    bg="blue",
    foreground="black"
)
random_defender.place(
    relx=0.75,
    rely=0.6,
    anchor="center"
)

# Change Logs
changelog_button = tk.Button(
    window,
    text="Change Logs",
    command=show_changelogs,
    font=("Helvetica", 14)
)
changelog_button.config(
    activebackground="black",
    activeforeground="purple",
    bg="purple",
    fg="black"
)
changelog_button.place(
    relx=0.05,
    rely=0.95,
    anchor="sw"
)

# Reset
reset_button = tk.Button(
    window,
    text="Reset",
    command=reset_text,
    font=("Helvetica", 8)
)
reset_button.config(
    activebackground="black",
    activeforeground="white",
    bg="grey",
    fg="black"
)
reset_button.place(
    relx=0.5,
    rely=0.95,
    anchor="s"
)

# Close
exit_button = tk.Button(
    window,
    text="Close The Program",
    command=window.destroy,
    font=("Helvetica", 14)
)
exit_button.config(
    activebackground="red",
    activeforeground="black",
    bg="grey",
    fg="red"
)
exit_button.place(
    relx=0.95,
    rely=0.95,
    anchor="se"
)

# START
window.mainloop()