# Title:   Home.Windows.TileBox()
# Desc:    Display opening documents in vertical and horizontal arrangement like a box
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.Windows.TileBox
# ---
# Prepare 2 JPT documents
Geometry.Part.Cube()
JPT.ViewFitToModel()
JPT.CreateNewDocument()
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], strName="Cube_2", iPartColor=6409934)
JPT.ViewFitToModel()

# Tile box arrangement
Home.Windows.TileBox(iMode=1)  # [hl]
