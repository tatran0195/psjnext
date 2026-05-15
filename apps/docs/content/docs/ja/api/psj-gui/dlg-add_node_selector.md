---
title: "dlg.add _node _selector()"
description: "Add \"Node\" to the selection list, allowing user to select nodes and store the selected nodes to the selection list"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add "Node" to the selection list, allowing user to select nodes and store the selected nodes to the selection list.

## Syntax

```psj
dlg.add _node _selector(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### text

- Specify the title of selector.
- The default value is "".

## Return Code

This function does not have output value.

## Sample Code

```psj {11}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _listbox(name="ListBox3",multisel=True,options=["item1","item2","item3"],width=100,height=100,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _node _selector()
    dlg.generate _window()
    
if __name__=='__main__':
    main()
```
