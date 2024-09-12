import random
from airium import Airium
import lib.cohost as cohost

DEBUG = False
WIDTH = 350

cohost_image_map = {
    "server": "https://staging.cohostcdn.org/attachment/5049baa9-de65-4599-9823-a7dc93dbc07f/server.png",
    "door_labels": "https://staging.cohostcdn.org/attachment/fb2eee83-3e5b-4a79-b388-d71082394d92/door_labels.png",
    "dark": "https://staging.cohostcdn.org/attachment/07e63e8d-1098-4757-8505-8cfa56be288a/dark.png",
    "light": "https://staging.cohostcdn.org/attachment/5f3bcaba-b0c9-4bfc-9369-e6dda0b43939/light.png",
    "stair_bottom": "https://staging.cohostcdn.org/attachment/1d221d0e-e3df-43d8-8a86-b28585567911/stair_bottom.png",
    "generic_corridor": "https://staging.cohostcdn.org/attachment/b4602237-4a44-4ea0-ad7c-0a28175e8908/generic_corridor.png",
    "stair_top": "https://staging.cohostcdn.org/attachment/98869355-dcf5-42a4-8804-9859310704c2/stair_top.png",
    "cabinet_approach": "https://staging.cohostcdn.org/attachment/0e266651-a607-4d67-bbe2-161af31e54d7/cabinet_approach.png",
    "brushes_cabinet": "https://staging.cohostcdn.org/attachment/71c6ec33-dabc-4960-80f9-1b625250128e/brushes_cabinet.png",
    "brush2_coat": "https://staging.cohostcdn.org/attachment/ed83b6a9-dbc5-4a48-b090-d883d1e5f368/brush2_coat.png",
    "brush1_coat": "https://staging.cohostcdn.org/attachment/75779144-9108-4593-8a14-672d4355d56e/brush1_coat.png",
    "brush2": "https://staging.cohostcdn.org/attachment/34f5d0d7-5a56-4653-9d47-a56dec2680ed/brush2.png",
    "brush1": "https://staging.cohostcdn.org/attachment/b49c83b4-09b9-4fe3-81c2-d6fd9f683cf8/brush1.png",
    "bucket2": "https://staging.cohostcdn.org/attachment/cfdd3448-2f42-494d-b57f-88a603a20ba5/bucket2.png",
    "varnish_empty": "https://staging.cohostcdn.org/attachment/ddcda401-6644-4b5b-812e-964f23dcac48/varnish_empty.png",
    "varnish_full": "https://staging.cohostcdn.org/attachment/8c756324-e5a3-4c75-82b1-1362611fcb55/varnish_full.png",
    "server3": "https://staging.cohostcdn.org/attachment/771c5733-c57c-4e6f-bbaa-986d709721d6/server3.png",
    "lit_clear": "https://staging.cohostcdn.org/attachment/dd2a24d2-76a2-4f83-a4f1-489ef15c119e/lit_clear.png",
}
names = [
    "server",
    "door_labels",
    "dark",
    "light",
    "stair_bottom",
    "generic_corridor",
    "stair_top",
    "cabinet_approach",
    "brushes_cabinet",
    "brush2_coat",
    "brush1_coat",
    "brush2",
    "brush1",
    "bucket2",
    "varnish_empty",
    "varnish_full",
    "server3",
    "lit_clear",
]


local_image_map = {key: f"varnish/processed/{key}.png" for key in names}

image_map = cohost_image_map


def body(a):
    description = """
    A crude point and click game where you take on the role of a server janitor who is paged to resolve FIRST BYTE TIMEOUT errors by varnishing the cache server.
    By clicking on specific parts of the images, you move to new locations. The images are low resolution and severely dithered.
    The main puzzle is figuring out how to find a source of varnish, but also along the way you need to find a hidden location where you can pick up a brush with which you can apply varnish to the cache server at the end of the game.
    """
    cohost.with_description(a, content, description, "crime")
    a("")
    a("---")
    a("")
    with a.a(href="https://cohost.org/rykarn/tagged/my%20games"):
        a("Try my other games!")
    with a.details():
        with a.summary():
            with a.b():
                a("SPOILERS")

        with a.details():
            with a.summary():
                a("I'm unable to make it through the dark corridor!")
            a(
                "There is a light switch to the left of the door to help you see the hazard. Also, even if you can see the hazard, you should remove it before proceeding!"
            )

        with a.details():
            with a.summary():
                a("I need a brush to apply the varnish!")
            a("One of the scenes has a hidden area where you can find a brush.")
            with a.details():
                with a.summary():
                    a("I can't find this hidden area!")
                a(
                    "It is beneath the stairs."
                )
            with a.details():
                with a.summary():
                    a("I need the CORRECT brush to apply the varnish!")
                a(
                    "The light brush to the right in the drawer has the word VARNISH written on it, though it might be hard to see. Be sure to pick up that one!"
                )
        with a.details():
            with a.summary():
                a("I keep getting lost in the catacombs!")
            a("Don't go in the catacombs. Look carefully and you might find a different location to go to instead!")
        with a.details():
            with a.summary():
                a("I want to see all the endings!")
            a("There is 1 good ending and 5 bad endings. Good luck finding them!")


