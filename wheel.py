import random
from airium import Airium
import lib.cohost as cohost

eggbug_wink = "https://cohost.org/static/3bc3a1c5272e2ceb8712.png"
eggbug_normal = "https://cohost.org/static/17aa2d48956926005de9.png"
eggbug_smug = "https://cohost.org/static/228d3a13bd5f7796b434.png"
eggbug_evil = "https://cohost.org/static/c4f3f2c6b9ffb85934e7.png"
eggbug_surprised = "https://cohost.org/static/b25a9fdf230219087003.png"
eggbug_afraid = "https://cohost.org/static/d2753b632211c395538e.png"
eggbug_logo = "https://cohost.org/static/41454e429d62b5cb7963.png"
eggbug_hearts = "https://cohost.org/static/d7ec7f057e6fb15a94cc.png"
bang_image = "https://staging.cohostcdn.org/attachment/1051f297-f225-4b4e-a574-c90cb82698e9/bang1.svg"

arrow_image = "https://staging.cohostcdn.org/attachment/79268e7d-85ee-43ee-9650-1a9a2a35d937/down-arrow-1.svg"

tempo = 4
gold = "#ffab5c"
dark_cherry = "#3b132c"


def reveal(delay):
    return cohost.style(
        {"transform": "scale(0)"}
        | cohost.animation(
            duration=0.01,
            delay=delay,
            direction="normal",
            count=1,
            fill="forwards",
            easing="steps(2, jump-none)",
        )
    )


def reveal_d(delay):
    return {"transform": "scale(0)"} | cohost.animation(
        duration=0.01,
        delay=delay,
        direction="normal",
        count=1,
        fill="forwards",
        easing="steps(2, jump-none)",
    )


def reveal_vanish(delay_reveal, delay_vanish):
    return cohost.style(
        {"transform": "scale(0)"}
        | cohost.animation(
            duration=delay_vanish - delay_reveal,
            delay=delay_reveal,
            direction="normal",
            count=1,
            fill="none",
            easing="steps(2, jump-start)",
        )
    )


page_width = 360
dialogue_height = 80
dialogue_width = 230
eggbug_dialogue_left = 100
eggbug_dialogue_top = 10
player_dialogue_top = 450
balance_height = dialogue_height
balance_width = 100
balance_top = player_dialogue_top
balance_left = 10
player_dialogue_left = balance_left + balance_width + 10
wheel_top = eggbug_dialogue_top + dialogue_height + 120
wheel_container_height = 250
wheel_container_width = 250
wheel_diam = 200
eggbug_style = {
    "left": f"10px",
    "top": f"{eggbug_dialogue_top}px",
    "position": "absolute",
    "width": f"{dialogue_height}px",
    "height": f"{dialogue_height}px",
    "border": "2px solid black",
    "display": "flex",
    "justify-content": "center",
    "align-items": "center",
    "background-color": "white",
}
balance_style = eggbug_style | {
    "height": f"{balance_height}px",
    "width": f"{balance_width}px",
    "top": f"0px",
    "left": f"0px",
}
balance_container_style = {
    "top": f"{balance_top}px",
    "left": f"{balance_left}px",
    "position": "absolute",
    'color': 'black',
}

dialogue_style = {
    "width": f"{dialogue_width}px",
    "height": f"{dialogue_height}px",
    "border": "2px solid black",
    "background-color": "white",
    "position": "absolute",
    "font-size": "1rem",
    "display": "flex",
    "align-items": "center",
    "padding": "3px",
    "text-decoration": "none",
    'color': 'black'
}
wheel_container_style = {
    "position": "absolute",
    "top": f"{wheel_top}px",
    "left": "30px",
    "height": f"{wheel_container_height}px",
    "width": f"{wheel_container_width}px",
    "border": "2px solid black",
    "display": "flex",
    "justify-content": "center",
    "align-items": "center",
    "flex-direction": "column",
    "background-color": "#aaaaff",
}
eggbug_dialogue_style = dialogue_style | {
    "left": f"{eggbug_dialogue_left}px",
    "top": f"{eggbug_dialogue_top}px",
}
player_dialogue_style = dialogue_style | {
    "left": f"{player_dialogue_left}px",
    "top": f"{player_dialogue_top}px",
    "cursor": "pointer",
}

