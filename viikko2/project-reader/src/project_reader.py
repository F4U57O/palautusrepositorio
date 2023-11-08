from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml = tomli.loads(content)
        name = toml.get("tool", {}).get("poetry", {}).get("name", [])
        description = toml.get("tool", {}).get("poetry", {}).get("description", [])
        license = toml.get("tool", {}).get("poetry", {}).get("license", [])
        authors = toml.get("tool", {}).get("poetry", {}).get("authors", [])
        dependencies = toml.get("tool", {}).get("poetry", {}).get("dependencies", [])
        dev_dependencies = toml.get("tool", {}).get("poetry", {}).get("group", {}).get("dev", {}).get("dependencies", [])

        return Project(name, description, license, authors, dependencies, dev_dependencies)


