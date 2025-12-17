select rep.repository_id, rep.name, count(*)
from repository rep, developer_commit dc
where rep.repository_id = dc.repository_id
group by dc.repository_id

select rep.repository_id, rep.name, count(*)
from repository rep, developer_commit dc, developer_new dn
where rep.repository_id = dc.repository_id
and dn.developer_id = dc.developer_id
and rep.repository_id = dn.repository_id
group by dc.repository_id

select rep.repository_id, rep.name, dev.developer_id, dev.name, count(*)
from repository rep, developer_commit dc, developer_new dn, developer dev
where rep.repository_id = dc.repository_id
and dn.developer_id = dc.developer_id
and dev.developer_id = dc.developer_id
and rep.repository_id = dn.repository_id
group by dc.repository_id, dc.developer_id
having count(*) >= 5
order by count(*) desc

select amend_commit.commit_id, amend_commit.repository_id, amend_commit.developer_id, 
amend_commit.number_of_amend_files, amend_commit.number_of_amend_classes, amend_commit.number_of_amend_methods, 
prior_commit.number_of_known_files, prior_commit.number_of_known_classes, prior_commit.number_of_known_methods 
from prior_commit, amend_commit, developer_new
where prior_commit.commit_id = amend_commit.commit_id
and developer_new.repository_id = prior_commit.repository_id
and developer_new.developer_id = prior_commit.developer_id

