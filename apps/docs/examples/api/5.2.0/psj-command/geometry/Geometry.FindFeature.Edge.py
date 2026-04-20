# Title:   Geometry.FindFeature.Edge()
# Desc:    Find and select the specific edges according to their characteristic
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.FindFeature.Edge
# ---
cube=Geometry.Part.Cube()
edges = Geometry.FindFeature.Edge(crlParts=[cube])  # [hl]
JPT.Debugger(edges)
