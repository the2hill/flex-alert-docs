<a name="top"></a>
<p style="font-size: 28px; font-weight: bold;">Prometheus Alert Documentation</p>

## Blackbox Alerts<br>
<summary><strong>Blackbox Alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **Service Down** | "Service probe has failed for more than two minutes on (instance {{ $labels.instance }})" | "Service probe has failed for more than two minutes.<br>LABELS = {{ $labels }}<br>" |
| **TLS certificate expiring** | "SSL certificate will expire soon on (instance {{ $labels.instance }})" | "SSL certificate expires within 30 days.<br>VALUE = {{ $value }}<br>LABELS = {{ $labels }}<br>" |
| **TLS certificate expiring** | "SSL certificate will expire soon on (instance {{ $labels.instance }})" | "SSL certificate expires within 15 days.<br>VALUE = {{ $value }}<br>LABELS = {{ $labels }}<br>" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## Cinder NetApp cluster alerts<br>
<summary><strong>Cinder NetApp cluster alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **CinderNetAppClusterPoolFreeSpaceWarning** | "Cinder NetApp (cinder02) free pool capacity has dropped below 30% of total" | "Cinder NetApp volume cinder02: {{ $labels.name }}<br>Free Space: {{ $value }}%<br>LABELS: {{ $labels }}" |
| **CinderNetAppClusterPoolFreeSpaceWarning** | "Cinder NetApp (cinder01) free pool capacity has dropped below 30% of total" | "Cinder NetApp volume cinder01: {{ $labels.name }}<br>Free Space: {{ $value }}%<br>LABELS: {{ $labels }}" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## Cinder block node alerts<br>
<summary><strong>Cinder block node alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **CinderBlockNodeFreeSpaceWarning** | "Cinder block node free capacity < 5.5 TB (30% of total)" | "Cinder block node: {{ $labels.name }}<br>Free Space: {{ $value }} GB<br>LABELS: {{ $labels }}" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## Cinder volume error status alerts<br>
<summary><strong>Cinder volume error status alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **CinderVolumeStatusErrorCounterWarning** | "There are {{ $value }} Cinder volumes in error state" | "There are {{ $value }} Cinder volumes in error state.<br>LABELS: {{ $labels }}" |
| **CinderVolumeStatusErrorDeletingCountWarning** | "There are {{ $value }} Cinder volumes in error_deleting state" | "There are {{ $value }} Cinder volumes in error_deleting state.<br>LABELS: {{ $labels }}" |
| **CinderVolumeStatusErrorDeletingWarning** | "Cinder volume with status == error_deleting" | "Cinder volume ID: {{ $labels.id }}<br>NAME: {{ $labels.name }}<br>LABELS: {{ $labels }}" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## Cinder volume status duration alerts<br>
<summary><strong>Cinder volume status duration alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **CinderVolumeStatusStuckInCreatingCountWarning** | "There are {{ $value }} Cinder volumes stuck in creating state" | "There are {{ $value }} Cinder volumes stuck in creating state.<br>LABELS: {{ $labels }}" |
| **CinderVolumeStatusStuckInCreatingWarning** | "Cinder volume with status == creating for approximately 10 minutes." | "Cinder volume ID: {{ $labels.id }}<br>NAME: {{ $labels.name }}<br>LABELS: {{ $labels }}" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## Compute Resource Alerts<br>
<summary><strong>Compute Resource Alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **AbnormalInstanceFailures** | "Instance build failure rate is abnormally high" | "This indicates a major problem building compute instances.<br>View logs and take action to resolve the build failures.<br>" |
| **InstancesStuckInFailureState** | "Instances stuck in failure state for a prolonged period" | "There are instances stuck in a building or error state for a prolonged period<br>that need to be cleaned up.<br>" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## Floating IP availability alerts<br>
<summary><strong>Floating IP availability alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **flipAvailabilityCritical** | "Floating IPs available less than twenty" | "There are less than 20 floating IPs available to assign" |
| **flipAvailabilityWarning** | "Floating IPs available less than one hundred" | "There are less than 100 floating IPs available to assign" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## HP RAID controller and pd and ld disk alerts<br>
<summary><strong>HP RAID controller and pd and ld disk alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **HpSmartArrayControllerStatusCritical** | "HP RAID controller status alert" | "{{ $labels.name }}<br>RAID card type: {{ $labels.product_name }}<br>labels: {{ $labels }}" |
| **HpSmartArrayLdStatusWarning** | "HP RAID logical disk status alert: possible LD array recovery in-progress" | "{{ $labels.name }}<br>labels: {{ $labels }}" |
| **HpSmartArrayPdStatusCritical** | "HP RAID physical disk failure" | "{{ $labels.name }}<br>Port:Box:Bay: {{ $labels.port }}:{{ $labels.box }}:{{ $labels.bay }}<br>Serial: {{ $labels.serial }}<br>labels: {{ $labels }}" |
| **HpSmartArrayPdUsageWarning** | "HP RAID physical disk usage remaining has dropped below 60%" | "{{ $labels.name }}<br>Usage Remaining: {{ $value }}<br>Port:Box:Bay: {{ $labels.port }}:{{ $labels.box }}:{{ $labels.bay }}<br>Serial: {{ $labels.serial }}<br>labels: {{ $labels }}" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## Image Resource Alerts<br>
<summary><strong>Image Resource Alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **AbnormalImageFailures** | "Image create failure rate is abnormally high" | "This indicates a major problem creating images.<br>View logs and take action to resolve the build failures.<br>" |
| **ImagesStuckInFailureState** | "Images stuck in failure state for a prolonged period" | "There are images stuck in a failure state for a prolonged period<br>that need to be cleaned up.<br>" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## Linux MDM device and RAID alerts<br>
<summary><strong>Linux MDM device and RAID alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **NodeMdInfoFailedDeviceCritical** | "NVME device on Linux software RAID failure info" | "{{ $labels.name }}<br>Number MD Failed:{{ $labels.FailedDevices }}<br>LABELS: {{ $labels }}" |
| **NodeMdInfoStateCritical** | "Linux software MD RAID State is NOT active\|clean" | "{{ $labels.name }}<br>State:{{ $labels.State }}<br>LABELS: {{ $labels }}" |
| **NodeMdInfoSuperblockPersistenceCritical** | "Linux software MD Superblock is NOT persistent" | "{{ $labels.name }}<br>Persistence:{{ $labels.Persistence }}<br>LABELS: {{ $labels }}" |
| **NodeMdStateCritical** | "Linux MDM RAID State is {{ $labels.state }}" | "{{ $labels.name }}<br>MD RAID status:{{ $value }}<br>MD RAID device:{{ $labels.device }}<br>LABELS: {{ $labels }}" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## MariaDB backup alerts<br>
<summary><strong>MariaDB backup alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **mariadbBackupCritical** | "Second successive MariaDB backup not successful within 1 hour of scheduled run" | "Second successive MariaDB backup not successful within 1 hour of scheduled run.<br>" |
| **mariadbBackupWarning** | "Last MariaDB backup not successful within 1 hour of scheduled run" | "Last MariaDB backup not successful within 1 hour of scheduled run.<br>" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## Megaraid RAID controller and pd and vd disk alerts<br>
<summary><strong>Megaraid RAID controller and pd and vd disk alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **MegaraidBbuStatusCritical** | "DELL megaraid Battery Backup Unit (BBU) status alert" | "{{ $labels.name }}<br>Controller: {{ $labels.controller }}<br>labels: {{ $labels }}" |
| **MegaraidBlockStoragePassthruDisksCritical** | "DELL megaraid block storage data disk alert" | "{{ $labels.name }}<br>Slot: {{ $labels.slot }}<br>Serial: {{ $labels.serial }}<br>labels: {{ $labels }}" |
| **MegaraidDegradedControllerWarning** | "DELL megaraid controller is in degraded state." | "{{ $labels.name }}<br>Controller: {{ $labels.controller }}<br>labels: {{ $labels }}" |
| **MegaraidFailedControllerCritical** | "DELL Megaraid controller has failed." | "{{ $labels.name }}<br>Controller: {{ $labels.controller }}<br>LABELS: {{ $labels }}" |
| **MegaraidLogicalVdOperatingSystemCritical** | "DELL megaraid virtual disk (Operating System RAID1) alert" | "{{ $labels.name }}<br>Slot: {{ $labels.slot }}<br>labels: {{ $labels }}" |
| **MegaraidPdOsCritical** | "DELL megaraid block storage data disk alert" | "{{ $labels.name }}<br>Slot: {{ $labels.slot }}<br>Serial: {{ $labels.serial }}<br>labels: {{ $labels }}" |
| **MegaraidPdPredictiveMediaErrorsInfo** | "DELL megaraid physical disk media errors detected" | "{{ $labels.name }}<br>Controller: {{ $labels.controller }}<br>Slot: {{ $labels.slot }}<br>labels: {{ $labels }}" |
| **MegaraidPdSmartdInfo** | "DELL megaraid physical disk SMARTD alert" | "{{ $labels.name }}<br>Controller: {{ $labels.controller }}<br>Slot: {{ $labels.slot }}<br>labels: {{ $labels }}" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## Multipath path checker alerts<br>
<summary><strong>Multipath path checker alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **NodeDmpathInfoMultipathCritical** | "Multipathd paths are NOT active\|ready and paths are likely orphaned" | "{{ $labels.name }}<br>labels: {{ $labels }}" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## Mysql Alerts<br>
<summary><strong>Mysql Alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **MysqlDown** | "MariaDB down (instance {{ $labels.instance }})" | "MariaDB instance is down on {{ $labels.instance }}<br>VALUE = {{ $value }}<br>LABELS = {{ $labels }}<br>" |
| **MysqlRestarted** | "MySQL restarted (instance {{ $labels.instance }})" | "MySQL has just been restarted, less than one minute ago on {{ $labels.instance }}.<br>VALUE = {{ $value }}<br>LABELS = {{ $labels }}<br>" |
| **MysqlSlowQueries** | "MySQL slow queries (instance {{ $labels.instance }})" | "MySQL server has some new slow queries.<br>VALUE = {{ $value }}<br>LABELS = {{ $labels }}<br>" |
| **MysqlTooManyConnections(>80%)** | "Database too many connections (> 90%) (instance {{ $labels.instance }})" | "More than 90% of MySQL connections are in use on {{ $labels.instance }}<br>VALUE = {{ $value }}<br>LABELS = {{ $labels }}<br>" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## NVME disk alerts<br>
<summary><strong>NVME disk alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **NodeNvmeInfoDeviceStateCritical** | "NVME device has failed. state!=live" | "{{ $labels.name }}<br>Device: {{ $labels.device }}<br>State:{{ $labels.state }}<br>LABELS: {{ $labels }}" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## OVN backup alerts<br>
<summary><strong>OVN backup alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **ovnBackupDiskUsageCritical** | "OVN backup volume >= 90% disk usage" | "OVN backup volume >= 90% disk usage.<br>" |
| **ovnBackupDiskUsageWarning** | "OVN backup volume >= 80% disk usage" | "OVN backup volume >= 80% disk usage.<br>" |
| **ovnBackupUploadCritical** | "Second successive OVN backup not uploaded within 1 hour of scheduled run" | "Second successive OVN backup not uploaded within 1 hour of scheduled run.<br>" |
| **ovnBackupUploadWarning** | "Last OVN backup not uploaded within 1 hour of scheduled run" | "Last OVN backup not uploaded within 1 hour of scheduled run.<br>" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## Octavia Resource Alerts<br>
<summary><strong>Octavia Resource Alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **LoadbalancersInError** | "Loadbalancer stuck in error state for a prolonged period" | "This may indicate a potential problem with failover and/or health manager services.<br>This could also indicate other problems building load balancers in general.<br>" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## Volume Alerts<br>
<summary><strong>Volume Alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **KubernetesVolumeOutOfDiskSpace** | "Kubernetes Volume out of disk space (instance {{ $labels.instance }})" | "Volume is almost full (< 20% left).<br>VALUE = {{ $value }}<br>LABELS = {{ $labels }}<br>" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## alertmanager.rules<br>
<summary><strong>alertmanager.rules</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **AlertmanagerClusterCrashlooping** | "Half or more of the Alertmanager instances within the same cluster are crashlooping." | "{{ $value \| humanizePercentage }} of Alertmanager instances within the {{$labels.job}} cluster have restarted at least 5 times in the last 10m." |
| **AlertmanagerClusterDown** | "Half or more of the Alertmanager instances within the same cluster are down." | "{{ $value \| humanizePercentage }} of Alertmanager instances within the {{$labels.job}} cluster have been up for less than half of the last 5m." |
| **AlertmanagerClusterFailedToSendAlerts** | "All Alertmanager instances in a cluster failed to send notifications to a critical integration." | "The minimum notification failure rate to {{ $labels.integration }} sent from any instance in the {{$labels.job}} cluster is {{ $value \| humanizePercentage }}." |
| **AlertmanagerClusterFailedToSendAlerts** | "All Alertmanager instances in a cluster failed to send notifications to a non-critical integration." | "The minimum notification failure rate to {{ $labels.integration }} sent from any instance in the {{$labels.job}} cluster is {{ $value \| humanizePercentage }}." |
| **AlertmanagerConfigInconsistent** | "Alertmanager instances within the same cluster have different configurations." | "Alertmanager instances within the {{$labels.job}} cluster have different configurations." |
| **AlertmanagerFailedReload** | "Reloading an Alertmanager configuration has failed." | "Configuration has failed to load for {{ $labels.namespace }}/{{ $labels.pod}}." |
| **AlertmanagerFailedToSendAlerts** | "An Alertmanager instance failed to send notifications." | "Alertmanager {{ $labels.namespace }}/{{ $labels.pod}} failed to send {{ $value \| humanizePercentage }} of notifications to {{ $labels.integration }}." |
| **AlertmanagerMembersInconsistent** | "A member of an Alertmanager cluster has not found all other cluster members." | "Alertmanager {{ $labels.namespace }}/{{ $labels.pod}} has only found {{ $value }} members of the {{$labels.job}} cluster." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## config-reloaders<br>
<summary><strong>config-reloaders</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **ConfigReloaderSidecarErrors** | "config-reloader sidecar has not had a successful reload for 10m" | "Errors encountered while the {{$labels.pod}} config-reloader sidecar attempts to sync config in {{$labels.namespace}} namespace.<br>As a result, configuration for service running in {{$labels.pod}} may be stale and cannot be updated anymore." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## etcd<br>
<summary><strong>etcd</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **etcdDatabaseHighFragmentationRatio** | "etcd database size in use is less than 50% of the actual allocated storage." | "etcd cluster "{{ $labels.job }}": database size in use on instance {{ $labels.instance }} is {{ $value \| humanizePercentage }} of the actual allocated disk space, please run defragmentation (e.g. etcdctl defrag) to retrieve the unused fragmented disk space." |
| **etcdDatabaseQuotaLowSpace** | "etcd cluster database is running full." | "etcd cluster "{{ $labels.job }}": database size exceeds the defined quota on etcd instance {{ $labels.instance }}, please defrag or increase the quota as the writes to etcd will be disabled when it is full." |
| **etcdExcessiveDatabaseGrowth** | "etcd cluster database growing very fast." | "etcd cluster "{{ $labels.job }}": Predicting running out of disk space in the next four hours, based on write observations within the past four hours on etcd instance {{ $labels.instance }}, please check as it might be disruptive." |
| **etcdGRPCRequestsSlow** | "etcd grpc requests are slow" | "etcd cluster "{{ $labels.job }}": 99th percentile of gRPC requests is {{ $value }}s on etcd instance {{ $labels.instance }} for {{ $labels.grpc_method }} method." |
| **etcdHighCommitDurations** | "etcd cluster 99th percentile commit durations are too high." | "etcd cluster "{{ $labels.job }}": 99th percentile commit durations {{ $value }}s on etcd instance {{ $labels.instance }}." |
| **etcdHighFsyncDurations** | "etcd cluster 99th percentile fsync durations are too high." | "etcd cluster "{{ $labels.job }}": 99th percentile fsync durations are {{ $value }}s on etcd instance {{ $labels.instance }}." |
| **etcdHighFsyncDurations** | "etcd cluster 99th percentile fsync durations are too high." | "etcd cluster "{{ $labels.job }}": 99th percentile fsync durations are {{ $value }}s on etcd instance {{ $labels.instance }}." |
| **etcdHighNumberOfFailedGRPCRequests** | "etcd cluster has high number of failed grpc requests." | "etcd cluster "{{ $labels.job }}": {{ $value }}% of requests for {{ $labels.grpc_method }} failed on etcd instance {{ $labels.instance }}." |
| **etcdHighNumberOfFailedGRPCRequests** | "etcd cluster has high number of failed grpc requests." | "etcd cluster "{{ $labels.job }}": {{ $value }}% of requests for {{ $labels.grpc_method }} failed on etcd instance {{ $labels.instance }}." |
| **etcdHighNumberOfFailedProposals** | "etcd cluster has high number of proposal failures." | "etcd cluster "{{ $labels.job }}": {{ $value }} proposal failures within the last 30 minutes on etcd instance {{ $labels.instance }}." |
| **etcdHighNumberOfLeaderChanges** | "etcd cluster has high number of leader changes." | "etcd cluster "{{ $labels.job }}": {{ $value }} leader changes within the last 15 minutes. Frequent elections may be a sign of insufficient resources, high network latency, or disruptions by other components and should be investigated." |
| **etcdInsufficientMembers** | "etcd cluster has insufficient number of members." | "etcd cluster "{{ $labels.job }}": insufficient members ({{ $value }})." |
| **etcdMemberCommunicationSlow** | "etcd cluster member communication is slow." | "etcd cluster "{{ $labels.job }}": member communication with {{ $labels.To }} is taking {{ $value }}s on etcd instance {{ $labels.instance }}." |
| **etcdMembersDown** | "etcd cluster members are down." | "etcd cluster "{{ $labels.job }}": members are down ({{ $value }})." |
| **etcdNoLeader** | "etcd cluster has no leader." | "etcd cluster "{{ $labels.job }}": member {{ $labels.instance }} has no leader." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## fluentbit serviceMonitor alert<br>
<summary><strong>fluentbit serviceMonitor alert</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **MissingFluentbitServiceMonitor** | "ServiceMonitor 'fluentbit-fluent-bit' is either down or missing." | "Check if the Fluentbit ServiceMonitor is properly configured and deployed.<br>" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## general.rules<br>
<summary><strong>general.rules</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **InfoInhibitor** | "Info-level alert inhibition." | "This is an alert that is used to inhibit info alerts.<br>By themselves, the info-level alerts are sometimes very noisy, but they are relevant when combined with<br>other alerts.<br>This alert fires whenever there's a severity="info" alert, and stops firing when another alert with a<br>severity of 'warning' or 'critical' starts firing on the same namespace.<br>This alert should be routed to a null receiver and configured to inhibit alerts with severity="info".<br>" |
| **TargetDown** | "One or more targets are unreachable." | "{{ printf "%.4g" $value }}% of the {{ $labels.job }}/{{ $labels.service }} targets in {{ $labels.namespace }} namespace are down." |
| **Watchdog** | "An alert that should always be firing to certify that Alertmanager is working properly." | "This is an alert meant to ensure that the entire alerting pipeline is functional.<br>This alert is always firing, therefore it should always be firing in Alertmanager<br>and always fire against a receiver. There are integrations with various notification<br>mechanisms that send a notification when this alert is not firing. For example the<br>"DeadMansSnitch" integration in PagerDuty.<br>" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## kube-apiserver-slos<br>
<summary><strong>kube-apiserver-slos</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **KubeAPIErrorBudgetBurn** | "The API server is burning too much error budget." | "The API server is burning too much error budget on cluster {{ $labels.cluster }}." |
| **KubeAPIErrorBudgetBurn** | "The API server is burning too much error budget." | "The API server is burning too much error budget on cluster {{ $labels.cluster }}." |
| **KubeAPIErrorBudgetBurn** | "The API server is burning too much error budget." | "The API server is burning too much error budget on cluster {{ $labels.cluster }}." |
| **KubeAPIErrorBudgetBurn** | "The API server is burning too much error budget." | "The API server is burning too much error budget on cluster {{ $labels.cluster }}." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## kube-state-metrics<br>
<summary><strong>kube-state-metrics</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **KubeStateMetricsListErrors** | "kube-state-metrics is experiencing errors in list operations." | "kube-state-metrics is experiencing errors at an elevated rate in list operations. This is likely causing it to not be able to expose metrics about Kubernetes objects correctly or at all." |
| **KubeStateMetricsShardingMismatch** | "kube-state-metrics sharding is misconfigured." | "kube-state-metrics pods are running with different --total-shards configuration, some Kubernetes objects may be exposed multiple times or not exposed at all." |
| **KubeStateMetricsShardsMissing** | "kube-state-metrics shards are missing." | "kube-state-metrics shards are missing, some Kubernetes objects are not being exposed." |
| **KubeStateMetricsWatchErrors** | "kube-state-metrics is experiencing errors in watch operations." | "kube-state-metrics is experiencing errors at an elevated rate in watch operations. This is likely causing it to not be able to expose metrics about Kubernetes objects correctly or at all." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## kubernetes-apps<br>
<summary><strong>kubernetes-apps</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **KubeContainerWaiting** | "Pod container waiting longer than 1 hour" | "pod/{{ $labels.pod }} in namespace {{ $labels.namespace }} on container {{ $labels.container}} has been in waiting state for longer than 1 hour. (reason: "{{ $labels.reason }}") on cluster {{ $labels.cluster }}." |
| **KubeDaemonSetMisScheduled** | "DaemonSet pods are misscheduled." | "{{ $value }} Pods of DaemonSet {{ $labels.namespace }}/{{ $labels.daemonset }} are running where they are not supposed to run on cluster {{ $labels.cluster }}." |
| **KubeDaemonSetNotScheduled** | "DaemonSet pods are not scheduled." | "{{ $value }} Pods of DaemonSet {{ $labels.namespace }}/{{ $labels.daemonset }} are not scheduled on cluster {{ $labels.cluster }}." |
| **KubeDaemonSetRolloutStuck** | "DaemonSet rollout is stuck." | "DaemonSet {{ $labels.namespace }}/{{ $labels.daemonset }} has not finished or progressed for at least 15m on cluster {{ $labels.cluster }}." |
| **KubeDeploymentGenerationMismatch** | "Deployment generation mismatch due to possible roll-back" | "Deployment generation for {{ $labels.namespace }}/{{ $labels.deployment }} does not match, this indicates that the Deployment has failed but has not been rolled back on cluster {{ $labels.cluster }}." |
| **KubeDeploymentReplicasMismatch** | "Deployment has not matched the expected number of replicas." | "Deployment {{ $labels.namespace }}/{{ $labels.deployment }} has not matched the expected number of replicas for longer than 15 minutes on cluster {{ $labels.cluster }}." |
| **KubeDeploymentRolloutStuck** | "Deployment rollout is not progressing." | "Rollout of deployment {{ $labels.namespace }}/{{ $labels.deployment }} is not progressing for longer than 15 minutes on cluster {{ $labels.cluster }}." |
| **KubeHpaMaxedOut** | "HPA is running at max replicas" | "HPA {{ $labels.namespace }}/{{ $labels.horizontalpodautoscaler  }} has been running at max replicas for longer than 15 minutes on cluster {{ $labels.cluster }}." |
| **KubeHpaReplicasMismatch** | "HPA has not matched desired number of replicas." | "HPA {{ $labels.namespace }}/{{ $labels.horizontalpodautoscaler  }} has not matched the desired number of replicas for longer than 15 minutes on cluster {{ $labels.cluster }}." |
| **KubeJobFailed** | "Job failed to complete." | "Job {{ $labels.namespace }}/{{ $labels.job_name }} failed to complete. Removing failed job after investigation should clear this alert on cluster {{ $labels.cluster }}." |
| **KubeJobNotCompleted** | "Job did not complete in time" | "Job {{ $labels.namespace }}/{{ $labels.job_name }} is taking more than {{ "43200" \| humanizeDuration }} to complete on cluster {{ $labels.cluster }}." |
| **KubePodCrashLooping** | "Pod is crash looping." | "Pod {{ $labels.namespace }}/{{ $labels.pod }} ({{ $labels.container }}) is in waiting state (reason: "CrashLoopBackOff") on cluster {{ $labels.cluster }}." |
| **KubePodNotReady** | "Pod has been in a non-ready state for more than 15 minutes." | "Pod {{ $labels.namespace }}/{{ $labels.pod }} has been in a non-ready state for longer than 15 minutes on cluster {{ $labels.cluster }}." |
| **KubeStatefulSetGenerationMismatch** | "StatefulSet generation mismatch due to possible roll-back" | "StatefulSet generation for {{ $labels.namespace }}/{{ $labels.statefulset }} does not match, this indicates that the StatefulSet has failed but has not been rolled back on cluster {{ $labels.cluster }}." |
| **KubeStatefulSetReplicasMismatch** | "StatefulSet has not matched the expected number of replicas." | "StatefulSet {{ $labels.namespace }}/{{ $labels.statefulset }} has not matched the expected number of replicas for longer than 15 minutes on cluster {{ $labels.cluster }}." |
| **KubeStatefulSetUpdateNotRolledOut** | "StatefulSet update has not been rolled out." | "StatefulSet {{ $labels.namespace }}/{{ $labels.statefulset }} update has not been rolled out on cluster {{ $labels.cluster }}." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## kubernetes-resources<br>
<summary><strong>kubernetes-resources</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **CPUThrottlingHigh** | "Processes experience elevated CPU throttling." | "{{ $value \| humanizePercentage }} throttling of CPU in namespace {{ $labels.namespace }} for container {{ $labels.container }} in pod {{ $labels.pod }} on cluster {{ $labels.cluster }}." |
| **KubeCPUOvercommit** | "Cluster has overcommitted CPU resource requests." | "Cluster {{ $labels.cluster }} has overcommitted CPU resource requests for Pods by {{ $value }} CPU shares and cannot tolerate node failure." |
| **KubeCPUQuotaOvercommit** | "Cluster has overcommitted CPU resource requests." | "Cluster {{ $labels.cluster }}  has overcommitted CPU resource requests for Namespaces." |
| **KubeMemoryOvercommit** | "Cluster has overcommitted memory resource requests." | "Cluster {{ $labels.cluster }} has overcommitted memory resource requests for Pods by {{ $value \| humanize }} bytes and cannot tolerate node failure." |
| **KubeMemoryQuotaOvercommit** | "Cluster has overcommitted memory resource requests." | "Cluster {{ $labels.cluster }}  has overcommitted memory resource requests for Namespaces." |
| **KubeQuotaAlmostFull** | "Namespace quota is going to be full." | "Namespace {{ $labels.namespace }} is using {{ $value \| humanizePercentage }} of its {{ $labels.resource }} quota on cluster {{ $labels.cluster }}." |
| **KubeQuotaExceeded** | "Namespace quota has exceeded the limits." | "Namespace {{ $labels.namespace }} is using {{ $value \| humanizePercentage }} of its {{ $labels.resource }} quota on cluster {{ $labels.cluster }}." |
| **KubeQuotaFullyUsed** | "Namespace quota is fully used." | "Namespace {{ $labels.namespace }} is using {{ $value \| humanizePercentage }} of its {{ $labels.resource }} quota on cluster {{ $labels.cluster }}." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## kubernetes-storage<br>
<summary><strong>kubernetes-storage</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **KubePersistentVolumeErrors** | "PersistentVolume is having issues with provisioning." | "The persistent volume {{ $labels.persistentvolume }} {{ with $labels.cluster -}} on Cluster {{ . }} {{- end }} has status {{ $labels.phase }}." |
| **KubePersistentVolumeFillingUp** | "PersistentVolume is filling up." | "The PersistentVolume claimed by {{ $labels.persistentvolumeclaim }} in Namespace {{ $labels.namespace }} {{ with $labels.cluster -}} on Cluster {{ . }} {{- end }} is only {{ $value \| humanizePercentage }} free." |
| **KubePersistentVolumeFillingUp** | "PersistentVolume is filling up." | "Based on recent sampling, the PersistentVolume claimed by {{ $labels.persistentvolumeclaim }} in Namespace {{ $labels.namespace }} {{ with $labels.cluster -}} on Cluster {{ . }} {{- end }} is expected to fill up within four days. Currently {{ $value \| humanizePercentage }} is available." |
| **KubePersistentVolumeInodesFillingUp** | "PersistentVolumeInodes are filling up." | "The PersistentVolume claimed by {{ $labels.persistentvolumeclaim }} in Namespace {{ $labels.namespace }} {{ with $labels.cluster -}} on Cluster {{ . }} {{- end }} only has {{ $value \| humanizePercentage }} free inodes." |
| **KubePersistentVolumeInodesFillingUp** | "PersistentVolumeInodes are filling up." | "Based on recent sampling, the PersistentVolume claimed by {{ $labels.persistentvolumeclaim }} in Namespace {{ $labels.namespace }} {{ with $labels.cluster -}} on Cluster {{ . }} {{- end }} is expected to run out of inodes within four days. Currently {{ $value \| humanizePercentage }} of its inodes are free." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## kubernetes-system<br>
<summary><strong>kubernetes-system</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **KubeClientErrors** | "Kubernetes API server client is experiencing errors." | "Kubernetes API server client '{{ $labels.job }}/{{ $labels.instance }}' is experiencing {{ $value \| humanizePercentage }} errors on cluster {{ $labels.cluster }}." |
| **KubeVersionMismatch** | "Different semantic versions of Kubernetes components running." | "There are {{ $value }} different semantic versions of Kubernetes components running on cluster {{ $labels.cluster }}." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## kubernetes-system-apiserver<br>
<summary><strong>kubernetes-system-apiserver</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **KubeAPIDown** | "Target disappeared from Prometheus target discovery." | "KubeAPI has disappeared from Prometheus target discovery." |
| **KubeAPITerminatedRequests** | "The kubernetes apiserver has terminated {{ $value \| humanizePercentage }} of its incoming requests." | "The kubernetes apiserver has terminated {{ $value \| humanizePercentage }} of its incoming requests on cluster {{ $labels.cluster }}." |
| **KubeAggregatedAPIDown** | "Kubernetes aggregated API is down." | "Kubernetes aggregated API {{ $labels.name }}/{{ $labels.namespace }} has been only {{ $value \| humanize }}% available over the last 10m on cluster {{ $labels.cluster }}." |
| **KubeAggregatedAPIErrors** | "Kubernetes aggregated API has reported errors." | "Kubernetes aggregated API {{ $labels.instance }}/{{ $labels.name }} has reported {{ $labels.reason }} errors on cluster {{ $labels.cluster }}." |
| **KubeClientCertificateExpiration** | "Client certificate is about to expire." | "A client certificate used to authenticate to kubernetes apiserver is expiring in less than 7.0 days on cluster {{ $labels.cluster }}." |
| **KubeClientCertificateExpiration** | "Client certificate is about to expire." | "A client certificate used to authenticate to kubernetes apiserver is expiring in less than 24.0 hours on cluster {{ $labels.cluster }}." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## kubernetes-system-controller-manager<br>
<summary><strong>kubernetes-system-controller-manager</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **KubeControllerManagerDown** | "Target disappeared from Prometheus target discovery." | "KubeControllerManager has disappeared from Prometheus target discovery." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## kubernetes-system-kube-proxy<br>
<summary><strong>kubernetes-system-kube-proxy</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **KubeProxyDown** | "Target disappeared from Prometheus target discovery." | "KubeProxy has disappeared from Prometheus target discovery." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## kubernetes-system-kubelet<br>
<summary><strong>kubernetes-system-kubelet</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **KubeNodeEviction** | "Node is evicting pods." | "Node {{ $labels.node }} on {{ $labels.cluster }} is evicting Pods due to {{ $labels.eviction_signal }}.  Eviction occurs when eviction thresholds are crossed, typically caused by Pods exceeding RAM/ephemeral-storage limits." |
| **KubeNodeNotReady** | "Node is not ready." | "{{ $labels.node }} has been unready for more than 15 minutes on cluster {{ $labels.cluster }}." |
| **KubeNodePressure** | "Node has as active Condition." | "{{ $labels.node }} on cluster {{ $labels.cluster }} has active Condition {{ $labels.condition }}. This is caused by resource usage exceeding eviction thresholds." |
| **KubeNodeReadinessFlapping** | "Node readiness status is flapping." | "The readiness status of node {{ $labels.node }} has changed {{ $value }} times in the last 15 minutes on cluster {{ $labels.cluster }}." |
| **KubeNodeUnreachable** | "Node is unreachable." | "{{ $labels.node }} is unreachable and some workloads may be rescheduled on cluster {{ $labels.cluster }}." |
| **KubeletClientCertificateExpiration** | "Kubelet client certificate is about to expire." | "Client certificate for Kubelet on node {{ $labels.node }} expires in {{ $value \| humanizeDuration }} on cluster {{ $labels.cluster }}." |
| **KubeletClientCertificateExpiration** | "Kubelet client certificate is about to expire." | "Client certificate for Kubelet on node {{ $labels.node }} expires in {{ $value \| humanizeDuration }} on cluster {{ $labels.cluster }}." |
| **KubeletClientCertificateRenewalErrors** | "Kubelet has failed to renew its client certificate." | "Kubelet on node {{ $labels.node }} has failed to renew its client certificate ({{ $value \| humanize }} errors in the last 5 minutes) on cluster {{ $labels.cluster }}." |
| **KubeletDown** | "Target disappeared from Prometheus target discovery." | "Kubelet has disappeared from Prometheus target discovery." |
| **KubeletPlegDurationHigh** | "Kubelet Pod Lifecycle Event Generator is taking too long to relist." | "The Kubelet Pod Lifecycle Event Generator has a 99th percentile duration of {{ $value }} seconds on node {{ $labels.node }} on cluster {{ $labels.cluster }}." |
| **KubeletPodStartUpLatencyHigh** | "Kubelet Pod startup latency is too high." | "Kubelet Pod startup 99th percentile latency is {{ $value }} seconds on node {{ $labels.node }} on cluster {{ $labels.cluster }}." |
| **KubeletServerCertificateExpiration** | "Kubelet server certificate is about to expire." | "Server certificate for Kubelet on node {{ $labels.node }} expires in {{ $value \| humanizeDuration }} on cluster {{ $labels.cluster }}." |
| **KubeletServerCertificateExpiration** | "Kubelet server certificate is about to expire." | "Server certificate for Kubelet on node {{ $labels.node }} expires in {{ $value \| humanizeDuration }} on cluster {{ $labels.cluster }}." |
| **KubeletServerCertificateRenewalErrors** | "Kubelet has failed to renew its server certificate." | "Kubelet on node {{ $labels.node }} has failed to renew its server certificate ({{ $value \| humanize }} errors in the last 5 minutes) on cluster {{ $labels.cluster }}." |
| **KubeletTooManyPods** | "Kubelet is running at capacity." | "Kubelet '{{ $labels.node }}' is running at {{ $value \| humanizePercentage }} of its Pod capacity on cluster {{ $labels.cluster }}." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## kubernetes-system-scheduler<br>
<summary><strong>kubernetes-system-scheduler</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **KubeSchedulerDown** | "Target disappeared from Prometheus target discovery." | "KubeScheduler has disappeared from Prometheus target discovery." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## mariadb-alerts<br>
<summary><strong>mariadb-alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **MariaDBDown** | "MariaDB not up and running, immediate attention is required." | "MariaDB {{$labels.job}} on {{$labels.instance}} is not up." |
| **MariaDBReplicationErrors** | "MariaDB is reporting replication errors from {{$labels.instance}}, immediate attention is required." | "MariaDB {{$labels.job}} on {{$labels.instance}} is reporting replication errors." |
| **MysqlSlaveReplicationLag** | "MySQL Slave replication lag (instance {{ $labels.instance }})" | "MySQL replication lag on {{ $labels.instance }}<br>  VALUE = {{ $value }}<br>  LABELS = {{ $labels }}" |
| **MysqlTooManyConnections(>80%)** | "MySQL too many connections (> 80%) (instance {{ $labels.instance }})" | "More than 80% of MySQL connections are in use on {{ $labels.instance }}<br>  VALUE = {{ $value }}<br>  LABELS = {{ $labels }}" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## node-exporter<br>
<summary><strong>node-exporter</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **NodeBondingDegraded** | "Bonding interface is degraded" | "Bonding interface {{ $labels.master }} on {{ $labels.instance }} is in degraded state due to one or more slave failures." |
| **NodeCPUHighUsage** | "High CPU usage." | "CPU usage at {{ $labels.instance }} has been above 90% for the last 15 minutes, is currently at {{ printf "%.2f" $value }}%.<br>" |
| **NodeClockNotSynchronising** | "Clock not synchronising." | "Clock at {{ $labels.instance }} is not synchronising. Ensure NTP is configured on this host." |
| **NodeClockSkewDetected** | "Clock skew detected." | "Clock at {{ $labels.instance }} is out of sync by more than 0.05s. Ensure NTP is configured correctly on this host." |
| **NodeDiskIOSaturation** | "Disk IO queue is high." | "Disk IO queue (aqu-sq) is high on {{ $labels.device }} at {{ $labels.instance }}, has been above 10 for the last 30 minutes, is currently at {{ printf "%.2f" $value }}.<br>This symptom might indicate disk saturation.<br>" |
| **NodeFileDescriptorLimit** | "Kernel is predicted to exhaust file descriptors limit soon." | "File descriptors limit at {{ $labels.instance }} is currently at {{ printf "%.2f" $value }}%." |
| **NodeFileDescriptorLimit** | "Kernel is predicted to exhaust file descriptors limit soon." | "File descriptors limit at {{ $labels.instance }} is currently at {{ printf "%.2f" $value }}%." |
| **NodeFilesystemAlmostOutOfFiles** | "Filesystem has less than 5% inodes left." | "Filesystem on {{ $labels.device }}, mounted on {{ $labels.mountpoint }}, at {{ $labels.instance }} has only {{ printf "%.2f" $value }}% available inodes left." |
| **NodeFilesystemAlmostOutOfFiles** | "Filesystem has less than 3% inodes left." | "Filesystem on {{ $labels.device }}, mounted on {{ $labels.mountpoint }}, at {{ $labels.instance }} has only {{ printf "%.2f" $value }}% available inodes left." |
| **NodeFilesystemAlmostOutOfSpace** | "Filesystem has less than 5% space left." | "Filesystem on {{ $labels.device }}, mounted on {{ $labels.mountpoint }}, at {{ $labels.instance }} has only {{ printf "%.2f" $value }}% available space left." |
| **NodeFilesystemAlmostOutOfSpace** | "Filesystem has less than 3% space left." | "Filesystem on {{ $labels.device }}, mounted on {{ $labels.mountpoint }}, at {{ $labels.instance }} has only {{ printf "%.2f" $value }}% available space left." |
| **NodeFilesystemFilesFillingUp** | "Filesystem is predicted to run out of inodes within the next 24 hours." | "Filesystem on {{ $labels.device }}, mounted on {{ $labels.mountpoint }}, at {{ $labels.instance }} has only {{ printf "%.2f" $value }}% available inodes left and is filling up." |
| **NodeFilesystemFilesFillingUp** | "Filesystem is predicted to run out of inodes within the next 4 hours." | "Filesystem on {{ $labels.device }}, mounted on {{ $labels.mountpoint }}, at {{ $labels.instance }} has only {{ printf "%.2f" $value }}% available inodes left and is filling up fast." |
| **NodeFilesystemSpaceFillingUp** | "Filesystem is predicted to run out of space within the next 24 hours." | "Filesystem on {{ $labels.device }}, mounted on {{ $labels.mountpoint }}, at {{ $labels.instance }} has only {{ printf "%.2f" $value }}% available space left and is filling up." |
| **NodeFilesystemSpaceFillingUp** | "Filesystem is predicted to run out of space within the next 4 hours." | "Filesystem on {{ $labels.device }}, mounted on {{ $labels.mountpoint }}, at {{ $labels.instance }} has only {{ printf "%.2f" $value }}% available space left and is filling up fast." |
| **NodeHighNumberConntrackEntriesUsed** | "Number of conntrack are getting close to the limit." | "{{ $labels.instance }} {{ $value \| humanizePercentage }} of conntrack entries are used." |
| **NodeMemoryHighUtilization** | "Host is running out of memory." | "Memory is filling up at {{ $labels.instance }}, has been above 90% for the last 15 minutes, is currently at {{ printf "%.2f" $value }}%.<br>" |
| **NodeMemoryMajorPagesFaults** | "Memory major page faults are occurring at very high rate." | "Memory major pages are occurring at very high rate at {{ $labels.instance }}, 500 major page faults per second for the last 15 minutes, is currently at {{ printf "%.2f" $value }}.<br>Please check that there is enough memory available at this instance.<br>" |
| **NodeNetworkReceiveErrs** | "Network interface is reporting many receive errors." | "{{ $labels.instance }} interface {{ $labels.device }} has encountered {{ printf "%.0f" $value }} receive errors in the last two minutes." |
| **NodeNetworkTransmitErrs** | "Network interface is reporting many transmit errors." | "{{ $labels.instance }} interface {{ $labels.device }} has encountered {{ printf "%.0f" $value }} transmit errors in the last two minutes." |
| **NodeRAIDDegraded** | "RAID Array is degraded." | "RAID array '{{ $labels.device }}' at {{ $labels.instance }} is in degraded state due to one or more disks failures. Number of spare drives is insufficient to fix issue automatically." |
| **NodeRAIDDiskFailure** | "Failed device in RAID array." | "At least one device in RAID array at {{ $labels.instance }} failed. Array '{{ $labels.device }}' needs attention and possibly a disk swap." |
| **NodeSystemSaturation** | "System saturated, load per core is very high." | "System load per core at {{ $labels.instance }} has been above 2 for the last 15 minutes, is currently at {{ printf "%.2f" $value }}.<br>This might indicate this instance resources saturation and can cause it becoming unresponsive.<br>" |
| **NodeSystemdServiceCrashlooping** | "Systemd service keeps restaring, possibly crash looping." | "Systemd service {{ $labels.name }} has being restarted too many times at {{ $labels.instance }} for the last 15 minutes. Please check if service is crash looping." |
| **NodeSystemdServiceFailed** | "Systemd service has entered failed state." | "Systemd service {{ $labels.name }} has entered failed state at {{ $labels.instance }}" |
| **NodeTextFileCollectorScrapeError** | "Node Exporter text file collector failed to scrape." | "Node Exporter text file collector on {{ $labels.instance }} failed to scrape." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## node-network<br>
<summary><strong>node-network</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **NodeNetworkInterfaceFlapping** | "Network interface is often changing its status" | "Network interface "{{ $labels.device }}" changing its up status often on node-exporter {{ $labels.namespace }}/{{ $labels.pod }}" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## pod-state-alerts<br>
<summary><strong>pod-state-alerts</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **HighPodRestartRate** | "High pod restart count detected" | "Pod {{ $labels.pod }} in namespace {{ $labels.namespace }} is restarting frequently, which may indicate network instability." |
| **KubePodNotReadyCritical** | "Pod has been in a non-ready state for more than 5 minutes." | "Pod {{ $labels.namespace }}/{{ $labels.pod }} has been in a non-ready state for longer than 5 minutes." |
| **TooManyContainerRestarts** | "Container named {{ $labels.container }} in {{ $labels.pod }} in {{ $labels.namespace }} has restarted too many times in a short period and needs to be investigated." | "Namespace: {{$labels.namespace}}<br>Pod name: {{$labels.pod}}<br>Container name: {{$labels.container}}<br>" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## prometheus<br>
<summary><strong>prometheus</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **PrometheusBadConfig** | "Failed Prometheus configuration reload." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} has failed to reload its configuration." |
| **PrometheusDuplicateTimestamps** | "Prometheus is dropping samples with duplicate timestamps." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} is dropping {{ printf "%.4g" $value  }} samples/s with different values but duplicated timestamp." |
| **PrometheusErrorSendingAlertsToAnyAlertmanager** | "Prometheus encounters more than 3% errors sending alerts to any Alertmanager." | "{{ printf "%.1f" $value }}% minimum errors while sending alerts from Prometheus {{$labels.namespace}}/{{$labels.pod}} to any Alertmanager." |
| **PrometheusErrorSendingAlertsToSomeAlertmanagers** | "More than 1% of alerts sent by Prometheus to a specific Alertmanager were affected by errors." | "{{ printf "%.1f" $value }}% of alerts sent by Prometheus {{$labels.namespace}}/{{$labels.pod}} to Alertmanager {{$labels.alertmanager}} were affected by errors." |
| **PrometheusHighQueryLoad** | "Prometheus is reaching its maximum capacity serving concurrent requests." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} query API has less than 20% available capacity in its query engine for the last 15 minutes." |
| **PrometheusKubernetesListWatchFailures** | "Requests in Kubernetes SD are failing." | "Kubernetes service discovery of Prometheus {{$labels.namespace}}/{{$labels.pod}} is experiencing {{ printf "%.0f" $value }} failures with LIST/WATCH requests to the Kubernetes API in the last 5 minutes." |
| **PrometheusLabelLimitHit** | "Prometheus has dropped targets because some scrape configs have exceeded the labels limit." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} has dropped {{ printf "%.0f" $value }} targets because some samples exceeded the configured label_limit, label_name_length_limit or label_value_length_limit." |
| **PrometheusMissingRuleEvaluations** | "Prometheus is missing rule evaluations due to slow rule group evaluation." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} has missed {{ printf "%.0f" $value }} rule group evaluations in the last 5m." |
| **PrometheusNotConnectedToAlertmanagers** | "Prometheus is not connected to any Alertmanagers." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} is not connected to any Alertmanagers." |
| **PrometheusNotIngestingSamples** | "Prometheus is not ingesting samples." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} is not ingesting samples." |
| **PrometheusNotificationQueueRunningFull** | "Prometheus alert notification queue predicted to run full in less than 30m." | "Alert notification queue of Prometheus {{$labels.namespace}}/{{$labels.pod}} is running full." |
| **PrometheusOutOfOrderTimestamps** | "Prometheus drops samples with out-of-order timestamps." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} is dropping {{ printf "%.4g" $value  }} samples/s with timestamps arriving out of order." |
| **PrometheusRemoteStorageFailures** | "Prometheus fails to send samples to remote storage." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} failed to send {{ printf "%.1f" $value }}% of the samples to {{ $labels.remote_name}}:{{ $labels.url }}" |
| **PrometheusRemoteWriteBehind** | "Prometheus remote write is behind." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} remote write is {{ printf "%.1f" $value }}s behind for {{ $labels.remote_name}}:{{ $labels.url }}." |
| **PrometheusRemoteWriteDesiredShards** | "Prometheus remote write desired shards calculation wants to run more than configured max shards." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} remote write desired shards calculation wants to run {{ $value }} shards for queue {{ $labels.remote_name}}:{{ $labels.url }}, which is more than the max of {{ printf `prometheus_remote_storage_shards_max{instance="%s",job="kube-prometheus-stack-prometheus",namespace="prometheus"}` $labels.instance \| query \| first \| value }}." |
| **PrometheusRuleFailures** | "Prometheus is failing rule evaluations." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} has failed to evaluate {{ printf "%.0f" $value }} rules in the last 5m." |
| **PrometheusSDRefreshFailure** | "Failed Prometheus SD refresh." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} has failed to refresh SD with mechanism {{$labels.mechanism}}." |
| **PrometheusScrapeBodySizeLimitHit** | "Prometheus has dropped some targets that exceeded body size limit." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} has failed {{ printf "%.0f" $value }} scrapes in the last 5m because some targets exceeded the configured body_size_limit." |
| **PrometheusScrapeSampleLimitHit** | "Prometheus has failed scrapes that have exceeded the configured sample limit." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} has failed {{ printf "%.0f" $value }} scrapes in the last 5m because some targets exceeded the configured sample_limit." |
| **PrometheusTSDBCompactionsFailing** | "Prometheus has issues compacting blocks." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} has detected {{$value \| humanize}} compaction failures over the last 3h." |
| **PrometheusTSDBReloadsFailing** | "Prometheus has issues reloading blocks from disk." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} has detected {{$value \| humanize}} reload failures over the last 3h." |
| **PrometheusTargetLimitHit** | "Prometheus has dropped targets because some scrape configs have exceeded the targets limit." | "Prometheus {{$labels.namespace}}/{{$labels.pod}} has dropped {{ printf "%.0f" $value }} targets because the number of targets exceeded the configured target_limit." |
| **PrometheusTargetSyncFailure** | "Prometheus has failed to sync targets." | "{{ printf "%.0f" $value }} targets in Prometheus {{$labels.namespace}}/{{$labels.pod}} have failed to sync because invalid configuration was supplied." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## prometheus-operator<br>
<summary><strong>prometheus-operator</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **PrometheusOperatorListErrors** | "Errors while performing list operations in controller." | "Errors while performing List operations in controller {{$labels.controller}} in {{$labels.namespace}} namespace." |
| **PrometheusOperatorNodeLookupErrors** | "Errors while reconciling Prometheus." | "Errors while reconciling Prometheus in {{ $labels.namespace }} Namespace." |
| **PrometheusOperatorNotReady** | "Prometheus operator not ready" | "Prometheus operator in {{ $labels.namespace }} namespace isn't ready to reconcile {{ $labels.controller }} resources." |
| **PrometheusOperatorReconcileErrors** | "Errors while reconciling objects." | "{{ $value \| humanizePercentage }} of reconciling operations failed for {{ $labels.controller }} controller in {{ $labels.namespace }} namespace." |
| **PrometheusOperatorRejectedResources** | "Resources rejected by Prometheus operator" | "Prometheus operator in {{ $labels.namespace }} namespace rejected {{ printf "%0.0f" $value }} {{ $labels.controller }}/{{ $labels.resource }} resources." |
| **PrometheusOperatorStatusUpdateErrors** | "Errors while updating objects status." | "{{ $value \| humanizePercentage }} of status update operations failed for {{ $labels.controller }} controller in {{ $labels.namespace }} namespace." |
| **PrometheusOperatorSyncFailed** | "Last controller reconciliation failed" | "Controller {{ $labels.controller }} in {{ $labels.namespace }} namespace fails to reconcile {{ $value }} objects." |
| **PrometheusOperatorWatchErrors** | "Errors while performing watch operations in controller." | "Errors while performing watch operations in controller {{$labels.controller}} in {{$labels.namespace}} namespace." |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

