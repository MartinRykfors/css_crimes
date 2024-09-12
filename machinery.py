import random
from airium import Airium
import lib.cohost as cohost
import textwrap

image_map = {
    "stair_detail1": "https://staging.cohostcdn.org/attachment/c2353e0a-60aa-4837-9899-15b3325c13fe/stair_detail1.jpg",
    "stair_detail2": "https://staging.cohostcdn.org/attachment/36af29fb-0d1f-42b9-a186-19821f225032/stair_detail2.jpg",
    "sw_1": "https://staging.cohostcdn.org/attachment/67773e17-3cd8-43ef-a7f4-81ade06f019a/sw_1.jpg",
    "s_well": "https://staging.cohostcdn.org/attachment/51435c35-aa67-40d2-9cc5-d1ee9ce6a9c1/s_well.jpg",
    "vent1": "https://staging.cohostcdn.org/attachment/39e4d78c-a246-4eba-bec6-bca65a154774/vent1.jpg",
    "vent2": "https://staging.cohostcdn.org/attachment/fd8733be-cb78-44a6-805d-9f4338a0db57/vent2.jpg",
    "ne4": "https://staging.cohostcdn.org/attachment/96ac3bc8-0baf-4d7c-878a-d41d94b151f4/ne4.jpg",
    "ne5": "https://staging.cohostcdn.org/attachment/693918f7-c88d-46e8-934a-39717abc64b5/ne5.jpg",
    "nw_detail1": "https://staging.cohostcdn.org/attachment/03128be8-c1f0-4114-97b2-1738da47371e/nw_detail1.jpg",
    "nw_detail2": "https://staging.cohostcdn.org/attachment/4e827256-fb2d-42c9-802b-74e07b3174af/nw_detail2.jpg",
    "nw_detail3": "https://staging.cohostcdn.org/attachment/66eab803-b5b0-4807-8d33-ba67a3a41713/nw_detail3.jpg",
    "pillar1": "https://staging.cohostcdn.org/attachment/b843791e-10a0-462d-91aa-4f3313e56cba/pillar1.jpg",
    "pillar2": "https://staging.cohostcdn.org/attachment/8fda2f13-9231-4c28-99a0-0f5cab4cb65a/pillar2.jpg",
    "pillar3": "https://staging.cohostcdn.org/attachment/f99351a2-c646-41ea-9dcd-c8ed91c71574/pillar3.jpg",
    "pipes1": "https://staging.cohostcdn.org/attachment/f53fa8a7-548a-4fc8-8557-2811aeed9548/pipes1.jpg",
    "s1": "https://staging.cohostcdn.org/attachment/52241564-63f1-4aff-9221-bd4b3ccedb05/s1.jpg",
    "s2": "https://staging.cohostcdn.org/attachment/02dee91c-fc49-49de-b580-47e82b807b8e/s2.jpg",
    "seismic": "https://staging.cohostcdn.org/attachment/d8927a26-118e-40f7-ad20-2739fa43c06c/seismic.jpg",
    "sniper_room": "https://staging.cohostcdn.org/attachment/8c108a23-dab0-41f8-bf05-fd45ef161c55/sniper_room.jpg",
    "sniper_stair": "https://staging.cohostcdn.org/attachment/cae242c7-9393-42de-8cbc-a2bd0dc0364c/sniper_stair.jpg",
    "big_stair3": "https://staging.cohostcdn.org/attachment/92fc614f-adf2-463b-a4ed-9c41ccc1199b/big_stair3.jpg",
    "big_stair": "https://staging.cohostcdn.org/attachment/7084eba5-d744-461b-aae3-ba7a01713bde/big_stair.jpg",
    "big_stair2": "https://staging.cohostcdn.org/attachment/5c28acb8-8505-4a81-8964-a388f4ea6d42/big_stair2.jpg",
    "e1": "https://staging.cohostcdn.org/attachment/2aaacc08-9df3-4552-bca7-ac879255f946/e1.jpg",
    "extrusion1": "https://staging.cohostcdn.org/attachment/34e6e823-d8ab-44a8-8755-c0366c27b246/extrusion1.jpg",
    "extrusion2": "https://staging.cohostcdn.org/attachment/006277a6-b07f-46d2-9c2f-ab3c71a7ab3a/extrusion2.jpg",
    "extrusion3": "https://staging.cohostcdn.org/attachment/e6d9bb90-3f93-4a9d-b6ee-5fed4be2aa2f/extrusion3.jpg",
    "gear1": "https://staging.cohostcdn.org/attachment/b8d91055-c291-4372-9d18-52065b8dfc65/gear1.jpg",
    "maplist": "https://staging.cohostcdn.org/attachment/0aec2173-db2d-4b70-b65b-24b6dc55f473/maplist.jpg",
    "n1": "https://staging.cohostcdn.org/attachment/073813d3-d323-42b4-9476-67f3edacb34e/n1.jpg",
    "n2": "https://staging.cohostcdn.org/attachment/567aeac9-1128-49ba-bbfd-d71f15669b70/n2.jpg",
    "n3": "https://staging.cohostcdn.org/attachment/4ece807e-ed44-4c28-9646-26cbda704f25/n3.jpg",
    "n4": "https://staging.cohostcdn.org/attachment/d78e97e8-bf5d-400d-b812-f6c9c704b2ec/n4.jpg",
    "ne1": "https://staging.cohostcdn.org/attachment/5181e417-9bd9-40cf-9fe6-96765fa53b98/ne1.jpg",
    "ne2": "https://staging.cohostcdn.org/attachment/5177a969-3b2c-4abb-b6b0-550fd0d1a628/ne2.jpg",
    "ne3": "https://staging.cohostcdn.org/attachment/599d8359-edfc-4d05-9f6b-d3500c8676d2/ne3.jpg",
    "sw_2": "https://staging.cohostcdn.org/attachment/65a6a99b-4bbd-4f84-a0da-5ece756b5398/sw_2.jpg",
    "down_well": "https://staging.cohostcdn.org/attachment/f00aea2f-c823-4382-96b1-fe2666b77e03/down_well.gif",
    "driveshaft": "https://staging.cohostcdn.org/attachment/5b4891de-43d3-4c25-be37-1c11e6455de4/driveshaft.gif",
    "through": "https://staging.cohostcdn.org/attachment/82794df2-307d-4fa5-a015-3f45d375855f/through.gif",
    "elevator": "https://staging.cohostcdn.org/attachment/7a75785c-fa22-40a4-af39-d79bbb34a93b/elevator.gif",
}

