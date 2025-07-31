import re

text = "Once upon a time"
result = re.match(r"o.*time", text, flags=re.IGNORECASE)  # Match at the beginning

if result is None:
    print("No match found")
else:
    print("Match found:", result.group())