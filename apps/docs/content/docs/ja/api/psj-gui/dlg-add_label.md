---
title: "dlg.add _label()"
description: "Add a Label to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a Label to the creating dialog.

## Syntax

```psj
dlg.add _label(...)
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
### text

- Specify text which will be displayed.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### width

- Specify the width of the Label.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### height

- Specify the height of the Label.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### text\_halign

- Specify the alignment in horizontal direction:
  - "left": align the showing text to the left in the horizontal direction.
  - "center": align the showing text to the center in the horizontal direction.
  - "right": align the showing text to the right in the horizontal direction.
- The default value is "left".

<!-- @since:5.0.1 @optional -->
### text\_valign

- Specify the alignment in vertical direction:
  - "top": align the showing text to the top in the vertical direction.
  - "middle": align the showing text to the middle in the vertical direction.
  - "bottom": align the showing text to the bottom in the vertical direction.
- The default value is "top".

## Return Code

This function does not have output value.

## Sample Code

```psj {5-6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _label(name="Label2",text="Label",width=30,height=30,
      text _halign="center",text _valign="middle",layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
