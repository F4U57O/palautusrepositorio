from project_reader import ProjectReader
from project import Project

def main():
    url = "https://raw.githubusercontent.com/ohjelmistotuotanto-hy/tehtavat/main/viikko2/test-project/pyproject.toml"
    reader = ProjectReader(url)
    print(reader.get_project())
    
    

if __name__ == "__main__":
    main()
