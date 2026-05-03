---
title: "dlg.show_dlg_help_button()"
description: "Show or hide the help button in the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Show or hide the help button in the creating dialog.

## Syntax

```psj
dlg.show_dlg_help_button(...)
```

## Inputs

### `shown` @type(Boolean) @required

- The visibility of the help button:
  - _True_: show the help button
  - _False_: hide the help button

## Return Code

This function does not have output value.

## Sample Code

```psj {13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label2",text="Label",layout="Layout1")
    dlg.add_textbox(name="TextBox3",layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.show_dlg_help_button(shown=False)
    dlg.generate_window()

if __name__=='__main__':
    main()
```
