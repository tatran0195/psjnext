---
title: "dlg.add _layout()"
description: "Add a Layout to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a Layout to the creating dialog.

## Syntax

```psj
dlg.add _layout(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the created component.

<!-- @since:5.0.1 @type:String @required -->
### `layout`

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @type:Orientation object @required -->
### `orientation`

- The arrangement direction of inside components:
  - _orientation.horizontal_: all components inside are arranged horizontally.
  - _orientation.vertical_: all components inside are arranged vertically.

<!-- @since:5.0.1 @type:List @optional @default:[] -->
### `margin`

- The all the values defining the positions of the creating Layout.
  The list of positions is defined in the order of \[left,top,right,bottom].

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,margin=[0,10,0,10],layout="Window")
    dlg.add _label(name="Label2",text="Jupiter",layout="Layout1")
    dlg.add _textbox(name="TextBox3",layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
