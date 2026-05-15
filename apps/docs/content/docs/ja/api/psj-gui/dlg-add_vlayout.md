---
title: "dlg.add _vlayout()"
description: "Add a vertical Layout to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a vertical Layout to the creating dialog.

## Syntax

```psj
dlg.add _vlayout(...)
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

- Specify all the value defining the positions of the creating layout.
  The list of positions is defined in the order of \[left,top,right,bottom].
- The default value is \[].

## Return Code

This function does not have output value.

## Sample Code

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _vertex _selector()
    dlg.add _vlayout(name="footer",margin=[0,0,0,20],layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
