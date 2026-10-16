import os

filepath = r"E:\MyProject\MyWiki\wiki\llm-evaluation.md"
with open(filepath, 'r', encoding='utf-8') as f:
    c = f.read()

# Replace with exact quoted string
old_str = "S%E1%BB%95%20tay%20h%C6%B0%E1%BB%9Bng%20d%E1%BA%ABn%20c%C3%A1ch%20d%C3%B9ng%20LLM%20%C4%91%E1%BB%83%20t%E1%BB%B1%20%C4%91%C3%A1nh%20gi%C3%A1%20c%C3%A2u%20tr%E1%BB%9F%20l%E1%BB%9Di%20c%E1%BB%A7a%20LLM.pdf"
new_str = "S%E1%BB%95%20tay%20h%C6%B0%E1%BB%9Bng%20d%E1%BA%ABn%20c%C3%A1ch%20d%C3%B9ng%20LLM%20%C4%91%E1%BB%83%20t%E1%BB%B1%20%C4%91%C3%A1nh%20gi%C3%A1%20c%C3%A2u%20tr%E1%BA%A3%20l%E1%BB%9Di%20c%E1%BB%A7a%20LLM.pdf"

c = c.replace(old_str, new_str)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated llm-evaluation.md successfully.")
