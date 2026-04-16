# Title:   Tools.CustomNote.Create()
# Desc:    Create a custom note
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.CustomNote.Create
# ---
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

Tools.CustomNote.Create(  # [hl:start]
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0029, 0.0063, 0.01], 
    iTargetEntityType=5, 
    crTarget=Elem(1022), 
    strParentName="Collection_1", 
    listContent=["Top Face"], 
    iFontSize=18, 
    bBold=True, 
    iBackgroundColor=13826810, 
    iOutlineColor=2763429, 
    iArrowColor=2763429)  # [hl:end]