def remap(spec):
    return int(spec * 10 * WIDTH / 424)


def pos2spec(spec):
    return {
        "left": f"{remap(spec[0])}px",
        "top": f"{remap(spec[1])}px",
        "width": f"{remap(spec[2])}px",
        "height": f"{remap(spec[3])}px",
    }


def reveal_d(delay):
    return {"transform": "scale(0)"} | cohost.animation(
        duration=0.01,
        delay=delay,
        direction="normal",
        count=1,
        fill="forwards",
        easing="steps(2, jump-none)",
    )


class Scene:
    def __init__(self, triggers, animate=True):
        self.triggers = triggers
        self.children = []
        self.animate = animate

    def render(self, a, z):
        pass


class ImageScene(Scene):
    def __init__(self, triggers, src, description="", animate=True):
        super().__init__(triggers)
        self.src = src
        self.description = description
        self.children = [Scene([]), Scene([])]
        self.inventory = [(None, False), (None, False)]
        self.animate = animate

    def with_inventory(self, slot, inventory):
        new = ImageScene(
            self.triggers, self.src, self.description, animate=self.animate
        )
        new.inventory = self.inventory.copy()
        new.inventory[slot] = inventory
        new.childern = []
        return new

    def render(self, a, z):
        with a.div(
            style=cohost.style(
                {
                    "display": "grid",
                    "grid-template-columns": "1fr",
                    "grid-template-rows": "1fr",
                }
            )
        ):
            with a.div(
                style=cohost.style(
                    {"grid-column": "1 / span 1", "grid-row": "1 / span 1"}
                )
            ):
                a.img(src=image_map[self.src], style=cohost.style({"margin": "0px"}))
            with a.div(
                style=cohost.style(
                    {"grid-column": "1 / span 1", "grid-row": "1 / span 1"}
                )
            ):
                with a.div(
                    style=cohost.style(
                        {
                            "transform": "scale(1, 0.0001)",
                            "transform-origin": "bottom right",
                        }
                        | (
                            cohost.animation(
                                direction="reverse",
                                count=1,
                                delay=0.3 if self.animate else 0,
                                duration=0 if (DEBUG or not self.animate) else 0.8,
                                fill="both",
                                easing="steps(10, jump-end)",
                            )
                        )
                    )
                ):
                    with a.div(
                        style=cohost.style(
                            {
                                "width": "100%",
                                "height": f"{WIDTH}px",
                                "background-color": "black",
                            }
                        )
                    ):
                        pass
        with a.div(
            style=cohost.style(
                {
                    "width": "100%",
                    "height": "6rem",
                    "background-color": "black",
                    # "color": "white",
                    # "font-family": "monospace",
                    "display": "flex",
                    "flex-direction": "column",
                    "gap": "1rem",
                    "padding-top": "1rem",
                }
            )
        ):
            a(self.description)
        with a.div(
            style=cohost.style(
                {
                    "width": "100%",
                    "background-color": "black",
                    # "font-family": "monospace",
                    "display": "flex",
                    "justify-content": "space-evenly",
                }
            )
        ):
            for item, selected in self.inventory:
                with a.div(
                    style=cohost.style(
                        {
                            "width": "60px",
                            "aspect-ratio": "1",
                            "background-color": "#000000",
                            "border": "6px solid {}".format(
                                "#ffff00" if selected else "#222222"
                            ),
                        }
                    )
                ):
                    if item:
                        a.img(
                            src=image_map[item], style=cohost.style({"margin": "0px"})
                        )


