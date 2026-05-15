---
title: "dlg.get _item _text()"
description: "Get text inside the component"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Get text inside the component.

## Syntax

```psj
dlg.get _item _text(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the component which user want to get text.

## Return Code

A _String_ specifying the text inside the component.

## Sample Code

```psj {3}
from pyjdg import *
def onGetButtonClicked(dlg):
    print(dlg.get _item _text(name="TextBox1"))

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _textbox(name="TextBox1",layout="Window")
    dlg.add _button(name="Button2",text="Get text",width=60,height=22,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _command(name="Button2",callfunc=onGetButtonClicked)

if __name__=='__main__':
    main()
```
