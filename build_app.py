# -*- coding: utf-8 -*-
"""
Main build script for Teledata One Web Application.
Assembles all modules into a production single-file standalone index.html,
plus PWA and Capacitor packaging configuration.
"""
import os
import json
import base64

from css_styles import CSS_CONTENT
from content_ch1_to_ch6 import get_ch1_to_ch6_html
from content_ch7 import get_ch7_html
from content_ch8_to_ch9 import get_ch8_to_ch9_html
from content_ch10 import get_ch10_html
from content_ch11_and_end import get_ch11_and_end_html
from app_js import APP_JS_CONTENT

base_dir = r"C:\Users\PREDATOR\.gemini\antigravity\scratch\teledata-one-guide"

with open(os.path.join(base_dir, "images_base64.json"), "r", encoding="utf-8") as f:
    images = json.load(f)

logo_b64 = images.get("logo", "")

# Build Navigation Tabs with Chapter numbers, names, start pages, and page count difference
tabs_data = [
    {"id": "cover", "num": "0", "title": "الغلاف والبيانات", "page": "ص 1", "diff": "6 ص"},
    {"id": "ch1", "num": "1", "title": "مقدمة الدليل", "page": "ص 7", "diff": "2 ص"},
    {"id": "ch2", "num": "2", "title": "السلامة والضمان", "page": "ص 9", "diff": "1 ص"},
    {"id": "ch3", "num": "3", "title": "تعريف المنتج", "page": "ص 10", "diff": "3 ص"},
    {"id": "ch4", "num": "4", "title": "إدارة الجهاز", "page": "ص 13", "diff": "1 ص"},
    {"id": "ch5", "num": "5", "title": "المواصفات التقنية", "page": "ص 14", "diff": "4 ص"},
    {"id": "ch6", "num": "6", "title": "تكوين العتاد", "page": "ص 18", "diff": "1 ص"},
    {"id": "ch7", "num": "7", "title": "التخطيط والتوصيلات", "page": "ص 19", "diff": "27 ص"},
    {"id": "ch8", "num": "8", "title": "لوحة التحكم", "page": "ص 46", "diff": "4 ص"},
    {"id": "ch9", "num": "9", "title": "العمليات الأساسية", "page": "ص 50", "diff": "7 ص"},
    {"id": "ch10", "num": "10", "title": "التكوين", "page": "ص 57", "diff": "28 ص"},
    {"id": "ch11", "num": "11", "title": "الاستخدام", "page": "ص 85", "diff": "10 ص"},
    {"id": "notes", "num": "12", "title": "ملاحظات ختامية", "page": "ص 95", "diff": "1 ص"},
    {"id": "faults", "num": "⚠️", "title": "الأعطال والرسائل", "page": "دليل سريع", "diff": ""},
    {"id": "maint", "num": "🛠️", "title": "دليل الصيانة", "page": "سجل المتابعة", "diff": ""}
]

tabs_html = ""
for t in tabs_data:
    tabs_html += f"""
    <button class="tab-btn {'active' if t['id'] == 'cover' else ''}" data-chapter="{t['id']}" onclick="showChapter('{t['id']}')">
      <span class="tab-num">{t['num']}</span>
      <span class="tab-title">{t['title']}</span>
      <span class="tab-pages">{t['page']}{' · ' + t['diff'] if t['diff'] else ''}</span>
    </button>
    """

full_html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
  <title>Teledata One | الدليل التفاعلي الذكي للوحة إنذار الحريق</title>
  <meta name="description" content="تطبيق ويب تفاعلي ودليل المستخدم والتركيب للوحة إنذار الحريق Teledata One. يعمل دون إنترنت ومكتفٍ بذاته بالكامل.">
  <meta name="theme-color" content="#0f172a">
  <link rel="manifest" href="manifest.json">
  <style>
{CSS_CONTENT}
  </style>
