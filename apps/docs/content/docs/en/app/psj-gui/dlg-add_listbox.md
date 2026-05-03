---
title: "dlg.add_listbox()"
description: "Add a ListBox to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Add a ListBox to the creating dialog.

## Syntax

```psj
dlg.add_listbox(...)
```

## Inputs

### `name` @type(String) @required

- The name of the created component.

### `layout` @type(String) @required

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

### `multisel` @type(Boolean) @default(False)

- The permission that allow user to select multiple values at the same time:
  - _True_: user can select multiple values.
  - _False_: user can select only one value per time.

### `options` @type(List\[String]) @default(\[])

- All the options of the ListBox component.

### `width` @type(Integer) @default(0)

- The width of the ListBox.

### `height` @type(Integer) @default(0)

- The height of the ListBox.

## Return Code

This function does not have output value.

## Sample Code

```psj {5-6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_listbox(name="ListBox3",multisel=True,
      options=["item1","item2","item3"],width=100,height=150,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")

    dlg.generate_window()
if __name__=='__main__':
    main()
```
