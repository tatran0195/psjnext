# Title:   dlg.activate_selector()
# Desc:    Activate selector by selector id.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-activate_selector
# ---
from pyjdg import *

def sampleSelection(dlg):
    select1=[]
    select2=[]
    faces=JPT.GetAllFaces()
    for f in faces:
        if f.id % 2 == 0:
            select1.append(f.id)
        else:
            select2.append(f.id)
    JPT.ClearAllSelection()

    dlg.activate_selector(selector_id=0)  # [hl]
    for id in select1:
        JPT.SelectionByID(JPT.DItemType.FACE, id, True)
    dlg.activate_selector(selector_id=1)  # [hl]
    for id in select2:
        JPT.SelectionByID(JPT.DItemType.FACE, id, True)
    
def main():
    dlg=JDGCreator(title="Dialog")
    dlg.add_face_selector(text="Face 1")
    dlg.add_face_selector(text="Face 2")
    dlg.add_label(
        name="Label2",width=200,height=70,
        text="Click Apply button and open the selection list and confirm that " 
             "selectors with even IDs are selected in Face 1," 
             "and selectors with odd IDs are selected in Face 2.",
        text_halign="left",text_valign="top",layout="Window")
    
    dlg.generate_window()
    Geometry.Part.Cube()
    dlg.on_dlg_apply(callfunc=sampleSelection)

if __name__=='__main__':
    main()
