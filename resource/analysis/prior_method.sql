select dc.commit_id, dc.author, dc.authored_date,
dc.number_of_repo_packages, dc.number_of_repo_files, dc.number_of_repo_classes, dc.number_of_repo_methods,
count(distinct(pf.package_id)), count(distinct(pf.file_id)), count(distinct(pc.class_id)), count(distinct(pm.method_id))
from developer_commit dc, prior_file pf
left outer join prior_class pc on
    pc.commit_id = pf.commit_id and
    pc.file_id = pf.file_id
left outer join prior_method pm on
        pm.commit_id = pc.commit_id and
        pm.class_id == pc.class_id
where pf.commit_id = dc.commit_id
group by dc.commit_id
order by dc.developer_id, dc.authored_date asc
