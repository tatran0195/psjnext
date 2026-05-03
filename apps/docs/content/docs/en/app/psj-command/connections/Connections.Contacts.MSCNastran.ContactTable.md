---
title: "Connections.Contacts.MSCNastran.ContactTable()"
description: "create contacts of MSC Nastran Contact Table"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > MSCNastran > ContactTable"
---

## Description

Create contacts of MSC Nastran Contact Table

## Syntax

```psj
Connections.Contacts.MSCNastran.ContactTable(strName="", nastranContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
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
Connections.Contacts.MSCNastran.ContactTable(strName="", nastranContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
```
