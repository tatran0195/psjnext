---
title: "dlg.add _tabwnd _page()"
description: "Add a TabItem (page) to the TabWnd component"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a TabItem (page) to the TabWnd component.

## Syntax

```psj
dlg.add _tabwnd _page(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the TabWnd component in which the creating TabItem will be put added to.

<!-- @since:5.0.1 @required -->
### page\_name

- Specify the name of the created component.

<!-- @since:5.0.1 @optional -->
### page\_text

- Specify text which will be displayed as a title.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### page\_orientation

- Specify the orientation of the creating tab page. It has 2 options:
  - "vertical": aligning all the inside components in the vertical direction.
  - "horizontal": aligning all the inside components in the horizontal direction.
- The default value is "vertical".

## Return Code

This function does not have output value.

## Sample Code

```psj {6,9}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",include _apply=False)
    dlg.add _tabwnd(name="TabWnd2",width=200,height=200,layout="Window")
    dlg.add _tabwnd _page(name="TabWnd2",page _name="TabItem3",page _text="TabItem",page _orientation="vertical")
    dlg.add _label(name="Label5",text="Label",text _halign="left",text _valign="top",layout="TabItem3")
    dlg.add _textbox(name="TextBox6",layout="TabItem3")
    dlg.add _tabwnd _page(name="TabWnd2",page _name="TabItem4",page _text="TabItem",page _orientation="horizontal")
    dlg.add _label(name="Label7",text="Label",text _halign="left",text _valign="top",layout="TabItem4")
    dlg.add _textbox(name="TextBox8",layout="TabItem4")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
