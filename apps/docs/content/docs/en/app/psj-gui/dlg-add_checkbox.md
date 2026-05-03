---
title: "dlg.add_checkbox()"
description: "Add a CheckBox to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Add a CheckBox to the creating dialog.

## Syntax

```psj
dlg.add_checkbox(...)
```

## Inputs

### `name` @type(String) @required

- The name of the created component.

### `layout` @type(String) @required

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

### `text` @type(String) @default("")

- Text which will be displayed next to the CheckBox.

### `checked` @type(Boolean) @default(False)

- The default state of this component:
  - _True_: the default state of this component is checked.
  - _False_: the default state of this component is unchecked.

### `lefttext` @type(Boolean) @default(False)

- The text is on left side of CheckBox:
  - _True_: the text is on left side of the CheckBox.
  - _False_: the text is on right side of the CheckBox.

### `width` @type(Integer) @default(0)

- The width of the CheckBox.

### `height` @type(Integer) @default(0)

- The height of the CheckBox.

## Return Code

This function does not have output value.

## Sample Code

```psj {5,6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_checkbox(name="CheckBox2",text="CheckBox",lefttext=True,checked=True,layout="Window")
    dlg.add_checkbox(name="CheckBox3",text="CheckBox",lefttext=False,checked=True,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