display_style = {
    "border": "2px solid black",
    "display": "flex",
    "justify-content": "center",
    "align-items": "center",
    "background-color": "#333333",
    "font-size": "1.5em",
    "width": "260px",
    "height": "60px",
}
display_container_style = {
    "position": "absolute",
    "top": f"{wheel_top - 90}px",
    "left": f"{page_width / 2 - 130}px",
}


a = Airium(base_indent="")


def body(a):
    description = """Eggbug offers you to pay $5 to play a Wheel of Fortune game.
    If you take up their offer, there are three possible outcomes.
    If you lose, Eggbug tells you a secret that you can reset the game and get your money back by pressing the read more link.
    If you win, you only gain the amount you paid to play. Eggbug argues with you that it was still a net positive because of the excitement of playing and winning.
    In the third, secret, outcome of the game, the wheel goes haywire and accelerates uncontrollably.
    Eggbug escapes just before the wheel explodes and the screen goes black.
    You wake up seeing the game in disarray. The wheel is broken and only a part of it is still attached to its axis.
    Suddenly, the wheels indicator arrow comes falling down and lands just below the remainder of the wheel pointing up, indicating that you have won.
    You win back your five dollars and the game ends.
    """
    cohost.with_description(a, game, description, "wof")

    a("")
    a("---")
    a("")
    a(":eggbug-wink: Hey, since you're here, why not try my other games?")
    with a.ul():
        with a.li():
            with a.a(href="https://cohost.org/rykarn/post/2356687-rock-paper-scissors"):
                a('Rock Paper Scissors Game!')
        with a.li():
            with a.a(href="https://cohost.org/rykarn/post/2231825-matchstick-game"):
                a('Matchstick Game!')


def eggbug(a, src, extensions={}, mirror=-1):
    with a.div(style=cohost.style(eggbug_style | extensions)):
        with a.div(style=cohost.style({"transform": f"scale({mirror}, 1)"})):
            a.img(src=src)


def balance(a, amount, delta="", color="green", delay=0, flash="", extensions={}, z=0):
    with a.div(style=cohost.style(balance_container_style | {"z-index": z})):
        with a.div(
            style=cohost.style(balance_style | extensions | {"font-size": "1.4rem"})
        ):
            a(f"💵: ${amount}")
            if delta:
                with a.div(
                    style=cohost.style(
                        {
                            "position": "absolute",
                            "color": color,
                            "transform": "translateY(-25px)",
                        }
                        | cohost.animation(direction="reverse", count=1, delay=delay)
                    )
                ):
                    with a.div(style=reveal(delay)):
                        with a.div(style=cohost.style({"font-size": "1.8rem"})):
                            a(f"{delta}")


def eggbug_say(a, text, extensions={}):
    with a.div(style=cohost.style(eggbug_dialogue_style | extensions)):
        a(text)


def player_say(a, text, extensions={}):
    with a.div(style=cohost.style(player_dialogue_style | extensions)):
        a("➡️ {}".format(text))


def player_say_a(a, text, extensions={}, reveal_t=0, z=1):
    with a.a(
        style=cohost.style(
            player_dialogue_style | extensions | {"z-index": z} | reveal_d(reveal_t)
        )
    ):
        a("➡️ {}".format(text))


def player_blocker(a, z=1):
    with a.a(
        style=cohost.style(
            player_dialogue_style
            | {
                "background-color": "rgba(0.5, 0.5, 0.5, 0.5)",
                "border": "1px solid black",
                "z-index": z,
            }
        )
    ):
        pass


def arrow(a, duration, rot):
    with a.div(
        style=cohost.style(
            {
                "position": "absolute",
                "left": f"{page_width / 2 - 25}px",
                "top": f"{wheel_top - 20}px",
                "width": "50px",
                "height": "50px",
                "display": "flex",
                "justify-content": "center",
            }
        )
    ):
        with a.div(style=cohost.style({"transform": " translateY(-12px)"})):
            with a.div(
                style=cohost.style(
                    {"transform": f"scale(1) rotate(-{rot}deg)"}
                    | cohost.animation(direction="reverse", duration=duration)
                )
            ):
                with a.div(
                    style=cohost.style({"transform": "scale(1.8) translateY(8px)"})
                ):
                    a.img(
                        src=arrow_image,
                        width="20px",
                        height="20px",
                        style=cohost.style({"margin": "0px"}),
                    )


