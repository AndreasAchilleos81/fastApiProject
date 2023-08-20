import os


class HostAndPort:
    HOST: str = os.environ.get("HOST", "localhost")
    PORT: int = os.environ.get("PORT", 8000)
