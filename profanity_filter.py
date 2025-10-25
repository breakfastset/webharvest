text = "What the fish? I will beat the donkey off him."

profanities = ["fish", "donkey"]

filter_text = text
for profanity in profanities:
    filter_text = filter_text.replace(profanity, "x" * len(profanity))

print(filter_text)