def arrow_slowdown(a, rot):
    with a.div(
        style=cohost.style(
            {
                "position": "absolute",
                "left": f"{page_width / 2 - 25}px",
                "top": f"{wheel_top - 20}px",
                "width": "50px",
                "height": "50px",
                "display": "flex",
                "justify-content": "center",
            }
        )
    ):
        with a.div(style=cohost.style({"transform": " translateY(-12px) "})):
            with a.div(style=cohost.style({"transform": f" rotate({rot * 7}deg) "})):
                delay = 0
                dur = 0.1
                count = 5
                with a.div(style=tick(rot, dur, count, delay)):
                    delay += dur * count
                    dur = 0.2
                    count = 4
                    with a.div(style=tick(rot, dur, count, delay)):
                        delay += dur * count
                        dur = 0.3
                        count = 4
                        with a.div(style=tick(rot, dur, count, delay)):
                            delay += dur * count
                            dur = 0.5
                            count = 1
                            with a.div(style=tick(rot, dur, count, delay)):
                                delay += dur * count
                                dur = 1.3
                                count = 1
                                with a.div(style=tick(rot, dur, count, delay)):
                                    final_arrow(a)


def tick(rot, duration, count, delay):
    return cohost.style(
        {"transform": f"scale(1) rotate({rot}deg)"}
        | cohost.animation(
            direction="normal",
            duration=duration,
            count=count,
            delay=delay,
            fill="none",
        )
    )


def final_arrow(a):
    with a.div(style=cohost.style({"transform": "scale(1.8) translateY(8px)"})):
        a.img(
            src=arrow_image,
            width="20px",
            height="20px",
            style=cohost.style({"margin": "0px"}),
        )


def display_graphic(a, win, delay=0):
    with a.div(style=cohost.style(display_style)):
        with a.div(
            style=cohost.style(
                {
                    "position": "absolute",
                    "color": "#000000",
                }
            )
        ):
            a("YOU WIN")
    if win:
        with a.div(
            style=cohost.style(
                {
                    "transform": "scale(0)",
                    "top": "0px",
                    "left": "0px",
                    "position": "absolute",
                    "z-index": 1,
                }
                | cohost.animation(
                    easing="steps(2, jump-none)", direction="normal", delay=delay
                )
            )
        ):
            with a.div(
                style=cohost.style(
                    display_style
                    | {
                        "background-color": "orange",
                    }
                )
            ):
                with a.div(
                    style=cohost.style(
                        {
                            "color": "#ffffff",
                        }
                    )
                ):
                    a("YOU WIN")


def display(a, win, z=None):
    with a.div(
        style=cohost.style(
            display_container_style | ({"z-index": z} if z is not None else {})
        )
    ):
        display_graphic(a, win)


def wheel(a, duration, easing="cubic-bezier(0,0,1,1)", offset=10, count="infinite"):
    with a.div(
        style=cohost.style(
            {
                "transform": f"rotate({offset}deg)",
                "position": "absolute",
                "top": f"{wheel_top}px",
                "left": f"{page_width / 2 - wheel_diam / 2}px",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "background": "repeating-conic-gradient(from 0deg, {} 0deg 30deg, {} 30deg 90deg)".format(
                        gold, dark_cherry
                    ),
                    # "border": "2px solid black",
                    "height": f"{wheel_diam}px",
                    "width": f"{wheel_diam}px",
                    "border-radius": f"{wheel_diam / 2}px",
                    "display": "flex",
                    "justify-content": "center",
                    "align-items": "center",
                    # "position": "absolute",
                    # "top": f"{wheel_top}px",
                    # "left": f"{page_width / 2 - wheel_diam / 2}px",
                }
                | (
                    cohost.animation(
                        direction="normal",
                        duration=duration,
                        easing=easing,
                        count=count,
                    )
                    if duration
                    else {}
                )
            )
        ):
            logo(a)


def logo(a):
    with a.div(
        style=cohost.style(
            {
                "height": "60px",
                "width": "60px",
                "border-radius": "30px",
                "background-color": "white",
                "border": "2px solid black",
                "transform": "rotate(10deg)",
            }
        )
    ):
        with a.div(style=cohost.style({"transform": "translateY(-3px) scale(0.7)"})):
            a.img(src=eggbug_logo, style=cohost.style({"margin": "0px"}))