</head>
<body>

  <!-- Top Fixed Application Header -->
  <header class="app-header">
    <div class="top-bar">
      <!-- Brand -->
      <div class="brand-section">
        <button class="action-btn" onclick="toggleMobileSidebar()" style="display: none; padding: 6px 10px;" id="mobile-menu-btn" title="فهرس الفصل">☰</button>
        <img src="{logo_b64}" alt="Teledata Logo" class="brand-logo-img">
        <div class="brand-title">
          <div class="brand-title-main">
            <span>Teledata One</span>
            <span class="brand-badge">EN 54-2/4</span>
          </div>
          <span class="brand-subtitle">دليل المستخدم والتركيب الذكي (الإصدار 1.3.7)</span>
        </div>
      </div>

      <!-- Omnisearch Bar -->
      <div class="search-wrapper">
        <div class="search-input-box">
          <svg class="search-icon" viewBox="0 0 24 24">
            <path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
          </svg>
          <input type="text" id="search-input" class="search-input" placeholder="ابحث في الدليل (عناوين، أعطال، أكواد J4، كواشف، مصطلحات)..." oninput="handleSearchInput(event)">
          <button id="search-clear-btn" class="search-clear-btn" onclick="clearSearch()" title="مسح">✕</button>
        </div>
        
        <!-- Live Search Dropdown -->
        <div id="search-dropdown" class="search-dropdown">
          <div class="search-results-header">
            <span>نتائج البحث الفوري</span>
            <span id="search-count">0 نتيجة</span>
          </div>
          <div id="search-results-list"></div>
        </div>
      </div>

      <!-- Quick Header Action Buttons -->
      <div class="header-actions">
        <button class="action-btn" onclick="showChapter('faults')" title="جدول الأعطال والرسائل والأكواد">
          ⚠️ <span class="hide-mobile">الأعطال</span>
        </button>
        <button class="action-btn" onclick="showChapter('maint')" title="دليل الصيانة وسجل المتابعة">
          🛠️ <span class="hide-mobile">الصيانة</span>
        </button>
        <button class="action-btn" onclick="openBookmarksModal()" title="الإشارات المرجعية المحفوظة">
          📑 <span class="hide-mobile">الإشارات</span>
        </button>
        <button class="action-btn" onclick="printCurrentChapter()" title="طباعة هذا الفصل">
          🖨️
        </button>
        <button id="theme-toggle-btn" class="action-btn" onclick="toggleTheme()" title="تبديل الوضع الليلي / النهاري">
          🌙
        </button>
      </div>
    </div>

    <!-- Scrollable Chapter Tab Bar -->
    <nav class="tabs-nav-bar">
      {tabs_html}
    </nav>
  </header>

  <!-- Mobile Sidebar Backdrop -->
  <div id="sidebar-backdrop" class="sidebar-backdrop" onclick="closeMobileSidebar()"></div>

  <!-- App Main Layout Container -->
  <div class="app-container">
    <!-- Active Chapter Sticky Sidebar (Collapsible Tree) -->
    <aside id="app-sidebar" class="sidebar">
      <div class="sidebar-title">
        <span>فهرس الفصل الحالي</span>
        <button class="icon-btn" onclick="closeMobileSidebar()" style="display: none;" id="sidebar-close-btn">✕</button>
      </div>
      <ul id="sidebar-toc-tree" class="toc-tree">
        <!-- Dynamically updated based on active chapter -->
      </ul>
      <div style="margin-top: auto; padding-top: 12px; border-top: 1px solid var(--border-color); font-size: 0.78rem; color: var(--text-muted); text-align: center;">
        Teledata s.r.l. Milan, Italy<br>
        v. 1.3.7 ENG — نوفمبر 2019
      </div>
    </aside>

    <!-- Main Content Reader -->
    <main class="main-content">
      <!-- Last Read Position Banner -->
      <div id="resume-banner" class="resume-banner">
        <div class="resume-text" id="resume-text"></div>
        <div style="display: flex; gap: 8px;">
          <button id="resume-btn" class="action-btn btn-accent" style="padding: 4px 10px; font-size: 0.82rem;">استئناف القراءة</button>
          <button id="resume-dismiss-btn" class="icon-btn" title="إغلاق">✕</button>
        </div>
      </div>

      <!-- Chapters HTML Inclusions -->
      {get_ch1_to_ch6_html(images)}
      {get_ch7_html(images)}
      {get_ch8_to_ch9_html(images)}
      {get_ch10_html(images)}
      {get_ch11_and_end_html(images)}
    </main>
  </div>

  <!-- Floating Action Buttons -->
  <div class="fab-container">
    <button class="fab-btn" onclick="showChapter('cover')" title="الصفحة الرئيسية">
      <span class="fab-tooltip">الصفحة الرئيسية</span>
      <svg viewBox="0 0 24 24"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>
    </button>
    <button class="fab-btn" onclick="goBack()" title="رجوع لآخر موضع">
      <span class="fab-tooltip">رجوع</span>
      <svg viewBox="0 0 24 24"><path d="M20 11H7.83l5.59-5.59L12 4l-8 8 8 8 1.41-1.41L7.83 13H20v-2z"/></svg>
    </button>
    <button class="fab-btn" onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }})" title="أعلى الصفحة">
      <span class="fab-tooltip">للأعلى</span>
      <svg viewBox="0 0 24 24"><path d="M7.41 15.41L12 10.83l4.59 4.58L18 14l-6-6-6 6z"/></svg>
    </button>
  </div>

  <!-- Interactive Lightbox Modal -->
  <div id="lightbox-modal" class="lightbox-modal" onclick="if(event.target===this) closeLightbox()">
    <div class="lightbox-toolbar">
      <div class="lightbox-controls">
        <button class="lb-btn" onclick="zoomLightbox(1.25)" title="تكبير">+</button>
        <button class="lb-btn" onclick="zoomLightbox(0.8)" title="تصغير">−</button>
        <button class="lb-btn" onclick="resetLightboxZoom()" title="إعادة ضبط 100%">1:1</button>
        <button class="lb-btn" onclick="toggleLightboxFullscreen()" title="ملء الشاشة">⛶</button>
      </div>
      <button class="lb-btn" onclick="closeLightbox()" title="إغلاق (Esc)">✕</button>
    </div>
    <div id="lightbox-viewport" class="lightbox-viewport">
      <img id="lightbox-image" class="lightbox-image" src="" alt="Zoomable Figure">
    </div>
    <div id="lightbox-caption" class="lightbox-caption-bar"></div>
  </div>

  <!-- Bookmarks Modal -->
  <div id="bookmarks-modal" class="modal-backdrop" onclick="if(event.target===this) closeBookmarksModal()">
    <div class="modal-card">
      <div class="modal-header">
        <div class="modal-title">📑 الإشارات المرجعية المحفوظة</div>
        <button class="icon-btn" onclick="closeBookmarksModal()">✕</button>
      </div>
      <div class="modal-body">
        <ul id="bookmarks-list" class="bookmark-list"></ul>
      </div>
    </div>
  </div>

  <script>
{APP_JS_CONTENT}
  </script>
