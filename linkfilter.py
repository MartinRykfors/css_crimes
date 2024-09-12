from airium import Airium
import lib.cohost as cohost

a = Airium(base_indent="")


# f3f3f3 outer background
# 330000 borders
# font-family: Verdana, Arial, Helvetica, sans-serif;
# link 996633
def body(a):
    with a.div(
        style=cohost.style(
            {
                "display": "grid",
                "grid-template-columns": "100px auto",
                "background-color": "#f3f3f3",
                "font-family": "Verdana, Arial, Helvetica, sans-serif",
            }
        )
    ):
        with a.div(style=cohost.style({"grid-column": "1 / span 1"})):
            a.img(
                src="https://staging.cohostcdn.org/attachment/571348c0-2595-4e39-84e9-48bf154d8837/robot.gif", alt="A robot, taken from the 2002 design of linkfilter.net"
            )
        with a.div(style=cohost.style({"grid-column": "2 / span 1"})):
            with a.div(
                style=cohost.style({"display": "flex", "flex-direction": "column"})
            ):
                with a.div(
                    style=cohost.style(
                        {
                            "display": "flex",
                            "justify-content": "right",
                            "padding-bottom": "20px",
                        }
                    )
                ):
                    a.img(
                        src="https://staging.cohostcdn.org/attachment/4a24f31c-3911-410c-8362-7047b595dd2e/linkfilter.svg", alt="The cohost logo, rendered as the linkfilter.net logo from 2002."
                    )
                with a.div(
                    style=cohost.style(
                        {
                            "background-color": "#330000",
                            "width": "100%",
                            "padding": "3px",
                            "margin-bottom": "40px",
                        }
                    )
                ):
                    with a.div(
                        style=cohost.style(
                            {
                                "display": "flex",
                                "color": "white",
                                "justify-content": "space-between",
                            }
                        )
                    ):
                        with a.div(
                            style=cohost.style(
                                {"font-size": "14px", "font-weight": "bold"}
                            )
                        ):
                            a("Big ups to you if this rings a bell")
                        with a.div(
                            style=cohost.style(
                                {"font-size": "10px", "font-weight": "bold"}
                            )
                        ):
                            a('the "other" pile')

                    with a.div(
                        style=cohost.style(
                            {
                                "background-color": "white",
                                # "height": "100px",
                                "font-size": "0.8em",
                            }
                        )
                    ):
                        with a.div(style=cohost.style({"margin": "2px"})):
                            with a.div(
                                style=cohost.style(
                                    {
                                        "display": "flex",
                                        "justify-content": "space-between",
                                    }
                                )
                            ):
                                with a.div(
                                    style=cohost.style({"margin-bottom": "10px"})
                                ):
                                    a("Link #")
                                    with a.span(
                                        style=cohost.style({"color": "#996633"})
                                    ):
                                        a("555")
                                    a("submitted by ")
                                    with a.span(
                                        style=cohost.style({"color": "#996633"})
                                    ):
                                        a("@rykarn")
                                    a("on 14.07.02 19:32PM.  (+348XP)")
                                    a.br()
                                    with a.span(
                                        style=cohost.style({"color": "#996633"})
                                    ):
                                        a("http://cohost.org/rykarn")
                                with a.div(style=cohost.style({})):
                                    a.img(
                                        src="https://staging.cohostcdn.org/avatar/7744-90e2ac93-f936-4293-8394-47d5a70341da-profile.png",
                                        style=cohost.style(
                                            {"width": "40px", "height": "40px", 'margin': '2px'}
                                        ),
                                    )
                            with a.div(style=cohost.style({"margin-bottom": "10px"})):
                                a(
                                    (
                                        "linkfilter.net was the initial dose what ended up becoming this "
                                        "steady drip feed of internet poison into my veins. "
                                        "So much weird early 00s internet stuff, flash animations, news articles, personal pages. "
                                        "It led me to finding SA (via the music video / flash animation for The Laziest Men on Mars - The Terrible Secret of Space). "
                                        "The SA mp3 sharing forums ended up shaping my music tastes to a huge degree (there were a handful of FTP servers "
                                        "ran by forum users to which you uploaded your cd rips and made a post about. Voltron lives forever in my heart). "
                                    )
                                )
                                a.br()
                                a(
                                    (
                                        "My taste in music led me to dipping my toes into my own music production (though nothing really materialized from that in the end). "
                                        "It made me want to spend a year studying abroad in Berlin and experience the techno music scene there. "
                                        "It led to my interest in signal processing, which led me to picking that as my Master's thesis project and it led "
                                        "to me getting a specific job in the UK, where I spent the last 3 and-a-bit years of my twenties before moving back home."
                                    )
                                )
                                a.br()
                                a(
                                    (
                                        "There is no real point to what I am writing here, I really just wanted to create another internet nostalgia trip "
                                        "using these wonderful css tricks that cohost allows us to use. But it did lead me to ponder a bit about the "
                                        "bifurcation upon bifurcation that is the set of all possible paths your life can end up taking, and hopefully "
                                        "you found this worthy of your time spent reading it."
                                    )
                                )

                            with a.div(
                                style=cohost.style(
                                    {"display": "flex", "justify-content": "center"}
                                )
                            ):
                                with a.span(style=cohost.style({"color": "#996633"})):
                                    a("Comments")
                                a(": 0 Hits: 1 Points: 3598 Vote Now! [")
                                with a.span(style=cohost.style({"color": "#996633"})):
                                    a("1 2 3 4 5 6 7 8 9 10")
                                a("]")


cohost.create_document(body, "post.html")
