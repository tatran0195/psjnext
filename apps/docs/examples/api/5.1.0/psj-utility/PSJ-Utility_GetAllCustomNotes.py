# Title:   JPT.GetAllCustomNotes()
# Desc:    Get all the information of all custom notes
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetAllCustomNotes
# ---
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Tools.CustomNote.Create(
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    strParentName="Collection_1", 
    listContent=["Note 1"], 
    iBackgroundColor=15794160, 
    iOutlineColor=14772545, 
    iArrowColor=16711680, 
    iFontSize=16, 
    iAlignment=1
    )
Tools.CustomNote.Create(
    strNoteName="CustomNote_2", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    crParentCollection=CustomNoteCollection(1), 
    listContent=["Note 2"], 
    iFontSize=16, 
    iBackgroundColor=11394815, 
    iOutlineColor=128, 
    iArrowColor=3937500, 
    iAlignment=1
    )
Tools.CustomNote.Create(
    strNoteName="CustomNote_3", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    crParentCollection=CustomNoteCollection(1), 
    listContent=["Note 3"], 
    iFontSize=16, bBold=True, 
    iBackgroundColor=14480885, 
    iOutlineWidth=2, 
    iOutlineColor=25600, 
    iArrowColor=9498256, 
    iArrowType=0
    )
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()
JPT.Exec('ViewSpreadNote()')

# Get the information of all existing Custom Notes
listDCustomNotes = JPT.GetAllCustomNotes()  # [hl]
JPT.Debugger(listDCustomNotes)

# Print all the related information of each existing custom note in list
for custom_note in listDCustomNotes:
    JPT.Debugger(custom_note)
