import reflex as rx

plugins = [rx.plugins.SitemapPlugin(), rx.plugins.RadixThemesPlugin()]
config = rx.Config(app_name="consensus_frontend", plugins=plugins)
