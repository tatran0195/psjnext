---
title: "dlg.disable_item()"
description: "Change the \"Enable\" option of an inputted component to off (Disabled)"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Change the "Enable" option of an inputted component to off (Disabled).

## Syntax

```psj
dlg.disable_item(...)
```

## Inputs

### `name` @type(String) @required

- The name of the component.

## Return Code

This function does not have output value.

## Sample Code

```psj {14}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_label(name="Label1",text="Label",layout="Window")
    dlg.add_textbox(name="TextBox2",layout="Window")
    dlg.add_textbox(name="TextBox3",layout="Window")
    dlg.add_textbox(name="TextBox4",layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.disable_item(name="TextBox3")
    dlg.generate_window()
    
if __name__=='__main__':
    main()
```
