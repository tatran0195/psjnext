---
title: "dlg.add _barpart _selector()"
description: "Add \"Bar\" to the selection list, allowing user to select bar parts and store the selected bar parts to the selection list"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add "Bar" to the selection list, allowing user to select bar parts and store the selected bar parts to the selection list.

## Syntax

```psj
dlg.add _barpart _selector(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @optional @default:"Bar" -->
### `text`

- The title of selector.

- A _String_ specifying text which will be displayed as button label.

## Return Code

This function does not have output value.

## Sample Code

```psj {13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label2",text="Mesh Count",layout="Layout1")
    dlg.add _textbox(name="TextBox3",layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _barpart _selector(text="Bar 1")
    dlg.generate _window()
    
if __name__=='__main__':
    main()
```
