---
title: "dlg.add _textbox()"
description: "Add a Textbox to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a Textbox to the creating dialog.

## Syntax

```psj
dlg.add _textbox(...)
```

## Inputs

<!-- @since:5.0.1 @required -->
### name

- Specify the name of the created component.

<!-- @since:5.0.1 @required -->
### layout

- Specify the created Layout name
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @optional -->
### text

- Specify text which will be displayed.
- The default value is "".

<!-- @since:5.0.1 @optional -->
### readonly

- Specify the read-only state of Textbox is used or not.
  - _True_: The text is read-only state. It can't be editable.
  - _False_: The text can be edited manually.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### text\_color

- Specify the text color.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bk\_color

- Specify the background color.
- The default value is 16777215.

<!-- @since:5.0.1 @optional -->
### width

- Specify the width of the Textbox.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### height

- Specify the height of the Textbox.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### text\_align

- Specify the text position which will be displayed.
  - "Left": align text to left side.
  - "Center": center text to the middle.
  - "Right": align text to right side.
- The default value is "Left".

<!-- @since:5.0.1 @optional -->
### type

- Specify the data type for the Textbox:
  - "string": input values are in the _String_ format.
  - "double": input values are in the _Double_ format.
  - "integer": input values are in the _Integer_ format.
- The default value is "string".

## Return Code

This function does not have output value.

## Sample Code

```psj {7-8,11-12,15-16,19-20,30-31,34-35}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",include _apply=False)
    dlg.add _layout(name="Layout2",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label3",text="String Type",width=100,text _halign="left",text _valign="top",layout="Layout2")
    dlg.add _textbox(name="TextBox4",width=150,height=25,readonly=True,
        text="TechnoStar",type="string",text _align="left",layout="Layout2")
    dlg.add _layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label7",text="String Type",width=100,text _halign="left",text _valign="top",layout="Layout6")
    dlg.add _textbox(name="TextBox8",width=150,height=25,readonly=False,
        text="12345",type="string",bk _color=16711168,text _color=255,text _align="left",layout="Layout6")
    dlg.add _layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label10",text="Integer Type",width=100,text _halign="left",text _valign="top",layout="Layout9")
    dlg.add _textbox(name="TextBox11",width=150,height=25,readonly=False,
        text="TechnoStar",type="integer",text _align="center",layout="Layout9")
    dlg.add _layout(name="Layout12",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label13",text="Integer Type",width=100,text _halign="left",text _valign="top",layout="Layout12")
    dlg.add _textbox(name="TextBox14",width=150,height=25,readonly=True,
        text="12345",bk _color=65535,text _color=255,type="integer",text _align="center",layout="Layout12")
    font _TextBox14=PSJFont()
    font _TextBox14.size=12
    font _TextBox14.bold=True
    font _TextBox14.italic=False
    font _TextBox14.underline=True
    font _TextBox14.strikeout=False
    dlg.set _item _font(name="TextBox14",font=font _TextBox14)
    dlg.add _layout(name="Layout15",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label16",text="Double Type",width=100,text _halign="left",text _valign="top",layout="Layout15")
    dlg.add _textbox(name="TextBox17",width=150,height=25,readonly=False,
        text="TechnoStar",type="double",text _align="right",layout="Layout15")
    dlg.add _layout(name="Layout18",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label19",text="Double Type",width=100,text _halign="left",text _valign="top",layout="Layout18")
    dlg.add _textbox(name="TextBox20",width=150,height=25,readonly=True,
        text="12345.123",type="double",text _align="right",layout="Layout18")
    font _TextBox20=PSJFont()
    font _TextBox20.size=12
    font _TextBox20.bold=False
    font _TextBox20.italic=True
    font _TextBox20.underline=True
    font _TextBox20.strikeout=False
    dlg.set _item _font(name="TextBox20",font=font _TextBox20)
    dlg.generate _window()

if __name__=='__main__':
    main()
```