def broken_wheel(a, z=0):
    with a.div(
        style=cohost.style(
            {
                "transform": f"rotate(140deg)",
                "position": "absolute",
                "top": f"{wheel_top}px",
                "left": f"{page_width / 2 - wheel_diam / 2}px",
                "z-index": z,
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "background": f"conic-gradient({dark_cherry} 10deg, {gold} 10deg 40deg, {dark_cherry} 40deg 60deg, rgba(0, 0, 0, 0) 60deg)",
                    "height": f"{wheel_diam}px",
                    "width": f"{wheel_diam}px",
                    "border-radius": f"{wheel_diam / 2}px",
                    "display": "flex",
                    "justify-content": "center",
                    "align-items": "center",
                    "transform": "scale(1) rotate(17deg)",
                }
                | (
                    cohost.animation(
                        direction="alternate",
                        duration=2,
                        easing="cubic-bezier(.37,-0.01,.64,.99)",
                    )
                )
            )
        ):
            with a.div(
                style=cohost.style(
                    {
                        "height": "20px",
                        "width": "20px",
                        "border-radius": "10px",
                        "background-color": "gray",
                        "border": "1px solid black",
                    }
                )
            ):
                pass


def wheel_blur(a, duration):
    with a.div(
        style=cohost.style(
            {
                "transform": f"rotate(10deg)",
                "position": "absolute",
                "top": f"{wheel_top}px",
                "left": f"{page_width / 2 - wheel_diam / 2}px",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "background": "repeating-conic-gradient({} 0deg 80deg, {} 160deg 180deg)".format(
                        dark_cherry, gold
                    ),
                    # "border": "2px solid black",
                    "height": f"{wheel_diam}px",
                    "width": f"{wheel_diam}px",
                    "border-radius": f"{wheel_diam / 2}px",
                    "display": "flex",
                    "justify-content": "center",
                    "align-items": "center",
                    # "position": "absolute",
                    # "top": f"{wheel_top}px",
                    # "left": f"{page_width / 2 - wheel_diam / 2}px",
                }
                | (
                    cohost.animation(
                        direction="normal",
                        duration=duration,
                    )
                )
            )
        ):
            with a.div(
                style=cohost.style(
                    {
                        "height": "60px",
                        "width": "60px",
                        "border-radius": "30px",
                        "background-color": "white",
                        "border": "2px solid black",
                        "transform": "rotate(10deg)",
                    }
                )
            ):
                with a.div(
                    style=cohost.style({"transform": "translateY(-3px) scale(0.7)"})
                ):
                    a.img(src=eggbug_logo, style=cohost.style({"margin": "0px"}))


def button(a, text, text_color, background_color, reveal_t=0, z=0):
    with a.a(
        style=cohost.style(
            player_dialogue_style
            | {
                "background-color": background_color,
                "display": "flex",
                "justify-content": "center",
                "font-size": "2rem",
            }
            | (reveal_d(reveal_t) if reveal_t else {})
            | ({"z-index": z} if z else {})
        )
    ):
        with a.div(style=cohost.style({"color": text_color})):
            a(text)


def page(a, z=None):
    with a.div(
        style=cohost.style(
            {"position": "absolute"} | ({"z-index": z} if z is not None else {})
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "width": f"{page_width}px",
                    "height": "550px",
                    "border": "1px solid black",
                    "position": "absolute",
                    "background-color": "#9c4b64",
                }
                | ({"z-index": z} if z is not None else {})
            )
        ):
            pass


def game(a):
    with a.div(
        style="display:flex; flex-direction:row; background-color: rgb(250 216 214); border-radius:0.5rem; color:rgb(34 0 16); padding: 0.75rem; gap: 1rem; align-items:center;align-self:stretch;box-sizing:border-box; width:100%; margin-top:0.75rem; margin-bottom:0.75rem; line-height:1.5"
    ):
        with a.div(
            style="width: 1.5rem; height: 1.5rem; flex-shrink:0; align-self:flex-start; background-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCAyNCAyNCIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZT0icmdiKDIyOSwgMTA3LCAxMTEpIiBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9InctNiBzZWxmLXN0YXJ0IHRleHQtc3RyYXdiZXJyeSI+PHBhdGggc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBkPSJNMTIgOXYzLjc1bS05LjMwMyAzLjM3NmMtLjg2NiAxLjUuMjE3IDMuMzc0IDEuOTQ4IDMuMzc0aDE0LjcxYzEuNzMgMCAyLjgxMy0xLjg3NCAxLjk0OC0zLjM3NEwxMy45NDkgMy4zNzhjLS44NjYtMS41LTMuMDMyLTEuNS0zLjg5OCAwTDIuNjk3IDE2LjEyNnpNMTIgMTUuNzVoLjAwN3YuMDA4SDEydi0uMDA4eiI+PC9wYXRoPjwvc3ZnPgo=)"
        ):
            pass
        with a.div():
            with a.p(style="margin:0"):
                with a.b():
                    a("Warning: Flashing imagery.")

    with a.div(style=cohost.style({"height": "580px"})):
        with a.div(
            style=cohost.style(
                {
                    "position": "absolute",
                    "top": "100px",
                    "height": "0px",
                }
            )
        ):
            start_scene(a)
            # bang(a)
            # i_want_my_money_back(a)





