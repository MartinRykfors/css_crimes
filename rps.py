from airium import Airium
import lib.cohost as cohost


def reveal(delay):
    # delay = delay / 10
    return {"transform": "scale(0)"} | cohost.animation(
        duration=0.01,
        delay=delay,
        direction="normal",
        count=1,
        fill="forwards",
    )


eggbug_wink = "https://cohost.org/static/3bc3a1c5272e2ceb8712.png"
eggbug_normal = "https://cohost.org/static/17aa2d48956926005de9.png"
eggbug_smug = "https://cohost.org/static/228d3a13bd5f7796b434.png"
eggbug_evil = "https://cohost.org/static/c4f3f2c6b9ffb85934e7.png"
eggbug_surprised = "https://cohost.org/static/b25a9fdf230219087003.png"
eggbug_afraid = "https://cohost.org/static/d2753b632211c395538e.png"

selection_top = 300
dialogue_width = 250
dialogue_height = 100
dialogue_top = selection_top + 60
player_dialogue_left = 10
eggbug_dialogue_left = 120

button_size = 50


dialogue_style = {
    "width": f"{dialogue_width}px",
    "height": f"{dialogue_height}px",
    "border": "2px solid black",
    "background-color": "white",
    "position": "absolute",
    "font-size": "1rem",
    "display": "flex",
    # "justify-content": "center",
    "align-items": "center",
    "padding": "3px",
    "text-decoration": "none",
    'color': 'black',
}

player_dialogue_style = dialogue_style | {
    "left": f"{player_dialogue_left}px",
    "top": f"{dialogue_top}px",
}
eggbug_dialogue_style = dialogue_style | {
    "left": f"{eggbug_dialogue_left}px",
    "top": f"10px",
}
plus_style = {
    "position": "absolute",
    "top": f"{selection_top - 10}px",
    "left": "10px",
    "box-shadow": "0px 0px 6px 6px #ffe5c4",
}

eggbug_style = {
    "left": f"10px",
    "top": f"10px",
    "position": "absolute",
    "width": f"{dialogue_height}px",
    "height": f"{dialogue_height}px",
    "border": "2px solid black",
    "display": "flex",
    "justify-content": "center",
    "align-items": "center",
    "transform": "scale(-1, 1)",
    "background-color": "white",
}
choice_top = 10 + dialogue_height + 10
eggbug_choice = {
    "left": f"10px",
    "top": f"{choice_top}px",
    "position": "absolute",
    "width": f"{button_size}px",
    "height": f"{button_size}px",
    "border": "2px solid black",
    "display": "flex",
    "justify-content": "center",
    "align-items": "center",
    "font-size": "2rem",
}

darkness = {
    "width": "1000px",
    "height": "1000px",
    "background-color": "black",
    "top": "0px",
    "position": "absolute",
    "z-index": 10,
} | reveal(2)

a = Airium(base_indent="")


def body(a):
    description = (
        "The post consists of an interactive rock paper scissors game which you play against eggbug. "
        "When you select one of rock, paper or scissors, eggbug immediately plays the winning move. "
        "A sequence of interactive dialogue then appears. "
        "Eggbug says 'I win, now pay up!' "
        "You respond with 'Hey no fair! You were hard-coded to play the winning move!' "
        "Eggbug replies 'I won fair and square, now pay up!' "
        "You answer 'What is this about paying? I did not agree to this!' "
        "On saying this, the screen goes black. Eggbug appears on the screen, bigger now. They say 'Pay up. I am done asking nicely'. "
        "A link to buy cohost plus appears."
    )
    cohost.with_description(a, game, description, "rps")


def game(a):
    with a.div(
        style=cohost.style(
            {"width": "500px", "height": "500px", "border": "1px solid black"}
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "position": "absolute",
                    "top": "10px",
                    "height": "0px",
                }
            )
        ):
            with a.div(style=cohost.style(eggbug_style)):
                a.img(src=eggbug_normal)
            with a.div(style=cohost.style(eggbug_choice)):
                pass

            initial(a, 1)
            initial(a, 2)
            initial(a, 3)
            win(a)


def win(a):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            left = 10 + 2 * 80 + 5
            with a.a(
                style=cohost.style(
                    {
                        "width": f"12px",
                        "height": f"10px",
                        "left": f"{left}px",
                        "top": f"{selection_top+2}px",
                        # "background-color": "red",
                        "position": "absolute",
                        "font-size": "2rem",
                        "z-index": 1,
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                        "cursor": "pointer",
                        "text-decoration": "none",
                        "transform": "translateY(25px)",
                    }
                    | cohost.animation(duration=2, direction="alternate")
                )
            ):
                pass
        for i in range(0, 3):
            left = 10 + i * 80
            color = "rgb(0 128 0 / 0.5)" if i + 1 == 3 else "rgb(128 128 128 / 0.5)"
            with a.div(
                style=cohost.style(
                    {
                        "width": f"{button_size}px",
                        "height": f"{button_size}px",
                        "left": f"{left}px",
                        "top": f"{selection_top}px",
                        "border": "3px solid black",
                        "background-color": color,
                        "position": "absolute",
                        "font-size": "2rem",
                        "z-index": 2,
                    }
                )
            ):
                pass
        with a.div(style=cohost.style(eggbug_choice)):
            icon(a, 2)
        with a.div(style=cohost.style(eggbug_style)):
            a.img(src=eggbug_smug)
        with a.div(style=cohost.style(eggbug_dialogue_style | reveal(1))):
            a("{}! I win!".format(winning_move(1)))

        with a.div(style=cohost.style(eggbug_style | reveal(4))):
            with a.div(style=cohost.style({"transform": "scale(-1, 1)"})):
                a.img(src=eggbug_surprised)
        with a.div(style=cohost.style(eggbug_dialogue_style | reveal(4))):
            a("Wait a minute...")

        with a.div(style=cohost.style(eggbug_style | reveal(7))):
            with a.div(style=cohost.style({"transform": "scale(-1, 1)"})):
                a.img(src=eggbug_afraid)
        with a.div(style=cohost.style(eggbug_dialogue_style | reveal(7))):
            a("What's going on? I'm always supposed to win this!")


