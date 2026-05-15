---
title: "dlg.close()"
description: "Close the dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Close the dialog.

## Syntax

```psj
dlg.close(...)
```

## Inputs

This function does not require any input value.

## Return Code

This function does not have output value.

## Sample Code

```psj {4}
from pyjdg import *

def on _button _clicked(dlg):
    dlg.close()

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,
        layout="Window")
    dlg.add _label(name="Label2",
        text="Click any button to close this dialog!",layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonApply",text="Apply",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _button _clicked(name="ButtonApply",callfunc=on _button _clicked)
    dlg.on _button _clicked(name="ButtonOk",callfunc=on _button _clicked)

if __name__=='__main__':
    main()
```