</body>
</html>
"""

out_html_path = os.path.join(base_dir, "index.html")
with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Generated standalone index.html successfully! Size: {os.path.getsize(out_html_path) / 1024 / 1024:.2f} MB")

# Generate manifest.json for PWA & Capacitor
manifest = {
    "name": "Teledata One Fire Alarm Manual",
    "short_name": "Teledata One",
    "description": "دليل المستخدم والتركيب الذكي للوحة إنذار الحريق Teledata One",
    "start_url": "./index.html",
    "display": "standalone",
    "orientation": "any",
    "background_color": "#0f172a",
    "theme_color": "#0f172a",
    "icons": [
        {
            "src": "assets/images_webp/page_1_img_2_9.webp",
            "sizes": "512x512",
            "type": "image/webp"
        }
    ]
}

with open(os.path.join(base_dir, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

# Generate sw.js (Offline cache Service Worker)
sw_content = """// Service Worker for Teledata One Offline PWA
const CACHE_NAME = 'teledata-one-v1';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './manifest.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request).catch(() => caches.match('./index.html'));
    })
  );
});
"""

with open(os.path.join(base_dir, "sw.js"), "w", encoding="utf-8") as f:
    f.write(sw_content)

# Generate capacitor.config.json for APK building
capacitor_config = {
    "appId": "com.teledata.one.manual",
    "appName": "Teledata One Manual",
    "webDir": ".",
    "bundledWebRuntime": False,
    "android": {
        "allowMixedContent": True
    }
}

with open(os.path.join(base_dir, "capacitor.config.json"), "w", encoding="utf-8") as f:
    json.dump(capacitor_config, f, indent=2)

# Generate package.json
package_json = {
    "name": "teledata-one-guide",
    "version": "1.3.7",
    "description": "Interactive Offline User & Installation Manual for Teledata One Fire Alarm Control Panel",
    "main": "index.html",
    "scripts": {
        "build": "python build_app.py",
        "capacitor:add:android": "npx cap add android",
        "capacitor:build": "npx cap sync"
    },
    "keywords": [
        "fire-alarm",
        "teledata-one",
        "user-manual",
        "installation-guide",
        "pwa",
        "capacitor",
        "offline"
    ],
    "author": "almhtrf111312",
    "license": "MIT"
}

with open(os.path.join(base_dir, "package.json"), "w", encoding="utf-8") as f:
    json.dump(package_json, f, indent=2)

print("All configuration files (manifest.json, sw.js, capacitor.config.json, package.json) generated!")
