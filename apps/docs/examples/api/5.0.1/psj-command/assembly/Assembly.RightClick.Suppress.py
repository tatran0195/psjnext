# Title:   Assembly.RightClick.Suppress()
# Desc:    Suppress part on Assembly tree
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assembly/Assembly.RightClick.Suppress
# ---
Geometry.Part.Cube()
result = Assembly.RightClick.Suppress(crlParts=[Part(1)])
print(result)
