---
title: "dlg.add_imagectrl()"
description: "Add a frame to put an image to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Add a frame to put an image to the creating dialog.

## Syntax

```psj
dlg.add_imagectrl(...)
```

## Inputs

### `name` @type(String) @required

- The name of the created component.

### `image_file` @type(String) @required

- The location of an image to display as default.

### `layout` @type(String) @required

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

## Return Code

This function does not have output value.

## Sample Code

```psj {7}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    image = JPT.GetProgramPath() + \
        r"SampleData\PSJ\PSJ-GUI\CreateBolt\CreatingBolt_Pics\M30.JPG"
    dlg.add_imagectrl(name="ImageCtrl",image_file=image,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
