from dotenv import load_dotenv
import os

loaded = load_dotenv(".env")

print("Loaded:", loaded)
print("Key:", os.getenv("GROQ_API_KEY"))