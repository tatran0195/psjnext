# Title:   Assembly.RightClick.UnSuppress()
# Desc:    Unsuppress part on Assembly tree
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assembly/Assembly.RightClick.UnSuppress
# ---
Geometry.Part.Cube()
Assembly.RightClick.Suppress(crlParts=[Part(1)])
result = Assembly.RightClick.UnSuppress(crlParts=[Part(1)])
print(result)
