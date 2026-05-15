---
title: "dlg.activate _selector()"
description: "Activate selector by selector id."
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Activate selector by selector id.

## Syntax

```psj
dlg.activate _selector(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### selector\_id

- Specify the selector id.

## Return Code

This function does not have output value.

## Sample Code

```psj {14,17}
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

    dlg.activate _selector(selector _id=0)
    for id in select1:
        JPT.SelectionByID(JPT.DItemType.FACE, id, True)
    dlg.activate _selector(selector _id=1)
    for id in select2:
        JPT.SelectionByID(JPT.DItemType.FACE, id, True)
    
def main():
    dlg=JDGCreator(title="Dialog")
    dlg.add _face _selector(text="Face 1")
    dlg.add _face _selector(text="Face 2")
    dlg.add _label(
        name="Label2",width=200,height=70,
        text="Click Apply button and open the selection list and confirm that " 
             "selectors with even IDs are selected in Face 1," 
             "and selectors with odd IDs are selected in Face 2.",
        text _halign="left",text _valign="top",layout="Window")
    
    dlg.generate _window()
    Geometry.Part.Cube()
    dlg.on _dlg _apply(callfunc=sampleSelection)

if __name__=='__main__':
    main()
```
