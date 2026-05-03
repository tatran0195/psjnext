---
title: "Connections.Contacts.ADVC.ContactClearance()"
description: "contact clearance for ADVC contact"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > ADVC > ContactClearance"
macro_link: "[ContactClearance](../../macro/connections/ContactClearance)"
---

## Description

Contact clearance for ADVC contact

## Syntax

```psj
Connections.Contacts.ADVC.ContactClearance(strName, dClearanceVal, iLocalUnit, iSolverType, crlTargets, crEdit=None)
```

## Inputs

### `strName` @type(String) @required

- The name.

### `dClearanceVal` @type(Double) @required

- The clearance value.

### `iLocalUnit` @type(Integer) @required

- The local unit.

### `iSolverType` @type(Integer) @required

- The solver type.

### `crlTargets` @type(List\[Cursor]) @required

- The target.

### `crEdit` @type(Cursor) @default(None)

- The edit.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.ADVC.ContactClearance(strName, dClearanceVal, iLocalUnit, iSolverType, crlTargets, crEdit=None)
```
