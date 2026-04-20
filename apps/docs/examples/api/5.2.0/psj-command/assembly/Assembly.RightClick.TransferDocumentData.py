# Title:   Assembly.RightClick.TransferDocumentData()
# Desc:    Transfer data information of entity between documents
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assembly/Assembly.RightClick.TransferDocumentData
# ---
# Create a Cube in 1st document.
doc1=JPT.GetActiveDocument()
Geometry.Part.Cube()

#2nd doc is created
doc2=JPT.CreateNewDocument()

# Copy/Transfer Cube into document 2: 
result = Assembly.RightClick.TransferDocumentData(  # [hl:start]
    strSourceDocTitle=doc1.docName, 
    strDestDocTitle=doc2.docName,
    crlParts=[Part(1)], 
    strlNewPartName=[])  # [hl:end]

# Check cube in both 1st and 2nd document.
Home.Windows.TileVertical(iMode=1)
Home.Synchronize()
JPT.ViewFitToModel()
