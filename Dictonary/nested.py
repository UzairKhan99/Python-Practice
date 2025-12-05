Here is a clean, corrected example of a ** nested dictionary ** with your idea, plus simple usage.
You can copy–paste this whole block into your IDE:

```python
# ============================
# Nested Dictionary Example
# ============================
#
# A nested dictionary = a dictionary INSIDE a dictionary.
#
# Structure idea:
# programming_languages = {
#     "python": { ...inner dict... },
#     "java":   { ...inner dict... },
# }

programming_languages = {
    "python": {
        "name": "Python",
        "use_case": ["ai", "ml", "webdev"],
        "creator": "Guido van Rossum",
    },
    "java": {
        "name": "Java",
        "use_case": ["enterprise", "android", "backend"],
        "creator": "James Gosling",
    }
}

print("Full nested dictionary:")
print(programming_languages)

# ----------------------------------
# Accessing inner dictionaries
# ----------------------------------

print("\nAccessing inner dictionary for 'python':")
python_info = programming_languages["python"]
print(python_info)

print("\nAccessing specific values:")
print("Python name:", programming_languages["python"]["name"])
print("Python use cases:", programming_languages["python"]["use_case"])
print("Java creator:", programming_languages["java"]["creator"])

# Accessing an element inside the inner list:
print("\nFirst Python use case:",
      programming_languages["python"]["use_case"][0])  # "ai"


# ----------------------------------
# Adding a new language (new nested dict)
# ----------------------------------

programming_languages["javascript"] = {
    "name": "JavaScript",
    "use_case": ["frontend", "backend", "fullstack"],
    "creator": "Brendan Eich",
}

print("\nAfter adding 'javascript':")
print(programming_languages)


# ----------------------------------
# Updating an inner value
# ----------------------------------

programming_languages["python"]["use_case"].append("automation")
print("\nAfter adding 'automation' to python use_case:")
print(programming_languages["python"]["use_case"])


# ----------------------------------
# Looping over nested dictionary
# ----------------------------------

print("\nLooping over all languages and their info:")

for lang_key, info_dict in programming_languages.items():
    print(f"\nLanguage key: {lang_key}")
    print(" Name:", info_dict["name"])
    print(" Use cases:", info_dict["use_case"])
    print(" Creator:", info_dict["creator"])

# Quick summary (as comments):
# - Outer dict keys: "python", "java", "javascript"
# - Each value is another dict with keys like "name", "use_case", "creator"
# - Access pattern: outer_dict[outer_key][inner_key]
#   e.g. programming_languages["python"]["use_case"]
```
