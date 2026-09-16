def title(string):
    output = f"--- {string}"
    return output

def h1(string):
    output = f"# {string}"
    return output

def h2(string):
    output = f"## {string}"
    return output

def h3(string):
    output = f"### {string}"
    return output

def link(link, title):
    output = f"[{title}]({link})"
    return output

def inline_code(code_string):
    output = f"`{code_string}`"
    return output

def code_block(code, language=None):
    output = f"""```{language}
{code}
```"""

def dotpoint(string, indentation=1):
    output = f"{' '*indentation}- {string}"
    return output

def unchecked_task(string, indentation=1):
    output = f"{' '*indentation}- [ ] {string}"
    return output

def checked_task(string, indentation=1):
    output = f"{' '*indentation}- [x] {string}"
    return output
