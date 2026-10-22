# -*- coding: utf-8 -*-
"""
CSS styles for Teledata One Industrial Interactive Manual.
Modern, clean industrial palette (Dark Slate, Steel Blue, Fire Red, Hazard Amber, Safety Green).
"""

CSS_CONTENT = """
:root {
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --bg-tertiary: #334155;
  --bg-card: #1e293b;
  --bg-card-hover: #273549;
  --text-primary: #f8fafc;
  --text-secondary: #cbd5e1;
  --text-muted: #94a3b8;
  --border-color: #334155;
  --border-light: #475569;
  
  --brand-red: #ef4444;
  --brand-red-bg: rgba(239, 68, 68, 0.12);
  --brand-amber: #f59e0b;
  --brand-amber-bg: rgba(245, 158, 11, 0.12);
  --brand-green: #10b981;
  --brand-green-bg: rgba(16, 185, 129, 0.12);
  --brand-blue: #38bdf8;
  --brand-blue-bg: rgba(56, 189, 248, 0.12);
  --brand-purple: #a855f7;
  
  --font-arabic: 'Cairo', 'Noto Naskh Arabic', -apple-system, BlinkMacSystemFont, 'Segoe UI', Tahoma, Arial, sans-serif;
  --font-mono: 'Consolas', 'Monaco', 'Courier New', monospace;
  
  --header-height: 125px;
  --sidebar-width: 290px;
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4), 0 2px 4px -2px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.5), 0 4px 6px -4px rgba(0, 0, 0, 0.5);
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 16px;
  --transition: all 0.2s ease-in-out;
}

[data-theme="light"] {
  --bg-primary: #f8fafc;
  --bg-secondary: #ffffff;
  --bg-tertiary: #f1f5f9;
  --bg-card: #ffffff;
  --bg-card-hover: #f8fafc;
  --text-primary: #0f172a;
  --text-secondary: #334155;
  --text-muted: #64748b;
  --border-color: #e2e8f0;
  --border-light: #cbd5e1;
  
  --brand-red: #dc2626;
  --brand-red-bg: #fef2f2;
  --brand-amber: #d97706;
  --brand-amber-bg: #fffbeb;
  --brand-green: #059669;
  --brand-green-bg: #ecfdf5;
  --brand-blue: #0284c7;
  --brand-blue-bg: #f0f9ff;
  --brand-purple: #9333ea;
  
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}

html {
  font-family: var(--font-arabic);
  direction: rtl;
  scroll-behavior: smooth;
  font-size: 16px;
  line-height: 1.7;
  background-color: var(--bg-primary);
  color: var(--text-primary);
}

body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
}

/* Bilingual isolation */
bdi, .tech-term {
  direction: ltr;
  unicode-bidi: isolate;
  font-family: var(--font-mono);
  font-size: 0.9em;
  font-weight: 600;
  color: #38bdf8;
  background-color: rgba(56, 189, 248, 0.12);
  padding: 1px 6px;
  border-radius: 4px;
  display: inline-block;
  vertical-align: baseline;
}
[data-theme="light"] bdi, [data-theme="light"] .tech-term {
  color: #0369a1;
  background-color: #e0f2fe;
}

/* App Header */
.app-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background-color: var(--bg-secondary);
  border-bottom: 1px solid var(--border-color);
  box-shadow: var(--shadow-md);
}

.top-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 16px;
  gap: 12px;
}

.brand-section {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-shrink: 0;
}

.brand-logo-img {
  height: 28px;
  width: auto;
  object-fit: contain;
}

.brand-title {
  display: flex;
  flex-direction: column;
}

.brand-title-main {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 6px;
}

.brand-badge {
  font-size: 0.7rem;
  background-color: var(--brand-red);
  color: #fff;
  padding: 1px 6px;
  border-radius: 12px;
  font-weight: 600;
}

.brand-subtitle {
  font-size: 0.75rem;
  color: var(--text-muted);
}

/* Search Bar */
.search-wrapper {
  flex: 1;
  max-width: 600px;
  position: relative;
}

.search-input-box {
  display: flex;
  align-items: center;
  background-color: var(--bg-tertiary);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 4px 12px;
  transition: var(--transition);
}

.search-input-box:focus-within {
  border-color: var(--brand-blue);
  box-shadow: 0 0 0 2px var(--brand-blue-bg);
}

.search-icon {
  width: 18px;
  height: 18px;
  fill: var(--text-muted);
  flex-shrink: 0;
}

.search-input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  padding: 6px 10px;
  font-family: inherit;
  font-size: 0.95rem;
  color: var(--text-primary);
  direction: rtl;
}

.search-input::placeholder {
  color: var(--text-muted);
}

.search-clear-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  color: var(--text-muted);
  font-size: 1rem;
  display: none;
  align-items: center;
  justify-content: center;
}

.search-clear-btn:hover {
  color: var(--text-primary);
}

/* Search Results Dropdown */
.search-dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  margin-top: 8px;
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  max-height: 480px;
  overflow-y: auto;
  z-index: 1050;
  display: none;
}

.search-dropdown.active {
  display: block;
}

.search-results-header {
  padding: 8px 14px;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--text-muted);
  border-bottom: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: var(--bg-tertiary);
}

.search-result-item {
  padding: 12px 14px;
  border-bottom: 1px solid var(--border-color);
  cursor: pointer;
  transition: var(--transition);
}

.search-result-item:hover, .search-result-item:focus {
  background-color: var(--bg-card-hover);
}

.search-result-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
}

.result-chapter-badge {
  font-size: 0.7rem;
  background-color: var(--brand-blue-bg);
  color: var(--brand-blue);
  padding: 2px 8px;
  border-radius: 4px;
  font-weight: 600;
}

.result-page-badge {
  font-size: 0.7rem;
  background-color: var(--bg-tertiary);
  color: var(--text-muted);
  padding: 2px 6px;
  border-radius: 4px;
}

.result-section-title {
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--text-primary);
}

.result-snippet {
  font-size: 0.85rem;
  color: var(--text-secondary);
  line-height: 1.5;
}

.result-highlight {
  background-color: rgba(245, 158, 11, 0.35);
  color: inherit;
  font-weight: 700;
  padding: 0 2px;
  border-radius: 2px;
}

/* Header Action Buttons */
.header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}

.action-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background-color: var(--bg-tertiary);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  font-family: inherit;
  font-size: 0.85rem;
  font-weight: 600;
  transition: var(--transition);
  text-decoration: none;
}

.action-btn:hover {
  background-color: var(--bg-card-hover);
  color: var(--text-primary);
  border-color: var(--border-light);
}

.action-btn svg {
  width: 16px;
  height: 16px;
  fill: currentColor;
}

.action-btn.btn-accent {
  background-color: var(--brand-blue);
  color: #fff;
  border-color: var(--brand-blue);
}
.action-btn.btn-accent:hover {
  filter: brightness(1.1);
}

/* Tab Bar */
.tabs-nav-bar {
  display: flex;
  overflow-x: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--border-light) transparent;
  padding: 0 16px;
  border-top: 1px solid var(--border-color);
  background-color: var(--bg-secondary);
  gap: 4px;
}

.tabs-nav-bar::-webkit-scrollbar {
  height: 4px;
}

.tabs-nav-bar::-webkit-scrollbar-thumb {
  background-color: var(--border-light);
  border-radius: 4px;
}

.tab-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  white-space: nowrap;
  padding: 9px 14px;
  background: transparent;
  border: none;
  border-bottom: 3px solid transparent;
  color: var(--text-muted);
  cursor: pointer;
  font-family: inherit;
  font-size: 0.88rem;
  font-weight: 600;
  transition: var(--transition);
  text-decoration: none;
}

.tab-btn:hover {
  color: var(--text-primary);
  background-color: var(--bg-card-hover);
}

.tab-btn.active {
  color: var(--brand-blue);
  border-bottom-color: var(--brand-blue);
  background-color: var(--brand-blue-bg);
}

.tab-num {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  background-color: var(--bg-tertiary);
  padding: 1px 6px;
  border-radius: 4px;
}

.tab-pages {
  font-size: 0.72rem;
  background-color: rgba(255, 255, 255, 0.08);
  padding: 1px 5px;
  border-radius: 10px;
  color: var(--text-muted);
}
[data-theme="light"] .tab-pages {
  background-color: rgba(0, 0, 0, 0.06);
}

/* App Main Layout */
.app-container {
  display: flex;
  margin-top: var(--header-height);
  min-height: calc(100vh - var(--header-height));
}

/* Sidebar TOC */
.sidebar {
  width: var(--sidebar-width);
  flex-shrink: 0;
  position: sticky;
  top: var(--header-height);
  height: calc(100vh - var(--header-height));
  overflow-y: auto;
  background-color: var(--bg-secondary);
  border-left: 1px solid var(--border-color);
  padding: 16px 12px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.sidebar-title {
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 0 8px 8px;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.toc-tree {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.toc-item {
  display: flex;
  flex-direction: column;
}

.toc-link {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 6px 10px;
  border-radius: var(--radius-sm);
  color: var(--text-secondary);
  text-decoration: none;
  font-size: 0.86rem;
  transition: var(--transition);
}

.toc-link:hover {
  background-color: var(--bg-card-hover);
  color: var(--text-primary);
}

.toc-link.active {
  background-color: var(--brand-blue-bg);
  color: var(--brand-blue);
  font-weight: 700;
}

.toc-sub-tree {
  list-style: none;
  margin-right: 14px;
  padding-right: 8px;
  border-right: 2px solid var(--border-color);
  display: flex;
  flex-direction: column;
  gap: 2px;
  margin-top: 2px;
}

.toc-sub-tree .toc-link {
  font-size: 0.8rem;
  padding: 4px 8px;
}

/* Content Area */
.main-content {
  flex: 1;
  max-width: 1050px;
  margin: 0 auto;
  padding: 24px 28px 80px;
  width: 100%;
}

.chapter-view {
  display: none;
}

.chapter-view.active {
  display: block;
  animation: fadeIn 0.25s ease-in-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Breadcrumbs & Header */
.chapter-hero {
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 20px 24px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
}

.breadcrumbs {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-bottom: 8px;
}

.breadcrumbs a {
  color: inherit;
  text-decoration: none;
}
.breadcrumbs a:hover {
  color: var(--brand-blue);
}

.chapter-main-title {
  font-size: 1.8rem;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}

.chapter-meta-pills {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.82rem;
}

.meta-pill {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 3px 10px;
  border-radius: 12px;
  background-color: var(--bg-tertiary);
  color: var(--text-secondary);
  font-weight: 600;
}

.meta-pill.pill-primary {
  background-color: var(--brand-blue-bg);
  color: var(--brand-blue);
}

/* Section Card */
.doc-section {
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 24px;
  margin-bottom: 24px;
  box-shadow: var(--shadow-sm);
  transition: box-shadow 0.3s ease, border-color 0.3s ease;
  position: relative;
}

.doc-section:target, .doc-section.pulse-highlight {
  border-color: var(--brand-amber);
  box-shadow: 0 0 0 4px var(--brand-amber-bg), var(--shadow-md);
  animation: targetPulse 3.5s ease-out;
}

@keyframes targetPulse {
  0% { box-shadow: 0 0 0 6px rgba(245, 158, 11, 0.6); }
  50% { box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.3); }
  100% { box-shadow: none; }
}

.section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border-color);
}

.section-title {
  font-size: 1.35rem;
  font-weight: 700;
  color: var(--text-primary);
  display: flex;
  align-items: center;
  gap: 8px;
}

.section-page-tag {
  font-size: 0.78rem;
  background-color: var(--bg-tertiary);
  color: var(--text-muted);
  padding: 2px 8px;
  border-radius: 12px;
  font-weight: 600;
}

.section-actions {
  display: flex;
  align-items: center;
  gap: 6px;
}

.icon-btn {
  background: none;
  border: 1px solid transparent;
  color: var(--text-muted);
  padding: 4px 6px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: var(--transition);
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-btn:hover {
  background-color: var(--bg-tertiary);
  color: var(--text-primary);
  border-color: var(--border-color);
}

.icon-btn.bookmarked {
  color: var(--brand-amber);
}

/* Callout Alert Boxes */
.callout {
  border-radius: var(--radius-sm);
  padding: 14px 18px;
  margin: 16px 0;
  display: flex;
  flex-direction: column;
  gap: 6px;
  border-right: 4px solid;
}

.callout-title {
  font-weight: 700;
  font-size: 0.95rem;
  display: flex;
  align-items: center;
  gap: 8px;
}

.callout-content {
  font-size: 0.9rem;
  line-height: 1.6;
}

.callout-warning {
  background-color: var(--brand-red-bg);
  border-right-color: var(--brand-red);
  color: var(--text-primary);
}
.callout-warning .callout-title {
  color: var(--brand-red);
}

.callout-note {
  background-color: var(--brand-blue-bg);
  border-right-color: var(--brand-blue);
  color: var(--text-primary);
}
.callout-note .callout-title {
  color: var(--brand-blue);
}

.callout-suggestion {
  background-color: var(--brand-green-bg);
  border-right-color: var(--brand-green);
  color: var(--text-primary);
}
.callout-suggestion .callout-title {
  color: var(--brand-green);
}

.callout-path {
  background-color: var(--bg-tertiary);
  border-right-color: var(--brand-purple);
  padding: 10px 16px;
}
.callout-path .path-code {
  font-family: var(--font-mono);
  font-size: 0.92rem;
  font-weight: 700;
  color: #38bdf8;
  direction: ltr;
  display: inline-block;
}
.callout-path .path-desc {
  font-size: 0.82rem;
  color: var(--text-muted);
  margin-top: 4px;
}

/* Tables */
.table-responsive {
  width: 100%;
  overflow-x: auto;
  margin: 16px 0;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-color);
  background-color: var(--bg-card);
}

.doc-table {
  width: 100%;
  border-collapse: collapse;
  text-align: right;
  font-size: 0.88rem;
}

.doc-table th {
  background-color: var(--bg-tertiary);
  color: var(--text-primary);
  padding: 10px 14px;
  font-weight: 700;
  border-bottom: 2px solid var(--border-light);
  white-space: nowrap;
}

.doc-table td {
  padding: 10px 14px;
  border-bottom: 1px solid var(--border-color);
  color: var(--text-secondary);
  vertical-align: top;
}

.doc-table tr:hover td {
  background-color: var(--bg-card-hover);
}

.doc-table td bdi {
  margin: 1px 0;
}

/* Figures & Images */
.figure-card {
  background-color: var(--bg-tertiary);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 12px;
  margin: 20px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  transition: var(--transition);
}

.figure-card:hover {
  border-color: var(--border-light);
}

.figure-img-wrapper {
  position: relative;
  width: 100%;
  max-width: 720px;
  cursor: zoom-in;
  overflow: hidden;
  border-radius: var(--radius-sm);
  display: flex;
  justify-content: center;
  background-color: rgba(0, 0, 0, 0.2);
}

.figure-img {
  width: 100%;
  height: auto;
  max-height: 520px;
  object-fit: contain;
  transition: transform 0.25s ease;
  display: block;
}

.figure-img-wrapper:hover .figure-img {
  transform: scale(1.015);
}

.zoom-hint {
  position: absolute;
  bottom: 8px;
  left: 8px;
  background-color: rgba(15, 23, 42, 0.85);
  color: #fff;
  font-size: 0.72rem;
  padding: 4px 8px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  gap: 4px;
  pointer-events: none;
  backdrop-filter: blur(4px);
}

.figure-caption {
  font-size: 0.86rem;
  color: var(--text-secondary);
  text-align: center;
  margin-top: 10px;
  line-height: 1.5;
  padding: 0 8px;
}

.figure-caption strong {
  color: var(--brand-amber);
}

/* Steps list */
.step-list {
  list-style: none;
  counter-reset: step-counter;
  margin: 16px 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.step-item {
  position: relative;
  padding-right: 36px;
  font-size: 0.92rem;
  line-height: 1.6;
}

.step-item::before {
  counter-increment: step-counter;
  content: counter(step-counter);
  position: absolute;
  right: 0;
  top: 0;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background-color: var(--brand-blue);
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 700;
  font-family: var(--font-mono);
}

/* Lightbox Modal */
.lightbox-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(10, 15, 30, 0.94);
  backdrop-filter: blur(8px);
  z-index: 2000;
  display: none;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  touch-action: none;
}

.lightbox-modal.active {
  display: flex;
}

.lightbox-toolbar {
  position: absolute;
  top: 16px;
  left: 16px;
  right: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 2010;
}

.lightbox-controls {
  display: flex;
  gap: 8px;
}

.lb-btn {
  background-color: rgba(30, 41, 59, 0.85);
  border: 1px solid var(--border-color);
  color: #fff;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 1.2rem;
  transition: var(--transition);
}

.lb-btn:hover {
  background-color: var(--brand-blue);
}

.lightbox-viewport {
  width: 100%;
  height: 100%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: grab;
}

.lightbox-viewport.grabbing {
  cursor: grabbing;
}

.lightbox-image {
  max-width: 90vw;
  max-height: 80vh;
  object-fit: contain;
  transform-origin: center center;
  transition: transform 0.1s ease-out;
  user-select: none;
  -webkit-user-drag: none;
}

.lightbox-caption-bar {
  position: absolute;
  bottom: 20px;
  left: 20px;
  right: 20px;
  background-color: rgba(30, 41, 59, 0.88);
  backdrop-filter: blur(6px);
  border: 1px solid var(--border-color);
  color: #fff;
  padding: 12px 18px;
  border-radius: var(--radius-md);
  text-align: center;
  font-size: 0.9rem;
  max-width: 800px;
  margin: 0 auto;
}

/* Floating Action Buttons */
.fab-container {
  position: fixed;
  bottom: 24px;
  left: 24px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  z-index: 999;
}

.fab-btn {
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  width: 46px;
  height: 46px;
  border-radius: 50%;
  box-shadow: var(--shadow-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition);
  position: relative;
}

.fab-btn:hover {
  background-color: var(--brand-blue);
  color: #fff;
  border-color: var(--brand-blue);
  transform: translateY(-2px);
}

.fab-btn svg {
  width: 20px;
  height: 20px;
  fill: currentColor;
}

.fab-tooltip {
  position: absolute;
  right: 56px;
  white-space: nowrap;
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 0.78rem;
  font-weight: 600;
  box-shadow: var(--shadow-md);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease;
}

.fab-btn:hover .fab-tooltip {
  opacity: 1;
}

/* Resume Banner */
.resume-banner {
  background-color: var(--brand-blue-bg);
  border: 1px solid var(--brand-blue);
  border-radius: var(--radius-md);
  padding: 12px 18px;
  margin-bottom: 20px;
  display: none;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.resume-banner.active {
  display: flex;
}

.resume-text {
  font-size: 0.88rem;
  color: var(--text-primary);
}

/* Printable Checklist Form */
.print-checklist-header {
  border: 2px solid var(--text-primary);
  padding: 16px;
  margin-bottom: 20px;
  border-radius: var(--radius-sm);
}

.checklist-meta-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
  margin-top: 10px;
}

.meta-field {
  display: flex;
  gap: 8px;
  font-size: 0.88rem;
  border-bottom: 1px dotted var(--border-light);
  padding-bottom: 4px;
}

/* Modal styles for Bookmarks */
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(4px);
  z-index: 1500;
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.modal-backdrop.active {
  display: flex;
}

.modal-card {
  background-color: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  max-width: 550px;
  width: 100%;
  max-height: 80vh;
  display: flex;
  flex-direction: column;
  box-shadow: var(--shadow-lg);
}

.modal-header {
  padding: 16px 20px;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.modal-title {
  font-size: 1.15rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 8px;
}

.modal-body {
  padding: 16px 20px;
  overflow-y: auto;
}

.bookmark-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.bookmark-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px 14px;
  background-color: var(--bg-tertiary);
  border-radius: var(--radius-sm);
  transition: var(--transition);
}

.bookmark-item:hover {
  background-color: var(--bg-card-hover);
}

.bookmark-link {
  color: var(--text-primary);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
}

/* Responsive adjustments */
@media (max-width: 1024px) {
  .sidebar {
    position: fixed;
    top: var(--header-height);
    right: -320px;
    z-index: 1010;
    transition: right 0.3s ease;
    box-shadow: var(--shadow-lg);
  }
  .sidebar.mobile-open {
    right: 0;
  }
  .sidebar-backdrop {
    position: fixed;
    top: var(--header-height);
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1005;
    display: none;
  }
  .sidebar-backdrop.active {
    display: block;
  }
}

@media (max-width: 768px) {
  :root {
    --header-height: 140px;
  }
  .top-bar {
    flex-wrap: wrap;
    padding: 8px 12px;
  }
  .search-wrapper {
    order: 3;
    max-width: 100%;
    width: 100%;
    margin-top: 4px;
  }
  .main-content {
    padding: 16px 14px 80px;
  }
  .chapter-main-title {
    font-size: 1.4rem;
  }
  .section-title {
    font-size: 1.15rem;
  }
  .fab-container {
    bottom: 16px;
    left: 16px;
  }
}

/* Print Styles */
@media print {
  body {
    background-color: #fff !important;
    color: #000 !important;
  }
  .app-header, .sidebar, .fab-container, .resume-banner, .section-actions, .lightbox-modal, .modal-backdrop {
    display: none !important;
  }
  .app-container {
    margin-top: 0 !important;
  }
  .main-content {
    max-width: 100% !important;
    padding: 0 !important;
  }
  .chapter-view {
    display: none !important;
  }
  .chapter-view.print-active {
    display: block !important;
  }
  .doc-section {
    border: 1px solid #ccc !important;
    background: transparent !important;
    page-break-inside: avoid;
    box-shadow: none !important;
  }
  .figure-img {
    max-height: 400px !important;
  }
}
"""
