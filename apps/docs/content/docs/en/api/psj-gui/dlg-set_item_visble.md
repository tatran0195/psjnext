---
title: "dlg.set _item _visible()"
description: "Set the state of the created component as visible or hidden, usable for all ToolBox types"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Set the state of the created component as visible or hidden, usable for all ToolBox types.

## Syntax

```psj
dlg.dlg.set _item _visible(...)
```

## Inputs

<!-- @since:5.1.0 @type:String @required -->
### `name`

- The name of the component to be shown or hidden.

<!-- @since:5.1.0 @type:Boolean @required -->
### `visible`

- The state of the specified component:
  - _True_: Show the component.
  - _False_: Hide the component.

## Return Code

This function does not have output value.

## Sample Code

```psj {6-8,10-12}
from pyjdg import *

def on _combobox _changed(dlg):
    combobox _sel = dlg.get _combobox _sel(name="ComboBox4")
    if combobox _sel == 1:
        dlg.set _item _visible(name="PageItem8",visible=False)
        dlg.set _item _visible(name="PageItem9",visible=False)
        dlg.set _item _visible(name="Table14",visible=False)
    if combobox _sel == 0:
        dlg.set _item _visible(name="PageItem8",visible=True)
        dlg.set _item _visible(name="PageItem9",visible=True)
        dlg.set _item _visible(name="Table14",visible=True)

def main():
    dlg=JDGCreator(title="Dialog",include _apply=False)
    dlg.add _layout(name="Layout2",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label3",text="Select Layout",text _halign="left",text _valign="top",layout="Layout2")
    dlg.add _combobox(name="ComboBox4",options=["Layout1","Layout2"],index=0,layout="Layout2")
    dlg.add _layout(name="Layout5",orientation=orientation.horizontal,layout="Window")
    dlg.add _pagesctrl(name="PagesCtrl6",width=260,height=160,current _page=2,layout="Layout5")
    dlg.add _pageitem(name="PagesCtrl6",page _name="PageItem7",page _header="First page")
    dlg.add _groupbox(name="GroupBox10",text="GroupBox",layout="PageItem7")
    dlg.add _layout(name="Layout11",orientation=orientation.horizontal,layout="GroupBox10")
    dlg.add _label(name="Label12",text="Label",text _halign="left",text _valign="top",layout="Layout11")
    dlg.add _browser(name="Browser13",mode="file",file _filter="All Files(*.*)",layout="Layout11")
    dlg.add _table(name="Table14",width=260,height=160,columns=["Heading1","Heading2"],rows=5,layout="GroupBox10")
    dlg.add _pageitem(name="PagesCtrl6",page _name="PageItem8",page _header="Second page")
    dlg.add _pageitem(name="PagesCtrl6",page _name="PageItem9",page _header="Third page")
    dlg.generate _window()
    dlg.set _pagesctrl _current _page(name="PagesCtrl6",page _index=0)
    dlg.on _combobox _sel(name="ComboBox4",callfunc=on _combobox _changed)

if __name__=='__main__':
    main()
```
