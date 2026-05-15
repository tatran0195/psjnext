---
title: "dlg.add _hlayout()"
description: "Add a horizontal Layout to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a horizontal Layout to the creating dialog.

## Syntax

```psj
dlg.add _hlayout(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the created component.

<!-- @since:5.0.1 @required -->
### layout

- Specify the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @optional -->
### margin

- Specify all the values defining the positions of the creating layout.
  The list of positions is defined in the order of \[left,top,right,bottom].
- The default value is \[].

## Return Code

This function does not have output value.

## Sample Code

```psj {8}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label2",text="Jupiter",layout="Layout1")
    dlg.add _textbox(name="TextBox3",layout="Layout1")
    dlg.add _hlayout(name="footer",margin=[0,10,0,10],layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
