---
title: "dlg.add _elementedge _selector()"
description: "Add \"Elem edge\" to the selection list, allowing user to select element edges and store the selected element edges to the selection list"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add "Elem edge" to the selection list, allowing user to select element edges and store the selected element edges to the selection list.

## Syntax

```psj
dlg.add _elementedge _selector(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"Elem edge" -->
### `text`

- The title of selector.

## Return Code

This function does not have output value.

## Sample Code

```psj {19}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label2",text="Length in X",layout="Layout1")
    dlg.add _textbox(name="TextBox3",layout="Layout1")
    dlg.add _layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label7",text="Length in Y",layout="Layout6")
    dlg.add _textbox(name="TextBox8",layout="Layout6")
    dlg.add _layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label10",text="Length in Z",layout="Layout9")
    dlg.add _textbox(name="TextBox11",layout="Layout9")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _elementedge _selector(text = "Element edge 1")
    dlg.generate _window()
    
if __name__=='__main__':
    main()
```
