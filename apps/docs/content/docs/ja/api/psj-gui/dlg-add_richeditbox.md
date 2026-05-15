---
title: "dlg.add _richeditbox()"
description: "Add a rich edit box to the dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a rich edit box to the dialog.

## Syntax

```psj
dlg.add _richeditbox(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the created component.

<!-- @since:5.0.1 @required -->
### layout

- Specify the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @optional -->
### text

- Specify text displayed by default.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### width

- Specify the width of the rich edit box.
- The default value is 60.

<!-- @since:5.0.1 @optional -->
### height

- Specify the height of the rich edit box.
- The default value is 22.

## Return Code

This function does not have output value.

## Sample Code

```psj {5-6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _richeditbox(name="RichEditBox17",text="RichEditBox content",
        width=200,height=200,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
