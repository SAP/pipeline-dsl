import unittest

from conpype.resources import *


class TestGitResource(unittest.TestCase):

    def test_basic(self):
        repo = GitRepo("https://example.com/repo.git")

        obj = repo.concourse(name="test")
        self.assertDictEqual(obj, {
            "name": "test",
            "type": "git",
            "icon": "git",
            "source": {
                "uri": "https://example.com/repo.git"
            }
        })


class TestCronResource(unittest.TestCase):

    def test_basic(self):
        repo = Cron("definition")

        obj = repo.concourse("test")
        self.assertDictEqual(obj, {
            "name": "test",
            "type": "cron",
            "icon": "clock-outline",
            "source": {
                "cron": "definition",
                "location": "Europe/Berlin",
            }
        })

        obj = repo.resource_type()
        self.assertDictEqual(obj, {
            "name": "cron",
            "type": "docker-image",
            "source": {
                "repository": "phil9909/concourse-cron-resource",
                "tag": "latest",
            }
        })


class TestDockerImageResource(unittest.TestCase):

    def test_basic(self):
        resource = DockerImage("repo", "username", "password", "tag")

        obj = resource.concourse("test")
        self.assertDictEqual(obj, {
            "name": "test",
            "type": "docker-image",
            "icon": "docker",
            "source": {
                "repository": "repo",
                "username": "username",
                "password": "password",
                "tag": "tag"
            }
        })

        location = resource.get("test")
        self.assertEqual(location.digest(), "latest")


class TestGoogleCloudStorageResource(unittest.TestCase):

    def test_basic(self):
        resource = GoogleCloudStorage("bucket", "regexp", "credentials")

        obj = resource.concourse("test")
        self.assertDictEqual(obj, {
            "name": "test",
            "type": "gcs",
            "icon": "file-cloud",
            "source": {
                "bucket": "bucket",
                "regexp": "regexp",
                "json_key": "credentials",
            }
        })

        self.assertDictEqual(resource.resource_type(), {
            "name": "gcs",
            "type": "docker-image",
            "source": {
                "repository": "frodenas/gcs-resource",
                "tag": "latest",
            }
        })


class TestPoolResource(unittest.TestCase):

    def test_basic(self):
        resource = Pool("uri", "branch", "pool", "username", "password")

        obj = resource.concourse("test")
        self.assertDictEqual(obj, {
            "name": "test",
            "type": "pool_stable",
            "icon": "lock",
            "source": {
                "uri": "uri",
                "branch": "branch",
                "pool": "pool",
                "username": "username",
                "password": "password",
            }
        })

        self.assertDictEqual(resource.resource_type(), {
            "name": "pool_stable",
            "type": "docker-image",
            "source": {
                "repository": "concourse/pool-resource",
                "tag": "1.1.1",
            }
        })

class TestGithubResource(unittest.TestCase):

    def test_basic(self):
        resource = GithubRelease("owner", "repo", "access_token", pre_release = True, release = False, github_api_url = "github_api_url", github_uploads_url= "github_uploads_url")

        obj = resource.concourse("test")
        self.assertDictEqual(obj, {
            "name": "test",
            "type": "github-release",
            "icon": "github",
            "source": {
                "owner": "owner",
                "repository":"repo",
                "access_token": "access_token",
                "pre_release": True,
                "release": False,
                "github_api_url": "github_api_url",
                "github_uploads_url": "github_uploads_url"
            }
        })

class TestSemVerResource(unittest.TestCase):

    def test_private_key(self):
        resource = SemVer(SemVerGitDriver("git@github.com:concourse/concourse.git", "version", "version-file", private_key="testkey", username="user", git_user="git_user", depth=1, skip_ssl_verification=True, commit_message="Commit Message"))
        obj = resource.concourse("test")
        
        self.assertDictEqual(obj, {
            "name": "test",
            "type": "semver",
            "icon": "creation",
            "source": {
                "driver": "git",
                "uri": "git@github.com:concourse/concourse.git",
                "branch": "version",
                "file": "version-file",
                "private_key": "testkey",
                "username": "user",
                "depth": 1,
                "git_user": "git_user",
                "skip_ssl_verification": True,
                "commit_message": "Commit Message"
            }
        })

    def test_password(self):
        resource = SemVer(SemVerGitDriver("git@github.com:concourse/concourse.git", "version", "version-file", password="pw", username="user", git_user="git_user", depth=1, skip_ssl_verification=True, commit_message="Commit Message"))
        obj = resource.concourse("test")
        
        self.assertDictEqual(obj, {
            "name": "test",
            "type": "semver",
            "icon": "creation",
            "source": {
                "driver": "git",
                "uri": "git@github.com:concourse/concourse.git",
                "branch": "version",
                "file": "version-file",
                "password": "pw",
                "username": "user",
                "depth": 1,
                "git_user": "git_user",
                "skip_ssl_verification": True,
                "commit_message": "Commit Message"
            }
        })

if __name__ == '__main__':
    unittest.main()

# run > python -munittest in main conpype dir to execute