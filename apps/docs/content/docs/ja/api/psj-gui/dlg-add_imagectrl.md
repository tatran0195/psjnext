---
title: "dlg.add _imagectrl()"
description: "Add a frame to put an image to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a frame to put an image to the creating dialog.

## Syntax

```psj
dlg.add _imagectrl(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the created component.

<!-- @since:5.0.1 @required -->
### image\_file

- Specify the location of an image to display as default.

<!-- @since:5.0.1 @required -->
### layout

- Specify the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

## Return Code

This function does not have output value.

## Sample Code

```psj {7}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    image = JPT.GetProgramPath() + \
        r"SampleData\PSJ\PSJ-GUI\CreateBolt\CreatingBolt _Pics\M30.JPG"
    dlg.add _imagectrl(name="ImageCtrl",image _file=image,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
