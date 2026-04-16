---
id: dlg.set_item_size_behavior
title: dlg.set_item_size_behavior()
author: TechnoStar Co., Ltd.
author_url: https://www.e-technostar.com/
description: Set display behavior of TabWnd, ImageCtrl, Table, PagesCtrl
---

import Tabs from "@theme/Tabs";
import TabItem from "@theme/TabItem";

## Description

Set display behavior of TabWnd, ImgCtrl, Table, PagesCtrl.

## Syntax

```psj
dlg.set_item_size_behavior(...)
```

## Inputs

### `name`

- A _String_ specifying name of the used component.
- This is a required input.

### `behavior`

- An _Enum_ specifying display type of the used component:
    - size_behavior.greedy: Set the displaying component based on the user input width and height, allow resizing component size according to dialog size.
    - size_behavior.fixed: Set the displaying component based on the user input width and height, and won't resize component size according to dialog size.
      For ImageCtrl, `fixed` will take original size of the image to display fitfully.
    - size_behavior.horizontal: Set the displaying component with fixing height based on user input and allow resizing component only horizontally.
    - size_behavior.vertical: Set the displaying component with fixing width based on user input and allow resizing component only vertically.
- The default value is size_behavior.greedy.

## Return Code

This function does not have output value.

## Sample Code

<Tabs>
<TabItem value="TabWnd" label="TabWnd" default>

```psj include="../../../../../examples/cli/5.0.1/psj-gui/dlg-set_item_size_behavior.py"

```

</TabItem>
<TabItem value="ImageCtrl" label="ImageCtrl">

```psj {7}
from pyjdg import *
TechnoStarImage = JPT.GetProgramPath() + "SampleData/PSJ/PSJ-Utility/Utils/TechnoStar.ico"

def main():
    dlg=JDGCreator(title="Dialog")
    dlg.add_imagectrl(name="ImageCtrl2",width=100,height=100,image_file=TechnoStarImage,layout="Window")
    dlg.set_item_size_behavior(name="ImageCtrl2",behavior=size_behavior.fixed)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```

</TabItem>
<TabItem value="Table" label="Table">

```psj {9}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog")
    dlg.add_table(name="Table2",width=400,height=250,columns=["Heading1","Heading2","Heading3"],rows=5,layout="Window")
    dlg.set_table_column_data_type(name="Table2",col=0,data_type="String")
    dlg.set_table_column_data_type(name="Table2",col=1,data_type="String")
    dlg.set_table_column_data_type(name="Table2",col=2,data_type="String")
    dlg.set_item_size_behavior(name="Table2",behavior=size_behavior.horizontal)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```

</TabItem>
<TabItem value="PagesCtrl" label="PagesCtrl">

```psj {6}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog")
    dlg.add_pagesctrl(name="PagesCtrl2",width=300,height=250,layout="Window")
    dlg.set_item_size_behavior(name="PagesCtrl2",behavior=size_behavior.vertical)
    dlg.add_pageitem(name="PagesCtrl2",page_name="PageItem3",page_header="PageItem")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```

</TabItem>

</Tabs>
