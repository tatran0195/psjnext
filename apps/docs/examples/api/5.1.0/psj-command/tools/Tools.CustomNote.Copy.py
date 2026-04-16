# Title:   Tools.CustomNote.Copy()
# Desc:    Copy custom notes.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.CustomNote.Copy
# ---
# Create a custom note and collection in document 1.
doc1=JPT.GetActiveDocument()
original_cnote=Tools.CustomNote.Create(
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    strParentName="Collection_1", 
    listContent=["Original Note"], 
    iAlignment=1)

# Prepare a new document.
doc2=JPT.CreateNewDocument()

# Create a custom note and collection in a new document (document 2).
Tools.CustomNote.Create(
    strNoteName="CustomNote_1", 
    dlNotePosition=[0.0, 0.0, 0.0], 
    strParentName="Collection_1", 
    listContent=["Note in new doc"], 
    iAlignment=1)

cnotes_collections=JPT.GetAllByTypeID(JPT.DItemType.CUSTOM_NOTE_COLLECTION)

# Copy custom note in document 1 to document 2.

if cnotes_collections:
    Tools.CustomNote.Copy(  # [hl:start]
        strSrcDocumentName=doc1.docName, 
        strDestDocumentName=doc2.docName, 
        crlTargets=[original_cnote], 
        strlNames=["CustomNote_1(Copied)"], 
        crCollection=CustomNoteCollection(cnotes_collections[0].id))  # [hl:end]

JPT.Exec('ViewSpreadNote()')
