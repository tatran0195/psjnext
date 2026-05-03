---
title: "dlg.set_groupbox_orientation()"
description: "Set the layout of all the components inside the inputted GroupBox component to be aligned in the horizontal or vertical direction"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Set the layout of all the components inside the GroupBox component to be aligned in the horizontal or vertical direction.

## Syntax

```psj
dlg.set_groupbox_orientation(...)
```

## Inputs

### `name` @type(String) @required

- The name of the component using for setting the orientation option.

### `orientation` @type(String) @required

- The orientation option of the GroupBox:
  - "vertical": align all the inside components in the vertical direction.
  - "horizontal": align all the inside components in the horizontal direction.

## Return Code

This function does not have output value.

## Sample Code

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_groupbox(name="GroupBox1",text="GroupBox",layout="Window")
    dlg.set_groupbox_orientation(name="GroupBox1",orientation="vertical")
    dlg.add_label(name="Label2",text="Label",layout="GroupBox1")
    dlg.add_textbox(name="TextBox3",layout="GroupBox1")
    dlg.add_label(name="Label4",text="Label",layout="GroupBox1")
    dlg.add_textbox(name="TextBox5",layout="GroupBox1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
