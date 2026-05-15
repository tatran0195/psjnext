---
title: "dlg.set _item _size _behavior()"
description: "Set display behavior of TabWnd, ImageCtrl, Table, PagesCtrl"
version _introduced: "5.0.1"
available _versions: "all"
---

import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";

## Description

Set display behavior of TabWnd, ImgCtrl, Table, PagesCtrl.

## Syntax

```psj
dlg.set _item _size _behavior(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify name of the used component.

<!-- @since:5.0.1 @optional -->
### behavior

- Specify display type of the used component:
  - size\_behavior.greedy: Set the displaying component based on the user input width and height, allow resizing component size according to dialog size.
  - size\_behavior.fixed: Set the displaying component based on the user input width and height, and won't resize component size according to dialog size.
    For ImageCtrl, `fixed` will take original size of the image to display fitfully.
  - size\_behavior.horizontal: Set the displaying component with fixing height based on user input and allow resizing component only horizontally.
  - size\_behavior.vertical: Set the displaying component with fixing width based on user input and allow resizing component only vertically.
- The default value is size\_behavior.greedy.

## Return Code

This function does not have output value.

## Sample Code

<Tabs>
<TabItem value="TabWnd" label="TabWnd" default>

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog")
    dlg.add _tabwnd(name="TabWnd2",width=400,height=300,layout="Window")
    dlg.set _item _size _behavior(name="TabWnd2",behavior=size _behavior.greedy)
    dlg.add _tabwnd _page(name="TabWnd2",page _name="TabItem3",page _text="TabItem")
    dlg.add _label(name="Label4",text="Label",text _halign="left",text _valign="top",layout="TabItem3")
    dlg.add _textbox(name="TextBox5",layout="TabItem3")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```

</TabItem>
<TabItem value="ImageCtrl" label="ImageCtrl">

```psj {7}
from pyjdg import *
TechnoStarImage = JPT.GetProgramPath() + "SampleData/PSJ/PSJ-Utility/Utils/TechnoStar.ico"

def main():
    dlg=JDGCreator(title="Dialog")
    dlg.add _imagectrl(name="ImageCtrl2",width=100,height=100,image _file=TechnoStarImage,layout="Window")
    dlg.set _item _size _behavior(name="ImageCtrl2",behavior=size _behavior.fixed)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```

</TabItem>
<TabItem value="Table" label="Table">

```psj {9}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog")
    dlg.add _table(name="Table2",width=400,height=250,columns=["Heading1","Heading2","Heading3"],rows=5,layout="Window")
    dlg.set _table _column _data _type(name="Table2",col=0,data _type="String")
    dlg.set _table _column _data _type(name="Table2",col=1,data _type="String")
    dlg.set _table _column _data _type(name="Table2",col=2,data _type="String")
    dlg.set _item _size _behavior(name="Table2",behavior=size _behavior.horizontal)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```

</TabItem>
<TabItem value="PagesCtrl" label="PagesCtrl">

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog")
    dlg.add _pagesctrl(name="PagesCtrl2",width=300,height=250,layout="Window")
    dlg.set _item _size _behavior(name="PagesCtrl2",behavior=size _behavior.vertical)
    dlg.add _pageitem(name="PagesCtrl2",page _name="PageItem3",page _header="PageItem")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```

</TabItem>

</Tabs>
