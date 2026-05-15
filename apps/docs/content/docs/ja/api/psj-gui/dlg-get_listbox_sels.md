---
title: "dlg.get _listbox _sels()"
description: "Get the index of the selecting ListBox option"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get the indexes of the selecting ListBox options.

## Syntax

```psj
dlg.get _listbox _sels(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### name

- Specify the name of the ListBox component.

## Return Code

An _[IntVector](../data-type/psj-utility/pre-utility/built-in-types/IntVector)_ specifying the indexes of the being selected ListBox options.

## Sample Code

```psj {4}
from pyjdg import *

def onButtonClicked(dlg):
    listBoxPos=dlg.get _listbox _sels(name="ListBox2")
    dlg.set _item _text(name="TextBox4",text=str(list(listBoxPos)))

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _listbox(name="ListBox2",multisel=True,
      options=["item1","item2","item3","item4"],width=100,height=150,layout="Window")
    dlg.set _item _size _behavior(name="ListBox2",behavior=size _behavior.fixed)
    dlg.add _layout(name="Layout3",orientation=orientation.horizontal,layout="Window")
    dlg.add _textbox(name="TextBox4",width=150,height=22,layout="Layout3")
    dlg.add _button(name="Button5",text="Get Index",width=60,height=22,bk _color=15790320,layout="Layout3")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _command(name="Button5",callfunc=onButtonClicked)

if __name__=='__main__':
    main()
```
