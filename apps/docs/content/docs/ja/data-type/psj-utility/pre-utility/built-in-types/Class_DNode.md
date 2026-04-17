---
title: DNode
id: DNode
---

## Description

This is an instance of a DNode class, represents a Node inside Jupiter.

## Properties

| Attribute  | Description                                                                                                                                                        |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| isFloating | Determine if the Node is a floating Node or not.<br /> The return value is `True` if it is a floating Node, `False` if not.                                        |
| typeID     | Type ID of the Node (ID = 10).<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                                |
| id         | External ID of the Node.<br />ID can be duplicated, but not recommended.<br />ID can be changed using the renumbering function.<br />The return value is ID (int). |
| pos        | Position coordinate of the Node.<br />The return value is [`TVector3d`](TVector3d).                                                                                |
| coordinate | Coordinate assigned to the Node.<br />The return value is [`DCoord`](DCoord).                                                                                      |
