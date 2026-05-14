---
title: "Connections.Contacts.MSCNastran.ContactTable()"
description: "create contacts of MSC Nastran Contact Table"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > MSCNastran > ContactTable"
---

## Description

Create contacts of MSC Nastran Contact Table

## Syntax

```psj
Connections.Contacts.MSCNastran.ContactTable(strName="", nastranContact=NASTRAN _CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:NASTRAN _CONTACT @optional @default:NASTRAN _CONTACT() -->
### `nastranContact`

- The contact.

<!-- @since:5.0.1 @type:Cursor Pair List @optional @default:[] -->
### `crplTarget`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Integer @optional @default:65280 -->
### `iColor`

- The color.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iMethod`

- The method.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.MSCNastran.ContactTable(strName="", nastranContact=NASTRAN _CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
```
