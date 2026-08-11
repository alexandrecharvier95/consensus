import reflex as rx


def index() -> rx.Component:
    """Page d'accueil de la plateforme Consensus."""
    return rx.container(
        rx.vstack(
            rx.heading("Bienvenue sur Consensus", size="9"),
            rx.text(
                "La plateforme collaborative de vote et de suivi des prix du carburant.",
                size="4",
                color="gray",
            ),
            rx.link(
                rx.button("Commencer", size="3"),
                href="/dashboard",
            ),
            spacing="6",
            align="center",
        ),
        padding="8",
    )


app = rx.App()
app.add_page(index, route="/")
