---
title: "Connections.Contacts.MSCNastran.ContactGroupByMatrix()"
description: "create contacts of MSC Nastran Contact Group By Matrix"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > MSCNastran > ContactGroupByMatrix"
---

## Description

Create contacts of MSC Nastran Contact Group By Matrix

## Syntax

```psj
Connections.Contacts.MSCNastran.ContactGroupByMatrix(strName="", nastranContact=NASTRAN _CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
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
Connections.Contacts.MSCNastran.ContactGroupByMatrix(strName="", nastranContact=NASTRAN _CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)
```
