---
title: "dlg.set _item _text()"
description: "Set the text which will be shown inside the component"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set the text which will be shown inside the component.

## Syntax

```psj
dlg.set _item _text(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the component.

<!-- @since:5.0.1 @type:String @required -->
### `text`

- The content displayed.

## Return Code

This function does not have output value.

## Sample Code

```psj {3}
from pyjdg import *
def onSetButtonClicked(dlg):
    dlg.set _item _text(name="TextBox1",text="This is sample text")

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _textbox(name="TextBox1",layout="Window")
    dlg.add _button(name="Button2",text="Set text",width=60,height=22,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _command(name="Button2",callfunc=onSetButtonClicked)

if __name__=='__main__':
    main()
```