def start_scene(a):
    page(a)
    wheel(a, 0)
    display(a, False)
    arrow(a, 1, 0)
    eggbug(a, eggbug_evil)
    eggbug_say(a, "Spin the wheel! Only $5!")
    balance(a, "5")
    spinning_scene(a)


def spinning_scene(a):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            button(a, "SPIN", "#00ff00", "green")

        page(a)
        button(a, "SPIN", "#338833", "#99bb99")
        wheel(a, 1)
        arrow(a, 0.1, 30)
        balance(a, "0", "-$5", "red", flash="rgb(255 100 100 / .7)")
        eggbug(a, eggbug_wink)
        eggbug_say(a, "Good luck! Remember, orange wins!")
        display(a, False)
        losing_scene(a)
        winning_scene(a)
        haywire_scene(a)


debug = False


def haywire_button(a):
    width = 15
    with a.div(
        style=cohost.style(
            {"transform": f"translateX({dialogue_width / 2 - width}px)"}
            | cohost.animation(direction="normal", duration=2.9)
        )
    ):
        with a.a(
            style=cohost.style(
                {
                    "position": "absolute",
                    "top": f"{player_dialogue_top}px",
                    "left": f"{player_dialogue_left}px",
                    "height": f"{dialogue_height}px",
                    "width": f"{width}px",
                    "cursor": "pointer",
                }
                | ({"background-color": "red"} if debug else {})
            )
        ):
            pass
        with a.a(
            style=cohost.style(
                {
                    "position": "absolute",
                    "top": f"{player_dialogue_top}px",
                    "left": f"{player_dialogue_left + dialogue_width / 2}px",
                    "height": f"{dialogue_height}px",
                    "width": f"{width}px",
                    "cursor": "pointer",
                }
                | ({"background-color": "red"} if debug else {})
            )
        ):
            pass


def winning_button(a):
    with a.div(
        style=cohost.style(
            {"transform": f"translateY({dialogue_height - dialogue_height / 2 + 5}px)"}
            | cohost.animation(direction="normal", duration=2.1)
        )
    ):
        with a.a(
            style=cohost.style(
                {
                    "position": "absolute",
                    "top": f"{player_dialogue_top}px",
                    "left": f"{player_dialogue_left}px",
                    "height": f"{dialogue_height / 2 - 5}px",
                    "width": f"{dialogue_width}px",
                    "cursor": "pointer",
                }
                | ({"background-color": "gray"} if debug else {})
            )
        ):
            pass


def wheel_slowdown(a, offset):
    page(a)
    button(a, "STOP", "#883333", "#bb9999")
    eggbug(a, eggbug_wink)
    with a.div(style=reveal(2)):
        eggbug(a, eggbug_surprised)
    balance(a, "0")
    display(a, False)
    wheel(a, 5, easing="cubic-bezier(.21,1.05,.84,.99)", offset=offset, count=1)
    arrow_slowdown(a, 30)


def losing_scene(a):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            with a.div(style=reveal(3)):
                button(a, "STOP", "#ff0000", "#aa0000")

        player_blocker(a)
        wheel_slowdown(a, 95)
        with a.div(style=reveal(5.5)):
            eggbug(a, eggbug_normal)
            eggbug_say(a, "So close! Better luck next time!")
        cheating_scene(a)


