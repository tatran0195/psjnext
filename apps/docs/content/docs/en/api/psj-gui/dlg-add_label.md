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

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `width`

- The width of the Label.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `height`

- The height of the Label.

<!-- @since:5.0.1 @type:String @optional @default:"left" -->
### `text _halign`

- The alignment in horizontal direction:
  - "left": align the showing text to the left in the horizontal direction.
  - "center": align the showing text to the center in the horizontal direction.
  - "right": align the showing text to the right in the horizontal direction.

<!-- @since:5.0.1 @type:String @optional @default:"top" -->
### `text _valign`

- The alignment in vertical direction:
  - "top": align the showing text to the top in the vertical direction.
  - "middle": align the showing text to the middle in the vertical direction.
  - "bottom": align the showing text to the bottom in the vertical direction.

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
