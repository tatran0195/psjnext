---
title: "Properties.RigidBody()"
description: "Assign properties to Rigid Body"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Properties > Rigid Body"
---

## Description

Assign a rigid property to a body.

## Syntax

```psj
Properties.RigidBody(...)
```

## Inputs

### `strName` @type(String) @default("RigidBody1")

- Name of the new property.

### `iPID` @type(Integer) @default(1)

- The property identification number.
  This number must be unique with respect to all other property's identification numbers.

### `iRefNodeId` @type(Integer) @default(0)

- The reference node ID.

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The entities to be applied the rigid body property.
  The target can be Face entities or Element entities.
- Th&#x65;_&#x63;rlTarget&#x73;_&#x61;n&#x64;_&#x63;rRigidBodyPropert&#x79;_&#x61;rguments are mutually exclusive (one of them must be specified).

### `crRigidBodyProperty` @type(Cursor) @default(None)

- The existing Rigid Body Property.
  - If this argument is no&#x74;_&#x4E;one_, the specified Rigid Body Property will be modified.
  - Otherwise, a new Rigid Body Property will be created.
- Th&#x65;_&#x63;rlTarget&#x73;_&#x61;n&#x64;_&#x63;rRigidBodyPropert&#x79;_&#x61;rguments are mutually exclusive (one of them must be specified).

## Return Code

A _Cursor_ specifying the newly created or the modified Rigid Body Property.

## Sample Code

```psj {2}
Geometry.Part.Cube()
Properties.RigidBody(crlTargets=[Face(26)])
```