def initial(a, move):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            left = 10 + (move - 1) * 80
            with a.a(
                style=cohost.style(
                    {
                        "width": f"{button_size}px",
                        "height": f"{button_size}px",
                        "left": f"{left}px",
                        "top": f"{selection_top}px",
                        "border": "2px solid black",
                        "background-color": "white",
                        "position": "absolute",
                        "font-size": "2rem",
                        "z-index": 1,
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                        "cursor": "pointer",
                        "text-decoration": "none",
                    }
                )
            ):
                icon(a, move)
        for i in range(0, 3):
            left = 10 + i * 80
            color = "rgb(0 128 0 / 0.5)" if i + 1 == move else "rgb(128 128 128 / 0.5)"
            with a.div(
                style=cohost.style(
                    {
                        "width": f"{button_size + 2}px",
                        "height": f"{button_size + 2}px",
                        "left": f"{left - 1}px",
                        "top": f"{selection_top - 1}px",
                        "border": "2px solid black",
                        "background-color": color,
                        "position": "absolute",
                        "font-size": "2rem",
                        "z-index": 2,
                    }
                )
            ):
                pass
        with a.div(style=cohost.style(eggbug_choice)):
            icon(a, (move % 3) + 1)
        with a.div(style=cohost.style(eggbug_style)):
            a.img(src=eggbug_smug)
        with a.div(style=cohost.style(eggbug_dialogue_style | reveal(1))):
            a("{}! I win! Now pay up!".format(winning_move(move)))
        dialogue1(a)


def winning_move(move):
    if move == 1:
        return "Paper"
    if move == 2:
        return "Scissors"
    return "Rock"


def dialogue1(a):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            with a.a(
                style=cohost.style(
                    player_dialogue_style
                    | {
                        "z-index": 3,
                        "cursor": "pointer",
                    }
                    | reveal(2)
                )
            ):
                a("➡️ Hey no fair! You were hard-coded to play the winning move!")
        with a.a(
            style=cohost.style(
                player_dialogue_style
                | {
                    "z-index": 4,
                    "background-color": "rgb(128 128 128 / 0.5)",
                }
            )
        ):
            pass
        with a.div(style=cohost.style(eggbug_style)):
            a.img(src=eggbug_wink)
        with a.div(style=cohost.style(eggbug_dialogue_style | {"z-index": 3})):
            pass
        with a.div(
            style=cohost.style(eggbug_dialogue_style | {"z-index": 4} | reveal(1))
        ):
            a("I won fair and square. Now pay up! :)")
        dialogue2(a)


def dialogue2(a):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            with a.a(
                style=cohost.style(
                    player_dialogue_style
                    | {
                        "z-index": 4,
                        "cursor": "pointer",
                    }
                    | reveal(2)
                )
            ):
                a("➡️ What's this about paying? I didn't agree to that!")
        with a.a(
            style=cohost.style(
                player_dialogue_style
                | {
                    "z-index": 4,
                    "background-color": "rgb(128 128 128 / 0.5)",
                }
            )
        ):
            pass
        with a.div(style=cohost.style(eggbug_dialogue_style | {"z-index": 5})):
            pass
        with a.div(style=cohost.style(eggbug_style)):
            a.img(src=eggbug_normal)

        with a.div(style=cohost.style(darkness)):
            with a.div(
                style=cohost.style(
                    {
                        "position": "absolute",
                        "height": "1000px",
                        "width": "1000px",
                        "transform": "translateX(-30px) translateY(-30px)",
                        "background-color": "black",
                        "z-index": -1,
                    }
                )
            ):
                pass

            with a.div(
                style=cohost.style(
                    eggbug_style
                    | {"height": "200px", "width": "200px", "background-color": "black"}
                    | reveal(4)
                )
            ):
                with a.div(
                    style=cohost.style(
                        {"transform": "scale(-1.8, 1.8) translateY(-20px)"}
                    )
                ):
                    a.img(
                        src=eggbug_normal, style={"height": "200px", "width": "200px"}
                    )
                with a.div(
                    style=cohost.style(
                        eggbug_dialogue_style
                        | {
                            "top": "170px",
                            "background-color": "red",
                            "box-shadow": "0px 0px 5px 5px red",
                            "border": "none",
                        }
                        | reveal(6)
                    )
                ):
                    a("Pay up. I am done asking nicely.")
                with a.a(href="https://cohost.org/rc/user/settings#cohost-plus"):
                    with a.div(style=cohost.style(plus_style | reveal(8))):
                        a.img(
                            src="https://cohost.org/static/c9cba9a97beb26e73cb4.png",
                            style=cohost.style({"margin": "0px"}),
                        )


def icon(a, move):
    if move == 1:
        with a.div(style=cohost.style({"transform": "rotate(-90deg)"})):
            a("✊")
        return

    if move == 2:
        with a.div(style=cohost.style({"transform": "rotate(-90deg)"})):
            a("✋")
        return

    with a.div(style=cohost.style({"transform": "rotate(-90deg)"})):
        a("✌️")


cohost.create_document(body, "post.html")
