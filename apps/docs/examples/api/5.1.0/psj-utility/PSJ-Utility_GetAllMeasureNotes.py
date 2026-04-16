# Title:   JPT.GetAllMeasureNotes()
# Desc:    Get all the information of all custom notes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllMeasureNotes
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Tools.Measure.Distance.CreateMeasureNote.TwoNodes(
    strNoteName="Distance_1", 
    crFirstNode=Node(250), 
    crSecondNode=Node(261)
    )
Tools.Measure.Distance.CreateMeasureNote.TwoNodes(
    strNoteName="Distance_1", 
    crFirstNode=Node(257), 
    crSecondNode=Node(291)
    )
Tools.Measure.Angle.CreateMeasureNote.ThreeNodes(
    strNoteName="Angle_1", 
    crFirstNode=Node(441), 
    crSecondNode=Node(438), 
    crThirdNode=Node(475)
    )

# Get the information of all existing measure notes
listDMeasureNotes = JPT.GetAllMeasureNotes()  # [hl]
JPT.Debugger(listDMeasureNotes)

# Print all the related information of each existing measure notes in list
for measure_note in listDMeasureNotes:
    JPT.Debugger(measure_note)
