select
  a.itemid,
  a.triggerid,
  b.name as metric,
  c.host as hostname,
  d.appid as appid
from (select distinct itemid, triggerid from function) a
left join items b
on a.itemid = b.itemid
left join hosts c
on b.hostid = c.hostid
left join (
  select
    a.itemid,
    b.name as appid
  from items_applications a
  left join applications b
  on a.applicationid = b.applicationid) d
on a.itemid = d.itemid
where a.host like "10.%"
