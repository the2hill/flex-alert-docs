- [Blackbox Alerts](#blackbox-alerts) 
- [Compute Resource Alerts](#compute-resource-alerts) 
- [Image Resource Alerts](#image-resource-alerts) 
- [Linux MDM device and RAID alerts](#linux-mdm-device-and-raid-alerts) 
- [MariaDB backup alerts](#mariadb-backup-alerts) 
- [Multipath path checker alerts](#multipath-path-checker-alerts) 
- [Mysql Alerts](#mysql-alerts) 
- [OVN backup alerts](#ovn-backup-alerts) 
- [Octavia Resource Alerts](#octavia-resource-alerts) 
- [Volume Alerts](#volume-alerts) 
- [alertmanager.rules](#alertmanager.rules) 
- [config-reloaders](#config-reloaders) 
- [etcd](#etcd) 
- [fluentbit serviceMonitor alert](#fluentbit-servicemonitor-alert) 
- [general.rules](#general.rules) 
- [kube-apiserver-slos](#kube-apiserver-slos) 
- [kube-state-metrics](#kube-state-metrics) 
- [kubernetes-apps](#kubernetes-apps) 
- [kubernetes-resources](#kubernetes-resources) 
- [kubernetes-storage](#kubernetes-storage) 
- [kubernetes-system](#kubernetes-system) 
- [kubernetes-system-apiserver](#kubernetes-system-apiserver) 
- [kubernetes-system-controller-manager](#kubernetes-system-controller-manager) 
- [kubernetes-system-kube-proxy](#kubernetes-system-kube-proxy) 
- [kubernetes-system-kubelet](#kubernetes-system-kubelet) 
- [kubernetes-system-scheduler](#kubernetes-system-scheduler) 
- [mariadb-alerts](#mariadb-alerts) 
- [node-exporter](#node-exporter) 
- [node-network](#node-network) 
- [pod-state-alerts](#pod-state-alerts) 
- [prometheus](#prometheus) 
- [prometheus-operator](#prometheus-operator) 
- [rabbitmq](#rabbitmq) 

---

## Blackbox Alerts

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **Service Down** | Service probe has failed for more than two minutes on (instance { $labels.instance }) | Service probe has failed for more than two minutes. LABELS = { $labels }  | critical |
| **TLS certificate expiring** | SSL certificate will expire soon on (instance { $labels.instance }) | SSL certificate expires within 30 days. VALUE = { $value } LABELS = { $labels }  | warning |
| **TLS certificate expiring** | SSL certificate will expire soon on (instance { $labels.instance }) | SSL certificate expires within 15 days. VALUE = { $value } LABELS = { $labels }  | critical |
---

## Compute Resource Alerts

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **AbnormalInstanceFailures** | Instance build failure rate is abnormally high | This indicates a major problem building compute instances. View logs and take action to resolve the build failures.  | critical |
| **InstancesStuckInFailureState** | Instances stuck in failure state for a prolonged period | There are instances stuck in a building or error state for a prolonged period that need to be cleaned up.  | warning |
---

## Image Resource Alerts

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **AbnormalImageFailures** | Image create failure rate is abnormally high | This indicates a major problem creating images. View logs and take action to resolve the build failures.  | critical |
| **ImagesStuckInFailureState** | Images stuck in failure state for a prolonged period | There are images stuck in a failure state for a prolonged period that need to be cleaned up.  | warning |
---

## Linux MDM device and RAID alerts

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **NodeMdInfoFailedDeviceCritical** | NVME device on Linux software RAID failure info | { $labels.name } Number MD Failed:{ $labels.FailedDevices } LABELS: { $labels } | critical |
| **NodeMdInfoStateCritical** | Linux software MD RAID State is NOT active or clean | { $labels.name } State:{ $labels.State } LABELS: { $labels } | critical |
| **NodeMdInfoSuperblockPersistenceCritical** | Linux software MD Superblock is NOT persistent | { $labels.name } Persistence:{ $labels.Persistence } LABELS: { $labels } | critical |
| **NodeMdStateCritical** | Linux MDM RAID State is { $labels.state } | { $labels.name } MD RAID status:{ $value } MD RAID device:{ $labels.device } LABELS: { $labels } | critical |
---

## MariaDB backup alerts

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **mariadbBackupCritical** | Second successive MariaDB backup not successful within 1 hour of scheduled run | Second successive MariaDB backup not successful within 1 hour of scheduled run.  | critical |
| **mariadbBackupWarning** | Last MariaDB backup not successful within 1 hour of scheduled run | Last MariaDB backup not successful within 1 hour of scheduled run.  | warning |
---

## Multipath path checker alerts

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **NodeDmpathInfoMultipathCritical** | Multipathd paths are NOT active or ready and paths are likely orphaned | { $labels.name } labels: { $labels } | critical |
---

## Mysql Alerts

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **MysqlDown** | MariaDB down (instance { $labels.instance }) | MariaDB instance is down on { $labels.instance } VALUE = { $value } LABELS = { $labels }  | critical |
| **MysqlRestarted** | MySQL restarted (instance { $labels.instance }) | MySQL has just been restarted, less than one minute ago on { $labels.instance }. VALUE = { $value } LABELS = { $labels }  | info |
| **MysqlSlowQueries** | MySQL slow queries (instance { $labels.instance }) | MySQL server has some new slow queries. VALUE = { $value } LABELS = { $labels }  | warning |
| **MysqlTooManyConnections(>80%)** | Database too many connections (> 90%) (instance { $labels.instance }) | More than 90% of MySQL connections are in use on { $labels.instance } VALUE = { $value } LABELS = { $labels }  | warning |
---

## OVN backup alerts

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **ovnBackupDiskUsageCritical** | OVN backup volume >= 90% disk usage | OVN backup volume >= 90% disk usage.  | critical |
| **ovnBackupDiskUsageWarning** | OVN backup volume >= 80% disk usage | OVN backup volume >= 80% disk usage.  | warning |
| **ovnBackupUploadCritical** | Second successive OVN backup not uploaded within 1 hour of scheduled run | Second successive OVN backup not uploaded within 1 hour of scheduled run.  | critical |
| **ovnBackupUploadWarning** | Last OVN backup not uploaded within 1 hour of scheduled run | Last OVN backup not uploaded within 1 hour of scheduled run.  | warning |
---

## Octavia Resource Alerts

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **LoadbalancersInError** | Loadbalancer stuck in error state for a prolonged period | This may indicate a potential problem with failover and/or health manager services. This could also indicate other problems building load balancers in general.  | critical |
---

## Volume Alerts

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **KubernetesVolumeOutOfDiskSpace** | Kubernetes Volume out of disk space (instance { $labels.instance }) | Volume is almost full (< 20% left). VALUE = { $value } LABELS = { $labels }  | warning |
---

## alertmanager.rules

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **AlertmanagerClusterCrashlooping** | Half or more of the Alertmanager instances within the same cluster are crashlooping. | { $value  or  humanizePercentage } of Alertmanager instances within the {$labels.job} cluster have restarted at least 5 times in the last 10m. | critical |
| **AlertmanagerClusterDown** | Half or more of the Alertmanager instances within the same cluster are down. | { $value  or  humanizePercentage } of Alertmanager instances within the {$labels.job} cluster have been up for less than half of the last 5m. | critical |
| **AlertmanagerClusterFailedToSendAlerts** | All Alertmanager instances in a cluster failed to send notifications to a critical integration. | The minimum notification failure rate to { $labels.integration } sent from any instance in the {$labels.job} cluster is { $value  or  humanizePercentage }. | critical |
| **AlertmanagerClusterFailedToSendAlerts** | All Alertmanager instances in a cluster failed to send notifications to a non-critical integration. | The minimum notification failure rate to { $labels.integration } sent from any instance in the {$labels.job} cluster is { $value  or  humanizePercentage }. | warning |
| **AlertmanagerConfigInconsistent** | Alertmanager instances within the same cluster have different configurations. | Alertmanager instances within the {$labels.job} cluster have different configurations. | critical |
| **AlertmanagerFailedReload** | Reloading an Alertmanager configuration has failed. | Configuration has failed to load for { $labels.namespace }/{ $labels.pod}. | critical |
| **AlertmanagerFailedToSendAlerts** | An Alertmanager instance failed to send notifications. | Alertmanager { $labels.namespace }/{ $labels.pod} failed to send { $value  or  humanizePercentage } of notifications to { $labels.integration }. | warning |
| **AlertmanagerMembersInconsistent** | A member of an Alertmanager cluster has not found all other cluster members. | Alertmanager { $labels.namespace }/{ $labels.pod} has only found { $value } members of the {$labels.job} cluster. | critical |
---

## config-reloaders

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **ConfigReloaderSidecarErrors** | config-reloader sidecar has not had a successful reload for 10m | Errors encountered while the {$labels.pod} config-reloader sidecar attempts to sync config in {$labels.namespace} namespace. As a result, configuration for service running in {$labels.pod} may be stale and cannot be updated anymore. | warning |
---

## etcd

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **etcdDatabaseHighFragmentationRatio** | etcd database size in use is less than 50% of the actual allocated storage. | etcd cluster "{ $labels.job }": database size in use on instance { $labels.instance } is { $value  or  humanizePercentage } of the actual allocated disk space, please run defragmentation (e.g. etcdctl defrag) to retrieve the unused fragmented disk space. | warning |
| **etcdDatabaseQuotaLowSpace** | etcd cluster database is running full. | etcd cluster "{ $labels.job }": database size exceeds the defined quota on etcd instance { $labels.instance }, please defrag or increase the quota as the writes to etcd will be disabled when it is full. | critical |
| **etcdExcessiveDatabaseGrowth** | etcd cluster database growing very fast. | etcd cluster "{ $labels.job }": Predicting running out of disk space in the next four hours, based on write observations within the past four hours on etcd instance { $labels.instance }, please check as it might be disruptive. | warning |
| **etcdGRPCRequestsSlow** | etcd grpc requests are slow | etcd cluster "{ $labels.job }": 99th percentile of gRPC requests is { $value }s on etcd instance { $labels.instance } for { $labels.grpc_method } method. | critical |
| **etcdHighCommitDurations** | etcd cluster 99th percentile commit durations are too high. | etcd cluster "{ $labels.job }": 99th percentile commit durations { $value }s on etcd instance { $labels.instance }. | warning |
| **etcdHighFsyncDurations** | etcd cluster 99th percentile fsync durations are too high. | etcd cluster "{ $labels.job }": 99th percentile fsync durations are { $value }s on etcd instance { $labels.instance }. | warning |
| **etcdHighFsyncDurations** | etcd cluster 99th percentile fsync durations are too high. | etcd cluster "{ $labels.job }": 99th percentile fsync durations are { $value }s on etcd instance { $labels.instance }. | critical |
| **etcdHighNumberOfFailedGRPCRequests** | etcd cluster has high number of failed grpc requests. | etcd cluster "{ $labels.job }": { $value }% of requests for { $labels.grpc_method } failed on etcd instance { $labels.instance }. | warning |
| **etcdHighNumberOfFailedGRPCRequests** | etcd cluster has high number of failed grpc requests. | etcd cluster "{ $labels.job }": { $value }% of requests for { $labels.grpc_method } failed on etcd instance { $labels.instance }. | critical |
| **etcdHighNumberOfFailedProposals** | etcd cluster has high number of proposal failures. | etcd cluster "{ $labels.job }": { $value } proposal failures within the last 30 minutes on etcd instance { $labels.instance }. | warning |
| **etcdHighNumberOfLeaderChanges** | etcd cluster has high number of leader changes. | etcd cluster "{ $labels.job }": { $value } leader changes within the last 15 minutes. Frequent elections may be a sign of insufficient resources, high network latency, or disruptions by other components and should be investigated. | warning |
| **etcdInsufficientMembers** | etcd cluster has insufficient number of members. | etcd cluster "{ $labels.job }": insufficient members ({ $value }). | critical |
| **etcdMemberCommunicationSlow** | etcd cluster member communication is slow. | etcd cluster "{ $labels.job }": member communication with { $labels.To } is taking { $value }s on etcd instance { $labels.instance }. | warning |
| **etcdMembersDown** | etcd cluster members are down. | etcd cluster "{ $labels.job }": members are down ({ $value }). | warning |
| **etcdNoLeader** | etcd cluster has no leader. | etcd cluster "{ $labels.job }": member { $labels.instance } has no leader. | critical |
---

## fluentbit serviceMonitor alert

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **MissingFluentbitServiceMonitor** | ServiceMonitor 'fluentbit-fluent-bit' is either down or missing. | Check if the Fluentbit ServiceMonitor is properly configured and deployed.  | critical |
---

## general.rules

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **InfoInhibitor** | Info-level alert inhibition. | This is an alert that is used to inhibit info alerts. By themselves, the info-level alerts are sometimes very noisy, but they are relevant when combined with other alerts. This alert fires whenever there's a severity="info" alert, and stops firing when another alert with a severity of 'warning' or 'critical' starts firing on the same namespace. This alert should be routed to a null receiver and configured to inhibit alerts with severity="info".  | none |
| **TargetDown** | One or more targets are unreachable. | { printf "%.4g" $value }% of the { $labels.job }/{ $labels.service } targets in { $labels.namespace } namespace are down. | warning |
| **Watchdog** | An alert that should always be firing to certify that Alertmanager is working properly. | This is an alert meant to ensure that the entire alerting pipeline is functional. This alert is always firing, therefore it should always be firing in Alertmanager and always fire against a receiver. There are integrations with various notification mechanisms that send a notification when this alert is not firing. For example the "DeadMansSnitch" integration in PagerDuty.  | none |
---

## kube-apiserver-slos

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **KubeAPIErrorBudgetBurn** | The API server is burning too much error budget. | The API server is burning too much error budget on cluster { $labels.cluster }. | critical |
| **KubeAPIErrorBudgetBurn** | The API server is burning too much error budget. | The API server is burning too much error budget on cluster { $labels.cluster }. | critical |
| **KubeAPIErrorBudgetBurn** | The API server is burning too much error budget. | The API server is burning too much error budget on cluster { $labels.cluster }. | warning |
| **KubeAPIErrorBudgetBurn** | The API server is burning too much error budget. | The API server is burning too much error budget on cluster { $labels.cluster }. | warning |
---

## kube-state-metrics

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **KubeStateMetricsListErrors** | kube-state-metrics is experiencing errors in list operations. | kube-state-metrics is experiencing errors at an elevated rate in list operations. This is likely causing it to not be able to expose metrics about Kubernetes objects correctly or at all. | critical |
| **KubeStateMetricsShardingMismatch** | kube-state-metrics sharding is misconfigured. | kube-state-metrics pods are running with different --total-shards configuration, some Kubernetes objects may be exposed multiple times or not exposed at all. | critical |
| **KubeStateMetricsShardsMissing** | kube-state-metrics shards are missing. | kube-state-metrics shards are missing, some Kubernetes objects are not being exposed. | critical |
| **KubeStateMetricsWatchErrors** | kube-state-metrics is experiencing errors in watch operations. | kube-state-metrics is experiencing errors at an elevated rate in watch operations. This is likely causing it to not be able to expose metrics about Kubernetes objects correctly or at all. | critical |
---

## kubernetes-apps

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **KubeContainerWaiting** | Pod container waiting longer than 1 hour | pod/{ $labels.pod } in namespace { $labels.namespace } on container { $labels.container} has been in waiting state for longer than 1 hour. (reason: "{ $labels.reason }") on cluster { $labels.cluster }. | warning |
| **KubeDaemonSetMisScheduled** | DaemonSet pods are misscheduled. | { $value } Pods of DaemonSet { $labels.namespace }/{ $labels.daemonset } are running where they are not supposed to run on cluster { $labels.cluster }. | warning |
| **KubeDaemonSetNotScheduled** | DaemonSet pods are not scheduled. | { $value } Pods of DaemonSet { $labels.namespace }/{ $labels.daemonset } are not scheduled on cluster { $labels.cluster }. | warning |
| **KubeDaemonSetRolloutStuck** | DaemonSet rollout is stuck. | DaemonSet { $labels.namespace }/{ $labels.daemonset } has not finished or progressed for at least 15m on cluster { $labels.cluster }. | warning |
| **KubeDeploymentGenerationMismatch** | Deployment generation mismatch due to possible roll-back | Deployment generation for { $labels.namespace }/{ $labels.deployment } does not match, this indicates that the Deployment has failed but has not been rolled back on cluster { $labels.cluster }. | warning |
| **KubeDeploymentReplicasMismatch** | Deployment has not matched the expected number of replicas. | Deployment { $labels.namespace }/{ $labels.deployment } has not matched the expected number of replicas for longer than 15 minutes on cluster { $labels.cluster }. | warning |
| **KubeDeploymentRolloutStuck** | Deployment rollout is not progressing. | Rollout of deployment { $labels.namespace }/{ $labels.deployment } is not progressing for longer than 15 minutes on cluster { $labels.cluster }. | warning |
| **KubeHpaMaxedOut** | HPA is running at max replicas | HPA { $labels.namespace }/{ $labels.horizontalpodautoscaler  } has been running at max replicas for longer than 15 minutes on cluster { $labels.cluster }. | warning |
| **KubeHpaReplicasMismatch** | HPA has not matched desired number of replicas. | HPA { $labels.namespace }/{ $labels.horizontalpodautoscaler  } has not matched the desired number of replicas for longer than 15 minutes on cluster { $labels.cluster }. | warning |
| **KubeJobFailed** | Job failed to complete. | Job { $labels.namespace }/{ $labels.job_name } failed to complete. Removing failed job after investigation should clear this alert on cluster { $labels.cluster }. | warning |
| **KubeJobNotCompleted** | Job did not complete in time | Job { $labels.namespace }/{ $labels.job_name } is taking more than { "43200"  or  humanizeDuration } to complete on cluster { $labels.cluster }. | warning |
| **KubePodCrashLooping** | Pod is crash looping. | Pod { $labels.namespace }/{ $labels.pod } ({ $labels.container }) is in waiting state (reason: "CrashLoopBackOff") on cluster { $labels.cluster }. | warning |
| **KubePodNotReady** | Pod has been in a non-ready state for more than 15 minutes. | Pod { $labels.namespace }/{ $labels.pod } has been in a non-ready state for longer than 15 minutes on cluster { $labels.cluster }. | warning |
| **KubeStatefulSetGenerationMismatch** | StatefulSet generation mismatch due to possible roll-back | StatefulSet generation for { $labels.namespace }/{ $labels.statefulset } does not match, this indicates that the StatefulSet has failed but has not been rolled back on cluster { $labels.cluster }. | warning |
| **KubeStatefulSetReplicasMismatch** | StatefulSet has not matched the expected number of replicas. | StatefulSet { $labels.namespace }/{ $labels.statefulset } has not matched the expected number of replicas for longer than 15 minutes on cluster { $labels.cluster }. | warning |
| **KubeStatefulSetUpdateNotRolledOut** | StatefulSet update has not been rolled out. | StatefulSet { $labels.namespace }/{ $labels.statefulset } update has not been rolled out on cluster { $labels.cluster }. | warning |
---

## kubernetes-resources

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **CPUThrottlingHigh** | Processes experience elevated CPU throttling. | { $value  or  humanizePercentage } throttling of CPU in namespace { $labels.namespace } for container { $labels.container } in pod { $labels.pod } on cluster { $labels.cluster }. | info |
| **KubeCPUOvercommit** | Cluster has overcommitted CPU resource requests. | Cluster { $labels.cluster } has overcommitted CPU resource requests for Pods by { $value } CPU shares and cannot tolerate node failure. | warning |
| **KubeCPUQuotaOvercommit** | Cluster has overcommitted CPU resource requests. | Cluster { $labels.cluster }  has overcommitted CPU resource requests for Namespaces. | warning |
| **KubeMemoryOvercommit** | Cluster has overcommitted memory resource requests. | Cluster { $labels.cluster } has overcommitted memory resource requests for Pods by { $value  or  humanize } bytes and cannot tolerate node failure. | warning |
| **KubeMemoryQuotaOvercommit** | Cluster has overcommitted memory resource requests. | Cluster { $labels.cluster }  has overcommitted memory resource requests for Namespaces. | warning |
| **KubeQuotaAlmostFull** | Namespace quota is going to be full. | Namespace { $labels.namespace } is using { $value  or  humanizePercentage } of its { $labels.resource } quota on cluster { $labels.cluster }. | info |
| **KubeQuotaExceeded** | Namespace quota has exceeded the limits. | Namespace { $labels.namespace } is using { $value  or  humanizePercentage } of its { $labels.resource } quota on cluster { $labels.cluster }. | warning |
| **KubeQuotaFullyUsed** | Namespace quota is fully used. | Namespace { $labels.namespace } is using { $value  or  humanizePercentage } of its { $labels.resource } quota on cluster { $labels.cluster }. | info |
---

## kubernetes-storage

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **KubePersistentVolumeErrors** | PersistentVolume is having issues with provisioning. | The persistent volume { $labels.persistentvolume } { with $labels.cluster -} on Cluster { . } {- end } has status { $labels.phase }. | critical |
| **KubePersistentVolumeFillingUp** | PersistentVolume is filling up. | The PersistentVolume claimed by { $labels.persistentvolumeclaim } in Namespace { $labels.namespace } { with $labels.cluster -} on Cluster { . } {- end } is only { $value  or  humanizePercentage } free. | critical |
| **KubePersistentVolumeFillingUp** | PersistentVolume is filling up. | Based on recent sampling, the PersistentVolume claimed by { $labels.persistentvolumeclaim } in Namespace { $labels.namespace } { with $labels.cluster -} on Cluster { . } {- end } is expected to fill up within four days. Currently { $value  or  humanizePercentage } is available. | warning |
| **KubePersistentVolumeInodesFillingUp** | PersistentVolumeInodes are filling up. | The PersistentVolume claimed by { $labels.persistentvolumeclaim } in Namespace { $labels.namespace } { with $labels.cluster -} on Cluster { . } {- end } only has { $value  or  humanizePercentage } free inodes. | critical |
| **KubePersistentVolumeInodesFillingUp** | PersistentVolumeInodes are filling up. | Based on recent sampling, the PersistentVolume claimed by { $labels.persistentvolumeclaim } in Namespace { $labels.namespace } { with $labels.cluster -} on Cluster { . } {- end } is expected to run out of inodes within four days. Currently { $value  or  humanizePercentage } of its inodes are free. | warning |
---

## kubernetes-system

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **KubeClientErrors** | Kubernetes API server client is experiencing errors. | Kubernetes API server client '{ $labels.job }/{ $labels.instance }' is experiencing { $value  or  humanizePercentage } errors on cluster { $labels.cluster }. | warning |
| **KubeVersionMismatch** | Different semantic versions of Kubernetes components running. | There are { $value } different semantic versions of Kubernetes components running on cluster { $labels.cluster }. | warning |
---

## kubernetes-system-apiserver

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **KubeAPIDown** | Target disappeared from Prometheus target discovery. | KubeAPI has disappeared from Prometheus target discovery. | critical |
| **KubeAPITerminatedRequests** | The kubernetes apiserver has terminated { $value  or  humanizePercentage } of its incoming requests. | The kubernetes apiserver has terminated { $value  or  humanizePercentage } of its incoming requests on cluster { $labels.cluster }. | warning |
| **KubeAggregatedAPIDown** | Kubernetes aggregated API is down. | Kubernetes aggregated API { $labels.name }/{ $labels.namespace } has been only { $value  or  humanize }% available over the last 10m on cluster { $labels.cluster }. | warning |
| **KubeAggregatedAPIErrors** | Kubernetes aggregated API has reported errors. | Kubernetes aggregated API { $labels.instance }/{ $labels.name } has reported { $labels.reason } errors on cluster { $labels.cluster }. | warning |
| **KubeClientCertificateExpiration** | Client certificate is about to expire. | A client certificate used to authenticate to kubernetes apiserver is expiring in less than 7.0 days on cluster { $labels.cluster }. | warning |
| **KubeClientCertificateExpiration** | Client certificate is about to expire. | A client certificate used to authenticate to kubernetes apiserver is expiring in less than 24.0 hours on cluster { $labels.cluster }. | critical |
---

## kubernetes-system-controller-manager

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **KubeControllerManagerDown** | Target disappeared from Prometheus target discovery. | KubeControllerManager has disappeared from Prometheus target discovery. | critical |
---

## kubernetes-system-kube-proxy

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **KubeProxyDown** | Target disappeared from Prometheus target discovery. | KubeProxy has disappeared from Prometheus target discovery. | critical |
---

## kubernetes-system-kubelet

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **KubeNodeEviction** | Node is evicting pods. | Node { $labels.node } on { $labels.cluster } is evicting Pods due to { $labels.eviction_signal }.  Eviction occurs when eviction thresholds are crossed, typically caused by Pods exceeding RAM/ephemeral-storage limits. | info |
| **KubeNodeNotReady** | Node is not ready. | { $labels.node } has been unready for more than 15 minutes on cluster { $labels.cluster }. | warning |
| **KubeNodePressure** | Node has as active Condition. | { $labels.node } on cluster { $labels.cluster } has active Condition { $labels.condition }. This is caused by resource usage exceeding eviction thresholds. | info |
| **KubeNodeReadinessFlapping** | Node readiness status is flapping. | The readiness status of node { $labels.node } has changed { $value } times in the last 15 minutes on cluster { $labels.cluster }. | warning |
| **KubeNodeUnreachable** | Node is unreachable. | { $labels.node } is unreachable and some workloads may be rescheduled on cluster { $labels.cluster }. | warning |
| **KubeletClientCertificateExpiration** | Kubelet client certificate is about to expire. | Client certificate for Kubelet on node { $labels.node } expires in { $value  or  humanizeDuration } on cluster { $labels.cluster }. | warning |
| **KubeletClientCertificateExpiration** | Kubelet client certificate is about to expire. | Client certificate for Kubelet on node { $labels.node } expires in { $value  or  humanizeDuration } on cluster { $labels.cluster }. | critical |
| **KubeletClientCertificateRenewalErrors** | Kubelet has failed to renew its client certificate. | Kubelet on node { $labels.node } has failed to renew its client certificate ({ $value  or  humanize } errors in the last 5 minutes) on cluster { $labels.cluster }. | warning |
| **KubeletDown** | Target disappeared from Prometheus target discovery. | Kubelet has disappeared from Prometheus target discovery. | critical |
| **KubeletPlegDurationHigh** | Kubelet Pod Lifecycle Event Generator is taking too long to relist. | The Kubelet Pod Lifecycle Event Generator has a 99th percentile duration of { $value } seconds on node { $labels.node } on cluster { $labels.cluster }. | warning |
| **KubeletPodStartUpLatencyHigh** | Kubelet Pod startup latency is too high. | Kubelet Pod startup 99th percentile latency is { $value } seconds on node { $labels.node } on cluster { $labels.cluster }. | warning |
| **KubeletServerCertificateExpiration** | Kubelet server certificate is about to expire. | Server certificate for Kubelet on node { $labels.node } expires in { $value  or  humanizeDuration } on cluster { $labels.cluster }. | warning |
| **KubeletServerCertificateExpiration** | Kubelet server certificate is about to expire. | Server certificate for Kubelet on node { $labels.node } expires in { $value  or  humanizeDuration } on cluster { $labels.cluster }. | critical |
| **KubeletServerCertificateRenewalErrors** | Kubelet has failed to renew its server certificate. | Kubelet on node { $labels.node } has failed to renew its server certificate ({ $value  or  humanize } errors in the last 5 minutes) on cluster { $labels.cluster }. | warning |
| **KubeletTooManyPods** | Kubelet is running at capacity. | Kubelet '{ $labels.node }' is running at { $value  or  humanizePercentage } of its Pod capacity on cluster { $labels.cluster }. | info |
---

## kubernetes-system-scheduler

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **KubeSchedulerDown** | Target disappeared from Prometheus target discovery. | KubeScheduler has disappeared from Prometheus target discovery. | critical |
---

## mariadb-alerts

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **MariaDBDown** | MariaDB not up and running, immediate attention is required. | MariaDB {$labels.job} on {$labels.instance} is not up. | critical |
| **MariaDBReplicationErrors** | MariaDB is reporting replication errors from {$labels.instance}, immediate attention is required. | MariaDB {$labels.job} on {$labels.instance} is reporting replication errors. | critical |
| **MysqlSlaveReplicationLag** | MySQL Slave replication lag (instance { $labels.instance }) | MySQL replication lag on { $labels.instance }   VALUE = { $value }   LABELS = { $labels } | critical |
| **MysqlTooManyConnections(>80%)** | MySQL too many connections (> 80%) (instance { $labels.instance }) | More than 80% of MySQL connections are in use on { $labels.instance }   VALUE = { $value }   LABELS = { $labels } | warning |
---

## node-exporter

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **NodeBondingDegraded** | Bonding interface is degraded | Bonding interface { $labels.master } on { $labels.instance } is in degraded state due to one or more slave failures. | warning |
| **NodeCPUHighUsage** | High CPU usage. | CPU usage at { $labels.instance } has been above 90% for the last 15 minutes, is currently at { printf "%.2f" $value }%.  | info |
| **NodeClockNotSynchronising** | Clock not synchronising. | Clock at { $labels.instance } is not synchronising. Ensure NTP is configured on this host. | warning |
| **NodeClockSkewDetected** | Clock skew detected. | Clock at { $labels.instance } is out of sync by more than 0.05s. Ensure NTP is configured correctly on this host. | warning |
| **NodeDiskIOSaturation** | Disk IO queue is high. | Disk IO queue (aqu-sq) is high on { $labels.device } at { $labels.instance }, has been above 10 for the last 30 minutes, is currently at { printf "%.2f" $value }. This symptom might indicate disk saturation.  | warning |
| **NodeFileDescriptorLimit** | Kernel is predicted to exhaust file descriptors limit soon. | File descriptors limit at { $labels.instance } is currently at { printf "%.2f" $value }%. | warning |
| **NodeFileDescriptorLimit** | Kernel is predicted to exhaust file descriptors limit soon. | File descriptors limit at { $labels.instance } is currently at { printf "%.2f" $value }%. | critical |
| **NodeFilesystemAlmostOutOfFiles** | Filesystem has less than 5% inodes left. | Filesystem on { $labels.device }, mounted on { $labels.mountpoint }, at { $labels.instance } has only { printf "%.2f" $value }% available inodes left. | warning |
| **NodeFilesystemAlmostOutOfFiles** | Filesystem has less than 3% inodes left. | Filesystem on { $labels.device }, mounted on { $labels.mountpoint }, at { $labels.instance } has only { printf "%.2f" $value }% available inodes left. | critical |
| **NodeFilesystemAlmostOutOfSpace** | Filesystem has less than 5% space left. | Filesystem on { $labels.device }, mounted on { $labels.mountpoint }, at { $labels.instance } has only { printf "%.2f" $value }% available space left. | warning |
| **NodeFilesystemAlmostOutOfSpace** | Filesystem has less than 3% space left. | Filesystem on { $labels.device }, mounted on { $labels.mountpoint }, at { $labels.instance } has only { printf "%.2f" $value }% available space left. | critical |
| **NodeFilesystemFilesFillingUp** | Filesystem is predicted to run out of inodes within the next 24 hours. | Filesystem on { $labels.device }, mounted on { $labels.mountpoint }, at { $labels.instance } has only { printf "%.2f" $value }% available inodes left and is filling up. | warning |
| **NodeFilesystemFilesFillingUp** | Filesystem is predicted to run out of inodes within the next 4 hours. | Filesystem on { $labels.device }, mounted on { $labels.mountpoint }, at { $labels.instance } has only { printf "%.2f" $value }% available inodes left and is filling up fast. | critical |
| **NodeFilesystemSpaceFillingUp** | Filesystem is predicted to run out of space within the next 24 hours. | Filesystem on { $labels.device }, mounted on { $labels.mountpoint }, at { $labels.instance } has only { printf "%.2f" $value }% available space left and is filling up. | warning |
| **NodeFilesystemSpaceFillingUp** | Filesystem is predicted to run out of space within the next 4 hours. | Filesystem on { $labels.device }, mounted on { $labels.mountpoint }, at { $labels.instance } has only { printf "%.2f" $value }% available space left and is filling up fast. | critical |
| **NodeHighNumberConntrackEntriesUsed** | Number of conntrack are getting close to the limit. | { $labels.instance } { $value  or  humanizePercentage } of conntrack entries are used. | warning |
| **NodeMemoryHighUtilization** | Host is running out of memory. | Memory is filling up at { $labels.instance }, has been above 90% for the last 15 minutes, is currently at { printf "%.2f" $value }%.  | warning |
| **NodeMemoryMajorPagesFaults** | Memory major page faults are occurring at very high rate. | Memory major pages are occurring at very high rate at { $labels.instance }, 500 major page faults per second for the last 15 minutes, is currently at { printf "%.2f" $value }. Please check that there is enough memory available at this instance.  | warning |
| **NodeNetworkReceiveErrs** | Network interface is reporting many receive errors. | { $labels.instance } interface { $labels.device } has encountered { printf "%.0f" $value } receive errors in the last two minutes. | warning |
| **NodeNetworkTransmitErrs** | Network interface is reporting many transmit errors. | { $labels.instance } interface { $labels.device } has encountered { printf "%.0f" $value } transmit errors in the last two minutes. | warning |
| **NodeRAIDDegraded** | RAID Array is degraded. | RAID array '{ $labels.device }' at { $labels.instance } is in degraded state due to one or more disks failures. Number of spare drives is insufficient to fix issue automatically. | critical |
| **NodeRAIDDiskFailure** | Failed device in RAID array. | At least one device in RAID array at { $labels.instance } failed. Array '{ $labels.device }' needs attention and possibly a disk swap. | warning |
| **NodeSystemSaturation** | System saturated, load per core is very high. | System load per core at { $labels.instance } has been above 2 for the last 15 minutes, is currently at { printf "%.2f" $value }. This might indicate this instance resources saturation and can cause it becoming unresponsive.  | warning |
| **NodeSystemdServiceCrashlooping** | Systemd service keeps restaring, possibly crash looping. | Systemd service { $labels.name } has being restarted too many times at { $labels.instance } for the last 15 minutes. Please check if service is crash looping. | warning |
| **NodeSystemdServiceFailed** | Systemd service has entered failed state. | Systemd service { $labels.name } has entered failed state at { $labels.instance } | warning |
| **NodeTextFileCollectorScrapeError** | Node Exporter text file collector failed to scrape. | Node Exporter text file collector on { $labels.instance } failed to scrape. | warning |
---

## node-network

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **NodeNetworkInterfaceFlapping** | Network interface is often changing its status | Network interface "{ $labels.device }" changing its up status often on node-exporter { $labels.namespace }/{ $labels.pod } | warning |
---

## pod-state-alerts

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **HighPodRestartRate** | High pod restart count detected | Pod { $labels.pod } in namespace { $labels.namespace } is restarting frequently, which may indicate network instability. | warning |
| **KubePodNotReadyCritical** | Pod has been in a non-ready state for more than 5 minutes. | Pod { $labels.namespace }/{ $labels.pod } has been in a non-ready state for longer than 5 minutes. | critical |
| **TooManyContainerRestarts** | Container named { $labels.container } in { $labels.pod } in { $labels.namespace } has restarted too many times in a short period and needs to be investigated. | Namespace: {$labels.namespace} Pod name: {$labels.pod} Container name: {$labels.container}  | critical |
---

## prometheus

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **PrometheusBadConfig** | Failed Prometheus configuration reload. | Prometheus {$labels.namespace}/{$labels.pod} has failed to reload its configuration. | critical |
| **PrometheusDuplicateTimestamps** | Prometheus is dropping samples with duplicate timestamps. | Prometheus {$labels.namespace}/{$labels.pod} is dropping { printf "%.4g" $value  } samples/s with different values but duplicated timestamp. | warning |
| **PrometheusErrorSendingAlertsToAnyAlertmanager** | Prometheus encounters more than 3% errors sending alerts to any Alertmanager. | { printf "%.1f" $value }% minimum errors while sending alerts from Prometheus {$labels.namespace}/{$labels.pod} to any Alertmanager. | critical |
| **PrometheusErrorSendingAlertsToSomeAlertmanagers** | More than 1% of alerts sent by Prometheus to a specific Alertmanager were affected by errors. | { printf "%.1f" $value }% of alerts sent by Prometheus {$labels.namespace}/{$labels.pod} to Alertmanager {$labels.alertmanager} were affected by errors. | warning |
| **PrometheusHighQueryLoad** | Prometheus is reaching its maximum capacity serving concurrent requests. | Prometheus {$labels.namespace}/{$labels.pod} query API has less than 20% available capacity in its query engine for the last 15 minutes. | warning |
| **PrometheusKubernetesListWatchFailures** | Requests in Kubernetes SD are failing. | Kubernetes service discovery of Prometheus {$labels.namespace}/{$labels.pod} is experiencing { printf "%.0f" $value } failures with LIST/WATCH requests to the Kubernetes API in the last 5 minutes. | warning |
| **PrometheusLabelLimitHit** | Prometheus has dropped targets because some scrape configs have exceeded the labels limit. | Prometheus {$labels.namespace}/{$labels.pod} has dropped { printf "%.0f" $value } targets because some samples exceeded the configured label_limit, label_name_length_limit or label_value_length_limit. | warning |
| **PrometheusMissingRuleEvaluations** | Prometheus is missing rule evaluations due to slow rule group evaluation. | Prometheus {$labels.namespace}/{$labels.pod} has missed { printf "%.0f" $value } rule group evaluations in the last 5m. | warning |
| **PrometheusNotConnectedToAlertmanagers** | Prometheus is not connected to any Alertmanagers. | Prometheus {$labels.namespace}/{$labels.pod} is not connected to any Alertmanagers. | warning |
| **PrometheusNotIngestingSamples** | Prometheus is not ingesting samples. | Prometheus {$labels.namespace}/{$labels.pod} is not ingesting samples. | warning |
| **PrometheusNotificationQueueRunningFull** | Prometheus alert notification queue predicted to run full in less than 30m. | Alert notification queue of Prometheus {$labels.namespace}/{$labels.pod} is running full. | warning |
| **PrometheusOutOfOrderTimestamps** | Prometheus drops samples with out-of-order timestamps. | Prometheus {$labels.namespace}/{$labels.pod} is dropping { printf "%.4g" $value  } samples/s with timestamps arriving out of order. | warning |
| **PrometheusRemoteStorageFailures** | Prometheus fails to send samples to remote storage. | Prometheus {$labels.namespace}/{$labels.pod} failed to send { printf "%.1f" $value }% of the samples to { $labels.remote_name}:{ $labels.url } | critical |
| **PrometheusRemoteWriteBehind** | Prometheus remote write is behind. | Prometheus {$labels.namespace}/{$labels.pod} remote write is { printf "%.1f" $value }s behind for { $labels.remote_name}:{ $labels.url }. | critical |
| **PrometheusRemoteWriteDesiredShards** | Prometheus remote write desired shards calculation wants to run more than configured max shards. | Prometheus {$labels.namespace}/{$labels.pod} remote write desired shards calculation wants to run { $value } shards for queue { $labels.remote_name}:{ $labels.url }, which is more than the max of { printf `prometheus_remote_storage_shards_max{instance="%s",job="kube-prometheus-stack-prometheus",namespace="prometheus"}` $labels.instance  or  query  or  first  or  value }. | warning |
| **PrometheusRuleFailures** | Prometheus is failing rule evaluations. | Prometheus {$labels.namespace}/{$labels.pod} has failed to evaluate { printf "%.0f" $value } rules in the last 5m. | critical |
| **PrometheusSDRefreshFailure** | Failed Prometheus SD refresh. | Prometheus {$labels.namespace}/{$labels.pod} has failed to refresh SD with mechanism {$labels.mechanism}. | warning |
| **PrometheusScrapeBodySizeLimitHit** | Prometheus has dropped some targets that exceeded body size limit. | Prometheus {$labels.namespace}/{$labels.pod} has failed { printf "%.0f" $value } scrapes in the last 5m because some targets exceeded the configured body_size_limit. | warning |
| **PrometheusScrapeSampleLimitHit** | Prometheus has failed scrapes that have exceeded the configured sample limit. | Prometheus {$labels.namespace}/{$labels.pod} has failed { printf "%.0f" $value } scrapes in the last 5m because some targets exceeded the configured sample_limit. | warning |
| **PrometheusTSDBCompactionsFailing** | Prometheus has issues compacting blocks. | Prometheus {$labels.namespace}/{$labels.pod} has detected {$value  or  humanize} compaction failures over the last 3h. | warning |
| **PrometheusTSDBReloadsFailing** | Prometheus has issues reloading blocks from disk. | Prometheus {$labels.namespace}/{$labels.pod} has detected {$value  or  humanize} reload failures over the last 3h. | warning |
| **PrometheusTargetLimitHit** | Prometheus has dropped targets because some scrape configs have exceeded the targets limit. | Prometheus {$labels.namespace}/{$labels.pod} has dropped { printf "%.0f" $value } targets because the number of targets exceeded the configured target_limit. | warning |
| **PrometheusTargetSyncFailure** | Prometheus has failed to sync targets. | { printf "%.0f" $value } targets in Prometheus {$labels.namespace}/{$labels.pod} have failed to sync because invalid configuration was supplied. | critical |
---

## prometheus-operator

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **PrometheusOperatorListErrors** | Errors while performing list operations in controller. | Errors while performing List operations in controller {$labels.controller} in {$labels.namespace} namespace. | warning |
| **PrometheusOperatorNodeLookupErrors** | Errors while reconciling Prometheus. | Errors while reconciling Prometheus in { $labels.namespace } Namespace. | warning |
| **PrometheusOperatorNotReady** | Prometheus operator not ready | Prometheus operator in { $labels.namespace } namespace isn't ready to reconcile { $labels.controller } resources. | warning |
| **PrometheusOperatorReconcileErrors** | Errors while reconciling objects. | { $value  or  humanizePercentage } of reconciling operations failed for { $labels.controller } controller in { $labels.namespace } namespace. | warning |
| **PrometheusOperatorRejectedResources** | Resources rejected by Prometheus operator | Prometheus operator in { $labels.namespace } namespace rejected { printf "%0.0f" $value } { $labels.controller }/{ $labels.resource } resources. | warning |
| **PrometheusOperatorStatusUpdateErrors** | Errors while updating objects status. | { $value  or  humanizePercentage } of status update operations failed for { $labels.controller } controller in { $labels.namespace } namespace. | warning |
| **PrometheusOperatorSyncFailed** | Last controller reconciliation failed | Controller { $labels.controller } in { $labels.namespace } namespace fails to reconcile { $value } objects. | warning |
| **PrometheusOperatorWatchErrors** | Errors while performing watch operations in controller. | Errors while performing watch operations in controller {$labels.controller} in {$labels.namespace} namespace. | warning |
---

## rabbitmq

| Alert Name | Summary | Description | Severity |
| :--- | :--- | :--- | :--- |
| **ContainerRestarts** | Investigate why the container got restarted. Check the logs of the current container: `kubectl -n { $labels.namespace } logs { $labels.pod }` Check the logs of the previous container: `kubectl -n { $labels.namespace } logs { $labels.pod } --previous` Check the last state of the container: `kubectl -n { $labels.namespace } get pod { $labels.pod } -o jsonpath='{.status.containerStatuses[].lastState}'`  | Over the last 10 minutes, container `{ $labels.container }` restarted `{ $value  or  printf "%.0f" }` times in pod `{ $labels.pod }` of RabbitMQ cluster `{ $labels.rabbitmq_cluster }` in namespace `{ $labels.namespace }`.  | warning |
| **FileDescriptorsNearLimit** | More than 80% of file descriptors are used on the RabbitMQ node. When this value reaches 100%, new connections will not be accepted and disk write operations may fail. Client libraries, peer nodes and CLI tools will not be able to connect when the node runs out of available file descriptors. See https://www.rabbitmq.com/production-checklist.html#resource-limits-file-handle-limit.  | `{ $value  or  humanizePercentage }` file descriptors of file descriptor limit are used in RabbitMQ node `{ $labels.rabbitmq_node }`, pod `{ $labels.pod }`, RabbitMQ cluster `{ $labels.rabbitmq_cluster }`, namespace `{ $labels.namespace }`.  | warning |
| **HighConnectionChurn** | More than 10% of total connections are churning. This means that client application connections are short-lived instead of long-lived. Read https://www.rabbitmq.com/connections.html#high-connection-churn to understand why this is an anti-pattern.  | Over the last 5 minutes, `{ $value  or  humanizePercentage }` of total connections are closed or opened per second in RabbitMQ cluster `{ $labels.rabbitmq_cluster }` in namespace `{ $labels.namespace }`.  | warning |
| **InsufficientEstablishedErlangDistributionLinks** | RabbitMQ clusters have a full mesh topology. All RabbitMQ nodes connect to all other RabbitMQ nodes in both directions. The expected number of established Erlang distribution links is therefore `n*(n-1)` where `n` is the number of RabbitMQ nodes in the cluster. Therefore, the expected number of distribution links are `0` for a 1-node cluster, `6` for a 3-node cluster, and `20` for a 5-node cluster. This alert reports that the number of established distributions links is less than the expected number. Some reasons for this alert include failed network links, network partitions, failed clustering (i.e. nodes can't join the cluster). Check the panels `All distribution links`, `Established distribution links`, `Connecting distributions links`, `Waiting distribution links`, and `distribution links` of the Grafana dashboard `Erlang-Distribution`. Check the logs of the RabbitMQ nodes: `kubectl -n { $labels.namespace } logs -l app.kubernetes.io/component=rabbitmq,app.kubernetes.io/name={ $labels.rabbitmq_cluster }`  | There are only `{ $value }` established Erlang distribution links in RabbitMQ cluster `{ $labels.rabbitmq_cluster }` in namespace `{ $labels.namespace }`.  | warning |
| **LowDiskWatermarkPredicted** | Based on the trend of available disk space over the past 24 hours, it's predicted that, in 24 hours from now, a disk alarm will be triggered since the free disk space will drop below the free disk space limit. This alert is reported for the partition where the RabbitMQ data directory is stored. When the disk alarm will be triggered, all publishing connections across all cluster nodes will be blocked. See https://www.rabbitmq.com/alarms.html, https://www.rabbitmq.com/disk-alarms.html, https://www.rabbitmq.com/production-checklist.html#resource-limits-disk-space, https://www.rabbitmq.com/persistence-conf.html, https://www.rabbitmq.com/connection-blocked.html.  | The predicted free disk space in 24 hours from now is `{ $value  or  humanize1024 }B` in RabbitMQ node `{ $labels.rabbitmq_node }`, pod `{ $labels.pod }`, RabbitMQ cluster `{ $labels.rabbitmq_cluster }`, namespace `{ $labels.namespace }`.  | warning |
| **MemoryAlarm** | A RabbitMQ node reached the `vm_memory_high_watermark` threshold. See https://www.rabbitmq.com/docs/alarms#overview, https://www.rabbitmq.com/docs/memory.  | RabbitMQ cluster `{ $labels.rabbitmq_cluster }` memory alarm active. Publishers are blocked.  | warning |
| **NoMajorityOfNodesReady** | No majority of nodes have been ready for the last 5 minutes. Check the details of the pods: `kubectl -n { $labels.namespace } describe pods -l app.kubernetes.io/component=rabbitmq,app.kubernetes.io/name={ $labels.label_app_kubernetes_io_name }`  | Only `{ $value }` replicas are ready in StatefulSet `{ $labels.statefulset }` of RabbitMQ cluster `{ $labels.label_app_kubernetes_io_name }` in namespace `{ $labels.namespace }`.  | warning |
| **PersistentVolumeMissing** | RabbitMQ needs a PersistentVolume for its data. However, there is no PersistentVolume bound to the PersistentVolumeClaim. This means the requested storage could not be provisioned. Check the status of the PersistentVolumeClaim: `kubectl -n { $labels.namespace } describe pvc { $labels.persistentvolumeclaim }`.  | PersistentVolumeClaim `{ $labels.persistentvolumeclaim }` of RabbitMQ cluster `{ $labels.label_app_kubernetes_io_name }` in namespace `{ $labels.namespace }` is not bound.  | critical |
| **QueueHasNoConsumers** | Messages are sitting idle in the queue, without any processing. This alert is highly application specific (and e.g. doesn't make sense for stream queues).  | Over the last 10 minutes, non-empty queue `{ $labels.queue }` with { $value } messages in virtual host `{ $labels.vhost }` didn't have any consumers in RabbitMQ cluster `{ $labels.rabbitmq_cluster }` in namespace `{ $labels.namespace }`.  | warning |
| **QueueIsGrowing** | Queue size is steadily growing over time.  | Over the last 10 minutes, queue `{ $labels.queue }` in virtual host `{ $labels.vhost }` was growing. 10 minute moving average has grown by { $value }. This happens in RabbitMQ cluster `{ $labels.rabbitmq_cluster }` in namespace `{ $labels.namespace }`.  | warning |
| **RabbitmqDiskAlarm** | A RabbitMQ node reached the `disk_free_limit` threshold. See https://www.rabbitmq.com/docs/alarms#overview, https://www.rabbitmq.com/docs/disk-alarms.  | RabbitMQ cluster `{ $labels.rabbitmq_cluster }` disk alarm active. Publishers are blocked.  | warning |
| **RabbitmqFileDescriptorAlarm** | A RabbitMQ node ran out of file descriptors. See https://www.rabbitmq.com/docs/alarms#file-descriptors.  | RabbitMQ cluster `{ $labels.rabbitmq_cluster }` file descriptor alarm active. Publishers are blocked.  | warning |
| **TCPSocketsNearLimit** | More than 80% of TCP sockets are open on the RabbitMQ node. When this value reaches 100%, new connections will not be accepted. Client libraries, peer nodes and CLI tools will not be able to connect when the node runs out of available TCP sockets. See https://www.rabbitmq.com/networking.html.  | `{ $value  or  humanizePercentage }` TCP sockets of TCP socket limit are open in RabbitMQ node `{ $labels.rabbitmq_node }`, pod `{ $labels.pod }`, RabbitMQ cluster `{ $labels.rabbitmq_cluster }`, namespace `{ $labels.namespace }`.  | warning |
| **UnroutableMessages** | There are messages published into an exchange which cannot be routed and are either dropped silently, or returned to publishers. Is your routing topology set up correctly? Check your application code and bindings between exchanges and queues. See https://www.rabbitmq.com/publishers.html#unroutable, https://www.rabbitmq.com/confirms.html#when-publishes-are-confirmed.  | There were `{ $value  or  printf "%.0f" }` unroutable messages within the last 5 minutes in RabbitMQ cluster `{ $labels.rabbitmq_cluster }` in namespace `{ $labels.namespace }`.  | warning |
---

