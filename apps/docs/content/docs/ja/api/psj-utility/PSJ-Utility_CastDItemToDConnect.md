---
title: "JPT.CastDItemToDConnect()"
description: "Convert DItem object to DConnect object to get the information of the selected coordinate system"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Convert _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object to _[DConnect](../data-type/psj-utility/pre-utility/built-in-types/DConnect)_ object to get the information of the selected coordinate system.

## Syntax

```psj
JPT.CastDItemToDConnect(DItemObject)
```

## Inputs

### `DItemObject`

- A _[DItem](../data-type/psj-utility/pre-utility/built-in-types/DItem)_ object which will be used to convert.

## Return Code

A _[DConnect](../data-type/psj-utility/pre-utility/built-in-types/DConnect)_ object (Connection with relating information).

## Sample Code

```psj {24}
# Prepare model
Geometry.Part.Cube(iPartColor=13290083)
Geometry.Part.Cube(dlOrigin=[0.012, 0.0, 0.0], strName="Cube _2", iPartColor=6149981)
Geometry.Part.Cube(dlOrigin=[0.024, 0.0, 0.0], strName="Cube _3", iPartColor=7664244)
Geometry.Part.Cube(dlOrigin=[0.036, 0.0, 0.0], strName="Cube _4", iPartColor=13588687)
Geometry.Part.Cube(dlOrigin=[0.036, 0.012, 0.0], strName="Cube _5", iPartColor=14048091)
Geometry.Part.Cube(dlOrigin=[0.024, 0.012, 0.0], strName="Cube _6", iPartColor=7138156)
Geometry.Part.Cube(dlOrigin=[0.012, 0.012, 0.0], strName="Cube _7", iPartColor=5489235)
Geometry.Part.Cube(dlOrigin=[0.0, 0.012, 0.0], strName="Cube _8", iPartColor=7632109)
Connections.MPC.General.NodesToNodes(crlMasterNodes=[Node(1932)], crlSlaveNodes=[Node(1429)], listMpcConnection=[MPC _CONNECTION(iDof=1), MPC _CONNECTION(iDof=2), MPC _CONNECTION(iDof=4), MPC _CONNECTION(), MPC _CONNECTION(), MPC _CONNECTION()], bUpdateDispCS=1)
Connections.RigidElements.RBE2.OneToOne(crlMasterTargets=[Node(940)], crlSlaveTargets=[Node(3363)])
Connections.RigidElements.RBE3.OneToMany(crlMasterTargets=[Node(459, 3889, 3859)], crlSlaveTargets=[Node(3879)], listRbe3TermConnection=[(0, 63, 1), (1, 7, 3)], strName="RBE3 _1")
Connections.SpringsDampers.Spring.OneToOne.sameDoFs(iMethod=17, strName="Spring _2", crlMasterTargets=[Node(2396)], crlSlaveTargets=[Node(2428)], iSpringType=2, posTStiffness=[1.7976931e+308, 1.7976931e+308, 1.7976931e+308], posRStiffness=[1.7976931e+308, 1.7976931e+308, 1.7976931e+308])
Connections.SpringsDampers.Bush.TwoNodes(crlMaster=[Node(2884)], crlSlave=[Node(2900)], iOriMode=1, dlVector=[0, 0, 0], dlStiffness=[DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL], dlDampCoef=[DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL], dlDampConst=[DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL, DFLT _DBL])
Connections.SpringsDampers.Damper.AnyEntities11DoFS(iMethod=17, strName="Damper _1", crlMasterTargets=[Node(3382)], crlSlaveTargets=[Node(3398)])
JPT.ViewFitToModel()

# Get RBE2 Connection object as DItem object from the created list of DItem objects
listDItemConnections = JPT.GetAllByTypeID(JPT.DItemType.CONNECT _RBE2)
dItemConnection = listDItemConnections[0]
JPT.Debugger(dItemConnection)

# Convert from the above DItem object to DConnect object
dConnection = JPT.CastDItemToDConnect(dItemConnection)
JPT.Debugger(dConnection)
```
