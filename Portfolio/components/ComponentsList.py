import reflex as rx
import Portfolio.Styles.StylesSheet as ss

def presentation(src: str, name: str, mail: str) -> rx.Component:
    return rx.fragment(
                rx.avatar(src=src,
                        size="2xl",
                        border="4px",
                        border_color=ss.colors.BACKGROUND.value
                        ),
                rx.heading(name, size="lg"),
                rx.text(mail)
            )

def link_icon_button(src: str, href: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.image(src=src,
                    width=ss.spaces.LARGE.value,
                    height=ss.spaces.LARGE.value    
                ),
        ),
        href=href,
        button=True,
        is_external=True
    )

def link_text_button(text: str, href: str) -> rx.Component:
    return rx.link(
            rx.button(
                text,
                _hover= {
                    "background_color":ss.colors.IMPORTANT.value,
                    "color":ss.colors.PARAGRAPH.value
                }
            ),
            href=href,
            button=True,
            is_external=True
        )
    
def project(title: str, body: str, description: str, href: str, tec:str) -> rx.Component:
    return rx.link(
            rx.card(
            header=rx.heading(title, size="md"),
            body=rx.vstack(
                rx.image(
                    src=body,
                    width="auto",
                    height="12em",
                    border_radius=ss.spaces.DEFAULT.value
                ),
                rx.text(description, rx.span(tec, font_weight="bold"),text_align="justify",max_width="100%"),
                spacing="1em"
            ),
            max_width="100%",
            align="center",
            flex="1",
            direction="column",
            justify="space_between"
        ),
        align_items="center",
        href=href,
        button=True,
        is_external=True,
        style={"width": "100%", "max-width": "28em"}
    )