#-*- coding: utf-8 -*-
import re
import string
import glob
import os.path
import io

def prettyfy_file_name(name):
    pretty_name = re.sub(r'-', ' ', name)
    pretty_name = pretty_name.replace('.md', '')
    return string.capwords(pretty_name)

def recursive_path_visit(parent, text):
    paths = sorted(os.listdir(parent))
    for path in paths:
        if path in {"README.md", "SUMMARY.md", "build.py"}:
            continue

        child = os.path.join(parent, path)
        if (os.path.isdir(child)):
            text.append(f"\n- [{prettyfy_file_name(path)}]({child}/README.md)")
            recursive_path_visit(child, text)
        if (os.path.isfile(child)):
            text.append(f"  - [{prettyfy_file_name(path)}]({child})")

text = []
text.append("# Summary")
text.append("\n[README](./README.md)")

recursive_path_visit(os.path.join(os.curdir), text)

with io.open('SUMMARY.md', 'r+', encoding='utf-8') as summary:
    summary.seek(0)
    summary.truncate()
    summary.write('\n'.join(text))    
