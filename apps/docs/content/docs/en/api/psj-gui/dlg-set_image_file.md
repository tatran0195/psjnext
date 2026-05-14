---
title: "dlg.set _image _file()"
description: "Set an image location to the ImageCtrl"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set an image to the ImageCtrl.

## Syntax

```psj
dlg.set _image _file(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the ImageCtrl component.

<!-- @since:5.0.1 @type:String @required -->
### `image _path`

- The full path of the image.

## Return Code

This function does not have output value.

## Sample Code

```psj {5}
from pyjdg import *

def onChangeButtonClicked(dlg):
    new _pic = JPT.GetProgramPath() + r"SampleData\PSJ\PSJ-GUI\CreateBolt\CreatingBolt _Pics\M4.JPG"
    dlg.set _image _file(name="ImageCtrl",image _path=new _pic)

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    image = JPT.GetProgramPath() + \
        r"SampleData\PSJ\PSJ-GUI\CreateBolt\CreatingBolt _Pics\M3.JPG"
    dlg.add _imagectrl(name="ImageCtrl",image _file=image,layout="Window")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ChangePic",text="Change",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()
    dlg.on _command(name="ChangePic",callfunc=onChangeButtonClicked)

if __name__=='__main__':
    main()
```