class GameOverScene(Scene):
    def __init__(self, prompt, result, win=False):
        super().__init__([])
        self.prompt = prompt
        self.result = result
        self.win = win

    def render(self, a, z):
        with a.div(
            style=cohost.style(
                {
                    "width": "100%",
                    "height": "100%",
                    "background-color": "black",
                    # "color": "white",
                    # "font-family": "monospace",
                    "display": "flex",
                    "flex-direction": "column",
                    "gap": "1rem",
                }
            )
        ):
            with a.div(style=cohost.style({"display": "flex"})):
                with a.div(style=cohost.style({})):
                    a("> ")
                with a.div(
                    style=cohost.style(
                        {
                            "display": "grid",
                            "grid-template-columns": "1fr",
                            "grid-template-rows": "1fr",
                        }
                    )
                ):
                    with a.div(
                        style=cohost.style(
                            {"grid-column": "1 / span 1", "grid-row": "1 / span 1"}
                        )
                    ):
                        with a.div(style=cohost.style({'display': 'flex'})):
                            with a.div(style=cohost.style({})):
                                a(self.prompt)
                            with a.div(
                                style=cohost.style(
                                    {"transform": "scale(0)"}
                                    | cohost.animation(
                                        easing="steps(2, jump-none)", direction="normal", delay=1.3
                                    )
                                )
                            ):
                                a("|&nbsp;")
                    with a.div(
                        style=cohost.style(
                            {"grid-column": "1 / span 1", "grid-row": "1 / span 1"}
                        )
                    ):
                        with a.div(
                            style=cohost.style(
                                {
                                    "transform": "scale(0.0001, 1)",
                                    "transform-origin": "top right",
                                }
                                | cohost.animation(
                                    direction="reverse",
                                    count=1,
                                    delay=1,
                                    duration=0.3,
                                    fill="both",
                                )
                            )
                        ):
                            with a.div(
                                style=cohost.style(
                                    {
                                        "width": "100%",
                                        "height": "calc(18px)",
                                        "background-color": "black",
                                    }
                                )
                            ):
                                pass

            with a.div(style=cohost.style({} | reveal_d(3))):
                if type(self.result) == list:
                    with a.div(
                        style=cohost.style(
                            {
                                "display": "flex",
                                "flex-direction": "column",
                                "gap": "1rem",
                            }
                        )
                    ):
                        for paragraph in self.result:
                            with a.p(style=cohost.style({"margin": "0px"})):
                                a(paragraph)
                else:
                    a(self.result)
            if not self.win:
                with a.div(style=cohost.style({} | reveal_d(6))):
                    a("FIRST BYTE TIMEOUT")
                    a.br()
                    a("You have failed to Varnish the Cache Server.")
                with a.div(style=cohost.style({} | reveal_d(8))):
                    a("Click 'read more' below to restart.")
            else:
                with a.div(style=cohost.style({} | reveal_d(8))):
                    a("Thank you for playing Cache Server Varnishing Game!")
                    a.br()
                    a("Programming and photography by @rykarn.")


class StartScene(Scene):
    def __init__(self, prompts):
        super().__init__([[0, 0, 42, 42]])
        self.prompts = prompts

    def render(self, a, z):
        with a.div(
            style=cohost.style(
                {
                    "width": "100%",
                    "height": "100%",
                    "background-color": "black",
                    # "color": "white",
                    # "font-family": "monospace",
                    "display": "flex",
                    "flex-direction": "column",
                    "gap": "1rem",
                }
            )
        ):
            for prompt in self.prompts:
                with a.p(style=cohost.style({"margin": "0px"})):
                    a(prompt)


