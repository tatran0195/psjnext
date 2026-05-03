---
title: "Connections.Contacts.MSCNastran.ContactGroupByMatrix()"
description: "create contacts of MSC Nastran Contact Group By Matrix"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > MSCNastran > ContactGroupByMatrix"
---

## Description

Create contacts of MSC Nastran Contact Group By Matrix

## Syntax

```psj
Connections.Contacts.MSCNastran.ContactGroupByMatrix(strName="", nastranContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
```

## Inputs

### `strName` @type(String) @default("")

- The name.

### `nastranContact` @type(NASTRAN\_CONTACT) @default(NASTRAN\_CONTACT())

- The contact.

### `crplTarget` @type(Cursor Pair List) @default(\[])

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `iColor` @type(Integer) @default(65280)

- The color.

### `iMethod` @type(Integer) @default(1)

- The method.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.MSCNastran.ContactGroupByMatrix(strName="", nastranContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
```
