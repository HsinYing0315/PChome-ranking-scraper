import pynecone as pc

config = pc.Config(
    app_name="PChome_ranking_scraper",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
