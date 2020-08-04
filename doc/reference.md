# Reference

This document is a reference of all provided classes

## Resources


### Cron

Upstream resource documentation: https://gitlab.com/phil9909/concourse-cron-resource/-/blob/master/README.md

Note: The location (used for timezone) is currently hardcoded to "Europe/Berlin".

Example:

```python
Cron("0 0 4 * * *")
```


### DockerImage

Upstream resource documentation: https://github.com/concourse/docker-image-resource/blob/master/README.md

Note: Only `repository`, `username`, `password` and `tag` are currently supported supported in source configuration.

Example:
```python
DockerImage("alpine")
```

After `get`ting the resource the following methods are available:

| method     | returns                                          | locally        |
|------------|--------------------------------------------------|----------------|
| `name`     | the given name                                   | the given name |
| `path`     | the location where concourse stored the resource | unavailable    |
| `digest()` | the pulled image digest                          | "latest"       |


### GoogleCloudStorageResource

Upstream resource documentation: https://github.com/frodenas/gcs-resource/blob/master/README.md

Note: `versioned_file` is currently unsupported.

Example:
```python
GoogleCloudStorageResource("my-bucket", "(.*).txt", "((MY_GCS_CREDENTIALS))")
```


### GitRepo

Upstream resource documentation: https://github.com/concourse/git-resource/blob/master/README.md

Note: Only `uri`, `username`, `password`, `branch`, `ignore_paths` and `tag_filter` are currently supported supported in source configuration.

Example:
```python
GitRepo("https://github.com/torvalds/linux")
```

After `get`ting the resource the following methods are available:

| method        | returns                                          | locally                                                                 |
|---------------|--------------------------------------------------|-------------------------------------------------------------------------|
| `name`        | the given name                                   | the given name                                                          |
| `path`        | the location where concourse stored the resource | `~/workspace/<name>`                                                    |
| `directory()` | the location where concourse stored the resource | `~/workspace/<name>`                                                    |
| `ref()`       | see upstream documentation                       | result of `git describe --tags` if successful else `git rev-parse HEAD` |
| `short_ref()` | see upstream documentation                       | result of `git rev-parse --short HEAD`                                  |


### GithubRelease

Upstream resource documentation: https://github.com/concourse/github-release-resource/blob/master/README.md

Note: Only `owner`, `repo`, `access_token`, `pre_release`, `release`, `github_api_url` and `github_uploads_url` are currently supported supported in source configuration.

Example:
```python
GithubRelease(owner="concourse", repo="concourse")
```

After `get`ting the resource the following methods are available:

| method              | returns                                          | locally                                  |
|---------------------|--------------------------------------------------|------------------------------------------|
| `name`              | the given name                                   | the given name                           |
| `path`              | the location where concourse stored the resource | unavailable                              |
| `tag(default=None)` | see upstream documentation                       | the `default` value passed to the method |


### ConcourseLockResource

Upstream resource documentation: https://github.com/concourse/pool-resource/blob/master/README.md

Note: Only `uri`, `branch`, `pool`, `username` and `password` are currently supported supported in source configuration.

Example:
```python
ConcourseLockResource("https://github.com/concourse/locks", username="((GITHUB_USER))", password="((GITHUB_TOKEN))", branch="master", pool="my-pool")
```


### SemVer

Upstream resource documentation: https://github.com/concourse/semver-resource/blob/master/README.md

Example:
```python
SemVer(driver=<see below>, initial_version="0.42.0")
```

After `get`ting the resource the following methods are available:

| method      | returns                                          | locally        |
|-------------|--------------------------------------------------|----------------|
| `name`      | the given name                                   | the given name |
| `path`      | the location where concourse stored the resource | unavailable    |
| `version()` | see upstream documentation                       | "0.0.1"        |

Note: Currently, git is the only supported driver.

### SemVerGitDriver


Note: Only `owner`, `repo`, `access_token`, `pre_release`, `release`, `github_api_url` and `github_uploads_url` are currently supported supported in source configuration.

Example:
```python
 SemVer(driver = SemVerGitDriver("https://github.com/concourse/version", username="((GITHUB_USER))", password="((GITHUB_TOKEN))", branch="version", file="version"))
```