from time import sleep
from random import choice
from colorama import Style,Fore

version = "2.0.0"
invput = Fore.RED + "\n| Invalid Input!" + Style.RESET_ALL

print(
    Fore.RED
    + f"\n| R6 Operator Picker! "
    + Style.RESET_ALL
    + Fore.CYAN
    + f"| Version: {version}"
    + Style.RESET_ALL
)
print(
    "______________________________________"
)
sleep(3)

while True:
    print(
        Fore.RED +
        "\n\n|-------------| Operator Picker V2 |-------------|"
        "\n\n| Select options by number!"
        + Style.RESET_ALL
    )

    menu_options = input(
        Fore.RED
        + "\n| 1. Random Attacker"
        + Style.RESET_ALL
        + Fore.BLUE
        + "\n| 2. Random Defender"
        + Style.RESET_ALL
        + Fore.MAGENTA
        + "\n| 3. Changelogs"
        + Style.RESET_ALL
        + "\n| 4. Exit Script"
        "\n\n> "
    )

    if menu_options == "1":
        while True:
            random_attacker = choice([
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
            print(
                Fore.RED
                + "\n\nYour ATTACKER is:"
            )
            sleep(3)
            print(
                f"\n\n               {random_attacker}!"
                + Style.RESET_ALL
            )
            sleep(1.5)
            prompt = input(
                "\n| 1. Pick Another!"
                "\n| 2. Return To Menu!"
                "\n\n> "
            )
            if prompt == "1":
                pass
            elif prompt == "2":
                break
            else:
                print(f"{invput}")
                sleep(2)
                break

    elif menu_options == "2":
        while True:
            random_defender = choice([
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
                "Skopós"
            ])
            print(
                Fore.BLUE
                + "\n\nYour DEFENDER is:"
            )
            sleep(3)
            print(
                f"\n\n               {random_defender}!"
                + Style.RESET_ALL
            )
            sleep(1.5)
            prompt = input(
                "\n| 1. Pick Another!"
                "\n| 2. Return To Menu!"
                "\n\n> "
            )
            if prompt == "1":
                pass
            elif prompt == "2":
                break
            else:
                print(f"{invput}")
                sleep(2)
                break

    elif menu_options == "3":
        print(
            Fore.RED
            + "\n\n|-------------|CHANGELOGS|-------------|"
        )
        sleep(0.5)
        print(
            "\n v1.0.0 - First Version Done! - 7/19/25"
        )
        sleep(0.5)
        print(
            "\n v1.0.1 - Made code more readable and reformatted some text! - 8/21/25"
        )
        sleep(0.5)
        print(
            "\n v2.0.0 - Completely Rewrote Script!"
            "\nAlso added more styling with colorama! - 8/22/25"
            + Style.RESET_ALL
        )
        sleep(1)
        input(
            "\n Press ENTER to return to menu\n\n> "
        )

    elif menu_options == "4":
        print("\nExiting...")
        sleep(2)
        break
    else:
        print(f"{invput}")
        sleep(2)