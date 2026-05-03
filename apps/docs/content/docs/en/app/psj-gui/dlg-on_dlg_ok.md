---
title: "dlg.on_dlg_ok()"
description: "Execute a created function when OK button is clicked"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Execute a created function when OK button is clicked.

## Syntax

```psj
dlg.on_dlg_ok(...)
```

## Inputs

### `callfunc` @type(PSJCallable) @required

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {11}
from pyjdg import *

def on_button_OK_clicked(dlg):
    print("OK button is clicked")

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True,include_apply=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label2",text="Please click on OK button!",layout="Layout1")
    dlg.generate_window()
    dlg.on_dlg_ok(callfunc=on_button_OK_clicked)

if __name__=='__main__':
    main()
```
