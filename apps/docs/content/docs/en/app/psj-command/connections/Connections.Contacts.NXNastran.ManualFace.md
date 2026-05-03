---
title: "Connections.Contacts.NXNastran.ManualFace()"
description: "Define contact settings between specified faces for the NX Nastran solver"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Connections > Contacts > NX Nastran > Manual Face"
---

## Description

Define contact settings between specified faces for the NX Nastran solver.

## Syntax

```psj
Connections.Contacts.NXNastran.ManualFace(...)
```

## Inputs

### `crlFaceMasters` @type(List\[Cursor]) @required

- The faces to be the master faces.

### `crlFaceSlaves` @type(List\[Cursor]) @required

- The faces to be the slave faces.

### `strName` @type(String) @default("ContactNXNastran\_1")

- The contact name.

### `iContactType` @type(Integer) @default(0)

- The behavior type of contact definition.
  - I&#x66;_&#x69;ContactType=0_, sliding contact.
  - I&#x66;_&#x69;ContactType=1_, tied contact.

### `iContactAlgorithm` @type(Integer) @default(0)

- The type of contact connection.
  - I&#x66;_&#x69;ContactAlgorithm=0_, contact between shell or solid element faces and shell or solid element faces.

### `dNormalPenaltyFactor` @type(Double) @default(10)

- The penalty factor for the normal direction. This argument is to be used i&#x66;_&#x69;ContactType=0_.

### `dTangentialPenaltyFactor` @type(Double) @default(1)

- The penalty factor for the tangential direction. This argument is to be used i&#x66;_&#x69;ContactType=0_.

### `dForceConvergenceTol` @type(Double) @default(0.01)

- Designating the Contact Force convergence tolerance. This argument is to be used i&#x66;_&#x69;ContactType=0_.

### `dMaxForceIteration` @type(Double) @default(10)

- Designating the maximum number of iterations for a force (inner) loop. This argument is to be used i&#x66;_&#x69;ContactType=0_.

### `dMaxStatusIteration` @type(Double) @default(20)

- Designating the maximum number of iterations for a status (outer) loop. This argument is to be used i&#x66;_&#x69;ContactType=0_.

### `dNumberOfChange` @type(Double) @default(0.02)

- The allowable number of contact changes. This argument is to be used i&#x66;_&#x69;ContactType=0_.

### `dMinContactPercentage` @type(Double) @default(100)

- The minimum contact set percentage. This argument is to be used i&#x66;_&#x69;ContactType=0_.

### `iShellThickness` @type(Integer) @default(0)

- Whether to include shell thickness for plate elements. The gap between connection regions will be independent of plate element thickness if this option is turned off. This argument is to be used i&#x66;_&#x69;ContactType=0_.
  - I&#x66;_&#x69;ShellThickness=0_, include half shell thickness as surface offset.
  - I&#x66;_&#x69;ShellThickness=1_, does not include thickness offset.

### `iContactStatus` @type(Integer) @default(0)

- The flag to indicate if the contact status for a specific sub-case is to start from the final status of the previous subcase. This argument is to be used i&#x66;_&#x69;ContactType=0_.
  - I&#x66;_&#x69;ContactStatus=0_, starts from previous subcase.
  - I&#x66;_&#x69;ContactStatus=1_, starts from initial state.

### `iInitGapOrPenetration` @type(Integer) @default(0)

- How Nastran handles initial gap or penetration of the generated contact elements. This setting is particularly useful if some of your elements unintentionally penetrate each other and you do not wish to modify or rebuild your model. This argument is to be used i&#x66;_&#x69;ContactType=0_.
  - I&#x66;_&#x69;InitGapOrPenetration=0_, use the value calculated from the grid coordinates.
  - I&#x66;_&#x69;InitGapOrPenetration=1_, sets the penetration to zero for all contact elements.
  - I&#x66;_&#x69;InitGapOrPenetration=2_, sets the both penetration and gap to zero for all contact elements.

### `iRegionRefine` @type(Integer) @default(0)

- Whether or not the source region is refined. This argument is to be used i&#x66;_&#x69;ContactType=0_.
  - I&#x66;_&#x69;RegionRefine=0_, refines the source region based on target surface definition.
  - I&#x66;_&#x69;RegionRefine=1_, does not refine the source region based on target surface definition.

### `iEvaluateOrder` @type(Integer) @default(1)

- The number of “Linear Contact Points” for a single element on the source region.
  - I&#x66;_&#x69;EvaluateOrder=0_, lowest order of points on source region.
  - I&#x66;_&#x69;EvaluateOrder=1_, medium order of points on source region.
  - I&#x66;_&#x69;EvaluateOrder=2_, highest order of points on source region.

### `dMinSearchDist` @type(Double) @default(0)

- The minimum distance for searching the contact elements. This argument is to be used i&#x66;_&#x69;ContactType=0_.

### `dMaxSearchDist` @type(Double) @default(0.01)

- The maximum distance for searching the contact elements. This argument is to be used i&#x66;_&#x69;ContactType=0_.

### `dFrictionCoeff` @type(Double) @default(0)

- The static coefficient of friction for the contact pair. This argument is to be used i&#x66;_&#x69;ContactType=0_.

### `dSearchDist` @type(Double) @default(0)

- The search range. This argument is to be used i&#x66;_&#x69;ContactType=1_.

### `dPenaltyFactor` @type(Double) @default(0)

- The penalty proportional coefficient. This argument is to be used i&#x66;_&#x69;ContactType=1_.

### `iShellZOffset` @type(Integer) @default(0)

- Whether the Z-Offset on shell elements should be included in the contact analysis.
  - I&#x66;_&#x69;ShellZOffset=0_, Z offset of shells is included as surface offset.
  - I&#x66;_&#x69;ShellZOffset=1_, Z offset of shells is NOT included as surface offset.

### `iContactColor` @type(Integer) @default(0)

- The contact-to-display marker color.

### `crContactNXNastran` @type(Cursor) @default(None)

- An existing contact setting (NX Nastran). If this parameter is used, the specified contact setting (NX Nastran) will be modified. Whe the default value is used, a new contact setting (NX Nastran) will be created.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {7,8,9,10,11}
Geometry.Part.Cube(iPartColor=4962231)

Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0],
                   strName="Cube_2", 
                   iPartColor=4803000)

creating_status = Connections.Contacts.NXNastran.ManualFace(crlFaceMasters=[Face(24)], 
                                                            crlFaceSlaves=[Face(49)],
                                                            dSearchDist=10.0, 
                                                            dPenaltyFactor=1.0, 
                                                            iContactColor=16711680)

JPT.Debugger(creating_status)
```
