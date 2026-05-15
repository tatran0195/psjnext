---
title: "dlg.hide _layout()"
description: "Hide the Layout and all of its children components inside"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Hide the Layout and all of its children components inside.

## Syntax

```psj
dlg.hide _layout(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the Layout component.

## Return Code

This function does not have output value.

## Sample Code

```psj {20}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label2",text="Label",layout="Layout1")
    dlg.add _textbox(name="TextBox3",layout="Layout1")
    dlg.add _layout(name="Layout4",orientation=orientation.horizontal,layout="Window")
    dlg.add _richeditbox(name="RichEditBox8",text="RichEditBox",width=200,height=200,layout="Layout4")
    dlg.add _layout(name="Layout5",orientation=orientation.horizontal,layout="Window")
    dlg.add _textbox(name="TextBox7",layout="Layout5")
    dlg.add _layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
    dlg.add _combobox(name="ComboBox9",layout="Layout6")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.hide _layout(name="Layout5")

if __name__=='__main__':
    main()
```
