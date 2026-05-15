---
title: "dlg.add _button()"
description: "Add a Button to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a Button to the creating dialog. The Button can be an image Button.

## Syntax

```psj
dlg.add _button(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the created component.

<!-- @since:5.0.1 @required -->
### layout

- Specify the created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @optional -->
### text

- Specify text which will be displayed on the Button.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### width

- Specify the width of the Button.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### height

- Specify the height of the Button.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### text\_color

- Specify the text color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bk\_color

- Specify the background color.
- The default value is 15790320.

<!-- @since:5.0.1 @optional -->
### img

- Specify the path of an image to be displayed on the Button.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### location

- Specify the location of an image to be displayed on the Button.
- The default value is "left".

## Return Code

This function does not have output value.

## Sample Code

```psj {8,16-17,25-26,34-35}
from pyjdg import *

TechnoStarImage = JPT.GetProgramPath() + "SampleData/PSJ/PSJ-Utility/Utils/TechnoStar.ico"

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add _layout(name="Layout2",orientation=orientation.horizontal,layout="Window")
    dlg.add _button(name="Button3",text="Button",width=60,height=22,layout="Layout2")
    font _Button3=PSJFont()
    font _Button3.size=10
    font _Button3.bold=True
    font _Button3.italic=False
    font _Button3.underline=False
    font _Button3.strikeout=False
    dlg.set _item _font(name="Button3",font=font _Button3)
    dlg.add _button(name="Button4",text="Button",width=60,height=22,bk _color=65535,
        text _color=255,img=TechnoStarImage,location="left",layout="Layout2")
    font _Button4=PSJFont()
    font _Button4.size=10
    font _Button4.bold=False
    font _Button4.italic=True
    font _Button4.underline=False
    font _Button4.strikeout=False
    dlg.set _item _font(name="Button4",font=font _Button4)
    dlg.add _button(name="Button5",text="Button",width=60,height=22,bk _color=65535,
        text _color=255,img=TechnoStarImage,location="right",layout="Layout2")
    font _Button5=PSJFont()
    font _Button5.size=10
    font _Button5.bold=False
    font _Button5.italic=False
    font _Button5.underline=True
    font _Button5.strikeout=False
    dlg.set _item _font(name="Button5",font=font _Button5)
    dlg.add _button(name="Button6",text="Button",width=60,height=22,bk _color=65535,
        text _color=255,img=TechnoStarImage,location="top",layout="Layout2")
    font _Button6=PSJFont()
    font _Button6.size=10
    font _Button6.bold=True
    font _Button6.italic=True
    font _Button6.underline=True
    font _Button6.strikeout=False
    dlg.set _item _font(name="Button6",font=font _Button6)
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
