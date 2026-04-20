# Title:   Tools.Measure.Angle.CreateMeasureNote.ProjectedNode()
# Desc:    Create a Measure Note for Measure > Angle > Projected Node
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Angle.CreateMeasureNote.ProjectedNode
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Coordinates.ThreeNode(strName="CRect_1", crlNodes=[Node(444, 317, 185)])
Tools.Measure.Angle.CreateMeasureNote.ProjectedNode(  # [hl:start]
    strNoteName="Angle1", 
    crNode=Node(346), 
    crCoordinate=Coord(1))  # [hl:end]
