import rhinoscriptsyntax as rs
import scriptcontext as sc

def two_point_copy():
    """Copy selected geometry from point 1 to point 2 (2-point copy)."""
    objs = rs.GetObjects("Select objects to copy", preselect=True)
    if not objs:
        return                       # user cancelled

    p1 = rs.GetPoint("Pick base point (point 1)")
    if not p1:
        return

    p2 = rs.GetPoint("Pick target point (point 2)")
    if not p2:
        return

    vec = rs.VectorCreate(p2, p1)    # translation vector

    rs.EnableRedraw(False)
    undo_id = sc.doc.BeginUndoRecord("Two-Point Copy")

    rs.CopyObjects(objs, vec)

    sc.doc.EndUndoRecord(undo_id)
    rs.EnableRedraw(True)

if __name__ == "__main__":
    two_point_copy()