start = StartScene(
    [
        "Your phone beeps in the night. A new notification, highest priority:",
        "<b>CRITICAL WARNING: Cache Server Varnish Levels low! Varnish Cache Server!</b>",
        "Startled, you immediately make your way to the Server Hall. You must Varnish the Cache Server before it is too late.",
        "Click to begin.",
    ]
)
start.animate = False
server = ImageScene(
    [[30, 2, 10, 38]],
    "server3",
    "You see the Cache Server. Its Varnish Levels are critically low.",
)
labeled_doors = ImageScene(
    [[5, 2, 15, 38], [24, 2, 15, 38]],
    "door_labels",
    "You see a door leading to the Catacombs and a door leading to the Varnish Storage.",
)
generic_corridor = ImageScene(
    [[16, 6, 9, 16]],
    "generic_corridor",
    "You see a Corridor.",
)
dark = ImageScene(
    [[6, 11, 6, 6], [12, 2, 20, 34]],
    "dark",
    "You see a Dark Corridor.",
)
lit = ImageScene(
    [[18, 22, 10, 8], [18, 4, 12, 17]],
    "light",
    "You see a Corridor containing a Foreign Object.",
)
lit_clear = ImageScene(
    [[13, 2, 20, 34]],
    "lit_clear",
    "You move the Foreign Object aside.",
)
game_over_failed_clear = GameOverScene(
    "enter corridor",
    "You walk down the corridor, but due to your failure to remove the Foreign Object from your path, you still end up tripping over it. You are knocked unconscious.",
)
stair_bottom = ImageScene(
    [[12, 0, 20, 20], [23, 22, 8, 20]],
    "stair_bottom",
    "You see the Bottom of the Stairwell.",
)
cabinet_approach = ImageScene(
    [[12, 14, 15, 15]],
    "cabinet_approach",
    "You see a Brush Cabinet.",
)
cabinet_open = ImageScene(
    [[10, 20, 17, 17], [28, 20, 8, 17]],
    "brushes_cabinet",
    "You open the Brush Drawer. You see several Brushes.",
)
game_over_catacombs = GameOverScene(
    "enter the catacombs",
    "You enter the Catacombs. You immediately get lost within its dark hallways and corridors. By the time you manage find your way back to the Server Facility, the Cache Server has already failed catastrophically due to low Varnish Levels.",
)
game_over_dark = GameOverScene(
    "enter the dark corridor",
    "You enter the Dark Corridor. Because of the insufficient light, you fail to notice a Foreign Object located in the middle of the floor. You trip and are knocked unconscious.",
)
stair_top = ImageScene(
    [[6, 8, 20, 22]],
    "stair_top",
    "You reach the Top of the Stairwell.",
)
varnish_full = ImageScene(
    [[18, 23, 10, 10]],
    "varnish_full",
    "You see the Varnish Storage Shelf.",
)
varnish_empty = ImageScene(
    [[2, 14, 11, 22]],
    "varnish_empty",
    "You collect a Varnish Bucket.",
).with_inventory(0, ("bucket2", False))
server_final = ImageScene(
    [[8, 53, 10, 10]],
    "server",
    "You return to the Server Hall. You see the Cache Server.",
).with_inventory(0, ("bucket2", False))
server_final_bucket = ImageScene(
    [[10, 10, 20, 30]],
    "server",
    "You select the Varnish Bucket.",
    animate=False,
).with_inventory(0, ("bucket2", True))
game_over_bucket = GameOverScene(
    "pour varnish over server",
    "You pour the contents of the Varnish Bucket onto the Cache Server. The server fails immediately and catastrophically due to severe overvarnishing. Standard Operating Procedures require that Varnishing Operations are only to be carried out using an approved Varnishing Brush.",
)

# paint brush server
server_final_paint = server_final.with_inventory(1, ("brush1", False))
server_final_paint.triggers = [[24, 53, 10, 10]]
server_final_paint.animate = True
server_final_paint_selected = server_final_paint.with_inventory(1, ("brush1", True))
server_final_paint_selected.description = "You select the Paint Brush."
server_final_paint_selected.triggers = [[8, 53, 10, 10]]
server_final_paint_selected.animate = False
server_final_paint_coated = server_final_paint.with_inventory(1, ("brush1_coat", True))
server_final_paint_coated.description = "You coat the Paint Brush with Varnish."
server_final_paint_coated.triggers = [[10, 10, 20, 30]]
server_final_paint_coated.animate = False
game_over_paint = GameOverScene(
    "use paint brush on server",
    "You apply a layer of Varnish to the Cache Server using the Varnish-coated Paint Brush. Due to the Paint Brush not conforming to the standards outlined in Varnishing Implement Specifications, Section 2.3 (b) (2) (Annexe A), the resulting layer of Varnish is not sufficient for resolving the low Varnish Levels of the Cache Server. The Cache Server fails catastrophically despite your efforts.",
)

# varnish brush server
server_final_varnish = server_final.with_inventory(1, ("brush2", False))
server_final_varnish.animate = True
server_final_varnish.triggers = [[24, 53, 10, 10]]
server_final_varnish_selected = server_final_varnish.with_inventory(1, ("brush2", True))
server_final_varnish_selected.description = "You select the Varnish Brush."
server_final_varnish_selected.triggers = [[8, 53, 10, 10]]
server_final_varnish_selected.animate = False
server_final_varnish_coated = server_final_varnish.with_inventory(
    1, ("brush2_coat", True)
)
server_final_varnish_coated.description = "You coat the Varnish Brush with Varnish."
server_final_varnish_coated.triggers = [[10, 10, 20, 30]]
server_final_varnish_coated.animate = False
game_over_varnish = GameOverScene(
    "use varnish brush on server",
    [
        "You expertly apply a layer of Varnish to the Cache Server using the Varnish-coated Varnish Brush. A notification appears on your phone:",
        "<b>RESOLVED: Cache Server Varnish Levels Nominal.</b>",
        "You have Varnished the Cache Server.",
    ],
    win=True,
)


