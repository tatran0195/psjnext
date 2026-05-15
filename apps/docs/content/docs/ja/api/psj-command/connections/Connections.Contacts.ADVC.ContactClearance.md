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

<!-- @since:5.0.1 @required -->
### strName

- Specify the name.

<!-- @since:5.0.1 @required -->
### dClearanceVal

- Specify the clearance value.

<!-- @since:5.0.1 @required -->
### iLocalUnit

- Specify the local unit.

<!-- @since:5.0.1 @required -->
### iSolverType

- Specify the solver type.

<!-- @since:5.0.1 @required -->
### crlTargets

- Specify the target.

<!-- @since:5.0.1 @optional -->
### crEdit

- Specify the edit.
- The default value is None.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
Connections.Contacts.ADVC.ContactClearance(strName, dClearanceVal, iLocalUnit, iSolverType, crlTargets, crEdit=None)
```
