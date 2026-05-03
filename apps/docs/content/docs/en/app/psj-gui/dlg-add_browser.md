---
title: "dlg.add_browser()"
description: "Add a file/folder Browser component to the creating dialog"
version_introduced: "5.0.1"
available_versions: "all"
---

## Description

Add a file/folder Browser component to the creating dialog.

## Syntax

```psj
dlg.add_browser(...)
```

## Inputs

### `name` @type(String) @required

- The name of the created component.

### `layout` @type(String) @required

- The created Layout name.
  The created Layout can be a GroupBox component, Layout component, etc.

### `mode` @type(String) @default("file")

- The Browser type:
  - "file": allowing user to select a file/files.
  - "folder": allowing user to select a folder/folders.

### `file_filter` @type(String) @default("")

- The format of the selectable file/files with type (\*.extension).
  - For example: All Files (\*.\*), Abaqus (\*.inp)

### `default` @type(String) @default("")

- The default text which will be shown on the textbox of this component.

### `multisel` @type(Boolean) @default(False)

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
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label3",text="Open",layout="Layout1")
    dlg.add_browser(name="Open File/Folder2",mode="file",file_filter="All Files(*.*)",
      default="C:\\temp",multisel=True,layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
```