start.children = [server]
server.children = [dark]
dark.children = [lit, game_over_dark]
lit.children = [lit_clear, game_over_failed_clear]
lit_clear.children = [generic_corridor]
generic_corridor.children = [stair_bottom]
stair_bottom.children = [stair_top, cabinet_approach]
cabinet_approach.children = [cabinet_open]


stair_top.children = [labeled_doors]
labeled_doors.children = [game_over_catacombs, varnish_full]
varnish_full.children = [varnish_empty]
varnish_empty.children = [server_final]
server_final.children = [server_final_bucket]
server_final_bucket.children = [game_over_bucket]

server_final_paint.children = [server_final_paint_selected]
server_final_paint_selected.children = [server_final_paint_coated]
server_final_paint_coated.children = [game_over_paint]

server_final_varnish.children = [server_final_varnish_selected]
server_final_varnish_selected.children = [server_final_varnish_coated]
server_final_varnish_coated.children = [game_over_varnish]


# paint brush
stair_bottom_p = stair_bottom.with_inventory(1, ("brush1", False))
stair_bottom_p.description = "You take a Paint Brush from the Brush Drawer."
stair_top_p = stair_top.with_inventory(1, ("brush1", False))
labeled_doors_p = labeled_doors.with_inventory(1, ("brush1", False))
varnish_full_p = varnish_full.with_inventory(1, ("brush1", False))
varnish_empty_p = varnish_empty.with_inventory(1, ("brush1", False))
server_final_p = server_final.with_inventory(1, ("brush1", False))

stair_bottom_p.children = [stair_top_p]
stair_top_p.children = [labeled_doors_p]
labeled_doors_p.children = [game_over_catacombs, varnish_full_p]
varnish_full_p.children = [varnish_empty_p]
varnish_empty_p.children = [server_final_paint]

# paint brush
stair_bottom_v = stair_bottom.with_inventory(1, ("brush2", False))
stair_bottom_v.description = "You take a Varnish Brush from the Brush Drawer."
stair_top_v = stair_top.with_inventory(1, ("brush2", False))
labeled_doors_v = labeled_doors.with_inventory(1, ("brush2", False))
varnish_full_v = varnish_full.with_inventory(1, ("brush2", False))
varnish_empty_v = varnish_empty.with_inventory(1, ("brush2", False))
server_final_v = server_final.with_inventory(1, ("brush2", False))

stair_bottom_v.children = [stair_top_v]
stair_top_v.children = [labeled_doors_v]
labeled_doors_v.children = [game_over_catacombs, varnish_full_v]
varnish_full_v.children = [varnish_empty_v]
varnish_empty_v.children = [server_final_varnish]

cabinet_open.children = [stair_bottom_p, stair_bottom_v]


starting_scene = start


def scene(a, s, z, trigger, animate):
    with a.details():
        with a.summary(style=cohost.style({"font-size": 0})):
            with a.div(
                style=cohost.style(
                    {
                        "position": "absolute",
                        "background-color": "red",
                        "opacity": "30%" if DEBUG else "0%",
                        "cursor": "pointer",
                        "z-index": z,
                    }
                    | pos2spec(trigger)
                    | (reveal_d(0 if (DEBUG or not animate) else 1.3))
                )
            ):
                pass
        with a.div(
            style=cohost.style(
                {
                    "z-index": z + 1,
                    "position": "absolute",
                    "height": "600px",
                    "width": f"{WIDTH}px",
                }
            )
        ):
            s.render(a, z)
        for c, t in zip(s.children, s.triggers):
            scene(a, c, z + 2, t, s.animate)


def content(a):
    with a.div(
        style=cohost.style(
            {
                "position": "relative",
                "height": "600px",
                "width": f"{WIDTH}px",
                "background-color": "black",
                "font-family": "monospace",
                "color": "white",
                "font-size": "12px",
            }
        )
    ):
        with a.div(
            style=cohost.style(
                {
                    "z-index": 0,
                    "position": "absolute",
                    "height": "600px",
                    "width": f"{WIDTH}px",
                }
            )
        ):
            starting_scene.render(a, 0)
        for c, t in zip(starting_scene.children, starting_scene.triggers):
            scene(a, c, 1, t, starting_scene.animate)


cohost.create_document(body, "post.html")