def cheating_scene(a):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            player_say_a(a, "Won't be a next time. I'm out of money.", reveal_t=8, z=1)

        player_blocker(a)
        eggbug_say(a, "")
        tempo = 5
        with a.div(style=reveal(1)):
            eggbug_say(a, "Really? Ok then, I'll let you in on a little secret!")
        with a.div(style=reveal(tempo * 1)):
            eggbug(a, eggbug_wink)
            with a.div(style=cohost.style(eggbug_dialogue_style)):
                with a.div():
                    a("If you press the ")
                    with a.span(
                        style=cohost.style(
                            {"color": "rgb(131 73 79)", "font-weight": 700}
                        )
                    ):
                        a("read more")
                    a("link below the post, this entire game will reset.")
        with a.div(style=reveal(tempo * 2)):
            eggbug(a, eggbug_evil)
            eggbug_say(a, "You'll get your money back!")
        with a.div(style=reveal(tempo * 3)):
            eggbug(a, eggbug_smug)
            eggbug_say(a, "I won't tell.")


def winning_scene(a):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            with a.div(style=reveal(3)):
                winning_button(a)

        player_blocker(a)
        wheel_slowdown(a, 152)
        with a.div(style=reveal(5.5)):
            display(a, True)
        with a.div(style=reveal(6.0)):
            eggbug(a, eggbug_hearts)
            eggbug_say(a, "You win! Congratulations!")
        what_do_i_win(a)


def what_do_i_win(a):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            player_say_a(a, "Sweet! What do I win?", reveal_t=9, z=1)

        player_blocker(a, z=2)
        eggbug_say(a, "")
        with a.div(style=reveal(1)):
            eggbug(a, eggbug_hearts)
            eggbug_say(a, "Tadaah! You win $5!")
        with a.div(style=reveal(3)):
            balance(a, "5", "+$5", "green", delay=3, flash="rgb(100 255 100 / .7)")
        is_that_the_price(a)


def is_that_the_price(a):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            player_say_a(
                a, "Wait, what? I win the same amount I paid?", reveal_t=5, z=3
            )

        player_blocker(a, z=4)
        eggbug_say(a, "")
        display(a, False)
        balance(a, 5)
        with a.div(style=reveal(1)):
            eggbug(a, eggbug_normal)
            eggbug_say(a, "Well, I mean...")
        with a.div(style=reveal(1 * tempo)):
            eggbug(a, eggbug_normal, mirror=1)
            eggbug_say(a, "Ok, sure. Financially, you broke even.")
        with a.div(style=reveal(2 * tempo)):
            eggbug(a, eggbug_smug)
            eggbug_say(a, "But are you not one experience richer?")
        with a.div(style=reveal(3 * tempo)):
            eggbug(a, eggbug_surprised)
            eggbug_say(a, "The excitement of playing! The joy of winning!")
        with a.div(style=reveal(4 * tempo)):
            eggbug(a, eggbug_wink)
            eggbug_say(a, "Sounds like a net positive to me!")
        with a.div(style=reveal(5 * tempo)):
            eggbug(a, eggbug_evil)
            eggbug_say(a, "Besides, now you can play once more!")
        with a.div(style=reveal(7 * tempo)):
            eggbug(a, eggbug_wink)
            with a.div(style=cohost.style(eggbug_dialogue_style)):
                with a.div(style=cohost.style({"font-size": "0.85rem"})):
                    a("Just press the")
                    with a.span(
                        style=cohost.style(
                            {"color": "rgb(131 73 79)", "font-weight": 700}
                        )
                    ):
                        a("read more")
                    a("link to reset the game!")
                    a("Maybe the next outcome will be different!")


def haywire_scene(a):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            with a.div(style=reveal(3)):
                haywire_button(a)
                # button(a, "STOP", "#ff0000", "#aa0000")
        player_blocker(a)
        page(a)
        eggbug(a, eggbug_normal)
        button(a, "STOP", "#883333", "#bb9999")
        wheel(a, 1)
        arrow(a, 0.1, 30)
        balance(a, "0")
        display(a, False)
        with a.div(style=reveal(7)):
            eggbug_say(a, "Did you press the stop button?")
        yes_i_did(a)


def wheel_blocker(a):
    with a.div(
        style=cohost.style(
            {
                "position": "absolute",
                # "border": "1px solid black",
                "height": f"{wheel_diam * 1.2}px",
                "width": f"{wheel_diam * 1.5}px",
                "left": "20px",
                "top": "181px",
                "background-color": "#9c4b64",
            }
        )
    ):
        pass


