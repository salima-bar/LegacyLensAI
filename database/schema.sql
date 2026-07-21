CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TYPE project_status AS ENUM (
    'Uploaded',
    'Analyzing',
    'Completed',
    'Failed'
);

CREATE TYPE recommendation_priority AS ENUM (
    'Low',
    'Medium',
    'High',
    'Critical'
);

CREATE TYPE recommendation_category AS ENUM (
    'Architecture',
    'Security',
    'Performance',
    'Database',
    'Documentation',
    'Testing',
    'Dependency',
    'Code Quality'
);

-- =====================================================
-- USERS
-- =====================================================
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    full_name VARCHAR(100) NOT NULL,

    email VARCHAR(255) UNIQUE NOT NULL,

    password_hash TEXT NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- =====================================================
-- PROJECTS
-- =====================================================

CREATE TABLE projects (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    user_id UUID NOT NULL,

    name VARCHAR(255) NOT NULL,

    description TEXT,

    original_file_name VARCHAR(255) NOT NULL,

    storage_path TEXT NOT NULL,

    status project_status NOT NULL DEFAULT 'Uploaded',

    upload_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    last_analysis_date TIMESTAMP,

    current_analysis_id UUID,

    CONSTRAINT fk_project_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE

);
-- =====================================================
-- ANALYSES
-- =====================================================

CREATE TABLE analyses (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    project_id UUID NOT NULL,

    version INTEGER NOT NULL,

    summary TEXT,

    detected_technologies TEXT,

    programming_language VARCHAR(100),

    framework VARCHAR(100),

    analysis_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_analysis_project
        FOREIGN KEY (project_id)
        REFERENCES projects(id)
        ON DELETE CASCADE,

    CONSTRAINT uq_project_version
        UNIQUE(project_id, version)

);
-- =====================================================
-- PROJECT -> CURRENT ANALYSIS
-- =====================================================

ALTER TABLE projects

ADD CONSTRAINT fk_current_analysis

FOREIGN KEY (current_analysis_id)

REFERENCES analyses(id)

ON DELETE SET NULL;
-- =====================================================
-- ARCHITECTURES
-- =====================================================

CREATE TABLE architectures (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    analysis_id UUID UNIQUE NOT NULL,

    architecture_data TEXT NOT NULL,

    layers TEXT,

    dependencies TEXT,

    CONSTRAINT fk_architecture_analysis

        FOREIGN KEY (analysis_id)

        REFERENCES analyses(id)

        ON DELETE CASCADE

);
-- =====================================================
-- DOCUMENTATIONS
-- =====================================================

CREATE TABLE documentations (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    analysis_id UUID UNIQUE NOT NULL,

    content TEXT NOT NULL,

    format VARCHAR(50) DEFAULT 'Markdown',

    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_documentation_analysis

        FOREIGN KEY (analysis_id)

        REFERENCES analyses(id)

        ON DELETE CASCADE

);
-- =====================================================
-- ROADMAPS
-- =====================================================

CREATE TABLE roadmaps (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    analysis_id UUID UNIQUE NOT NULL,

    roadmap_data JSONB NOT NULL,

    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_roadmap_analysis

        FOREIGN KEY (analysis_id)

        REFERENCES analyses(id)

        ON DELETE CASCADE

);
-- =====================================================
-- RECOMMENDATIONS
-- =====================================================

CREATE TABLE recommendations (

    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    analysis_id UUID NOT NULL,

    title VARCHAR(255) NOT NULL,

    description TEXT NOT NULL,

    priority recommendation_priority,

    category recommendation_category,

    CONSTRAINT fk_recommendation_analysis

        FOREIGN KEY (analysis_id)

        REFERENCES analyses(id)

        ON DELETE CASCADE

);
-- =====================================================
-- INDEXES
-- =====================================================

CREATE INDEX idx_projects_user
ON projects(user_id);

CREATE INDEX idx_analysis_project
ON analyses(project_id);

CREATE INDEX idx_recommendation_analysis
ON recommendations(analysis_id);

CREATE INDEX idx_projects_status
ON projects(status);

