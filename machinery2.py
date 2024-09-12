import random
from airium import Airium
import lib.cohost as cohost
import textwrap

image_map = {"n1": "machinery/n1.jpg"}


def image(a, image_id, alt):
    with a.a(href=image_map[image_id]):
        a.img(src=image_map[image_id], alt=alt)


def code_block(a, content):
    lines = content.split("\n")
    with a.div(
        style=cohost.style(
            {
                "font-family": "monospace",
                "color": "white",
                "background-color": "#002244",
                # "white-space": "pre",
                "font-size": "0.8rem",
                'margin-bottom': '1rem',
                'margin-top': '1rem',
                'border-radius': '0.5rem',
                'padding': '0.5rem'
            }
        )
    ):
        for line in lines:
            with a.div(style=cohost.style(
            {
                "white-space": "break-spaces"
            }
        )):
                a(line)


def prose(a, content):
    a(textwrap.dedent(content))


def body(a):

    prose(
        a,
        """
Before we start playing, lets have a look at the readme!

    """,
    )
    code_block(
        a,
        textwrap.dedent(
            """================================================================
DM-1on1-Machinery
================================================================

Title                   		:the Machinery
Version                 		:1.0
Release Date            		:July 30 2003
Filename                		:DM-1on1-Machinery.ut2
Author(s)               		:Martin 'Rykforce' Rykfors
Additional support			    :Additional custom meshes by Punkamatic
Email Address           		:(redacted)
"""
        ),
    )
    prose(
        a,
        """
Ok, we're starting out strong. I love how my nickname back then was wordplay on my last name, much unlike now when my current nickname (given to me during my university days) is wordplay on my last name, but in Swedish this time around.

---

Note the additional custom meshes by Punkamatic! In the UT mapping forums I used to hang out in, he once made a thread about having made a set of static meshes (prefabricated 3D objects to include in maps) consisting of rusty gears and pulleys and such. These were the main source of inspiration for the map. I ended up including them in the map together with some gear models and other assets I made myself using Lightwave.

This map was originally made for UT2k3, but it worked just as well in UT2k4 with only a minor graphical difference.
    """,
    )

    code_block(a,
    """Other levels by author  :

UT			 		:DM-Rig RM1358, DM-Worship, DM-Q3DM19, CTF-HealPod13, DM-ColdMetal
					 CTF-Technetium CTF-TechnetiumV2
UT2003			    :Only this one currently
"""
)
    prose(a, """
    I had a small portfolio of maps for the first Unreal Tournament too. The first of them ranged in quality from really bad to bad, but towards the end with CTF-Technetium I had at least started to get the hang of creating somewhat interesting-looking maps with decent texturing and brushwork, though the actual gameplay was still pretty rough looking back.

    """)
    with a.div(style=cohost.style({'display': 'flex', 'justify-content': 'center'})):
        with a.figure():
            a.img(src='https://staging.cohostcdn.org/attachment/f81a559f-9a6c-401d-9440-ef65a4a77e75/CTF-TechnetiumV2_shot_1.png', alt="Screenshot of the Unreal Tournament map CTF-Technetium")
            with a.figcaption():
                a('CTF-Technetium.')


    code_block(a, """================================================================
--- Play Information ---

Game                    :Unreal Tournament 2003
Level Name              :CTF-1on1-Machinery
Single Player           :w/bots

New Sounds              :Yes (mylevel)
New Textures            :Yes (mylevel)
New StaticMeshes/Models	:yes (mylevel) aswell as RykforceSet3.usx
New Unreal Script       :No

Know bugs		        :FPS is not the best. Karma collision might be missing at some places.
Recommended players     :2 to 4 players """)

    prose(a, """
    FPS issues was something that a lot of people would criticize this map for. Mapping in UT2k3 was a different beast compared to the original Unreal Tournament. In UT, you could rely on geometry occluding other geometry behind it and thus causing the further away geometry to not be rendered, improving performance. In UT2k3, this would not happen. Instead you had to manually insert occlusion volumes that would cause geometries behind it not to render. And I think there was some limitation that forced you to ensure that those volumes had to somehow touch 'air' in the level, otherwise it would not work. I was not particularly good at doing that, nor did I really know how to properly evaluate how well your occlusion volumes were performing so I did not spend very much effort on it. All the details in this paragraph should be taken with a grain of salt as my recollection here is very fuzzy.

    This map also bundled a set of Static Meshes. This was also a big change going from UT to UT2k3. In UT, all you had to work with was <i>brushes</i>. In UT mapping, a brush is a piece of 3D geometry that either 'carves out' the existing geometry of the map (a subtractive brush) or one that is a solid object (additive brush) that can be carved out further by subtractive brushes and so on. On each face of the brush a texture is applied. The UT2k3 engine introduced <i>static meshes</i>, which were prefabricated pieces of geometry that could be added to a map. These static meshes could be far more detailed than a brush and were usually made in an external 3D modeling program. Many custom maps were limited to using the sets of static meshes provided by the base game. Being able to make your own static meshes unlocked a lot of potential to make something unique. For this reason, I <i>acquired</i> Lightwave and learned how to make 3D models that could be imported into UT2k3.
    """)

    code_block(a, """================================================================
--- Authors notes ---

This is my first map for UT2003, and Im sure there will be more from me even though the editor's constant crashes
held me back, but hey, you cant keep a good mapper down, right?

A note on the custom meshes, the meshes in the RykforceSet3.usx are made by Rykforce and may be used in other
peoples maps without Rykforces permission, as long as Rykforce is given credit for it (being mentioned in the maps
readme will do fine), and that nobody else takes credit for it.
The gear meshes in the mylevel package are made by Punkamatic.
All custom meshes where made in Lightwave or UED3""")

    prose(a, """
    Now I'm getting into the tough part of this project: Coming face to face with my awkward teenage self, his style of writing and the archived history of his interactions on the internet. But whatever, this is not too bad though I dread ever having to read more of my writing like forum posts and the such. I prefer leaving that in the past.

    The editor crashing was tough. I think I was still on windows 98 at the time (?) and this meant that the editor had some memory leak that would make it crash after running it for 15 minutes or so. After that, I would need to restart my computer in order to resume working. I think it got better once I got Windows XP installed. Again, my recollection might be fuzzy here.
    """)

    code_block(a, """================================================================
--- Thanks to ---

Gui, and cUnNiNg_StUnTs for feedback on the map. Thanks to Punkamatic for the additional custom meshes.


================================================================
--- Construction ---

Editor used             :UnrealED 3.
Construction Time       :About 4 weeks I'd say.""")

    prose(a, """Gui was a proficient mapper, author of maps that were given CliffyB's official 'Ownage' seal of approval, as well as maps that were included in official bonus map packs for the game. Nice guy, taught me lots about mapping. I do not remember cUnNiNg_StUnTs but he did apparently provide some good feedback on the map during testing.

You gotta love the '4 weeks I'd say' phrasing. Reading this surprised me though. Had you asked me prior to me reading this, I would have estimated spending much more time making this map. On the other hand, the map is pretty small, so maybe it is within reason? But on the other hand still, those constant crashes did not do much to keep me motivated to work at a steady pace. Curious.

The rest of the readme are just installation instructions and copyright notices, so we're done here.

Next up, actually playing the thing. This will involve me uploading a bunch of screenshots and writing a bunch of text, so it will likely take me a while. Thank you for reading!""")


cohost.create_document(body, "post.html", source_minify=True)
