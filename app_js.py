# -*- coding: utf-8 -*-
"""
Client-side JavaScript for Teledata One Web Application.
Offline-capable, smart bilingual search, lightbox zoom/pan, bookmarks, reading progress.
"""

APP_JS_CONTENT = """
// State
let currentChapter = 'cover';
let historyStack = [];
let bookmarks = JSON.parse(localStorage.getItem('teledata_bookmarks') || '[]');
let lastReadPos = JSON.parse(localStorage.getItem('teledata_last_pos') || 'null');

// Arabic Normalization
function normalizeArabic(text) {
  if (!text) return '';
  return text
    .replace(/[\\u064B-\\u065F\\u0670\\u0640]/g, '') // remove harakat and tatweel
    .replace(/[إأآا]/g, 'ا')
    .replace(/ة/g, 'ه')
    .replace(/[يى]/g, 'ي')
    .toLowerCase()
    .trim();
}

// Synonyms dictionary for parallel bilingual search
const synonyms = {
  'fault': ['عطل', 'اعطال', 'خلل', 'fault', 'faults'],
  'عطل': ['fault', 'faults', 'عطل', 'اعطال'],
  'alarm': ['انذار', 'حريق', 'alarms', 'alarm'],
  'انذار': ['alarm', 'alarms', 'انذار'],
  'loop': ['حلقه', 'حلقات', 'loop', 'loops'],
  'حلقه': ['loop', 'loops', 'حلقه'],
  'detector': ['كاشف', 'كواشف', 'detector', 'detectors'],
  'كاشف': ['detector', 'detectors', 'كاشف'],
  'module': ['وحده', 'وحدات', 'module', 'modules'],
  'وحده': ['module', 'modules', 'وحده'],
  'reset': ['اعاده ضبط', 'اعاده', 'reset'],
  'ضبط': ['reset', 'configure', 'ضبط'],
  'silence': ['كتم', 'صامت', 'silence', 'silenced', 'buzzer'],
  'كتم': ['silence', 'silenced', 'buzzer', 'كتم'],
  'zone': ['منطقه', 'مناطق', 'zone', 'zones'],
  'منطقه': ['zone', 'zones', 'منطقه'],
  'battery': ['بطاريه', 'بطاريات', 'battery', 'batteries'],
  'بطاريه': ['battery', 'batteries', 'بطاريه'],
  'power': ['تغذيه', 'طاقه', 'power', 'supply'],
  'تغذيه': ['power', 'supply', 'تغذيه'],
  'evacuation': ['اخلاء', 'evacuation'],
  'اخلاء': ['evacuation', 'اخلاء'],
  'maintenance': ['صيانه', 'maintenance'],
  'صيانه': ['maintenance', 'صيانه'],
  'ground': ['ارضي', 'تاريض', 'ground fault', 'ارضي'],
  'ارضي': ['ground', 'ground fault', 'تاريض']
};

// Search Database Index
let searchIndex = [];

function buildSearchIndex() {
  searchIndex = [];
  document.querySelectorAll('.doc-section').forEach(sec => {
    const secId = sec.id || '';
    const titleEl = sec.querySelector('.section-title');
    const title = titleEl ? titleEl.innerText : '';
    const pageEl = sec.querySelector('.section-page-tag');
    const page = pageEl ? pageEl.innerText : '';
    const chapterView = sec.closest('.chapter-view');
    const chId = chapterView ? chapterView.id.replace('view-', '') : 'cover';
    const text = sec.innerText;
    
    searchIndex.push({
      secId: secId,
      chapterId: chId,
      title: title,
      page: page,
      rawText: text,
      normText: normalizeArabic(text)
    });
  });
}

// Lightbox state
let currentScale = 1;
let translateX = 0;
let translateY = 0;
let isDragging = false;
let startX, startY;

function openLightbox(src, caption) {
  const modal = document.getElementById('lightbox-modal');
  const img = document.getElementById('lightbox-image');
  const cap = document.getElementById('lightbox-caption');
  
  img.src = src;
  cap.innerHTML = caption || '';
  currentScale = 1;
  translateX = 0;
  translateY = 0;
  updateImageTransform();
  
  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  const modal = document.getElementById('lightbox-modal');
  modal.classList.remove('active');
  document.body.style.overflow = '';
}

function zoomLightbox(factor) {
  currentScale = Math.min(Math.max(currentScale * factor, 0.5), 5);
  updateImageTransform();
}

function resetLightboxZoom() {
  currentScale = 1;
  translateX = 0;
  translateY = 0;
  updateImageTransform();
}

function updateImageTransform() {
  const img = document.getElementById('lightbox-image');
  img.style.transform = `translate(${translateX}px, ${translateY}px) scale(${currentScale})`;
}

// Fullscreen toggle for Lightbox
function toggleLightboxFullscreen() {
  const modal = document.getElementById('lightbox-modal');
  if (!document.fullscreenElement) {
    if (modal.requestFullscreen) modal.requestFullscreen();
  } else {
    if (document.exitFullscreen) document.exitFullscreen();
  }
}

// Search functionality
function handleSearchInput(e) {
  const query = e.target.value.trim();
  const clearBtn = document.getElementById('search-clear-btn');
  const dropdown = document.getElementById('search-dropdown');
  const countEl = document.getElementById('search-count');
  const resultsContainer = document.getElementById('search-results-list');
  
  if (query.length > 0) {
    clearBtn.style.display = 'flex';
  } else {
    clearBtn.style.display = 'none';
    dropdown.classList.remove('active');
    return;
  }
  
  const normQuery = normalizeArabic(query);
  const words = normQuery.split(/\\s+/);
  
  // Expand with synonyms
  let expandedTerms = [...words];
  words.forEach(w => {
    if (synonyms[w]) {
      expandedTerms.push(...synonyms[w].map(s => normalizeArabic(s)));
    }
  });
  expandedTerms = [...new Set(expandedTerms)];
  
  const matches = [];
  searchIndex.forEach(item => {
    let score = 0;
    let matchedSnippet = '';
    
    // Check title match
    const normTitle = normalizeArabic(item.title);
    if (normTitle.includes(normQuery)) {
      score += 15;
    }
    
    // Check words match
    let matchCount = 0;
    expandedTerms.forEach(term => {
      if (item.normText.includes(term)) {
        matchCount++;
        score += 3;
      }
    });
    
    if (score > 0) {
      // Find snippet
      const idx = item.normText.indexOf(words[0]);
      const start = Math.max(0, idx - 40);
      const end = Math.min(item.rawText.length, idx + 100);
      let snip = item.rawText.substring(start, end).replace(/\\s+/g, ' ');
      
      // Highlight matching word in snippet
      words.forEach(w => {
        const regex = new RegExp(`(${w})`, 'gi');
        snip = snip.replace(regex, '<mark class="result-highlight">$1</mark>');
      });
      
      matches.push({
        item: item,
        score: score,
        snippet: snip
      });
    }
  });
  
  // Sort by score
  matches.sort((a, b) => b.score - a.score);
  
  // Render dropdown
  resultsContainer.innerHTML = '';
  countEl.innerText = `${matches.length} نتيجة`;
  
  if (matches.length === 0) {
    resultsContainer.innerHTML = `
      <div style="padding: 20px; text-align: center; color: var(--text-muted); font-size: 0.9rem;">
        لم يتم العثور على نتائج مطابقة لـ "${query}".
      </div>
    `;
  } else {
    matches.slice(0, 20).forEach(m => {
      const div = document.createElement('div');
      div.className = 'search-result-item';
      div.onclick = () => {
        navigateToSection(m.item.chapterId, m.item.secId);
        dropdown.classList.remove('active');
      };
      
      const chName = getChapterTitle(m.item.chapterId);
      
      div.innerHTML = `
        <div class="search-result-header">
          <span class="result-chapter-badge">${chName}</span>
          ${m.item.page ? `<span class="result-page-badge">${m.item.page}</span>` : ''}
          <span class="result-section-title">${m.item.title || chName}</span>
        </div>
        <div class="result-snippet">...${m.snippet}...</div>
      `;
      resultsContainer.appendChild(div);
    });
  }
  
  dropdown.classList.add('active');
}

function clearSearch() {
  const input = document.getElementById('search-input');
  input.value = '';
  document.getElementById('search-clear-btn').style.display = 'none';
  document.getElementById('search-dropdown').classList.remove('active');
}

function getChapterTitle(chId) {
  const titles = {
    'cover': 'الغلاف والملكيات',
    'ch1': 'الفصل 1: مقدمة الدليل',
    'ch2': 'الفصل 2: السلامة والضمان',
    'ch3': 'الفصل 3: تعريف المنتج',
    'ch4': 'الفصل 4: إدارة الجهاز',
    'ch5': 'الفصل 5: المواصفات التقنية',
    'ch6': 'الفصل 6: تكوين العتاد',
    'ch7': 'الفصل 7: التخطيط والتوصيلات',
    'ch8': 'الفصل 8: لوحة التحكم',
    'ch9': 'الفصل 9: العمليات الأساسية',
    'ch10': 'الفصل 10: التكوين',
    'ch11': 'الفصل 11: الاستخدام',
    'notes': 'ملاحظات ختامية',
    'faults': 'الأعطال والرسائل',
    'maint': 'دليل الصيانة'
  };
  return titles[chId] || chId;
}

// Chapter & Section Navigation
function showChapter(chId, updateHistory = true) {
  if (updateHistory && currentChapter !== chId) {
    historyStack.push({ chapter: currentChapter, scroll: window.scrollY });
  }
  currentChapter = chId;
  
  // Hide all views
  document.querySelectorAll('.chapter-view').forEach(v => v.classList.remove('active'));
  
  // Show target view
  const target = document.getElementById('view-' + chId);
  if (target) {
    target.classList.add('active');
  }
  
  // Update Tab bar
  document.querySelectorAll('.tab-btn').forEach(btn => {
    if (btn.getAttribute('data-chapter') === chId) {
      btn.classList.add('active');
      btn.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    } else {
      btn.classList.remove('active');
    }
  });
  
  // Update Sidebar TOC
  updateSidebarTOC(chId);
  
  // Save position
  saveCurrentPosition(chId, '');
}

function navigateToSection(chId, secId) {
  showChapter(chId, true);
  
  if (secId) {
    setTimeout(() => {
      const el = document.getElementById(secId);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        el.classList.add('pulse-highlight');
        setTimeout(() => el.classList.remove('pulse-highlight'), 3500);
        
        saveCurrentPosition(chId, secId, el.querySelector('.section-title')?.innerText || '');
      }
    }, 120);
  } else {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
}

function goBack() {
  if (historyStack.length > 0) {
    const prev = historyStack.pop();
    showChapter(prev.chapter, false);
    if (prev.scroll) {
      setTimeout(() => window.scrollTo({ top: prev.scroll, behavior: 'smooth' }), 50);
    }
  } else {
    showChapter('cover');
  }
}

// Reading Progress Persistence
function saveCurrentPosition(chId, secId, secTitle) {
  const pos = {
    chapter: chId,
    section: secId,
    title: secTitle || getChapterTitle(chId),
    timestamp: Date.now()
  };
  localStorage.setItem('teledata_last_pos', JSON.stringify(pos));
}

function checkResumePosition() {
  const saved = localStorage.getItem('teledata_last_pos');
  if (saved) {
    try {
      const pos = JSON.parse(saved);
      if (pos && pos.chapter && pos.chapter !== 'cover') {
        const banner = document.getElementById('resume-banner');
        const textEl = document.getElementById('resume-text');
        if (banner && textEl) {
          textEl.innerHTML = `آخر موضع قرأته: <strong>${pos.title}</strong> (${getChapterTitle(pos.chapter)})`;
          banner.classList.add('active');
          document.getElementById('resume-btn').onclick = () => {
            banner.classList.remove('active');
            navigateToSection(pos.chapter, pos.section);
          };
          document.getElementById('resume-dismiss-btn').onclick = () => {
            banner.classList.remove('active');
          };
        }
      }
    } catch (e) {
      console.error(e);
    }
  }
}

// Bookmarks Management
function toggleBookmark(secId, title) {
  const idx = bookmarks.findIndex(b => b.secId === secId);
  const btn = document.querySelector(`[onclick*="${secId}"]`);
  
  if (idx > -1) {
    bookmarks.splice(idx, 1);
    if (btn) btn.classList.remove('bookmarked');
    showNotification('تمت إزالة الإشارة المرجعية');
  } else {
    bookmarks.push({
      secId: secId,
      chapter: currentChapter,
      title: title || secId,
      time: new Date().toLocaleDateString('ar-SA')
    });
    if (btn) btn.classList.add('bookmarked');
    showNotification('تم حفظ الإشارة المرجعية');
  }
  localStorage.setItem('teledata_bookmarks', JSON.stringify(bookmarks));
}

function openBookmarksModal() {
  const modal = document.getElementById('bookmarks-modal');
  const list = document.getElementById('bookmarks-list');
  list.innerHTML = '';
  
  if (bookmarks.length === 0) {
    list.innerHTML = '<li style="text-align: center; color: var(--text-muted); padding: 20px;">لا توجد إشارات مرجعية محفوظة بعد. اضغط على أيقونة 🔖 في أي قسم لحفظه.</li>';
  } else {
    bookmarks.forEach(b => {
      const li = document.createElement('li');
      li.className = 'bookmark-item';
      li.innerHTML = `
        <div>
          <a href="#${b.secId}" class="bookmark-link" onclick="closeBookmarksModal(); navigateToSection('${b.chapter}', '${b.secId}')">${b.title}</a>
          <div style="font-size: 0.75rem; color: var(--text-muted);">${getChapterTitle(b.chapter)}</div>
        </div>
        <button class="icon-btn" onclick="toggleBookmark('${b.secId}'); openBookmarksModal();" title="حذف">🗑️</button>
      `;
      list.appendChild(li);
    });
  }
  modal.classList.add('active');
}

function closeBookmarksModal() {
  document.getElementById('bookmarks-modal').classList.remove('active');
}

// Sidebar TOC generator for active chapter
function updateSidebarTOC(chId) {
  const tocContainer = document.getElementById('sidebar-toc-tree');
  if (!tocContainer) return;
  tocContainer.innerHTML = '';
  
  const currentView = document.getElementById('view-' + chId);
  if (!currentView) return;
  
  const sections = currentView.querySelectorAll('.doc-section');
  sections.forEach(sec => {
    const secId = sec.id;
    const titleEl = sec.querySelector('.section-title');
    if (!titleEl || !secId) return;
    
    const li = document.createElement('li');
    li.className = 'toc-item';
    
    const a = document.createElement('a');
    a.className = 'toc-link';
    a.href = '#' + secId;
    a.innerText = titleEl.innerText;
    a.onclick = (e) => {
      e.preventDefault();
      navigateToSection(chId, secId);
      // close mobile sidebar if open
      closeMobileSidebar();
    };
    
    li.appendChild(a);
    tocContainer.appendChild(li);
  });
}

function toggleMobileSidebar() {
  const sb = document.getElementById('app-sidebar');
  const bd = document.getElementById('sidebar-backdrop');
  sb.classList.toggle('mobile-open');
  bd.classList.toggle('active');
}

function closeMobileSidebar() {
  const sb = document.getElementById('app-sidebar');
  const bd = document.getElementById('sidebar-backdrop');
  if (sb) sb.classList.remove('mobile-open');
  if (bd) bd.classList.remove('active');
}

// Theme Toggle
function toggleTheme() {
  const html = document.documentElement;
  const current = html.getAttribute('data-theme') || 'dark';
  const target = current === 'dark' ? 'light' : 'dark';
  html.setAttribute('data-theme', target);
  localStorage.setItem('teledata_theme', target);
  
  const btn = document.getElementById('theme-toggle-btn');
  if (btn) btn.innerHTML = target === 'dark' ? '🌙' : '☀️';
}

function initTheme() {
  const saved = localStorage.getItem('teledata_theme') || 'dark';
  document.documentElement.setAttribute('data-theme', saved);
  const btn = document.getElementById('theme-toggle-btn');
  if (btn) btn.innerHTML = saved === 'dark' ? '🌙' : '☀️';
}

// Simple Notification Toast
function showNotification(msg) {
  let toast = document.getElementById('app-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'app-toast';
    toast.style.cssText = `
      position: fixed;
      bottom: 80px;
      left: 50%;
      transform: translateX(-50%);
      background-color: var(--bg-secondary);
      color: var(--text-primary);
      border: 1px solid var(--border-light);
      padding: 10px 20px;
      border-radius: 20px;
      box-shadow: var(--shadow-lg);
      font-size: 0.9rem;
      z-index: 3000;
      transition: opacity 0.3s ease;
      pointer-events: none;
    `;
    document.body.appendChild(toast);
  }
  toast.innerText = msg;
  toast.style.opacity = '1';
  setTimeout(() => {
    toast.style.opacity = '0';
  }, 2200);
}

// Print Current Chapter
function printCurrentChapter() {
  const currentView = document.getElementById('view-' + currentChapter);
  if (!currentView) return;
  
  document.querySelectorAll('.chapter-view').forEach(v => v.classList.remove('print-active'));
  currentView.classList.add('print-active');
  window.print();
}

// Faults & Codes Database
const faultsDatabase = [
  { code: 'Fire', ar: 'إنذار حريق من كاشف واحد على الأقل في النظام', color: '🔴 LED أحمر', page: 'ص 46', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'يضيء المؤشر الأحمر الرئيسي وتطلق اللوحة خرج الصفارة وتضاء مؤشرات حتى 10 كواشف في الحلقة.' },
  { code: 'Fault', ar: 'عطل عام في النظام (generic fault)', color: '🟡 LED أصفر', page: 'ص 46', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'مؤشر أصفر رئيسي يدل على وجود عطل عام في اللوحة أو أحد خطوطها أو أجهزتها.' },
  { code: 'Disablements', ar: 'أجهزة أو أجهزة طرفية معطّلة (مستثناة)', color: '🟡 LED أصفر', page: 'ص 46', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'يضيء المؤشر عند تعطيل أي جهاز أو حلقة أو منطقة أو خرج لتنبيه المشغل بأن جزءاً من النظام متجاوز.' },
  { code: 'Mon. Out. Act.', ar: 'خرج مراقَب مفعّل (Monitored Output Activated)', color: '🟡 LED أصفر', page: 'ص 46', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'يضيء عند تفعيل خط الخرج المراقب مثل صفارات الإنذار.' },
  { code: 'Mon. Out. Dis.', ar: 'خرج مراقَب معطّل (Monitored Output Disabled)', color: '🟡 LED أصفر', page: 'ص 46', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'يضيء عند استثناء أو تعطيل الخرج المراقب عن العمل.' },
  { code: 'Fault Mon. Out.', ar: 'عطل في خرج مراقَب (قطع أو دائرة قصيرة)', color: '🟡 LED أصفر', page: 'ص 47', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'يضيء عند كشف قطع أو شورت في كابل الخرج المراقب (الموصل J4 الأطراف 5 و 6).' },
  { code: 'CPU fault', ar: 'عطل في وحدة المعالجة المركزية', color: '🟡 LED أصفر', page: 'ص 47', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'عطل خطير يدل على توقف معالج اللوحة أو مراقب النظام (watchdog JP4).' },
  { code: 'Power', ar: 'تغذية رئيسية 220V موجودة', color: '🟢 LED أخضر', page: 'ص 47', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'مؤشر التغذية الرئيسي، ينطفئ فوراً عند انقطاع الكهرباء والتحول لبطاريات الاحتياط.' },
  { code: 'Test', ar: 'جهاز واحد على الأقل تحت الاختبار (Walk Test)', color: '🟡 LED أصفر', page: 'ص 47', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'يضيء المؤشر للتنبيه بأن اللوحة أو بعض أجهزتها في وضع الفحص الميداني.' },
  { code: 'Silenced', ar: 'الإنذار مكتوم مؤقتاً', color: '🟡 LED أصفر', page: 'ص 47', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'يضيء عندما يقوم المشغل بكتم جرس اللوحة والصفارات للتحقق من الإنذار.' },
  { code: 'Ext. Activation', ar: 'دائرة الإطفاء مفعّلة (غير متاحة حالياً)', color: '🟡 LED أصفر', page: 'ص 47', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'محجوز لدائرة الإطفاء التلقائي الخارجي.' },
  { code: 'Ext. Release', ar: 'دائرة الإطفاء محرّرة (غير متاحة حالياً)', color: '🟡 LED أصفر', page: 'ص 47', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'محجوز لإطلاق مادة الإطفاء.' },
  { code: 'Ext. Out Serv.', ar: 'عطل في دائرة الإطفاء (غير متاحة حالياً)', color: '🟡 LED أصفر', page: 'ص 47', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'محجوز لأعطال توصيل الإطفاء.' },
  { code: 'Ext. Locked', ar: 'دائرة الإطفاء مقفلة (غير متاحة حالياً)', color: '🟡 LED أصفر', page: 'ص 47', cat: 'led', ch: 'ch8', sec: 'sec-8-1', desc: 'محجوز لإقفال نظام الإطفاء.' },
  
  // Screen Messages
  { code: 'FAULT - Lost Comm. Loop 01 Det. 002', ar: 'فقدان الاتصال مع الكاشف رقم 002 في الحلقة 1', color: '🖥️ رسالة شاشة', page: 'ص 52', cat: 'screen', ch: 'ch9', sec: 'sec-9-1', desc: 'تظهر في شاشة Events in Progress عند انقطاع الإشارة مع الكاشف المحدد.' },
  { code: 'FAULT - Lost Comm. Loop 01 Mod. 011', ar: 'فقدان الاتصال مع الوحدة رقم 011 في الحلقة 1', color: '🖥️ رسالة شاشة', page: 'ص 52', cat: 'screen', ch: 'ch9', sec: 'sec-9-1', desc: 'تظهر عند انقطاع الاتصال مع وحدة إدخال أو إخراج معنونة.' },
  { code: 'Fault-Technology', ar: 'إنذار تكنولوجي أقل خطورة مع عطل في الوحدة', color: '🖥️ رسالة شاشة', page: 'ص 64', cat: 'screen', ch: 'ch10', sec: 'sec-10-4', desc: 'تفسير الحدث كعطل تكنولوجي بدلاً من إنذار حريق حرج.' },
  { code: 'Maint. Expiry', ar: 'تذكير انتهاء موعد الصيانة الدورية', color: '🖥️ نافذة منبثقة', page: 'ص 94', cat: 'screen', ch: 'ch11', sec: 'sec-11-7', desc: 'تظهر عند منتصف ليل التاريخ المحدد لتنبيه إدارة المنشأة بوجوب الصيانة.' },
  { code: 'Ground Fault Control', ar: 'عطل التأريض الكهربائي وتسرب الشيلد', color: '⚡ فحص كهربائي', page: 'ص 80', cat: 'hw', ch: 'ch10', sec: 'sec-10-8', desc: 'كشف تسرب التأريض بين شيلد الكابل وموصلات اللوحة أو دائرة قصر مع الهيكل.' },
  { code: 'Battery High Internal Resistance', ar: 'مقاومة البطارية الداخلية أعلى من 800mΩ', color: '🔋 فحص بطارية', page: 'ص 43', cat: 'hw', ch: 'ch7', sec: 'sec-7-9', desc: 'تطلق اللوحة إنذاراً صوتياً وبصرياً عند تدهور كفاءة البطارية.' },
  { code: 'Low Battery Voltage', ar: 'انخفاض جهد البطارية دون 21.6V', color: '🔋 جهد منخفض', page: 'ص 43', cat: 'hw', ch: 'ch7', sec: 'sec-7-9', desc: 'تطلق اللوحة إشارة صوتية ورسالة شاشة، ويلزم إعادة تغذية 230V لإعادة الشحن.' },
  { code: 'Battery Disconnected / Absent', ar: 'غياب أو عدم تركيب البطاريات الاحتياطية', color: '🔋 غياب بطارية', page: 'ص 43', cat: 'hw', ch: 'ch7', sec: 'sec-7-9', desc: 'تكتشفه اللوحة عند أول فحص أوتوماتيكي دوري وتعلن عطل صوتي وبصري.' },
  
  // Hardware & Connectors
  { code: 'J4 Pins 5 & 6 (SIR+ / SIR-)', ar: 'مخرج أجهزة الإنذار المراقَب (27Vdc @ 500mA)', color: '🔌 موصل باللوحة', page: 'ص 21، 34', cat: 'hw', ch: 'ch7', sec: 'sec-7-1', desc: 'يتطلب مقاومة نهاية خط 3.3kΩ ¼W ودايود 1N4007 لحماية المراقبة.' },
  { code: 'J4 Pins 7 & 8 (AL)', ar: 'مرحّل عطل NC جاف (Max 1A @ 30Vdc / 120Vac)', color: '🔌 مخرج مرحّل', page: 'ص 21', cat: 'hw', ch: 'ch7', sec: 'sec-7-1', desc: 'مخرج تلامس مغلق طبيعياً يُفتح عند حدوث أي عطل باللوحة.' },
  { code: 'J9 (FW+ / FW- / RET+ / RET-)', ar: 'أطراف إرسال وعودة الحلقة التناظرية الأولى', color: '🔌 موصل حلقة', page: 'ص 21، 35', cat: 'hw', ch: 'ch7', sec: 'sec-7-1', desc: 'الحلقة المغلقة تستخدم الأطراف الأربعة حتى 240 جهازاً، والمفتوحة تستخدم FW فقط حتى 32 جهازاً.' },
  { code: 'J10 (IN1, IN2, OC, GND)', ar: 'مدخلات رقمية ومخرج مجمّع مفتوح', color: '🔌 موصل منطقي', page: 'ص 21', cat: 'hw', ch: 'ch7', sec: 'sec-7-1', desc: 'إدخالان رقميان ومخرج Open Collector للتحكم المنطقي.' },
  { code: 'JP3 Jumper', ar: 'جامبر حماية البرمجة (مغلق = ممكّن)', color: '🔧 وصلة ضبط', page: 'ص 20، 49', cat: 'hw', ch: 'ch7', sec: 'sec-7-1', desc: 'يلزم إغلاقها للوصول إلى المستوى 3 وبرمجة اللوحة برمز المبرمج 33333.' },
  { code: 'JP4 Watchdog Jumper', ar: 'وصلة مراقب نظام المعالج (Watchdog)', color: '🔧 وصلة ضبط', page: 'ص 20', cat: 'hw', ch: 'ch7', sec: 'sec-7-1', desc: 'ضبط ومراقبة استقرار معالج 32-bit للوحة.' },
  { code: 'JP2 Firmware Update Jumper', ar: 'وصلة تحديث البرنامج الثابت FW', color: '🔧 وصلة ضبط', page: 'ص 20', cat: 'hw', ch: 'ch7', sec: 'sec-7-1', desc: 'تُغلق عند تحميل إصدار فيرموير جديد للوحة.' },
  
  // Diagnostic states
  { code: 'Detector Dirty (Red)', ar: 'كاشف متسخ يلزم تنظيفه أو استبداله', color: '🔴 تشخيص أحمر', page: 'ص 88', cat: 'diag', ch: 'ch11', sec: 'sec-11-4', desc: 'يظهر في قائمة Diagnostics للدلالة على وصول الغرفة للحد الأقصى للاتساخ.' },
  { code: 'Detector Near Dirty (Orange)', ar: 'كاشف يقترب من الاتساخ', color: '🟠 تشخيص برتقالي', page: 'ص 88', cat: 'diag', ch: 'ch11', sec: 'sec-11-4', desc: 'يُدرج الكاشف في جدول الصيانة الوشيك.' },
  { code: 'Detector Medium (Yellow-Green)', ar: 'كاشف نظافته متوسطة', color: '🟡 تشخيص أصفر مخضر', page: 'ص 88', cat: 'diag', ch: 'ch11', sec: 'sec-11-4', desc: 'حالة مقبولة تشغيلياً دون حاجة لإجراء فوري.' },
  { code: 'Detector Clean (Green)', ar: 'كاشف نظيف بحالة ممتازة', color: '🟢 تشخيص أخضر', page: 'ص 88', cat: 'diag', ch: 'ch11', sec: 'sec-11-4', desc: 'الكاشف نظيف وتيار الغرفة طبيعي تماماً.' },
  { code: 'Address Conflict', ar: 'تعارض عناوين (جهازان بنفس العنوان في الحلقة)', color: '⚠️ فحص تعارض', page: 'ص 90', cat: 'diag', ch: 'ch11', sec: 'sec-11-5', desc: 'يُكشف عبر Maintenance → Test → Conflicts لتغيير عنوان أحد الجهازين.' },
  { code: 'Type Mismatch', ar: 'عدم تطابق النوع الحقيقي مع المبرمج باللوحة', color: '⚠️ عدم تطابق', page: 'ص 90', cat: 'diag', ch: 'ch11', sec: 'sec-11-5', desc: 'يُكشف عبر Maintenance → Test → Mismatch (مثل برمجة كاشف كوحدة).' }
];

function populateFaultsTable(filter = 'all') {
  const tbody = document.getElementById('faults-tbody');
  if (!tbody) return;
  tbody.innerHTML = '';
  
  const filtered = faultsDatabase.filter(f => filter === 'all' || f.cat === filter);
  
  filtered.forEach(f => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><bdi style="font-weight: 700; color: #38bdf8;">${f.code}</bdi></td>
      <td><strong>${f.ar}</strong></td>
      <td>${f.color}</td>
      <td><span class="section-page-tag">${f.page}</span></td>
      <td>
        <div style="font-size: 0.84rem; margin-bottom: 4px;">${f.desc}</div>
        <a href="#${f.sec}" class="action-btn" style="padding: 2px 8px; font-size: 0.78rem;" onclick="navigateToSection('${f.ch}', '${f.sec}')">
          اذهب للصفحة في الدليل الكامل ➔
        </a>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function filterFaults(cat, btn) {
  document.querySelectorAll('#view-faults .action-btn').forEach(b => b.classList.remove('active'));
  if (btn) btn.classList.add('active');
  populateFaultsTable(cat);
}

// Lightbox event listeners for dragging and pinch-zoom
function initLightboxEvents() {
  const viewport = document.getElementById('lightbox-viewport');
  const img = document.getElementById('lightbox-image');
  
  viewport.addEventListener('mousedown', (e) => {
    if (e.target === img) {
      isDragging = true;
      startX = e.clientX - translateX;
      startY = e.clientY - translateY;
      viewport.classList.add('grabbing');
    }
  });
  
  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    translateX = e.clientX - startX;
    translateY = e.clientY - startY;
    updateImageTransform();
  });
  
  window.addEventListener('mouseup', () => {
    isDragging = false;
    viewport.classList.remove('grabbing');
  });
  
  // Wheel zoom
  viewport.addEventListener('wheel', (e) => {
    e.preventDefault();
    const delta = e.deltaY > 0 ? 0.9 : 1.1;
    zoomLightbox(delta);
  }, { passive: false });
  
  // Touch Pinch-to-zoom
  let initialPinchDist = 0;
  viewport.addEventListener('touchstart', (e) => {
    if (e.touches.length === 2) {
      initialPinchDist = Math.hypot(
        e.touches[0].clientX - e.touches[1].clientX,
        e.touches[0].clientY - e.touches[1].clientY
      );
    } else if (e.touches.length === 1) {
      isDragging = true;
      startX = e.touches[0].clientX - translateX;
      startY = e.touches[0].clientY - translateY;
    }
  }, { passive: true });
  
  viewport.addEventListener('touchmove', (e) => {
    if (e.touches.length === 2) {
      const currentDist = Math.hypot(
        e.touches[0].clientX - e.touches[1].clientX,
        e.touches[0].clientY - e.touches[1].clientY
      );
      if (initialPinchDist > 0) {
        const factor = currentDist / initialPinchDist;
        currentScale = Math.min(Math.max(currentScale * factor, 0.5), 5);
        updateImageTransform();
        initialPinchDist = currentDist;
      }
    } else if (e.touches.length === 1 && isDragging) {
      translateX = e.touches[0].clientX - startX;
      translateY = e.touches[0].clientY - startY;
      updateImageTransform();
    }
  }, { passive: true });
  
  viewport.addEventListener('touchend', () => {
    isDragging = false;
    initialPinchDist = 0;
  });
}

// Window OnLoad Initializations
window.addEventListener('DOMContentLoaded', () => {
  initTheme();
  buildSearchIndex();
  initLightboxEvents();
  populateFaultsTable('all');
  checkResumePosition();
  
  // Handle URL hash routing
  const hash = window.location.hash.replace('#', '');
  if (hash) {
    if (hash.startsWith('sec-')) {
      const targetSec = document.getElementById(hash);
      if (targetSec) {
        const parentView = targetSec.closest('.chapter-view');
        const chId = parentView ? parentView.id.replace('view-', '') : 'cover';
        navigateToSection(chId, hash);
      }
    } else if (hash.startsWith('ch-')) {
      showChapter(hash.replace('ch-', ''));
    } else if (hash.startsWith('view-')) {
      showChapter(hash.replace('view-', ''));
    } else {
      showChapter('cover');
    }
  } else {
    showChapter('cover');
  }
  
  // Close search dropdown on click outside
  document.addEventListener('click', (e) => {
    const searchWrapper = document.querySelector('.search-wrapper');
    if (searchWrapper && !searchWrapper.contains(e.target)) {
      document.getElementById('search-dropdown').classList.remove('active');
    }
  });
  
  // Register service worker if available
  if ('serviceWorker' in navigator && window.location.protocol.startsWith('http')) {
    navigator.serviceWorker.register('sw.js').catch(err => console.log('SW registration error:', err));
  }
});
"""
