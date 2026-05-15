---
title: "dlg.add _space()"
description: "Add a space between the created components"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a space between the created components.

## Syntax

```psj
dlg.add _space(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### layout

- Specify the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @optional -->
### name

- Specify the name of the created component.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### orientation

- Specify the direction to add a space component between 2 components:
  - "horizontal": Add a space component on the horizontal direction.
  - "vertical": Add a space component on the vertical direction.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### size

- Specify the size of space.
- The default value is 0.

## Return Code

This function does not have output value.

## Sample Code

```psj {8,16,19}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label2",text="Field 1",layout="Layout1")
    dlg.add _textbox(name="TextBox3",layout="Layout1")
    dlg.add _space(orientation="vertical",size=2,layout="Window")
    dlg.add _layout(name="Layout5",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label6",text="Field 2",layout="Layout5")
    dlg.add _textbox(name="TextBox7",layout="Layout5")
    dlg.add _layout(name="Layout8",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label9",text="Field 3",layout="Layout8")
    dlg.add _textbox(name="TextBox10",layout="Layout8")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
