---
title: "dlg.add _groupbox()"
description: "Add a GroupBox to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a GroupBox to the creating dialog.

## Syntax

```psj
dlg.add _groupbox(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the created component.

<!-- @since:5.0.1 @type:String @required -->
### `layout`

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `text`

- The text which will be displayed.

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _groupbox(name="GroupBox1",text="Jupiter",layout="Window")
    dlg.add _layout(name="Layout2",orientation=orientation.horizontal,layout="GroupBox1")
    dlg.add _label(name="Label3",text="Label",layout="Layout2")
    dlg.add _textbox(name="TextBox4",layout="Layout2")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
