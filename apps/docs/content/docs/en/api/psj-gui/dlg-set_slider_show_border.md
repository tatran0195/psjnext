---
title: "dlg.set _slider _show _border()"
description: "Show border of the SliderBar"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Show border of the SliderBar.

## Syntax

```psj
dlg.set _slider _show _border(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the SliderBar.

<!-- @since:5.0.1 @type:Boolean @required -->
### `enabled`

- The state of the slider's border:
  - _True_: show outside border of the creating SliderBar.
  - _False_: hide outside border of the creating SliderBar.

## Return Code

This function does not have output value.

## Sample Code

```psj {7}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _slider(name="Slider3",width=100,height=30,min=0,max=100,pos=0,layout="Layout1")
    dlg.set _slider _show _border(name="Slider3",enabled=True)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