## rabbitmq<br>
<summary><strong>rabbitmq</strong></summary><br>

| Alert Name | Summary | Description |
| --- | --- | --- |
| **ContainerRestarts** | "Investigate why the container got restarted.<br>Check the logs of the current container: `kubectl -n {{ $labels.namespace }} logs {{ $labels.pod }}`<br>Check the logs of the previous container: `kubectl -n {{ $labels.namespace }} logs {{ $labels.pod }} --previous`<br>Check the last state of the container: `kubectl -n {{ $labels.namespace }} get pod {{ $labels.pod }} -o jsonpath='{.status.containerStatuses[].lastState}'`<br>" | "Over the last 10 minutes, container `{{ $labels.container }}`<br>restarted `{{ $value \| printf "%.0f" }}` times in pod `{{ $labels.pod }}` of RabbitMQ cluster<br>`{{ $labels.rabbitmq_cluster }}` in namespace `{{ $labels.namespace }}`.<br>" |
| **FileDescriptorsNearLimit** | "More than 80% of file descriptors are used on the RabbitMQ node.<br>When this value reaches 100%, new connections will not be accepted and disk write operations may fail.<br>Client libraries, peer nodes and CLI tools will not be able to connect when the node runs out of available file descriptors.<br>See https://www.rabbitmq.com/production-checklist.html#resource-limits-file-handle-limit.<br>" | "`{{ $value \| humanizePercentage }}` file descriptors of file<br>descriptor limit are used in RabbitMQ node `{{ $labels.rabbitmq_node }}`,<br>pod `{{ $labels.pod }}`, RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}`,<br>namespace `{{ $labels.namespace }}`.<br>" |
| **HighConnectionChurn** | "More than 10% of total connections are churning.<br>This means that client application connections are short-lived instead of long-lived.<br>Read https://www.rabbitmq.com/connections.html#high-connection-churn to understand why this is an anti-pattern.<br>" | "Over the last 5 minutes, `{{ $value \| humanizePercentage }}`<br>of total connections are closed or opened per second in RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}`<br>in namespace `{{ $labels.namespace }}`.<br>" |
| **InsufficientEstablishedErlangDistributionLinks** | "RabbitMQ clusters have a full mesh topology.<br>All RabbitMQ nodes connect to all other RabbitMQ nodes in both directions.<br>The expected number of established Erlang distribution links is therefore `n*(n-1)` where `n` is the number of RabbitMQ nodes in the cluster.<br>Therefore, the expected number of distribution links are `0` for a 1-node cluster, `6` for a 3-node cluster, and `20` for a 5-node cluster.<br>This alert reports that the number of established distributions links is less than the expected number.<br>Some reasons for this alert include failed network links, network partitions, failed clustering (i.e. nodes can't join the cluster).<br>Check the panels `All distribution links`, `Established distribution links`, `Connecting distributions links`, `Waiting distribution links`, and `distribution links`<br>of the Grafana dashboard `Erlang-Distribution`.<br>Check the logs of the RabbitMQ nodes: `kubectl -n {{ $labels.namespace }} logs -l app.kubernetes.io/component=rabbitmq,app.kubernetes.io/name={{ $labels.rabbitmq_cluster }}`<br>" | "There are only `{{ $value }}` established Erlang distribution links<br>in RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}` in namespace `{{ $labels.namespace }}`.<br>" |
| **LowDiskWatermarkPredicted** | "Based on the trend of available disk space over the past 24 hours, it's predicted that, in 24 hours from now, a disk alarm will be triggered since the free disk space will drop below the free disk space limit.<br>This alert is reported for the partition where the RabbitMQ data directory is stored.<br>When the disk alarm will be triggered, all publishing connections across all cluster nodes will be blocked.<br>See<br>https://www.rabbitmq.com/alarms.html,<br>https://www.rabbitmq.com/disk-alarms.html,<br>https://www.rabbitmq.com/production-checklist.html#resource-limits-disk-space,<br>https://www.rabbitmq.com/persistence-conf.html,<br>https://www.rabbitmq.com/connection-blocked.html.<br>" | "The predicted free disk space in 24 hours from now is `{{ $value \| humanize1024 }}B`<br>in RabbitMQ node `{{ $labels.rabbitmq_node }}`, pod `{{ $labels.pod }}`,<br>RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}`, namespace `{{ $labels.namespace }}`.<br>" |
| **MemoryAlarm** | "A RabbitMQ node reached the `vm_memory_high_watermark` threshold.<br>See https://www.rabbitmq.com/docs/alarms#overview, https://www.rabbitmq.com/docs/memory.<br>" | "RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}` memory alarm active. Publishers are blocked.<br>" |
| **NoMajorityOfNodesReady** | "No majority of nodes have been ready for the last 5 minutes.<br>Check the details of the pods:<br>`kubectl -n {{ $labels.namespace }} describe pods -l app.kubernetes.io/component=rabbitmq,app.kubernetes.io/name={{ $labels.label_app_kubernetes_io_name }}`<br>" | "Only `{{ $value }}` replicas are ready in StatefulSet `{{ $labels.statefulset }}`<br>of RabbitMQ cluster `{{ $labels.label_app_kubernetes_io_name }}` in namespace `{{ $labels.namespace }}`.<br>" |
| **PersistentVolumeMissing** | "RabbitMQ needs a PersistentVolume for its data.<br>However, there is no PersistentVolume bound to the PersistentVolumeClaim.<br>This means the requested storage could not be provisioned.<br>Check the status of the PersistentVolumeClaim: `kubectl -n {{ $labels.namespace }} describe pvc {{ $labels.persistentvolumeclaim }}`.<br>" | "PersistentVolumeClaim `{{ $labels.persistentvolumeclaim }}` of<br>RabbitMQ cluster `{{ $labels.label_app_kubernetes_io_name }}` in namespace<br>`{{ $labels.namespace }}` is not bound.<br>" |
| **QueueHasNoConsumers** | "Messages are sitting idle in the queue, without any processing.<br>This alert is highly application specific (and e.g. doesn't make sense for stream queues).<br>" | "Over the last 10 minutes, non-empty queue `{{ $labels.queue }}` with {{ $value }} messages<br>in virtual host `{{ $labels.vhost }}` didn't have any consumers in<br>RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}` in namespace `{{ $labels.namespace }}`.<br>" |
| **QueueIsGrowing** | "Queue size is steadily growing over time.<br>" | "Over the last 10 minutes, queue `{{ $labels.queue }}` in virtual host `{{ $labels.vhost }}`<br>was growing. 10 minute moving average has grown by {{ $value }}.<br>This happens in RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}` in namespace `{{ $labels.namespace }}`.<br>" |
| **RabbitmqDiskAlarm** | "A RabbitMQ node reached the `disk_free_limit` threshold.<br>See https://www.rabbitmq.com/docs/alarms#overview, https://www.rabbitmq.com/docs/disk-alarms.<br>" | "RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}` disk alarm active. Publishers are blocked.<br>" |
| **RabbitmqFileDescriptorAlarm** | "A RabbitMQ node ran out of file descriptors.<br>See https://www.rabbitmq.com/docs/alarms#file-descriptors.<br>" | "RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}` file descriptor alarm active. Publishers are blocked.<br>" |
| **TCPSocketsNearLimit** | "More than 80% of TCP sockets are open on the RabbitMQ node.<br>When this value reaches 100%, new connections will not be accepted.<br>Client libraries, peer nodes and CLI tools will not be able to connect when the node runs out of available TCP sockets.<br>See https://www.rabbitmq.com/networking.html.<br>" | "`{{ $value \| humanizePercentage }}` TCP sockets of TCP socket<br>limit are open in RabbitMQ node `{{ $labels.rabbitmq_node }}`, pod `{{ $labels.pod }}`,<br>RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}`, namespace `{{ $labels.namespace }}`.<br>" |
| **UnroutableMessages** | "There are messages published into an exchange which cannot be routed and are either dropped silently, or returned to publishers.<br>Is your routing topology set up correctly?<br>Check your application code and bindings between exchanges and queues.<br>See<br>https://www.rabbitmq.com/publishers.html#unroutable,<br>https://www.rabbitmq.com/confirms.html#when-publishes-are-confirmed.<br>" | "There were `{{ $value \| printf "%.0f" }}` unroutable messages within the last<br>5 minutes in RabbitMQ cluster `{{ $labels.rabbitmq_cluster }}` in namespace<br>`{{ $labels.namespace }}`.<br>" |
<p align="right"><a href="#top">🔝 Back to Top</a></p>

---

