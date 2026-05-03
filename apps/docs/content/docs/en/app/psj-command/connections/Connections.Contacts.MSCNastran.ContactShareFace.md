---
title: "Connections.Contacts.MSCNastran.ContactShareFace()"
description: "create contacts of MSC Nastran Contact Share Face"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > MSCNastran > ContactShareFace"
---

## Description

Create contacts of MSC Nastran Contact Share Face

## Syntax

```psj
Connections.Contacts.MSCNastran.ContactShareFace(crlShareFace=[], strName="", nastranContact=NASTRAN_CONTACT(), crEdit=None, iColor=65280, iMethod=3)
```

## Inputs

### `crlShareFace` @type(List\[Cursor]) @default(\[])

- The share face.

### `strName` @type(String) @default("")

- The name.

### `nastranContact` @type(NASTRAN\_CONTACT) @default(NASTRAN\_CONTACT())

- The contact.

### `crEdit` @type(Cursor) @default(None)

- The edit.

### `iColor` @type(Integer) @default(65280)

- The color.

### `iMethod` @type(Integer) @default(3)

- The method.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.MSCNastran.ContactShareFace(crlShareFace=[], strName="", nastranContact=NASTRAN_CONTACT(), crEdit=None, iColor=65280, iMethod=3)
```
