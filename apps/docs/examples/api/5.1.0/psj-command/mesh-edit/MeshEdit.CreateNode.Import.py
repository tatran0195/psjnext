# Title:   MeshEdit.CreateNode.Import()
# Desc:    Create node by importing CSV file
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/mesh-edit/MeshEdit.CreateNode.Import
# ---
# Put your sample CSV file
csvFile = "C:/temp/NodeData.csv"

# Import nodes
newNode = MeshEdit.CreateNode.Import(strFilePath = csvFile)  # [hl]
JPT.Debugger(newNode) # for checking the return value
