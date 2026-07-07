# Software Requirements Specification

## 1. Introduction

### 1.1 Purpose

      The purpose of this Software Requirements Specification (SRS) is to define the functional and non-functional requirements of LegacyLens AI, an AI-powered web platform designed to analyze legacy software systems and assist developers in understanding, documenting, and modernizing existing applications.

      This document serves as the primary reference for stakeholders, developers, supervisors, and future contributors throughout the project lifecycle. It establishes a common understanding of the system's objectives, features, constraints, and expected behavior before implementation begins.

      The SRS also provides the foundation for system design, database modeling, API development, user interface design, testing, and future maintenance.
---
### 1.2 Scope

      LegacyLens AI is a web-based platform that helps software developers analyze legacy software projects without modifying their source code.

      The platform allows users to upload a software project as a ZIP archive. It then performs static analysis to identify the project's technology stack, architecture, dependencies, documentation quality, technical debt indicators, and modernization opportunities.

      Based on the analysis results, the platform generates:

      - An executive project summary
      - A health score
      - Technology detection
      - Dependency analysis
      - Architecture overview
      - Findings and detected issues
      - AI-generated recommendations
      - A modernization roadmap
      - Downloadable analysis reports

      Additionally, LegacyLens AI provides an integrated AI Assistant capable of answering user questions based on the analysis context, allowing developers to better understand the analyzed project and the suggested modernization strategy.

      The current version focuses on project analysis and recommendation generation. It does not modify, refactor, or automatically rewrite the client's source code.
---
### 1.3 Intended Audience

    This document is intended for the following stakeholders:

| Audience            | Description                                                       |
| ------------------- | -----------------------------------------------------------------
| Developers          | To understand the required functionality before implementation.   |
| Project Supervisor  | To evaluate the project requirements and ensure completeness.     |
| Software Engineers  | To review the system architecture and future scalability.         |
| Project Managers    | To understand the project's objectives and expected deliverables. |
| Future Contributors | To facilitate maintenance and future development of the platform. |
---

### 1.4 References

    The following references were considered during the preparation of this Software Requirements Specification:

   - IEEE 29148 – Systems and Software Engineering: Requirements Engineering.
   - React Documentation.
   - FastAPI Documentation.
   - PostgreSQL Documentation.
   - Docker Documentation.
   - Git Documentation.
   - Markdown Guide.
   - Project Vision Document (ProjectVision.md).
   - Project Scope Document (ProjectScope.md).
   - Project Glossary (Glossary.md).

----------------------------------------------------

## 2. Overall Description

### 2.1 Product Perspective

    LegacyLens AI is an independent AI-powered web platform designed to assist software developers in understanding and modernizing legacy software systems.

    The platform allows users to upload software projects in ZIP format, perform automated static analysis, and receive intelligent insights without modifying the original source code.

    LegacyLens AI combines software analysis, AI-generated documentation, modernization recommendations, dependency inspection, architecture visualization, and an integrated AI Assistant into a single workspace.

    The platform operates as a standalone web application and may be extended in the future with cloud deployment, repository integration, and IDE extensions.
---
### 2.2 Product Goals

    The primary goals of LegacyLens AI are:

   - Help developers quickly understand unfamiliar legacy software projects.
   - Detect technologies, frameworks, and dependencies automatically.
   - Generate AI-powered project summaries and documentation.
   - Identify technical debt and modernization opportunities.
   - Provide actionable recommendations for improving software quality.
   - Assist developers through an intelligent contextual AI Assistant.
   - Reduce the time required to analyze and understand complex software systems.

---
### 2.3 Product Functions
   
    The main functions of LegacyLens AI include:

- User authentication
- Project management
- ZIP project upload
- Static project analysis
- Technology stack detection
- Architecture overview generation
- Dependency analysis
- Findings identification
- AI-generated executive summary
- Documentation generation
- Modernization recommendations
- Roadmap generation
- Context-aware AI Assistant
- PDF report generation
- User settings management

---
### 2.4 User Classes

    LegacyLens AI is intended for different categories of users:

#### - Software Developers

    Developers use the platform to understand unfamiliar codebases, analyze software quality, and receive modernization recommendations.

#### - Project Managers

    Project managers use the generated reports to evaluate project health, identify risks, and estimate modernization efforts.

#### - Students and Researchers

    Students and researchers may use the platform as an educational tool to study software architecture and modernization techniques.
---
### 2.5 Operating Environment

    LegacyLens AI operates as a web-based application.

    The system can be accessed using modern web browsers such as Google Chrome, Microsoft Edge, or Mozilla Firefox.

    The backend runs on a local development server during the MVP phase.

    The application stores project information and analysis results in a PostgreSQL database.

    AI-powered features require an available AI model or API connection depending on the deployment configuration.
---
### 2.6 Design Constraints
    The current version of LegacyLens AI is subject to the following constraints:

