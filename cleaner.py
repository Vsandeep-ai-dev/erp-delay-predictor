filename = "your_file.py"  # Change to your actual file name

with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

# Replace non-breaking spaces with regular spaces
content = content.replace("\u00A0", " ")

with open(filename, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ Cleaned non-breaking spaces!")