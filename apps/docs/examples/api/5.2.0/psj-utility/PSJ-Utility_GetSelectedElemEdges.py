# Title:   JPT.GetSelectedElemEdges()
# Desc:    Get all information of the selected edges
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetSelectedElemEdges
# ---
# Get the information of the selected element edges.
# This function returns a list of DItemPair objects or DItemPairVetor object storing
# information of element edges in DItem format
# Element edges are not actual entity but defined by connection of 2 nodes.

listSelElemEdges = JPT.GetSelectedElemEdges()  # [hl]
for i in listSelElemEdges:
    print ('1st Node: {}'.format(i.firstDItem.id))
    print ('2nd Node: {}'.format(i.secondDItem.id))
