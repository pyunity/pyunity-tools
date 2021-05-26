import pyunity_tools

desc = pyunity_tools.__doc__.split("\n")
desc_new = [
    "# PyUnity Tools", "",
    "".join([
        "[![License](https://img.shields.io/pypi/l/pyunity-tools.svg?v=1)]",
        "(https://pypi.python.org/pypi/pyunity-tools)\n",
        "[![PyPI version](https://img.shields.io/pypi/v/pyunity-tools.svg?v=1)]",
        "(https://pypi.python.org/pypi/pyunity-tools)\n",
        "[![Python version](https://img.shields.io/pypi/pyversions/pyunity-tools.svg?logo=python&logoColor=FBE072)]",
        "(https://pypi.python.org/pypi/pyunity-tools)\n",
        "[![Commits since last release](https://img.shields.io/github/commits-since/pyunity/pyunity-tools/",
        "0.4.0.svg)](https://github.com/pyunity/pyunity-tools/compare/0.1.0...master)\n",
        "[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/pyunity/pyunity-tools.svg",
        "?logo=lgtm)](https://lgtm.com/projects/g/rayzchen/pyunity/context:python)\n",
    ])
]
skip = 0
for i in range(len(desc)):
    if skip:
        skip = 0
        continue
    if i != len(desc) - 1 and len(set(desc[i + 1])) == 1:
        if desc[i + 1][0] == "-":
            desc_new.append("### " + desc[i])
            skip = 1
        elif desc[i + 1][0] == "=":
            desc_new.append("## " + desc[i])
            skip = 1
    else:
        if "create a new pull request" in desc[i]:
            desc[i] = desc[i].replace(
                "create a new pull request",
                "[create a new pull request](https://github.com/rayzchen/pyunity/pulls)"
            )
        if desc[i] == "`here <https://github.com/rayzchen/pyunity>`_":
            continue
        desc_new.append(desc[i].replace("::", ":"))

with open("README.md", "w") as f:
    for line in desc_new:
        f.write(line + "\n")
