---
title: "dlg.add_label()"
description: "Add a Label to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Add a Label to the creating dialog.

## Syntax

```psj
dlg.add_label(...)
```

## Inputs

### `name` @type(String) @required

- The name of the created component.

### `layout` @type(String) @required

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

### `text` @type(String) @default("")

- Text which will be displayed.

### `width` @type(Integer) @default(0)

- The width of the Label.

### `height` @type(Integer) @default(0)

- The height of the Label.

### `text_halign` @type(String) @default("left")

- The alignment in horizontal direction:
  - "left": align the showing text to the left in the horizontal direction.
  - "center": align the showing text to the center in the horizontal direction.
  - "right": align the showing text to the right in the horizontal direction.

### `text_valign` @type(String) @default("top")

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
    dlg.add_label(name="Label2",text="Label",width=30,height=30,
      text_halign="center",text_valign="middle",layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
