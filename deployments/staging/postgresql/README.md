# Postgresql Chart

This chart is based on [stable/postgresql](https://github.com/kubernetes/charts/tree/5cc7686838b1358debb019cc5491c929809e6595/stable/postgresql). The reason to create it were:
* Use a `statefulSet` instead of a `deployment`
  * Allows us better control over the restarts of the database server as you have to manually stop the pod after changing it's config
* Use a `preStop` hook to stop the database
  * Allows us to use the [fast shutdown](https://www.postgresql.org/docs/9.6/static/server-shutdown.html) to stop the database server which also stops idling database connections. This is needed as our app servers always keep connections open. This means the server wouldn't shutdown in the grace period of Kubernetes and would be stopped using `SIGKILL` which leads to data corruption.
