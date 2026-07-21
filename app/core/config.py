import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY")
    GITHUB_TOKEN: str | None = os.getenv("GITHUB_TOKEN")


settings = Settings()