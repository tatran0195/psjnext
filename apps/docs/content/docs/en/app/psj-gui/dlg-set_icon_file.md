---
title: "dlg.set_icon_file()"
description: "Set icon for the creating GUI"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Set icon for the creating GUI dialog.

## Syntax

```psj
dlg.set_icon_file(...)
```

## Inputs

### `file` @type(String) @required

- The full path of the icon file using to set the icon for the creating GUI dialog.

## Return Code

This function does not have output value.

## Sample Code

```psj {8}
from pyjdg import *

def main():
    sel_ico = JPT.GetProgramPath() + \
        r"Lib\site-packages\win32\test\win32rcparser\python.ico"

    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.set_icon_file(file=sel_ico)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
