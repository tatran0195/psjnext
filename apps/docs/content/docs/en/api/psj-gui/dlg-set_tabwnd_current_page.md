---
title: "dlg.set _tabwnd _current _page()"
description: "Set the current page of the TabWnd to a specific TabItem order"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set the current page of the TabWnd to a specific TabItem order.

## Syntax

```psj
dlg.set _tabwnd _current _page(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the TabWnd component using for setting the current page.

<!-- @since:5.0.1 @type:Integer @required -->
### `page _index`

- The tab order.

## Return Code

This function does not have output value.

## Sample Code

```psj {23}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _tabwnd(name="TabWnd2",width=300,height=300,layout="Layout1")
    dlg.add _tabwnd _page(name="TabWnd2",page _name="TabItem3",page _text="Jupiter-Pre",page _orientation="horizontal")
    dlg.add _label(name="Label7",text="Label",layout="TabItem3")
    dlg.add _textbox(name="TextBox8",layout="TabItem3")
    dlg.add _tabwnd _page(name="TabWnd2",page _name="TabItem4",page _text="Jupiter-Post")
    dlg.add _radiobutton(name="RadioButton9",text="RadioButton",layout="TabItem4")
    dlg.add _radiobutton(name="RadioButton10",text="RadioButton",layout="TabItem4")
    dlg.add _tabwnd _page(name="TabWnd2",page _name="TabItem5",page _text="Sunshine")
    dlg.add _slider(name="Slider11",width=100,height=30,min=0,max=100,pos=0,layout="TabItem5")
    dlg.add _tabwnd _page(name="TabWnd2",page _name="TabItem6",page _text="PSJ")
    dlg.add _listbox(name="ListBox12",width=100,height=100,layout="TabItem6")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.set _tabwnd _current _page(name="TabWnd2",page _index=2)

if __name__=='__main__':
    main()
```
