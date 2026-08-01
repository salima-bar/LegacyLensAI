# LegacyLensAI

React + TypeScript + Vite implementation of LegacyLensAI. Visual design is
unchanged from the original build — this pass restructured it into a
reusable, production-shaped application.

## Run it

```bash
npm install
npm run dev
```

## Structure

```
src/
  components/        Sidebar, TopBar, AppShell, Logo, ScoreRing, StatusBadge
                      — shared across every authenticated page
  layouts/
    AnalysisLayout.tsx   Reusable layout for the Analysis page: project
                         header + tabs + persistent AI Assistant. Every
                         analyzed project renders through this same layout.
  features/analysis/
    ProjectHeader.tsx    Name, stack, last-analysis date, status
    AnalysisTabs.tsx     Overview / Documentation / Architecture /
                         Recommendations / Roadmap — route-driven
    AssistantPanel.tsx   Persistent chat panel, stays mounted across tabs
    TabPlaceholder.tsx   Shared "not implemented yet" state for tab content
    tabs/                One stub file per tab (layout only, no content)
  pages/               Landing, Login, Dashboard, Projects, Analysis, Settings
  data/mockData.ts     Mock projects, trend, and risk data
  types/index.ts        Shared domain types
  styles/global.css     Design tokens, fonts, and utility classes
                         (unchanged from the original design)
```

## Routing

```
/                                   Landing
/login                              Login
/app                                Dashboard   (default page after login)
/app/projects                       Projects
/app/analysis/:projectId            Analysis  → redirects to .../overview
/app/analysis/:projectId/overview
/app/analysis/:projectId/documentation
/app/analysis/:projectId/architecture
/app/analysis/:projectId/recommendations
/app/analysis/:projectId/roadmap
/app/settings                       Settings
```

`AppShell` renders the permanent Sidebar plus the routed page for every
`/app/*` route, so navigation between Dashboard, Projects, Analysis, and
Settings never unmounts the sidebar.

`AnalysisLayout` is the single reusable layout for the Analysis page. Tab
content is rendered through `<Outlet />` as nested routes, so switching
tabs swaps only the content pane — the project header, tab bar, and the
`AssistantPanel` (with its chat state) stay mounted the whole time.

## Status

Tab content for Overview / Documentation / Architecture / Recommendations /
Roadmap is intentionally not implemented — each renders a shared
`TabPlaceholder` for now. The layout, routing, and assistant panel are
complete and ready for that content to be built out per tab.
