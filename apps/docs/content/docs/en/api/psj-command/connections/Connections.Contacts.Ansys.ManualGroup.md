---
title: "Connections.Contacts.Ansys.ManualGroup()"
description: "create contact ansys Manual Group"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > Ansys > ManualGroup"
---

## Description

Create contact ansys Manual Group

## Syntax

```psj
Connections.Contacts.Ansys.ManualGroup(strName="ContactAnsys _1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS _CONTACT(), crplTarget=[], crEdit=None, iColor=16711680)
```

## Inputs

<!-- @since:5.0.1 @type:String @optional @default:"ContactAnsys _1" -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iMethod`

- The method.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iType`

- The type.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactAlgorithm`

- The contact algorithm.

<!-- @since:5.0.1 @type:ANSYS _CONTACT @optional @default:ANSYS _CONTACT() -->
### `ansysContact`

- The contact.

<!-- @since:5.0.1 @type:Cursor Pair List @optional @default:[] -->
### `crplTarget`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

<!-- @since:5.0.1 @type:Integer @optional @default:16711680 -->
### `iColor`

- The color.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.Ansys.ManualGroup(strName="ContactAnsys _1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS _CONTACT(), crplTarget=[], crEdit=None, iColor=16711680)
```
