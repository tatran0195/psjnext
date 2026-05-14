---
title: "Exchange.ClayWork()"
description: "Make a simple design change for solid mesh parts"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Exchange > ClayWork"
macro _link: ""
---

## Description

Make a simple design change for solid mesh parts.

## Syntax

```psj
Exchange.ClayWork(...)
```

## Inputs

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iProcess`

- The process type.
  - 0: Sphere
  - 1: Boolean +
  - 2: Boonlean -

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iWrappingType`

- The wrapping type. This argument only was used when`iProcess` = 1 or 2.
  - 0: Tight
  - 1: Convex

<!-- @since:5.1.0 @type:List[Double] @optional @default:[] -->
### `dlSphereCenter`

- The center coordinates of sphere.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dSphereRadius`

- The radius of sphere.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crTargetPart`

- The part to which the wrapped sphere will be added or scraped off. This argument only was used when`iProcess` = 1 or 2.

## Return Code

A _Boolean_ specifying the function successfully executed or not.

## Sample Code

```psj {15-21,25}
# Prepare model
Geometry.Part.Cube(iPartColor=6409934)
Meshing.SolidMeshing(
	crlParts=[Part(1)], 
	dGradingFactor=1.05, 
	dStretchLimit=0.1, 
	iSpeedVsQual=1, 
	iRegion=1, 
	bSafeMode=False, 
	iParallel=16, 
	bInternalMeshOnly=False, 
	iPartColor=65280)

# Add spheres
ret1 = Exchange.ClayWork(
		iProcesstype=0, 
		dlSphereCenter=[
			[0.006, 0.01, 0.002], [0.006, 0.01, 0.003], [0.006, 0.01, 0.004], [0.006, 0.01, 0.006], 
			[0.006, 0.01, 0.007], [0.004, 0.01, 0.007], [0.004, 0.01, 0.006], [0.004, 0.01, 0.004], 
			[0.004, 0.01, 0.003], [0.004, 0.01, 0.002]], 
		dSphereRadius=0.002)
print(ret1)

# Pile up the wrapped sphere
ret2 = Exchange.ClayWork(iProcesstype=1, iWrappingType=1, iFactor = 0.6, crTargetPart=Part(1))
print(ret2)
```
