---
title: "dlg.add_radiobutton()"
description: "Add a RadioButton to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Add a RadioButton to the creating dialog.

## Syntax

```psj
dlg.add_radiobutton(...)
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

- The width of the RadioButton.

### `height` @type(Integer) @default(0)

- The height of the RadioButton.

### `checked` @type(Boolean) @default(False)

- The default state of this component:
  - _True_: the default state of this component is checked.
  - _False_: the default state of this component is unchecked.

### `group` @type(Boolean) @default(False)

- The group in which this RadioButton will be added to:
  - _True_: creating RadioButton will be added separately from the previous RadioButton (different group of button). So, at the time selecting the creating RadioButton, the selected RadioButton will not be deselected.
  - _False_: creating RadioButton will be added to the same group with previous RadioButton. So, at the time selecting the creating RadioButton, the selected RadioButton will be deselected.

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_radiobutton(name="RadioButton16",text="RadioButton",layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    
if __name__=='__main__':
    main()
```
