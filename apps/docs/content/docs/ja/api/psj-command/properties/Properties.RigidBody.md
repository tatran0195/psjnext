---
title: "Properties.RigidBody()"
description: "Assign properties to Rigid Body"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Properties > Rigid Body"
---

## Description

Assign a rigid property to a body.

## Syntax

```psj
Properties.RigidBody(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### strName

- Specify name of the new property.
- The default value is "RigidBody1".

<!-- @since:5.0.1 @optional -->
### iPID

- Specify the property identification number.
  This number must be unique with respect to all other property's identification numbers.
- The default value is 1.

<!-- @since:5.0.1 @optional -->
### iRefNodeId

- Specify the reference node ID.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### crlTargets

- Specify the entities to be applied the rigid body property.
  The target can be Face entities or Element entities.
- The _crlTargets_ and _crRigidBodyProperty_ arguments are mutually exclusive (one of them must be specified).
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### crRigidBodyProperty

- Specify the existing Rigid Body Property.
  - If this argument is not _None_, the specified Rigid Body Property will be modified.
  - Otherwise, a new Rigid Body Property will be created.
- The _crlTargets_ and _crRigidBodyProperty_ arguments are mutually exclusive (one of them must be specified).
- The default value is _None_.

## Return Code

A _Cursor_ specifying the newly created or the modified Rigid Body Property.

## Sample Code

```psj {2}
Geometry.Part.Cube()
Properties.RigidBody(crlTargets=[Face(26)])
```
