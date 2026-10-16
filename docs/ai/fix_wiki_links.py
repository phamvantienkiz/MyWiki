import os
import re
import urllib.parse
import sys

if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

WIKI_DIR = r"E:\MyProject\MyWiki\wiki"
RESOURCES_DIR = r"E:\MyProject\MyWiki\resources"

def fix_wiki():
    wiki_files = [f for f in os.listdir(WIKI_DIR) if f.endswith('.md')]
    
    # Specific typo fixes
    typos = {
        "N%E1%BB%81n%20t%E1%BB%A7ng%20H%E1%BB%87%20th%E1%BB%91ng%20C%C6%A1%20s%E1%BB%9F%20d%E1%BB%AF%20li%E1%BB%87u%20cho%20Data%20Scientist%20%E2%80%93%20B%C3%A0i%20gi%E1%BA%A3ng%20c%E1%BB%A7a%20Ti%E1%BA%BFn%20si%20L%C3%AA%20Thi%E1%BB%87n%20H%C3%B2a.pdf":
        urllib.parse.quote("Nền tảng Hệ thống Cơ sở dữ liệu cho Data Scientist – Bài giảng của Tiến sĩ Lê Thiện Hòa.pdf"),
        "S%E1%BB%95%20tay%20h%C6%B0%E1%BB%9Bng%20d%E1%BB%8Fn%20c%C3%A1ch%20d%C3%B9ng%20LLM%20%C4%91%E1%BB%83%20t%E1%BB%B1%20%C4%91%C3%A1nh%20gi%C3%A1%20c%C3%A2u%20tr%E1%BB%9F%20l%E1%BB%9Di%20c%E1%BB%A7a%20LLM.pdf":
        urllib.parse.quote("Sổ tay hướng dẫn cách dùng LLM để tự đánh giá câu trở lời của LLM.pdf")
    }
    
    wikilink_replacements = {
        '[[deep-learning-overview]]': '[[index]]',
        '[[deep-learning-overview|': '[[index|',
        '[[kv-cache]]': '[[large-language-models|KV Cache]]'
    }

    files_modified = 0

    for wf in wiki_files:
        filepath = os.path.join(WIKI_DIR, wf)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        orig_content = content
        
        for k, v in typos.items():
            content = content.replace(k, v)
            
        for k, v in wikilink_replacements.items():
            content = content.replace(k, v)
            
        if content != orig_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            files_modified += 1

    print(f"Fixed remaining anomalies in {files_modified} files.")

if __name__ == '__main__':
    fix_wiki()
