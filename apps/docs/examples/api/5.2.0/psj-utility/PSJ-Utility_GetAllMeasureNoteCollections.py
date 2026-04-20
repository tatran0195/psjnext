# Title:   JPT.GetAllMeasureNoteCollections()
# Desc:    Get all the information of all measure note collections
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllMeasureNoteCollections
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)

Tools.Measure.Angle.CreateMeasureNote.ThreeNodes(
    strNoteName="Angle_1", 
    crFirstNode=Node(472), 
    crSecondNode=Node(83), 
    crThirdNode=Node(447)
    )

Tools.Measure.Area.CreateMeasureNote.Element(
    strNoteName="Area_1", 
    crlElements=[Elem(1001)]
    )

Tools.Measure.Radius.CreateMeasureNote.ThreeNodes(
    strNoteName="Radius_1", 
    crFirstNode=Node(189), 
    crSecondNode=Node(191), 
    crThirdNode=Node(216)
    )

JPT.ViewFitToModel()

listDMeasureNoteCollections = JPT.GetAllMeasureNoteCollections()  # [hl]
JPT.Debugger(listDMeasureNoteCollections)

