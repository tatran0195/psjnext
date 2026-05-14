---
title: "Connections.Contacts.NXNastran.ManualGroup()"
description: "Define contact settings between specified groups for the NX solver"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "Connections > Contacts > NXNastran > ManualGroup"
---

## Description

Define contact settings between specified groups for the NX solver.

## Syntax

```psj
Connections.Contacts.NXNastran.ManualGroup(...)
```

## Inputs

<!-- @since:5.0.1 @type:Cursor @required -->
### `crFaceMaster`

- The group of faces to be the master faces.

<!-- @since:5.0.1 @type:Cursor @required -->
### `crFaceSlave`

- The group of faces to be the slave faces.

<!-- @since:5.0.1 @type:String @optional @default:"ContactNXNastran _1" -->
### `strName`

- The contact name.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactType`

- The behavior type of the contact definition. The behavior type of contact definition is one of the following.
  - 0: General contact (Sliding contact).
  - 1: Tied contact.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactAlg`

- The type of contact connection.
  - 0: Face to Face - Contact between shell or solid element faces and shell or solid element faces.

<!-- @since:5.0.1 @type:Double @optional @default:10 -->
### `dNormalPenaltyFactor`

- The penalty factor for the normal direction. This argument is available to be used if _iContactType=0_.

<!-- @since:5.0.1 @type:Double @optional @default:1 -->
### `dTangentialPenaltyFactor`

- The penalty factor for the tangential direction. This argument is available to be used if _iContactType=0_.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dForceConvergenceTol`

- The designating the Contact Force convergence tolerance. This argument is available to be used if _iContactType=0_.

<!-- @since:5.0.1 @type:Double @optional @default:10 -->
### `dMaxForceIteration`

- The designating the maximum number of iterations for a force (inner) loop. This argument is available to be used if _iContactType=0_.

<!-- @since:5.0.1 @type:Double @optional @default:20 -->
### `dMaxStatusIteration`

- The designating the maximum number of iterations for a status (outer) loop. This argument is available to be used if _iContactType=0_.

<!-- @since:5.0.1 @type:Double @optional @default:0.02 -->
### `dNumberOfChange`

- The allowable number of contact changes. This argument is available to be used if _iContactType=0_.

<!-- @since:5.0.1 @type:Double @optional @default:100 -->
### `dMinContactPercentage`

- The minimum contact set percentage. This argument is available to be used if _iContactType=0_.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iShellThickness`

- Whether to include shell thickness for plate elements. The gap between connection regions will be independent of plate element thickness if this option is turned off. This argument is available to be used if _iContactType=0_.
  - 0: Includes half shell thickness as surface offset.
  - 1: Does not include thickness offset.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactStatus`

- The flag to indicate if the contact status for a specific sub-case is to start from the final status of the previous subcase. This argument is available to be used if _iContactType=0_.
  - 0: Starts from previous subcase.
  - 1: Starts from initial state.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iInitGapOrPenetration`

- The how Nastran handles initial gap or penetration of the generated contact elements. This setting is particularly useful if some of your elements unintentionally penetrate each other and you do not wish to modify or rebuild your model. This argument is available to be used if _iContactType=0_.
  - 0: Uses the value calculated from the grid coordinates.
  - 1: Sets the penetration to zero for all contact elements.
  - 2: Sets the both penetration and gap to zero for all contact elements.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iRegionRefine`

- Whether or not the source region is refined. This argument is available to be used if _iContactType=0_.
  - 0: Refines the source region based on target surface definition.
  - 1: Does not refine the source region based on target surface definition.

<!-- @since:5.0.1 @type:Integer @optional @default:1 -->
### `iEvaluateOrder`

- The number of “Linear Contact Points” for a single element on the source region.
  - 0: Lowest order of points on source region.
  - 1: Medium order of points on source region.
  - 2: Highest order of points on source region.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dMinSearchDist`

- The minimum distance for searching the contact elements. This argument is available to be used if _iContactType=0_.

<!-- @since:5.0.1 @type:Double @optional @default:0.01 -->
### `dMaxSearchDist`

- The maximum distance for searching the contact elements. This argument is available to be used if _iContactType=0_.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dFrictionCoef`

- The static coefficient of friction for the contact pair. This argument is available to be used if _iContactType=0_.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dSearchDist`

- The search range. This argument is available to be used if _iContactType=1_.

<!-- @since:5.0.1 @type:Double @optional @default:0 -->
### `dPenaltyFactor`

- The penalty proportional coefficient. This argument is available to be used if _iContactType=1_.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iShellZOffset`

- Whether the Z-Offset on shell elements should be included in the contact analysis.
  - 0: Z offset of shells is included as surface offset.
  - 1: Z offset of shells is NOT included as surface offset.

<!-- @since:5.0.1 @type:Integer @optional @default:0 -->
### `iContactColor`

- The contact-to-display marker color.

<!-- @since:5.0.1 @type:Cursor @optional @default:None -->
### `crContactNXNastran`

- An existing contact setting (NX Nastran). If this parameter is used, the specified contact setting (NX Nastran) will be modified. When the default value is used, a new contact setting (NX Nastran) will be created.

## Return Code

A _Cursor_ specifying the created contact.

## Sample Code

```psj {11,12,13,14,15,16}
Geometry.Part.Cube(iPartColor=12537679)
Geometry.Part.Cube(dlOrigin=[0.01, 0.0, 0.0], 
                   strName="Cube _2", 
                   iPartColor=6250449)

Tools.Group.CreateGroup(strGroupName="ContactAbaqus _1_Manual _Face _M", 
                        crlTargets=[Face(49)])
Tools.Group.CreateGroup(strGroupName="ContactAbaqus _1_Manual _Face _S", 
                        crlTargets=[Face(24)])

created _contact = Connections.Contacts.NXNastran.ManualGroup(crFaceMaster=Group(1), 
                                                             crFaceSlave=Group(2), 
                                                             dSearchDist=10.0, 
                                                             dPenatlyFactor=1.0, 
                                                             iColor=16711680, 
                                                             iMethod=1)

JPT.Debugger(created _contact)
```
