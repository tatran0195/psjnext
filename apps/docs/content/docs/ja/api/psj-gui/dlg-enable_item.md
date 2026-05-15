---
title: "dlg.enable _item()"
description: "Change the \"Enable\" option of an inputted component to on (Enabled)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Change the "Enable" option of an inputted component to on (Enabled).

## Syntax

```psj
dlg.enable _item(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the component.

## Return Code

This function does not have output value.

## Sample Code

```psj {15}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _label(name="Label1",text="Label",layout="Window")
    dlg.add _textbox(name="TextBox2",layout="Window")
    dlg.add _textbox(name="TextBox3",layout="Window")
    dlg.add _textbox(name="TextBox4",layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.disable _item(name="TextBox3")
    dlg.enable _item(name="TextBox3")
    dlg.generate _window()
    
if __name__=='__main__':
    main()
```
