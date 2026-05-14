---
title: "Connections.Contacts.MSCNastran.ContactShareFace()"
description: "create contacts of MSC Nastran Contact Share Face"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > MSCNastran > ContactShareFace"
---

## Description

Create contacts of MSC Nastran Contact Share Face

## Syntax

```psj
Connections.Contacts.MSCNastran.ContactShareFace(crlShareFace=[], strName="", nastranContact=NASTRAN _CONTACT(), crEdit=None, iColor=65280, iMethod=3)
```

## Inputs

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlShareFace`

- The share face.

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:NASTRAN _CONTACT @optional @default:NASTRAN _CONTACT() -->
### `nastranContact`

- The contact.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Integer @optional @default:65280 -->
### `iColor`

- The color.

<!-- @since:5.0.1 @type:Integer @optional @default:3 -->
### `iMethod`

- The method.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.MSCNastran.ContactShareFace(crlShareFace=[], strName="", nastranContact=NASTRAN _CONTACT(), crEdit=None, iColor=65280, iMethod=3)
```
