# ansible-elasticsearch

This is an role for install elasticsearch with binary tar ball.

## Prepare
1:Download the same version tar ball of elasticsearch and kibana,and copy it to the files directory;
2:Make sure the version is included in es_available_version of  defaults/main.yml;
you can overwrite es_available_version into the entry playbook
3:if u want to install xpack,download the xpack tar ball,then unarchive the package,and archive the single directory name like
elasticsearch-{{ es_verion }}.tar.gz,kibana-{{ es_version }}.tar.gz, and put them into file directory.
4:The following playbook is an example playbook:
```
---

- name: Elasticsearch with custom configuration
  hosts: es_cluster
  roles:
    - role: elasticsearch_install_v2
  vars:
    es_user: "hadoop"
    es_group: "hadoop"
    es_root_home: "/data01"
    es_version: "5.4.3"
    es_data_dirs:
      - "/opt/elasticsearch/data"
      - "/opt/elasticsearch/data1"
    es_log_dir: "/opt/elasticsearch/logs"
    es_config: 
      cluster.name: "custom-cluster"
      bootstrap.memory_lock: true
      bootstrap.system_call_filter: false 
      discovery.zen.ping.unicast.hosts: "10.0.0.2:9300"
      discovery.zen.minimum_master_nodes: "1"
      xpack.security.enabled: false
    es_jvm_custom_parameters:
      - "-XX:HeapDumpPath=/opt"
    es_heap_size: 1g
    es_start_service: false
    es_install_xpack: true
    kibana_config:
      server.port: 5601
      server.host: "10.0.0.2"
      elasticsearch.url: "http://10.0.0.2:9200"
      xpack.security.enabled: false
```
5: the inventry file shoud write like it:
role_id is not a nessary varible.It shoud be defined when you need install two instaces in a directory.
```
[es_cluster]
127.0.0.1 node_name=test_node1 is_master=true is_data=true http_port=9200 transport_port=9300 ansible_python_interpreter=/data01/anaconda2/bin/python install_kibana=true role_id=1
```
