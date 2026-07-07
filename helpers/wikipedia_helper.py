import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="BollywoodGPT/1.0 (simranakur10d@gmail.com)"
)

def get_actor_info(name):
    page = wiki.page(name)

    if not page.exists():
        return None

    return {
        "title": page.title,
        "summary": page.summary[:2000]
    }