def yes_i_did(a):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            player_say_a(a, "Yes I did.", reveal_t=9, z=1)
        player_blocker(a, z=2)
        eggbug_say(a, "")
        with a.div(style=reveal(1)):
            eggbug_say(a, "Ok, good. It should stop any second now.")
        with a.div(style=reveal(5)):
            wheel_blocker(a)
            wheel(a, 0.7)
            arrow(a, 0.08, 40)
        with a.div(style=reveal(7)):
            eggbug(a, eggbug_surprised)
            eggbug_say(a, "Um.")
        with a.div(style=reveal(9)):
            wheel_blocker(a)
            wheel(a, 0.5)
            arrow(a, 0.06, 60)
        with a.div(style=reveal(11)):
            eggbug(a, eggbug_normal)
            eggbug_say(a, "Could you try pressing the stop button again?")
        press_again(a)


def no_eggbug(a):
    with a.div(style=cohost.style(eggbug_style)):
        pass


def press_again(a):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            button(a, "STOP", "#ff0000", "#aa0000", reveal_t=13, z=3)
        with a.div(style=cohost.style({"z-index": 4})):
            button(a, "STOP", "#883333", "#bb9999", z=4)
        eggbug_say(a, "")
        with a.div(style=reveal(0.5)):
            wheel_blocker(a)
            shake(a, lambda: wheel_blur(a, 0.123), factor=0.5)

            shake(a, lambda: arrow(a, 0.06, 120), factor=0.1)
        with a.div(style=reveal(1.5)):
            eggbug(a, eggbug_afraid)
            eggbug_say(a, "Oh. Um.")
        with a.div(style=reveal(4)):
            eggbug(a, eggbug_smug)
            eggbug_say(a, "Closing time, thanks for playing!")
        with a.div(style=reveal(7)):
            eggbug(a, eggbug_afraid, mirror=1)
            eggbug_say(a, "BYE!")
        with a.div(style=reveal(8.5)):
            no_eggbug(a)
        bang(a)


def shake(a, content, factor=1):
    dx1 = 10 * factor
    dy1 = 8 * factor
    with a.div(
        style=cohost.style(
            {"position": "absolute", "transform": f"translateX({dx1}px)"}
            | cohost.animation(
                easing="steps(5, end)", duration=0.023, delay=random.uniform(-1, 0)
            )
            | {"z-index": 6}
        )
    ):
        with a.div(
            style=cohost.style(
                {"transform": f"translateX(-{dx1}px)"}
                | cohost.animation(
                    easing="steps(3, end)", duration=0.01, delay=random.uniform(-1, 0)
                )
                | {"z-index": 6}
            )
        ):
            with a.div(
                style=cohost.style(
                    {"transform": f"translateY({dy1}px)"}
                    | cohost.animation(
                        easing="steps(3, end)",
                        duration=0.027,
                        delay=random.uniform(-1, 0),
                    )
                    | {"z-index": 6}
                )
            ):
                with a.div(
                    style=cohost.style(
                        {"transform": f"translateY(-{dy1}px)"}
                        | cohost.animation(
                            easing="steps(3, end)",
                            duration=0.01,
                            delay=random.uniform(-1, 0),
                        )
                        | {"z-index": 6}
                    )
                ):
                    with a.div(style=cohost.style({"z-index": 6})):
                        content()


def bang_img(a):
    with a.div(
        style=cohost.style(
            {
                "position": "absolute",
                "height": "150px",
                "width": "330px",
                "top": "140px",
                "left": "20px",
            }
        )
    ):
        a.img(src=bang_image, width="400px", height="500px", style="margin:0px")


def broken_page(
    a,
    animate_display=True,
    win_delay=0,
    balance_delay=0,
    delta="",
    z=0,
    page_show=True,
    wheel_show=True,
):
    if page_show:
        page(a, z=z)
    balance(
        a,
        0,
        extensions={"transform": "rotate(10deg)"},
        delay=balance_delay,
        delta=delta,
        z=z,
    )
    if balance_delay:
        with a.div(style=reveal(balance_delay)):
            balance(
                a,
                5,
                extensions={"transform": "rotate(10deg)", "z-index": z},
                delay=balance_delay,
                delta=delta,
            )
    with a.div(
        style=cohost.style(
            {"position": "absolute", "top": "200px", "left": "-60px", "z-index": z}
        )
    ):
        with a.div(style=cohost.style({"transform": "rotate(89deg)"})):
            display_graphic(a, True if win_delay else False, win_delay)
    if wheel_show:
        broken_wheel(a, z=z)
    with a.div(
        style=cohost.style(
            {"position": "absolute", "top": "390px", "left": "260px", "z-index": z}
        )
    ):
        with a.div(style=cohost.style({"transform": "skew(-30deg) scale(1.2, 0.5)"})):
            logo(a)


