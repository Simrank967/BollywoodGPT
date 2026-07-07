from rapidfuzz import process

# Celebrity aliases
ACTORS = {
    "Shah Rukh Khan": [
        "srk",
        "shahrukh",
        "shah rukh",
        "sharuk",
        "king khan",
        "badshah"
    ],

    "Salman Khan": [
        "salman",
        "salmaan",
        "bhoi"
    ],

    "Ajay Devgn": [
        "ajay",
        "ajay devgan",
        "ajay devgn"
    ],

    "Aamir Khan": [
        "aamir",
        "amir"
    ],

    "Akshay Kumar": [
        "akshay",
        "akki"
    ],

    "Deepika Padukone": [
        "deepika",
        "deepka",
        "deepika padukon"
    ],

    "Ranbir Kapoor": [
        "ranbir"
    ],

    "Ranveer Singh": [
        "ranveer"
    ],

    "Alia Bhatt": [
        "alia"
    ],

    "Katrina Kaif": [
        "katrina"
    ]
}

# Build searchable dictionary
choices = {}

for actor, aliases in ACTORS.items():
    choices[actor.lower()] = actor

    for alias in aliases:
        choices[alias.lower()] = actor


def find_actor(text):

    text = text.lower()

    match = process.extractOne(
        text,
        choices.keys(),
        score_cutoff=75
    )

    if match:
        return choices[match[0]]

    return None