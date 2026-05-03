---
title: "dlg.add_combobox()"
description: "Add a ComboBox component to the dialog"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Add a ComboBox component to the dialog.

## Syntax

```psj
dlg.add_combobox(...)
```

## Inputs

### `name` @type(String) @required

- The name of the ComboBox component.

### `layout` @type(String) @required

- The Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

### `index` @type(Integer) @required

- The default option to be displayed of the ComboBox.
- The starting value is 0 (first option -> index=0).

### `options` @type(List\[String]) @default(\[])

- The options of the ComboBox.

### `width` @type(Integer) @default(0)

- The width of the ComboBox.

### `height` @type(Integer) @default(0)

- The height of the ComboBox.

## Return Code

This function does not have output value.

## Sample Code

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_combobox(name="ComboBox2",options=["item1","item2","item3","item4"],index=1,layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
