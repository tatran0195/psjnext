---
title: "dlg.show _dlg _help _button()"
description: "Show or hide the help button in the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show or hide the help button in the creating dialog.

## Syntax

```psj
dlg.show _dlg _help _button(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### shown

- Specify the visibility of the help button:
  - _True_: show the help button
  - _False_: hide the help button

## Return Code

This function does not have output value.

## Sample Code

```psj {13}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label2",text="Label",layout="Layout1")
    dlg.add _textbox(name="TextBox3",layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.show _dlg _help _button(shown=False)
    dlg.generate _window()

if __name__=='__main__':
    main()
```
