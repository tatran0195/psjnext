---
title: "dlg.add_groupbox()"
description: "Add a GroupBox to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Add a GroupBox to the creating dialog.

## Syntax

```psj
dlg.add_groupbox(...)
```

## Inputs

### `name` @type(String) @required

- The name of the created component.

### `layout` @type(String) @required

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

### `text` @type(String) @default("")

- Text which will be displayed.

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_groupbox(name="GroupBox1",text="Jupiter",layout="Window")
    dlg.add_layout(name="Layout2",orientation=orientation.horizontal,layout="GroupBox1")
    dlg.add_label(name="Label3",text="Label",layout="Layout2")
    dlg.add_textbox(name="TextBox4",layout="Layout2")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
