---
title: "dlg.add _separator()"
description: "Add a Separator to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a Separator to the creating dialog.

## Syntax

```psj
dlg.add _separator(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### name

- Specify the name of the created component.

<!-- @since:5.0.1 @required -->
### layout

- Specify the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

## Return Code

This function does not have output value.

## Sample Code

```psj {7}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout18",orientation=orientation.vertical,layout="Window")
    dlg.add _label(name="Label19",text="Label",text _valign="top",layout="Layout18")
    dlg.add _separator(name="Separator20",layout="Layout18")
    dlg.add _textbox(name="TextBox21",layout="Layout18")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