- The platform accepts only ZIP project uploads.
- Source code is analyzed without being modified.
- Internet access may be required for cloud-based AI services.
- Large projects may require additional processing time.
- Only static analysis is performed during the MVP phase.
---
### 2.7 Assumptions and Dependencies
    The system assumes that:

- Uploaded projects contain valid source code.
- Project files are complete and not corrupted.
- Configuration files are available when possible.
- Users have basic software development knowledge.
- The AI service is available during analysis.

----------------------------------------------------

## 3. Functional Requirements

### 3.1 Authentication

- FR-001 User Registration
 > The system shall allow a new user to create an account.
- FR-002 Login
 > The system shall allow registered users to log in securely.
- FR-003 Logout
 > The system shall allow users to terminate their active session.
- FR-004 Password Reset
 > The system shall allow users to reset their forgotten password.

---
### 3.2 Project Management

- FR-005 Create Project
 > The system shall allow users to create a new project workspace.
- FR-006 Edit Project
 > The user shall be able to edit the project's information.
- FR-007 Delete Project
 > The user shall be able to remove a project.
- FR-008 View Project List
 > The system shall display all analyzed projects.

---
### 3.3 Project Upload

- FR-009 Upload ZIP
 > The system shall allow users to upload a software project in ZIP format.
- FR-010 Validate Project
 > The system shall validate the uploaded archive before analysis.
- FR-011 Extract Files
 > The system shall automatically extract the uploaded archive.
- FR-012 Detect Project Type
 > The system shall identify the project type based on configuration files.

---
### 3.4 Project Analysis

- FR-013 Detect Programming Languages
 > The system shall detect programming Languages
- FR-014 Detect Frameworks
 > The system shall detect frameworks
- FR-015 Detect Dependencies
 > The system shall detect dependencies
- FR-016 Analyze Architecture
 > The system shall Analyse Architecture
- FR-017 Calculate Health Score
 > The system shall calculate Health Score
- FR-018 Detect Technical Debt Indicators
 > The system shall detect Technical Debt Indicateurs
- FR-019 Detect Documentation
 > The system shall detect Documentation
- FR-020 Generate Executive Summary
 > The system shall generate Executive Summary
- FR-021 Generate Findings
 > The system shall Genrate Findings
---
### 3.5 Documentation

- FR-022 Generate Documentation
- FR-023 View Documentation
- FR-024 Export Documentation
---
### 3.6 Recommendations

- FR-025 Generate Recommendations
- FR-026 Prioritize Recommendations
- FR-027 Generate Modernization Roadmap
---
### 3.7 AI Assistant

- FR-028 Ask Questions
 > The system shall provide an AI Assistant that answers questions related to the currently analyzed project.
- FR-029 Context Awareness
 > The AI Assistant shall use the current project analysis as context.
- FR-030 Explain Recommendations
- FR-031 Explain Architecture
- FR-032 Summarize Findings
---
### 3.9 Dashboard

- FR-036 Display Statistics
- FR-037 Display Recent Projects
- FR-038 Search Projects
---
### 3.10 Settings

- FR-039 Edit Profile
- FR-040 Change Theme
- FR-041 Delete Account

----------------------------------------------------

## 4. Non Functional Requirements

### 4.1 Performance

**NFR-001 – Analysis Performance**

 > The system should complete the analysis of small and medium-sized projects within an acceptable processing time.

**NFR-002 – User Interface Responsiveness**

 > The platform should provide smooth navigation and responsive interactions between pages.

**NFR-003 – AI Response Time**

 > The AI Assistant should generate responses within a reasonable time depending on the complexity of the request.
---
### 4.2 Reliability

**NFR-004 – Stable Operation**

 > The system should operate reliably without unexpected crashes during normal usage.

**NFR-005 – Data Integrity**

 > Analysis results should remain consistent and accurate after processing.
---
### 4.3 Availability

**NFR-006 – System Availability**

 > The platform should be available whenever the local server is running.

**NFR-007 – AI Service Availability**

 > AI-powered features depend on the availability of the configured AI model or service.
---
### 4.4 Security

**NFR-008 – Authentication Security**

 > Only authenticated users shall access project analysis features.

**NFR-009 – Password Protection**

 > User passwords shall be stored securely using password hashing.

**NFR-010 – Data Privacy**

 > Uploaded project files shall not be modified during the analysis process.

**NFR-011 – Access Control**

 > Users shall only access their own projects and reports.
---
### 4.5 Usability

**NFR-012 – User-Friendly Interface**

 > The platform should provide a clean and intuitive user interface.

**NFR-013 – Easy Navigation**

 > Users should easily navigate between Dashboard, Projects, Analysis, and Reports.

**NFR-014 – Consistent Design**

 > The interface should maintain a consistent layout across all pages.
---
### 4.6 Maintainability
 
