---
title: DCoord
id: DCoord
---

## Description

This is an instance of a DCoord class, represents Coordinate item inside Jupiter.

## Properties

| Attribute   | Description                                                                                                                                                           |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| isValid     | Determine the validation of the Coordinate.<br /> The return value is `True` if the Coordinate is valid, `False` if not (invalid).                                    |
| type        | Type name of the Coordinate.<br />The return value is Type (string).                                                                                                  |
| typeID      | Type ID of the Coordinate (ID = 27).<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                             |
| tableID     | Table ID of the Coordinate.<br />The return value is an [`Int notation of DTable Types`](../enumeration-types/dtable-types) (int).                                    |
| id          | External ID of the Coordinate.<br/>It can be duplicated, but not recommended.<br/>ID can be changed using the renumbering function.<br/>The return value is ID (int). |
| targets     | Hold the contents of the Coordinate.<br />The return value is a list of [`DItem`](DItem).                                                                             |
| masters     | Master face/edge/node of the Coordinate.<br />The return value is a list of [`DItem`](DItem).                                                                         |
| slaves      | Slave face/edge/node of the Coordinate.<br />The return value is a list of [`DItem`](DItem).                                                                          |
| parent      | A sub-assembly that is the parent of Coordinate in the assembly tree.<br />The return value is a list of [`DItem`](DItem).                                            |
| isHidden    | Determine display state of the Coordinate.<br />The return value is `True` if the Coordinate is hidden, `False` if the Coordinate is displayed.                       |
| name        | Name of the Coordinate.                                                                                                                                               |
| coordType   | Type of the Coordinate.<br />The return value is [`Type`](#coordtype) (string).                                                                                       |
| coordPoints | A list of defined Points for Coordinate.<br />The return value is [`TVector3d`](TVector3d).                                                                           |

## Attribute

### coordType

| Name              | Description                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| COORDINATE_RECT   | Cartesian Coordinate System (Oxyz).                                                                                                                    |
| COORDINATE_CYLIN  | Cylindrical Coordinate - (r, φ, z) Coordinate System, where (r, φ, z) are (radial distance, azimuth angle, axial Coordinate or height z) respectively. |
| COORDINATE_SPHERE | Spherical Coordinate - (r, θ, φ) Coordinate System, where (r, θ, φ) are (radial distance, azimuth angle, polar angle) respectively.                    |
