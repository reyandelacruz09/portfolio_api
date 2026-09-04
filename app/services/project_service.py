from app.repositories.content_repository import ContentRepository


class ProjectService:
    def __init__(self, db):
        self.content_repo = ContentRepository(db)

    def list_projects(self) -> list:
        content = self.content_repo.get_all()
        projects = content.get("projects", [])
        result = []
        for idx, project in enumerate(projects, start=1):
            result.append(
                {
                    "id": idx,
                    "title": project.get("title", ""),
                    "description": project.get("description", ""),
                    "image_url": project.get("image_url"),
                    "github_url": project.get("github") or project.get("github_url"),
                    "live_url": project.get("live") or project.get("live_url"),
                    "technologies": project.get("tech", []),
                }
            )
        return result

    def get_project(self, project_id: int):
        projects = self.list_projects()
        for project in projects:
            if project["id"] == project_id:
                return project
        return None
