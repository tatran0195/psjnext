# Title:   Tools.CustomNote.EditStyle()
# Desc:    Edit style of indicated custom notes.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.CustomNote.EditStyle
# ---
Geometry.Part.Cube(strName="Cube_1", iPartColor=6409934)

Tools.CustomNote(
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0, 0.01, 0.01],
    iTargetEntityType=1, crTarget=Node(8), 
    strParentName="Collection_1", 
    listContent=["My Custom Note 1"], 
    iFontSize=11, 
    bBold=True)

Tools.CustomNote(
    strNoteName="CustomNote_2", 
    dlNotePosition=[0.01, 0.01, 0.01], 
    iTargetEntityType=1, 
    crTarget=Node(7), c
    rParentCollection=CustomNoteCollection(1), 
    listContent=["My Custom Note 2"], 
    iFontSize=11, 
    bBold=True)

Tools.CustomNote.EditStyle(  # [hl:start]
    crlTargets=[CustomNoteCollection(1)], 
    bBold=True, 
    iBackgroundColor=13826810, 
    iOutlineColor=25600,   # [hl:end]
    iArrowColor=8421376)
