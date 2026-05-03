---
title: "dlg.set_image_file()"
description: "Set an image location to the ImageCtrl"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Set an image to the ImageCtrl.

## Syntax

```psj
dlg.set_image_file(...)
```

## Inputs

### `name` @type(String) @required

- The name of the ImageCtrl component.

### `image_path` @type(String) @required

- The full path of the image.

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def onChangeButtonClicked(dlg):
    new_pic = JPT.GetProgramPath() + r"SampleData\PSJ\PSJ-GUI\CreateBolt\CreatingBolt_Pics\M4.JPG"
    dlg.set_image_file(name="ImageCtrl",image_path=new_pic)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    image = JPT.GetProgramPath() + \
        r"SampleData\PSJ\PSJ-GUI\CreateBolt\CreatingBolt_Pics\M3.JPG"
    dlg.add_imagectrl(name="ImageCtrl",image_file=image,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ChangePic",text="Change",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.on_command(name="ChangePic",callfunc=onChangeButtonClicked)

if __name__=='__main__':
    main()
```
