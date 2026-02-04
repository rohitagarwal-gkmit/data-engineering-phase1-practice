import os
import dotenv

dotenv.load_dotenv(dotenv_path=".env")


DATABASE_URL: str | None = os.getenv(key="DATABASE_URL")
SECRET_KEY: str | None = os.getenv(key="SECRET_KEY", default="dev-secret-key")
