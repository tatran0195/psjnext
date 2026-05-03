---
title: "dlg.add_textbox()"
description: "Add a Textbox to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Add a Textbox to the creating dialog.

## Syntax

```psj
dlg.add_textbox(...)
```

## Inputs

### `name` @type(String) @required

- The name of the created component.

### `layout` @type(String) @required

- The created Layout name
  The created Layout can be a GroupBox component, Layout component, etc.

### `text` @type(String) @default("")

- Text which will be displayed.

### `readonly` @type(Boolean) @default(False)

- The read-only state of Textbox is used or not.
  - _True_: The text is read-only state. It can't be editable.
  - _False_: The text can be edited manually.

### `text_color` @type(Integer) @default(0) @since(5.1.0)

- The text color.

### `bk_color` @type(Integer) @default(16777215) @since(5.1.0)

- The background color.

### `width` @type(Integer) @default(0)

- The width of the Textbox.

### `height` @type(Integer) @default(0)

- The height of the Textbox.

### `text_align` @type(String) @default("Left")

- The text position which will be displayed.
  - "Left": align text to left side.
  - "Center": center text to the middle.
  - "Right": align text to right side.

### `type` @type(String) @default("string")

- The data type for the Textbox:
  - "string": input values are in th&#x65;_&#x53;trin&#x67;_&#x66;ormat.
  - "double": input values are in th&#x65;_&#x44;oubl&#x65;_&#x66;ormat.
  - "integer": input values are in th&#x65;_&#x49;ntege&#x72;_&#x66;ormat.

## Return Code

This function does not have output value.

## Sample Code

```psj {7-8,11-12,15-16,19-20,30-31,34-35}
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_layout(name="Layout2",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label3",text="String Type",width=100,text_halign="left",text_valign="top",layout="Layout2")
    dlg.add_textbox(name="TextBox4",width=150,height=25,readonly=True,
        text="TechnoStar",type="string",text_align="left",layout="Layout2")
    dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label7",text="String Type",width=100,text_halign="left",text_valign="top",layout="Layout6")
    dlg.add_textbox(name="TextBox8",width=150,height=25,readonly=False,
        text="12345",type="string",bk_color=16711168,text_color=255,text_align="left",layout="Layout6")
    dlg.add_layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label10",text="Integer Type",width=100,text_halign="left",text_valign="top",layout="Layout9")
    dlg.add_textbox(name="TextBox11",width=150,height=25,readonly=False,
        text="TechnoStar",type="integer",text_align="center",layout="Layout9")
    dlg.add_layout(name="Layout12",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label13",text="Integer Type",width=100,text_halign="left",text_valign="top",layout="Layout12")
    dlg.add_textbox(name="TextBox14",width=150,height=25,readonly=True,
        text="12345",bk_color=65535,text_color=255,type="integer",text_align="center",layout="Layout12")
    font_TextBox14=PSJFont()
    font_TextBox14.size=12
    font_TextBox14.bold=True
    font_TextBox14.italic=False
    font_TextBox14.underline=True
    font_TextBox14.strikeout=False
    dlg.set_item_font(name="TextBox14",font=font_TextBox14)
    dlg.add_layout(name="Layout15",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label16",text="Double Type",width=100,text_halign="left",text_valign="top",layout="Layout15")
    dlg.add_textbox(name="TextBox17",width=150,height=25,readonly=False,
        text="TechnoStar",type="double",text_align="right",layout="Layout15")
    dlg.add_layout(name="Layout18",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label19",text="Double Type",width=100,text_halign="left",text_valign="top",layout="Layout18")
    dlg.add_textbox(name="TextBox20",width=150,height=25,readonly=True,
        text="12345.123",type="double",text_align="right",layout="Layout18")
    font_TextBox20=PSJFont()
    font_TextBox20.size=12
    font_TextBox20.bold=False
    font_TextBox20.italic=True
    font_TextBox20.underline=True
    font_TextBox20.strikeout=False
    dlg.set_item_font(name="TextBox20",font=font_TextBox20)
    dlg.generate_window()

if __name__=='__main__':
    main()
```