**NFR-015 – Modular Design**

 > The application should follow a modular architecture to simplify future maintenance.

**NFR-016 – Code Readability**

 > The source code should be organized and documented to facilitate future development.
---
### 4.7 Scalability

**NFR-017 – Future Expansion**

 > The system should support future integration with cloud platforms and repository services.

**NFR-018 – Large Projects**

 > The architecture should allow analysis of larger software projects in future releases.
---
### 4.8 Portability

**NFR-019 – Cross-Platform Support**

 > The platform should operate on Windows, Linux, and macOS through modern web browsers.
---
### 4.9 Compatibility

**NFR-020 – Browser Compatibility**

 > The application should be compatible with modern web browsers such as Google Chrome, Microsoft Edge, and Mozilla Firefox.

**NFR-021 – Project Compatibility**

 > The platform should support software projects developed using different programming languages and frameworks.
----------------------------------------------------

## 5. External Interface Requirements

### 5.1 User Interface

    LegacyLens AI provides a modern web-based graphical user interface (GUI) accessible through standard web browsers.

    The interface is organized into the following main sections:

- Dashboard
- Projects
- Analysis
- AI Assistant
- Reports
- Settings

> The platform should provide a clean, responsive, and intuitive user experience to simplify project analysis and navigation.
---

### 5.2 Software Interfaces

    LegacyLens AI interacts with several software components during its execution.

    The platform communicates with:

- PostgreSQL database for persistent data storage.
- AI services or local language models for intelligent analysis and recommendations.
- Static analysis libraries used to inspect project files.
- PDF generation libraries for exporting analysis reports.

> These software interfaces operate transparently without requiring direct interaction from the user.
---

### 5.3 Database Interface

    The platform stores application data in a relational database.

    The database manages:

- User accounts
- Projects
- Analysis results
- Generated reports
- Recommendations
- AI conversations (optional)

> The application performs secure read and write operations while preserving data integrity.
---

### 5.4 File Interface

    The platform accepts project uploads in ZIP format.

    Uploaded archives are temporarily extracted for static analysis.

    The original project files remain unchanged throughout the analysis process.

    Generated reports may be exported in PDF format.
---

### 5.5 AI Interface

    LegacyLens AI integrates an AI-powered assistant capable of generating project summaries, answering user questions, explaining architecture, and providing modernization recommendations.

    The AI Assistant operates using the analysis results as contextual information and does not directly modify the client's source code.

    The quality of AI-generated responses depends on the completeness of the uploaded project and the availability of the configured AI model.
----------------------------------------------------

## 6. Data Requirements

### 6.1 Input Data

    LegacyLens AI accepts the following input data:

- User registration information
- User login credentials
- Software projects uploaded as ZIP archives
- Source code files
- Configuration files
- Build files
- Documentation files (README, Markdown, etc.)
- User questions submitted to the AI Assistant
---

### 6.2 Stored Data

    The platform stores the following information:

- User accounts
- Project metadata
- Uploaded project information
- Analysis results
- Health scores
- Technology stack information
- Dependency analysis
- Recommendations
- Generated reports
- AI conversation history (optional)
---

### 6.3 Output Data

    After analysis, the platform generates:

- Executive summaries
- Architecture overviews
- Technology stack reports
- Dependency reports
- Health scores
- Findings
- Modernization recommendations
- Modernization roadmap
- Downloadable PDF reports
- AI-generated responses
---

### 6.4 Data Lifecycle

    Project data follows the lifecycle below:

1. The user uploads a project.
2. The system validates the uploaded archive.
3. The archive is extracted.
4. Static analysis is performed.
5. Analysis results are generated.
6. Results are stored in the database.
7. Reports are generated.
8. Users may delete the project and its associated data.

----------------------------------------------------

## 7. Business Rules

### BR-001

> The platform shall never modify the client's source code.

---

### BR-002

> Only authenticated users can upload projects.

---

### BR-003

> Users can access only their own projects and reports.

---

### BR-004

> Only ZIP archives are accepted for project uploads.

---

### BR-005

> AI recommendations are advisory and shall not automatically modify project files.

---

### BR-006

> A project must be successfully analyzed before recommendations are generated.

---

### BR-007

> Reports are generated only after analysis completion.

---

### BR-008

> Deleting a project permanently removes all related analysis results.
----------------------------------------------------

## 8. Future Enhancements

    Future versions of LegacyLens AI may include:

- GitHub integration
- GitLab integration
- Bitbucket integration
- Direct repository analysis without ZIP upload
- Cloud deployment
- Multi-user collaboration
- Real-time project monitoring
- Support for additional programming languages
- RAG-based document retrieval
- IDE extensions for Visual Studio Code and JetBrains IDEs
- Automatic architecture diagram generation
- AI-powered code refactoring suggestions
- Project comparison between software versions
- Team dashboards and analytics