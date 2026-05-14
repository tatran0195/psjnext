---
title: "Connections.Contacts.ADVC.ContactClearance()"
description: "contact clearance for ADVC contact"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > ADVC > ContactClearance"
macro _link: "[ContactClearance](../../macro/connections/ContactClearance)"
---

## Description

Contact clearance for ADVC contact

## Syntax

```psj
Connections.Contacts.ADVC.ContactClearance(strName, dClearanceVal, iLocalUnit, iSolverType, crlTargets, crEdit=None)
```

## Inputs

<!-- @since:5.0.1 @type:String @required -->
### `strName`

- The name.

<!-- @since:5.0.1 @type:Double @required -->
### `dClearanceVal`

- The clearance value.

<!-- @since:5.0.1 @type:Integer @required -->
### `iLocalUnit`

- The local unit.

<!-- @since:5.0.1 @type:Integer @required -->
### `iSolverType`

- The solver type.

<!-- @since:5.0.1 @type:List[Cursor] @required -->
### `crlTargets`

- The target.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crEdit`

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.ADVC.ContactClearance(strName, dClearanceVal, iLocalUnit, iSolverType, crlTargets, crEdit=None)
```
