import reflex as rx
import Portfolio.components.ComponentsList as comp
import Portfolio.Styles.StylesSheet as ss

class State(rx.State):
    pass

def index():
    return rx.box(
        rx.tablet_and_desktop(
            rx.hstack(
                rx.card(
                    body=rx.vstack(
                        comp.presentation("FotoMia.jpg","Andrés Suárez",ss.cons.MAIL.value),
                        rx.hstack(
                            comp.link_icon_button("linkedin.svg",ss.cons.LINKEDIN_URL.value),
                            comp.link_icon_button("github.svg",ss.cons.GITHUB_URL.value),
                            comp.link_icon_button("cv.svg","Resume.pdf")
                        ),
                    ),
                    footer=rx.vstack(
                        rx.heading("Technical skills", size="lg"),
                        rx.unordered_list(
                            rx.list_item("Python"),
                            rx.list_item("C / C++"),
                            rx.list_item("Flask"),
                            rx.list_item("Basic HTML and SQL")
                        ),
                        rx.heading("Soft skills", size="lg"),
                        rx.unordered_list(
                            rx.list_item("Time management"),
                            rx.list_item("Communication"),
                            rx.list_item("Troubleshooting"),
                            rx.list_item("Adaptability")
                        ),
                        rx.heading("Languages"),
                        rx.unordered_list(
                            rx.list_item("Spanish: native "),
                            rx.list_item(
                                rx.text("English: B2"),
                                rx.link(
                                    rx.span("(click to see the certificate)",
                                            font_weight="bold"
                                        ),
                                    href="ITEP.pdf",
                                    is_button=True,
                                    is_external=True)
                            )
                        ),
                        rx.heading("Academic background"),
                        rx.hstack(
                            rx.text("11/2023"),
                            rx.icon(tag="arrow_right", color=ss.colors.BACKGROUND.value),
                            rx.text("Biomedical engineer, Militar university of Nueva Granada"),
                        ),
                        rx.heading("Certificates"),
                        rx.text("""To see a certificate, click on the corresponding button."""),
                        rx.list(
                            rx.list_item(comp.link_text_button("🔴 CS50P - Harvard", "certificado CS50P.pdf")),
                            rx.list_item(comp.link_text_button("🔴 CS50X - Harvard", "certificado CS50x.pdf")),
                            rx.list_item(comp.link_text_button("🔴 CS50AI - Harvard","CertificadoCS50AI.pdf")),
                            rx.list_item(comp.link_text_button("🔵 Sololearn - Python Intermediate","certificadoPythonIntermedio.pdf")),
                            rx.list_item(comp.link_text_button("🔵 Sololearn - Python Developer", "certificadoPythonDeveloper.pdf")),
                            spacing="0.75em"
                        ),
                        align_items="left"
                    ),
                    flex="0 0 300px",
                    align="center",
                    direction="column",
                    justify="space_between"
                ),

            rx.vstack(
                    rx.heading("About me", size="2xl"),
                    rx.vstack(
                        rx.text("""I am a biomedical engineer, with great interest in the world of software development. 
                                Especially machine learning and artificial intelligence. Currently I do not have work 
                                experience, so I have been concentrating on personal projects, like the ones I put here.""", 
                            text_align="justify",
                            width="85%"),
                        rx.text("""Besides my passion for programming, I have some hobbies like playing video games 🎮, 
                                playing sports ⚽️ and reading 📚.""",
                                width="85%",
                                text_align="left"),
                        align_items="center"
                    ),
                    rx.heading("Projects", size="2xl"),
                    rx.text("(Click inside the boxes for more details)"),
                    rx.vstack(
                        comp.project(
                            "Currency comparator with Euros",
                            "converter.png",
                            """It compares the value of euros that the user enters with another currency 
                            on a specific date that is also entered. You have the option to compare the euros with US dollars 
                            or to compare the euros in the user's possession with another currency different from those available 
                            in the API.""",
                            "https://github.com/Suarez-Andres/Currency-Converter"," This project was developed using Python."
                            ),
                        comp.project(
                            "Bulls and cows game",
                            "numbers.jpg",
                            """Website that combines frontend and backend so that the user can play "bulls and cows".""",
                            "https://github.com/Suarez-Andres/bullsandcows",
                            " This project was developed using Flask."
                        ),
                        width="100%",
                        padding_y="1em",
                        align="center"
                    ),
                    spacing="1em"
                ),
                align_items="start",
                padding="5",
                spacing="1em"
            )
        ),
        rx.mobile_only(
                rx.vstack(
                rx.card(
                    body=rx.vstack(
                        comp.presentation("FotoMia.jpg","Andrés Suárez",ss.cons.MAIL.value),
                        rx.hstack(
                            comp.link_icon_button("linkedin.svg",ss.cons.LINKEDIN_URL.value),
                            comp.link_icon_button("github.svg",ss.cons.GITHUB_URL.value),
                            comp.link_icon_button("cv.svg","Resume.pdf")
                        ),
                    ),
                    footer=rx.vstack(
                        rx.heading("Technical skills", size="lg"),
                        rx.unordered_list(
                            rx.list_item("Python"),
                            rx.list_item("C / C++"),
                            rx.list_item("Basic HTML and SQL")
                        ),
                        rx.heading("Soft skills", size="lg"),
                        rx.unordered_list(
                            rx.list_item("Time management"),
                            rx.list_item("Communication"),
                            rx.list_item("Troubleshooting"),
                            rx.list_item("Adaptability")
                        ),
                        rx.heading("Languages"),
                        rx.unordered_list(
                            rx.list_item("Spanish: native "),
                            rx.list_item(
                                rx.text("English: B2"),
                                rx.link(
                                    rx.span("(click to see the certificate)",
                                            font_weight="bold"
                                        ),
                                    href="ITEP.pdf",
                                    is_button=True,
                                    is_external=True)
                            )
                        ),
                        rx.heading("Academic background"),
                        rx.hstack(
                            rx.text("11/2023"),
                            rx.icon(tag="arrow_right", color=ss.colors.BACKGROUND.value),
                            rx.text("Biomedical engineer, Militar university of Nueva Granada"),
                        ),
                        rx.heading("Certificates"),
                        rx.text("""To see a certificate, click on the corresponding button."""),
                        rx.list(
                            rx.list_item(comp.link_text_button("🔴 CS50P - Harvard", "certificado CS50P.pdf")),
                            rx.list_item(comp.link_text_button("🔴 CS50X - Harvard", "certificado CS50x.pdf")),
                            rx.list_item(comp.link_text_button("🔴 CS50AI - Harvard","CertificadoCS50AI.pdf")),
                            rx.list_item(comp.link_text_button("🔵 Sololearn - Python Intermediate","certificadoPythonIntermedio.pdf")),
                            rx.list_item(comp.link_text_button("🔵 Sololearn - Python Developer", "certificadoPythonDeveloper.pdf")),
                            spacing="0.75em"
                        ),
                        align_items="left"
                    ),
                    flex="0 0 300px",
                    align="center",
                    direction="column",
                    justify="space_between"
                ),

            rx.vstack(
                    rx.heading("About me", size="2xl"),
                    rx.vstack(
                        rx.text("""I am a biomedical engineer, with great interest in the world of software development. 
                                Especially machine learning and artificial intelligence. Currently I do not have work 
                                experience, so I have been concentrating on personal projects, like the ones I put here.""", 
                            text_align="justify",
                            width="85%"),
                        rx.text("""Besides my passion for programming, I have some hobbies like playing video games 🎮, 
                                playing sports ⚽️ and reading 📚.""",
                                width="85%",
                                text_align="left"),
                        align_items="center"
                    ),
                    rx.heading("Projects", size="2xl"),
                    rx.text("(Click inside the boxes for more details)"),
                    rx.vstack(
                        comp.project(
                            "Currency comparator with Euros",
                            "converter.png",
                            """It compares the value of euros that the user enters with another currency 
                            on a specific date that is also entered. You have the option to compare the euros with US dollars 
                            or to compare the euros in the user's possession with another currency different from those available 
                            in the API.""",
                            "https://github.com/Suarez-Andres/Currency-Converter"," This project was developed using Python."
                            ),
                        comp.project(
                            "Bulls and cows game",
                            "numbers.jpg",
                            """Website that combines frontend and backend so that the user can play "bulls and cows".""",
                            "https://github.com/Suarez-Andres/bullsandcows",
                            " This project was developed using Flask."
                        ),
                        width="100%",
                        padding_y="1em",
                        align="center"
                    ),
                    spacing="1em"
                ),
                align_items="start",
                padding="5",
                spacing="1em"
            )
        )
    )

app = rx.App(
    stylesheets=ss.FONTS,
    style=ss.DEF_STYLES
)
app.add_page(
    index,
    title="Andrés Suárez - My web",
    image="code.svg",
    description="Hola, soy Andrés Suárez y este es mi portfolio."
    )