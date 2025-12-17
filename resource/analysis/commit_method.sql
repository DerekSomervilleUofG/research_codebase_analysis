select cf.commit_id, cf.name, cf.amendment_type, cf.lines_added,
       cc.name, cc.amendment_type,
       cm.name, cm.amendment_type, cm.lines_added, cm.lines_changed, cm.lines_similar, cm.lines_removed
from commit_file cf
left outer join commit_class cc on
    cc.commit_id = cf.commit_id and
    cc.file_id = cf.file_id
left outer join commit_method cm on
        cm.commit_id = cc.commit_id and
        cm.class_id == cc.class_id
