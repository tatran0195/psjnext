---
title: "dlg.on _active _tab _page()"
description: "Bind a created function after a TabItem is selected"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Bind a created function after a TabItem is selected.

## Syntax

```psj
dlg.on _active _tab _page(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of TabWnd.

<!-- @since:5.0.1 @type:PSJCallable @required -->
### `callfunc`

- The name of function wants to be bound to.

## Return Code

This function does not have output value.

## Sample Code

```psj {28}
from pyjdg import *

def captureTabWndPageChangeMessage(dlg,tabName,newTabPage):
    curPage=dlg.get _tabwnd _current _page(tabName)
    print("TabWnd:  "+ tabName +" changed page to "+ str(newTabPage))

def changeTabPage(dlg):
    dlg.set _tabwnd _current _page(name="TabWnd1",page _index=1)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _tabwnd(name="TabWnd1",width=200,height=200,layout="Window")
    dlg.add _tabwnd _page(name="TabWnd1",page _name="TabItem2",page _text="TabItem")
    dlg.add _combobox(name="ComboBox4",layout="TabItem2")
    dlg.add _combobox(name="ComboBox5",layout="TabItem2")
    dlg.add _button(name="Button6",text="Button",width=60,height=22,layout="TabItem2")
    dlg.add _button(name="Button7",text="Button",width=60,height=22,layout="TabItem2")
    dlg.add _tabwnd _page(name="TabWnd1",page _name="TabItem3",page _text="TabItem")
    dlg.add _checkbox(name="CheckBox8",text="CheckBox",layout="TabItem3")
    dlg.add _checkbox(name="CheckBox9",text="CheckBox",layout="TabItem3")
    dlg.add _button(name="Button10",text="Click Me to change TabPage",width=260,height=22,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _active _tab _page(name="TabWnd1",callfunc=captureTabWndPageChangeMessage)
    dlg.on _button _clicked(name="Button10",callfunc=changeTabPage)

if __name__=='__main__':
    main()
```
