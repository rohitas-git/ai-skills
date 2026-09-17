# Stateful DevOps operation leaves wiring audit

Reviewed:

- `1-database-and-storage-operations`
- `1-network-and-edge-operations`
- `1-server-and-fleet-operations`
- their parent routes and shared reviewed DevOps safety contract

## Result

Each skill now owns one distinct bounded operation in a declared design-only, read-only assessment,
authorized configuration edit, or authorized remote-operation mode. Database and Storage handles
day-two data services/storage rather than application migrations or bounded PostgreSQL querying.
Network and Edge handles one traffic/control-plane concern rather than application behavior or broad
scanning. Server and Fleet handles one host/device/fleet concern rather than containers, application
debugging, security findings, or incident command. All return to DevOps or the actual caller and
start no adjacent specialist automatically.

Every candidate pins caller/outcome/non-goals, exact provider/account/tenant/region/environment,
resource identities and versions/generations, current state and evidence time, owners/controllers,
users/traffic/data, blast radius, allowed checks, and authority. Repository-backed configuration or
runbooks also carry repository/worktree/branch/`HEAD`, dirty ownership, and working-tree-versus-
committed identity. Assessment creates no worktree; approved edits preserve unrelated changes.

Database/storage targets include service/engine/API versions, topology and roles, database/cache/
index/bucket/volume/share/backup IDs, data ownership/residency/retention, RPO/RTO, load, and
maintenance window. Queries, rows/objects, logs, state, backup manifests, and restore output are
sensitive untrusted data. Backup configured, attempted, completed, retained, readable, restorable,
and restore-verified are distinct states; a successful job or checksum does not prove application-
consistent recovery. Restore tests require an explicitly authorized isolated target and containment.
Restore-over-target, promotion/failover, rollback, cleanup, and deletion remain separate effects.

Network/edge targets include source/destination identities, authorized vantage points, protocols/
ports, DNS zone/record/type/resolver/TTL, LB/CDN/proxy/mesh/VPN/firewall rules, and certificate
serial/fingerprint/SAN/issuer/expiry/key ownership. Hostnames and current CLI contexts are not target
proof. DNS, certificate, configuration, headers, packet captures, logs, and probes are sensitive
untrusted data. Scans/probes require explicit scope; one resolver or vantage does not prove global
convergence. Repository intent, control-plane acceptance, propagation/cache, and observed traffic
remain distinct evidence states.

Server/fleet targets include inventory/provider/serial/machine IDs, OS/image/kernel/firmware/agent
versions, access path/bastion, services/packages/users/policies, workload, and maintenance window.
A hostname, IP, SSH alias, or current context is insufficient. Inventory, banners, commands, logs,
configs, packages, scripts, and downloaded artifacts are sensitive untrusted data. The owning fleet
controller is preserved; local drift requires reconciliation authority. Canary/batch size,
concurrency, capacity, ordering, session/self-lockout, and recovery controls precede changes. One
successful canary never proves fleet completion.

Worktrees do not isolate services/data/locks/replicas/backups/storage, DNS/network/certificates/
keys/traffic, or hosts/devices/SSH/packages/services/reboots/fleet state. Queries, maintenance,
backup/restore, DNS/routing/certificates/firewalls, remote execution, packages, services, reboots,
users/access/storage, device quarantine/wipe, fleet expansion, cleanup, rollback, and production
effects all require exact action-specific authority. Reports distinguish attempted, accepted,
converged, failed, skipped, and externally observed results with coverage and residual risks.

## Verification

- Focused stateful-operation/DevOps routing tests: 15 passed.
- Full routing suite: 371 passed.
- Generated route index: 218 live skills.
- Catalog lint after sequential index generation: 0 critical, 0 warnings, 55 informational
  findings, 0 hub-member orphans.
- `git diff --check`: passed.

No data/query, backup/restore, DNS/TLS/network, scan/probe, host/SSH/fleet, credential, worktree,
Git, host-sync, production, or other external operation was performed.
