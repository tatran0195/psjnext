# Title:   Geometry.Transform.Translation()
# Desc:    Move the parts along a given vector. The direction and magnitude of the vector are arbitrary or along the specific axis in the Cartesian coordinate system
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/geometry/Geometry.Transform.Translation
# ---
Geometry.Part.Cube(iPartColor=8124407)
translated_part = Geometry.Transform.Translation(crlParts=[Part(1)],  # [hl]
                                                 dlTranslationVector=[[-0.00666, 0.00222, 0]])  # [hl]
JPT.Debugger(translated_part)
