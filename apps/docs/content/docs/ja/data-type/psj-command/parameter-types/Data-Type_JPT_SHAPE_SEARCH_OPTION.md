---
title: SHAPE_SEARCH_OPTION
id: SHAPE_SEARCH_OPTION
---

## Description

A data type uses to control parameters of shape search.

## Attributes

### `iType`

- An _Integer_ specifying search target.
    - 0: Arc
    - 1: Circle/Concentric
    - 2: Loop
    - 3: Planar
    - 4: Cone
    - 5: Disc
    - 6: Hollow Disc
    - 7: Full
    - 8: Full Cylinder by One Face
    - 9: Closed Partial Cylinder
    - 10: Opened Partial Cylinder
    - 11: Fillet (Rad)
    - 12: Fillet (Arc Len.)
    - 13: Tiny Face

### `bAll`

- A _Boolean_ specifying search without diameter restriction.
- The default value is _False_.

### `dMin`

- A _Double_ specifying minimum diameter.
- The default value is 0[m].

### `dMax`

- A _Double_ specifying maximum diameter.
- The default value is 0.005 [m].
