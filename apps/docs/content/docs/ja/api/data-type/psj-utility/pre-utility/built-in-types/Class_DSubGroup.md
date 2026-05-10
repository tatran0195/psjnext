---
title: DSubGroup
id: DSubGroup
---

## Description

This is an instance of a DSubGroup class, represents a sub group inside Jupiter.

## Properties

| Attribute | Description                                                                                                                                                             |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| name      | Name of Sub Group.                                                                                                                                                      |     |
| typeID    | Type ID of the Sub Group (ID = 78).<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                                |
| id        | External ID of the Sub Group.<br />ID can be duplicated, but not recommended.<br />ID can be changed using the renumbering function.<br />The return value is ID (int). |
| parent    | Parent Group. <br />The return value is a [`DItem`](./DItem).                                                                                                           |
| children  | Child groups and Sub Groups that the Sub Group has.<br />The return value is a list of[`DItemVector`](./DItemVector).                                                   |