grid2 = {
    "display": "grid",
    "grid-template-columns": "repeat(2, 1fr)",
    "gap": "10px",
    "margin-bottom": "2rem",
}


def image(a, image_id, alt=""):
    with a.figure(style=cohost.style({"margin": "0.5rem"})):
        with a.a(href=image_map[image_id]):
            a.img(src=image_map[image_id], style=cohost.style({"margin": "0px"}))
        if alt:
            with a.figcaption():
                with a.span(style=cohost.style({"font-size": "0.8rem"})):
                    a(alt)


def section(a, title):
    with a.h3():
        a(title)


def prose(a, content):
    a(textwrap.dedent(content))


def body(a):
    prose(
        a,
        """
    (Note: All screenshots in this post can be clicked for a big version.)

    Every map would also come with a written piece of lore that would be displayed at the map selection screen. So again, time to dig into the the written prose of 15-year-old me.

    """,
    )
    image(a, "maplist")
    prose(
        a,
        """I am repeating this to myself: <i>Destroy the part of you that cringes, not the part of you that is cringe.</i> I am trying my hardest to do this, but cringing about myself is just such a deeply ingrained behavior in me (something I am genuinely trying to address). I was dreading this part, just reading the map description. And to be honest, while it is kind of excessive and the sentence structure leaves a bit to be desired, I will give myself this: It is decent. Good even. Really, it is an excellent map description considering it is written by a 15-year old kid whose native language is not English. Well done past-me. Now that I'm an adult with a degree and a job, a thing I have often been complimented for is my ability to communicate in text, in particular communicating about technical topics in a way understandable by many. And I guess the beginnings of that can be seen here? Sure it is not techincal writing, but damn, I get the point across. This is about machinery. Spinning gears and driveshafts. Seismic activity. Unpleasant environments.""",
    )
    prose(
        a,
        """

    Now, let's play!

    <h3>The Layout</h3>

    The map is divided into three main rooms with corridors connecting them. There are two levels with stairs and lifts connecting the levels at different places.

    We start in the <b>southwest room</b>:
    """,
    )
    with a.div(style=cohost.style(grid2)):
        image(
            a,
            "sw_1",
            alt="The southwest room, looking southeast. The hole up high on the south wall houses the Double Damage. I don't remember the details with the pipes lining the wall. They look cool!",
        )
        image(
            a,
            "sw_2",
            alt="Looking out over the southwest room from the Double Damage spot.",
        )

    prose(
        a,
        """

    ---

    """,
    )

    prose(
        a,
        """
    Let's head to the southern room, <b>the courtyard</b>:
    """,
    )

    with a.div(style=cohost.style(grid2)):
        image(a, "s1", alt="Some nice brushwork on the walls.")
        image(
            a,
            "s2",
            alt="The same brushwork on the opposite wall. The gear-tooth trim was made by me in Lightwave.",
        )
        image(
            a,
            "seismic",
            alt="Looking south. I love how what I in the description refer to as 'nearby seismic activity' means 'the entire place is situated inside a dang volcano'.",
        )
        image(
            a,
            "vent1",
            alt="A walkway along the southern wall leads to an elevator taking you up to the Double Damage pickup that we saw in the south west room.",
        )

    prose(
        a,
        """
    The vents along the southern walkway played a bigger role in initial versions of the map.
    """,
    )

    image(a, "vent2")

    prose(
        a,
        """
    These vents were programmed to spew fire at regular intervals in order to make getting the Double Damage a risky proposition. It was pretty elaborate, particle emitters would be triggered, sound effects would play and kill volumes would be activated to kill any player standing in the way. Early feedback on the map stated that this is not a good idea to have in a duel map, so it was cut out early.
    """,
    )
    prose(
        a,
        """

    Let's go back to the courtyard and jump down the hole to the lower levels!
    """,
    )

    with a.div(style=cohost.style(grid2)):
        image(a, "s_well", alt="Looking down the well housing the shield pickup.")
        image(
            a,
            "pillar1",
            alt="Heading east, looking back towards the well we dropped down from. Big cutouts in the walls reveal rotating driveshafts with universal joints.",
        )
        image(a, "pillar2", alt="Always treat rotating machinery with respect.")
        image(
            a,
            "pillar3",
            alt="The other side of the corridor has this weird pillar and some ammo pickups.",
        )

    prose(
        a,
        """

    Following the corridor east leads us to a staircase to the upper level and the eastern corridor connecting the courtyard with the big interior room.
    """,
    )

    image(
        a,
        "e1",
        alt="The eastern corridor. The big interior room can be seen to the right. Some nice brushwork on the walls, though I wish I had lit it up more so that these details could be seen better. The light fixtures were designed by me in Ligthtwave and I absolutely love the way they cast shadows on the walls!"
        "",
    )

    prose(
        a,
        """

    Let's head into the <b>interior room</b>. This room spans the entire northern part of the map and has a lot of different features.
    """,
    )

    with a.div(style=cohost.style(grid2)):
        image(
            a,
            "ne4",
            alt="Looking into the interior room. The theme of round features with gear teeth was something I tried to maintain consistently in the map.",
        )
        image(
            a,
            "ne2",
            alt="Entering the interior room, looking back at the eastern corridor from which we came.",
        )
        image(
            a,
            "ne1",
            alt="I was really proud of how the suspended gantry platform looked. The ceiling lights could probably have been positioned better to light up more of the details present in this scene.",
        )
        image(
            a,
            "n4",
            alt="Moving further into the interior room, still looking back east. Some really cool details here like the geartooth platform! Again I wish I had taken the opportunity to light them up better! A small passage leading upstairs to the sniper room can be seen in the center.",
        )
        image(
            a,
            "sniper_stair",
            alt="Heading upstairs into the sniper room. Ceiling windows reveal the same kind of architectural detail that we saw in the courtyard, on the opposite side of the map.",
        )
        image(
            a,
            "sniper_room",
            alt="The sniper room with some chutes leading out to the gantry room.",
        )

    prose(
        a,
        """
    <h3>The Brushwork</h3>

    By now we have seen most of the map, but I would like to take a moment to talk about brushes and UT mapping.

    As I mentioned in a previous post, a map consists of <i>brushes</i>. A <i>subtractive</i> brush carves out negative space out of solid-wall-space, while <i>additive</i> brushes create solid walls and objects. Brushes are made out of coarse geometries, cubes, cylinders and such. In Untreal Tournament mapping, you only used these brushes to build a level. With UT2k3 came <i>static meshes</i>, prefabricated 3D assets that could be added to the map. We have seen a mixutre of brushes and static meshes in these screenshots. All the big architectural elements are brushes and the detailed bits like the gear trim and light fixtures are static meshes for instance.

    I think there was a tendency for beginner mappers to rely too much on static meshes. Sure, they looked nice were much more detailed than a brush could ever be, but relying too much on just static meshes tended to create maps that were only box rooms with static meshes thrown in in an attempt to create detail. And those maps ended up looking just like that - box rooms with static meshes thrown in. What I think set good maps apart from beginner maps was that good maps would rely on a more elaborate composition of brushwork to create dedicated space and architecture in which the static meshes could live. The brushes set the stage so that the static meshes could really shine. And I think this is something my 15-year old self was starting to get the hang of!
    """,
    )

    with a.div(style=cohost.style(grid2)):
        image(
            a,
            "nw_detail1",
            alt="In the western part of the interior room. Note the square hole carved into the ceiling, in which a more detailed static mesh lives. Additional brushes create trim around the hole, making a nice contour to separate the ceiling texture from the hole.",
        )
        image(
            a,
            "nw_detail3",
            alt="Dropping down a level, looking at the western wall. Brushes with basic geometry carve out space for light sources (the cold green windows and the hot orange lights). The brick textures on the brushes themselves are properly aligned around the corners. <i>I absolutely love this.</i>",
        )
        image(
            a,
            "nw_detail2",
            alt="A bit of detail on the wall. A part of the top of this wall cutot was carved out in order to frame the light fixture above it. I love this too!",
        )
        image(
            a,
            "ne3",
            alt="Using brushes to create space in which the pipes with the cool-looking valve wheels can live.",
        )

    prose(
        a,
        """
    <h3>The Moving Parts</h3>

    The map was heavily inspired by a set of static meshes consisting of rusty gears and pulleys and it would not be worthy of the name 'Machinery' if it did not feature actual moving machinery.
    """,
    )
    with a.div(style=cohost.style(grid2)):
        image(a, "driveshaft", alt="")
        image(a, "through", alt="")
        image(a, "down_well", alt="")
        image(a, "elevator", alt="")

    prose(a, """
    <h3>And we're done (almost)</h3>

    PHEW! That was a lot of screenshotting and video capturing and reminiscing about something I made 20 years ago, and not seen again for almost as long. I am very happy I was able to make this post as it has been an idea I've been thinking about following through on for a very long time. If you made it this far, <b>thank you so much for reading! ❤️</b>

    I am not fully done though. I will follow up with a shorter post cataloguing things from after the map was released - how it was received and being contacted by an actual game studio looking for level designers for instance.
    """)


cohost.create_document(body, "post.html", source_minify=True)
