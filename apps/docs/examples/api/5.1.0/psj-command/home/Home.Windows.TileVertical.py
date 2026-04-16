# Title:   Home.Windows.TileVertical()
# Desc:    Display opening documents in a vertical side-by-side arrangement
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.Windows.TileVertical
# ---
# Prepare 2 JPT documents
Geometry.Part.Cube()
JPT.ViewFitToModel()
JPT.CreateNewDocument()
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
JPT.ViewFitToModel()

# Tile vertical arrangement
Home.Windows.TileVertical(iMode=0)  # [hl]
