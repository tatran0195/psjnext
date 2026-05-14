---
title: "dlg.add _browser()"
description: "Add a file/folder Browser component to the creating dialog"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Add a file/folder Browser component to the creating dialog.

## Syntax

```psj
dlg.add _browser(...)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `name`

- The name of the created component.

<!-- @since:5.0.1 @type:String @required -->
### `layout`

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

<!-- @since:5.0.1 @type:String @optional @default:"file" -->
### `mode`

- The Browser type:
  - "file": allowing user to select a file/files.
  - "folder": allowing user to select a folder/folders.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `file _filter`

- The format of the selectable file/files with type (\*.extension).
  - For example: All Files (\*.\*), Abaqus (\*.inp)

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `default`

- The default text which will be shown on the textbox of this component.

<!-- @since:5.0.1 @type:Boolean @optional @default:False -->
### `multisel`

- The possibility of the multiple selection:
  - _True_: allow user to select multiple files/folders at the same time.
  - _False_: allow user to select only one file/folder at a time.

## Return Code

This function does not have output value.

## Sample Code

```psj {7-8}
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add _layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add _label(name="Label3",text="Open",layout="Layout1")
    dlg.add _browser(name="Open File/Folder2",mode="file",file _filter="All Files(*.*)",
      default="C:\\temp",multisel=True,layout="Layout1")
    dlg.add _hlayout(name="footer",layout="Window")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.add _button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add _button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add _space(orientation="horizontal",layout="footer")
    dlg.generate _window()

if __name__=='__main__':
    main()
```
