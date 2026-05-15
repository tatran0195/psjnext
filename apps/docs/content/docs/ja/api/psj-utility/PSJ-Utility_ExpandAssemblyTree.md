---
title: "JPT.ExpandAssemblyTree()"
description: "Expand all the items existing on the Assembly window"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Expand all the items existing on the Assembly window.

> This utility is used to expand all the items existing on the Assembly window after using _[JPT.CollapseAssemblyTree()](JPT.CollapseAssemblyTree)_ utility.

## Syntax

```psj
JPT.ExpandAssemblyTree()
```

## Inputs

This utility function does not require any input value.

## Return Code

This utility function does not have output value.

## Sample Code

```psj {33}
# Preparing tree
Geometry.Part.Cube()
Geometry.Part.Cube(strName="Cube _2", iPartColor=6409934)
Geometry.Part.Cube(strName="Cube _3", iPartColor=13259210)
Geometry.Part.Cube(strName="Cube _4", iPartColor=7697908)
Geometry.Part.Cube(strName="Cube _5", iPartColor=7463537)
Geometry.Part.Cube(strName="Cube _6", iPartColor=7434735)
Geometry.Part.Cube(strName="Cube _7", iPartColor=14903267)
Geometry.Part.Cube(strName="Cube _8", iPartColor=15658599)
Geometry.Part.Cube(strName="Cube _9", iPartColor=7961077)
Geometry.Part.Cube(strName="Cube _10", iPartColor=7829501)
Geometry.Part.Cube(strName="Cube _11", iPartColor=11842649)
Geometry.Part.Cube(strName="Cube _12", iPartColor=14968422)
Geometry.Part.Cube(strName="Cube _13", iPartColor=6250447)
Geometry.Part.Cube(strName="Cube _14", iPartColor=12734402)
Assembly.RightClick.AddSubAssembly()
Assembly.RightClick.AddSubAssembly()
Assembly.RightClick.AddSubAssembly(crInst=Inst(1))
Assembly.RightClick.AddSubAssembly(crInst=Inst(2))
Assembly.RightClick.AddSubAssembly(crInst=Inst(4))
Assembly.RightClick.AddSubAssembly(crInst=Inst(5))
Assembly.RightClick.AddSubAssembly(crInst=Inst(3))
Assembly.RightClick.AddSubAssembly(crInst=Inst(6))
Assembly.RightClick.AddSubAssembly(crInst=Inst(7))
Assembly.RightClick.AddSubAssembly(crInst=Inst(7))
Assembly.RightClick.AddSubAssembly(crInst=Inst(7))
Connections.MPC.General.NodesToNodes(crlMasterNodes=[Node(6425)], crlSlaveNodes=[Node(6776)], listMpcConnection=[MPC _CONNECTION(iDof=1), MPC _CONNECTION(iDof=2), MPC _CONNECTION(iDof=4), MPC _CONNECTION(), MPC _CONNECTION(), MPC _CONNECTION()], bUpdateDispCS=1)
Connections.MPC.General.NodesToNodes(strName="MPC _2", crlMasterNodes=[Node(6776)], crlSlaveNodes=[Node(6775)], listMpcConnection=[MPC _CONNECTION(iDof=1), MPC _CONNECTION(iDof=2), MPC _CONNECTION(iDof=4), MPC _CONNECTION(), MPC _CONNECTION(), MPC _CONNECTION()], bUpdateDispCS=1)
Connections.MPC.General.NodesToNodes(strName="MPC _3", crlMasterNodes=[Node(6775)], crlSlaveNodes=[Node(6774)], listMpcConnection=[MPC _CONNECTION(iDof=1), MPC _CONNECTION(iDof=2), MPC _CONNECTION(iDof=4), MPC _CONNECTION(), MPC _CONNECTION(), MPC _CONNECTION()], bUpdateDispCS=1)
Connections.MPC.General.NodesToNodes(strName="MPC _4", crlMasterNodes=[Node(6774)], crlSlaveNodes=[Node(6773)], listMpcConnection=[MPC _CONNECTION(iDof=1), MPC _CONNECTION(iDof=2), MPC _CONNECTION(iDof=4), MPC _CONNECTION(), MPC _CONNECTION(), MPC _CONNECTION()], bUpdateDispCS=1)

# Expand all the items existing on the Assembly window
JPT.ExpandAssemblyTree()

# Collapse all the collapsed items existing on the Assembly window
JPT.CollapseAssemblyTree()
```
