---
title: "dlg.set _icon _file()"
description: "Set icon for the creating GUI"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set icon for the creating GUI dialog.

## Syntax

```psj
dlg.set _icon _file(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `file`

- The full path of the icon file using to set the icon for the creating GUI dialog.

## Return Code

This function does not have output value.

## Sample Code

```psj {8}
from pyjdg import *

def main():
    sel _ico = JPT.GetProgramPath() + \
        r"Lib\site-packages\win32\test\win32rcparser\python.ico"

    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.set _icon _file(file=sel _ico)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
