from airium import Airium
import lib.cohost as cohost
import random

a = Airium(base_indent="")

button_size = 40
button_left = 50
button_top = 250

sticks_top = 150

egg_top = 0
egg_left = 60

random_move = [3, 1, 2, 1, 3]

egg_style = {
    "position": "absolute",
    "top": f"{egg_top}px",
    "left": f"{egg_left}px",
    "z-index": 1,
    # "background-color": "white",
    "width": "80px",
    "height": "80px",
    "display": "flex",
    "align-items": "center",
}


def optimal(n):
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 3
    if n == 5:
        return 1

    r = (n - 1) % 4
    if r == 0:
        return random_move.pop()
    return r


num_sticks = 15


def body(a):
    cohost.with_description(
        a,
        game,
        (
            "15 matchsticks are laid out in a row. Eggbug sits on the other side of the matchsticks relative to you. "
            "Three buttons can be clicked, each one causing you to take either one, two or three matchsticks from the table. "
            "Whenever you click a button, Eggbug will also remove one, two or three matchsticks from the table. "
            "If you lose the game, eggbug will encourage you to try again. If you win, eggbug becomes happy and congratulates you."
        ),
        "matchstick",
    )
    a(
        "Take turns to draw one, two or three sticks from the board. Whoever has to draw the last stick "
    )
    with a.b():
        a("loses!")
    a("")
    a("---")
    a("")
    a(
        "Fun facts: Training the eggbugg Machine Learning AI for playing this Matchstick game generated approx. 3000 metric tons of carbon dioxide."
    )
    a(
        "Each game played requires the weekly energy consumption of an average Swedish household."
    )


def game(a):
    with a.div(
        style=cohost.style(
            {
                "width": "400px",
                "height": "315px",
                # 'background-color': 'red',
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "position": "absolute",
                    "top": "0px",
                    "height": "0px",
                }
            )
        ):
            with a.div(style=cohost.style(egg_style)):
                a.img(
                    src="https://cohost.org/static/17aa2d48956926005de9.png",
                    style=cohost.style(
                        {
                            "width": "80px",
                            "height": "80px",
                        }
                    ),
                )

            for initial_move in range(1, 4):
                game_state(a, [initial_move, optimal(num_sticks - initial_move)])
            with a.div(
                style=cohost.style(
                    {
                        "position": "absolute",
                        "top": f"{sticks_top}px",
                        "left": "20px",
                        "z-index": 0,
                        "background-color": "white",
                    }
                )
            ):
                draw_sticks(a, num_sticks, [])


def game_state(a, moves):
    print("iteration: {}".format(moves))
    remaining = num_sticks - sum(moves)
    print("remaining {}".format(remaining))

    from_player_move = moves[-2] if moves else None
    print("from_player_move {}".format(from_player_move))
    with a.details():
        if from_player_move:
            with a.summary(style=cohost.style({"font-size": 0})):
                left = button_left * from_player_move
                with a.a(
                    style=cohost.style(
                        {
                            "width": f"{button_size}px",
                            "height": f"{button_size}px",
                            "left": f"{left}px",
                            "top": f"{button_top}px",
                            "background-color": "green",
                            "position": "absolute",
                            "font-size": "1.5rem",
                            "z-index": len(moves),
                            "display": "flex",
                            "justify-content": "center",
                        }
                    )
                ):
                    a(from_player_move)

        draw_eggbug(a, remaining, moves)

        if remaining >= 2:
            game_state(a, moves + [1, optimal(remaining - 1)])
        else:
            draw_blocker(a, len(moves), button_left * 1)
        if remaining >= 3:
            game_state(a, moves + [2, optimal(remaining - 2)])
        else:
            draw_blocker(a, len(moves), button_left * 2)
        if remaining >= 4:
            game_state(a, moves + [3, optimal(remaining - 3)])
        else:
            draw_blocker(a, len(moves), button_left * 3)

        with a.div(
            style=cohost.style(
                {
                    "position": "absolute",
                    "top": f"{sticks_top}px",
                    "left": "20px",
                    "z-index": len(moves),
                    "background-color": "white",
                }
            )
        ):
            draw_sticks(a, remaining, moves)

        if remaining <= 1:
            return


def draw_blocker(a, z, left):
    a.div(
        style=cohost.style(
            {
                "width": f"{button_size}px",
                "height": f"{button_size}px",
                "left": f"{left}px",
                "top": f"{button_top}px",
                "background-color": "grey",
                "position": "absolute",
                "z-index": z + 1,
            }
        )
    )


def draw_eggbug(a, remaining, moves):
    if moves and moves[-1] == 0:
        with a.div(style=cohost.style(egg_style | {"width": "400px", "z-index": 3})):
            a.img(
                src="https://cohost.org/static/d7ec7f057e6fb15a94cc.png",
                style=cohost.style(
                    {
                        "width": "80px",
                        "height": "80px",
                    }
                ),
            )

            with a.div(style=cohost.style({})):
                a("You win! Well done!")
            return

    if remaining == 5:
        with a.div(style=cohost.style(egg_style)):
            a.img(
                src="https://cohost.org/static/c4f3f2c6b9ffb85934e7.png",
                style=cohost.style(
                    {
                        "width": "80px",
                        "height": "80px",
                    }
                ),
            )
            return

    if 2 <= remaining <= 4:
        with a.div(style=cohost.style(egg_style | {"z-index": 2})):
            a.img(
                src="https://cohost.org/static/b25a9fdf230219087003.png",
                style=cohost.style(
                    {
                        "width": "80px",
                        "height": "80px",
                    }
                ),
            )
            return

    if remaining == 1:
        with a.div(style=cohost.style(egg_style | {"width": "300px", "z-index": 3})):
            a.img(
                src="https://cohost.org/static/3bc3a1c5272e2ceb8712.png",
                style=cohost.style(
                    {
                        "width": "80px",
                        "height": "80px",
                    }
                ),
            )

            a("I win! Click the read more link to try again!")
            return


def draw_sticks(a, remaining, moves):
    random.seed(3)
    with a.div(style=cohost.style({"display": "flex"})):
        player_move = True
        for move in moves:
            for _ in range(move):
                r = random.random() * 8.0 - 4.0
                with a.div(
                    style=cohost.style(
                        {
                            "width": "5px",
                            "height": "50px",
                            "margin": "5px",
                            "background-color": "orange",
                            # "transform": f"translateY(-30px) rotate({r}deg)"
                            # if player_move
                            # else f"translateY(30px) rotate({r}deg)",
                            "transform": f"translateY(30px)"
                            if player_move
                            else f"translateY(-30px)",
                        }
                    )
                ):
                    pass

            player_move = not player_move

        for _ in range(remaining):
            with a.div(
                style=cohost.style(
                    {
                        "width": "5px",
                        "height": "50px",
                        "margin": "5px",
                        "background-color": "orange",
                    }
                )
            ):
                pass


cohost.create_document(body, "post.html")
