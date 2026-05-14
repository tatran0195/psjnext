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

<!-- @since:5.0.1 @type:String @optional @default:"RigidBody1" -->
### `strName`

- The name of the new property.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iPID`

- The property identification number.
  This number must be unique with respect to all other property's identification numbers.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iRefNodeId`

- The reference node ID.

<!-- @since:5.0.1 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The entities to be applied the rigid body property.
  The target can be Face entities or Element entities.
- The _crlTargets_ and _crRigidBodyProperty_ arguments are mutually exclusive (one of them must be specified).

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crRigidBodyProperty`

- The existing Rigid Body Property.
  - If this argument is not _None_, the specified Rigid Body Property will be modified.
  - Otherwise, a new Rigid Body Property will be created.
- The _crlTargets_ and _crRigidBodyProperty_ arguments are mutually exclusive (one of them must be specified).

## Return Code

A _Cursor_ specifying the newly created or the modified Rigid Body Property.

## Sample Code

```psj {2}
Geometry.Part.Cube()
Properties.RigidBody(crlTargets=[Face(26)])
```
