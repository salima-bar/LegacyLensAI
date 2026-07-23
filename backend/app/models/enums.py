from enum import Enum


class ProjectStatus(str, Enum):
    UPLOADED = "Uploaded"
    ANALYZING = "Analyzing"
    COMPLETED = "Completed"
    FAILED = "Failed"

class RecommendationPriority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class RecommendationCategory(str, Enum):
    SECURITY = "Security"
    PERFORMANCE = "Performance"
    CODE_QUALITY = "Code Quality"
    DEPENDENCY = "Dependency"
    DOCUMENTATION = "Documentation"
    BEST_PRACTICE = "Best Practice"
    MAINTAINABILITY = "Maintainability"
    SCALABILITY = "Scalability"


class RecommendationComponent(str, Enum):
    FRONTEND = "Frontend"
    BACKEND = "Backend"
    DATABASE = "Database"
    API = "API"
    AUTHENTICATION = "Authentication"
    ARCHITECTURE = "Architecture"
    CONFIGURATION = "Configuration"
    DEPLOYMENT = "Deployment"
    CI_CD = "CI/CD"