def bang(a):
    # broken_page(a)

    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            player_say_a(a, "Eggbug?", reveal_t=10, z=5)  # 10
        page(a, z=6)
        shake(a, lambda: display(a, False, z=6))
        shake(a, lambda: balance(a, 0))
        shake(a, lambda: player_say(a, "Eggbug?"))
        shake(a, lambda: wheel_blur(a, 0.123))
        shake(a, lambda: bang_img(a), factor=1.5)
        shake(a, lambda: no_eggbug(a), factor=1)
        shake(a, lambda: eggbug_say(a, ""), factor=1.5)
        with a.div(
            style=cohost.style(
                {
                    "width": f"{page_width}px",
                    "height": "550px",
                    "border": "1px solid black",
                    "position": "absolute",
                    "background-color": "#000000",
                    "z-index": 6,
                }
                | reveal_d(0.7)
            )
        ):
            pass
        with a.div(
            style=cohost.style(
                {"filter": "blur(8px)", "position": "absolute", "z-index": 7}
                | reveal_d(5)
            )
        ):
            broken_page(a, z=7)
        with a.div(
            style=cohost.style({"position": "absolute", "z-index": 7} | reveal_d(10))
        ):
            broken_page(a, z=7)
        ow_my_head(a)


def ow_my_head(a):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            player_say_a(a, "Ow, my head.", reveal_t=14, z=7)
        with a.div(style=cohost.style({"position": "absolute", "z-index": 8})):
            broken_page(a, animate_display=False, page_show=False, wheel_show=False)
            player_say(a, "Ow, my head.")
            player_blocker(a)
            i_want_my_money_back(a)


def i_want_my_money_back(a):
    # broken_page(a, animate_display=False, win_delay=2, balance_delay=4, delta="+5")
    # falling_arrow(a)

    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            player_say_a(a, "Eggbug? I'd like my money back please.", reveal_t=6, z=8)
        with a.div(style=cohost.style({"position": "absolute", "z-index": 9})):
            broken_page(
                a,
                animate_display=False,
                win_delay=2,
                balance_delay=4,
                delta="+$5",
                page_show=False,
                wheel_show=False,
            )
            player_say(a, "Eggbug? I'd like my money back please.")
            player_blocker(a)
            falling_arrow(a)
            with a.div(style=reveal(8)):
                with a.div(
                    style=cohost.style(
                        {
                            "width": f"{page_width}px",
                            "height": "550px",
                            "border": "1px solid black",
                            "position": "absolute",
                            "background-color": "#000000",
                            "display": "flex",
                            "justify-content": "center",
                            "align-items": "center",
                            "font-size": "3rem",
                            "color": "white",
                            "font-family": "cursive",
                        }
                    )
                ):
                    a("fin")


def falling_arrow(a):
    with a.div(
        style=cohost.style(
            {
                "position": "absolute",
                "top": "400px",
                "left": "178px",
                "width": "40px",
                "height": "40px",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {"transform": "translateY(-600px)"}
                | cohost.animation(
                    direction="normal", count=1, duration=0.3, fill="forwards"
                )
            )
        ):
            with a.div(
                style=cohost.style(
                    cohost.animation(
                        direction="normal", count=2, duration=0.15, fill="forwards"
                    )
                )
            ):
                with a.div(style=cohost.style({"transform": "scale(1, -1)"})):
                    with a.div(style=cohost.style({"transform": "translateY(-20px)"})):
                        with a.div(
                            style=cohost.style(
                                {"transform": "scale(1) rotate(16deg)"}
                                | cohost.animation(duration=0.03, count=20)
                            )
                        ):
                            with a.div(
                                style=cohost.style(
                                    {"transform": "translateY(20px) rotate(-8deg)"}
                                )
                            ):
                                a.img(
                                    src=arrow_image,
                                    style=cohost.style({"margin": "0px"}),
                                )


cohost.create_document(body, "post.html")
