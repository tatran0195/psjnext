---
title: DBody
id: DBody
---

## Description

This is an instance of a DBody class, represents a Part inside Jupiter.

## Properties

| Attribute             | Description                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| name                  | Name of the Part.                                                                                                                                                  |
| typeID                | Type ID of the Part (ID = 3).<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                                 |
| id                    | External ID of the Part.<br />ID can be duplicated, but not recommended.<br />ID can be changed using the renumbering function.<br />The return value is ID (int). |
| faces                 | The faces belong to the Part.<br />The return value is a list of faces.                                                                                            |
| edges                 | The edges belong to the Part.<br />The return value is a list of edges.                                                                                            |
| nodes                 | The nodes belong to the Part.<br />The return value is a list of nodes.                                                                                            |
| elems                 | The elements belong to the Part.<br />The return value is a list of elements.                                                                                      |
| vertex                | The vertex belong to the Part.<br />The return value is a list of vertex.                                                                                          |
| connections           | The connections attached to the Part.<br />The return value is a list of connections.                                                                              |
| contacts              | The contacts attached to the Part.<br />The return value is a list of contacts.                                                                                    |
| materials             | The materials assigned to the Part.<br />The return value is a list of materials.                                                                                  |
| properties            | The properties assigned to the Part. <br />The return value is a list of properties.                                                                               |
| loadAndBCs            | The loads and boundary conditions attached to the Part.<br />The return value is a list of loads and boundary conditions.                                          |
| localMeshSettings     | The local mesh settings assigned to the Part.<br />The return value is a list of local mesh settings.                                                              |
| area                  | The total area of all faces belong the Part.<br />The return value is Area (float).                                                                                |
| volume                | The volume of the Part.<br />The return value is Volume (float).                                                                                                   |
| mass                  | The mass of the Part.<br />The return value is Mass (float).                                                                                                       |
| gravityCenter         | The gravity center of the Part.<br />The return value is GravityCenter (list of float).                                                                            |
| momentInertia         | The moment of inertia of the Part.<br />The return value is MomentInertia (list of float).                                                                         |
| color\* [^(1)]        | Body face color information.<br />This value can be adjusted.<br />The return value is a RGB color.                                                                |
| colorMesh\* [^(1)]    | Mesh of body color information.<br />This value can be adjusted.<br />The return value is a RGB color.                                                             |
| transparency\* [^(1)] | The transparency of the Part.<br />This value can be adjusted.<br />The return value is a transparency level (from 0 - 100).                                       |

### Notice

[^(1)]: An asterisk symbol \* in attribute name means that attribute can be changed/assigned from the current to the new value.
