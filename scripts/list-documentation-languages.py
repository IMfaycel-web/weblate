import json

from weblate_language_data.docs import DOCUMENTATION_LANGUAGES

languages = list(DOCUMENTATION_LANGUAGES.values())

print(f"languages={json.dumps(languages)}")
