from urllib.parse import urlparse


def parse_repository_url(repository_url: str) -> tuple[str, str]:
    path = urlparse(repository_url).path.strip("/")

    parts = path.split("/")

    if len(parts) < 2:
        raise ValueError("Invalid GitHub repository URL.")

    owner = parts[0]
    repository = parts[1]

    return owner, repository