# -*- coding: utf-8 -*-
"""
Content for Chapter 8 (Control Panel) and Chapter 9 (Basic Operations).
Extracted strictly from pages 46 to 56 of Teledata One Manual.
"""

def get_ch8_to_ch9_html(images):
    img_fig16 = images.get("fig_16", "")
    img_fig17 = images.get("fig_17", "")
    img_fig18 = images.get("fig_18", "")
    img_fig19 = images.get("fig_19", "")
    img_fig20 = images.get("fig_20", "")
    img_fig21 = images.get("fig_21", "")
    img_fig22 = images.get("fig_22", "")
    img_fig23 = images.get("fig_23", "")
    img_fig24 = images.get("fig_24", "")

    return f"""
<!-- Chapter 8: Control Panel -->
<div id="view-ch8" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>الفصل 8</span>
    </div>
    <div class="chapter-main-title">
      <span>8 لوحة التحكم</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">ص 46 - 49</span>
        <span class="meta-pill">4 صفحات</span>
      </div>
    </div>
  </div>

  <div class="doc-section" id="sec-8-overview">
    <div class="section-header">
      <h3 class="section-title">نظرة عامة على لوحة التحكم</h3>
      <span class="section-page-tag">ص 46</span>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig16}', 'الشكل 16: الواجهة الأمامية للوحة التحكم ومؤشرات الحالة')">
        <img src="{img_fig16}" alt="الشكل 16" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 16:</strong> الواجهة الأمامية للوحة التحكم. يشير الرقم 1 إلى مؤشرات الحالة (<bdi>LED</bdi>)، والرقم 2 إلى الواجهة الرسومية (شاشة اللمس).
      </div>
    </div>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المنطقة</th><th>الوصف</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>مؤشرات الحالة <bdi>LED</bdi>.</td></tr>
          <tr><td>2</td><td>الواجهة الرسومية (شاشة اللمس).</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8.1 Status LEDs -->
  <div class="doc-section" id="sec-8-1">
    <div class="section-header">
      <h3 class="section-title">8.1 مؤشرات الحالة <bdi>LED</bdi></h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 46 - 47</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-8-1', '8.1 مؤشرات الحالة LED')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>
    <p style="margin-bottom: 12px;">توجد على لوحة التحكم المؤشرات التالية مع بيان لون كل مؤشر ودلالته:</p>

    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>الاسم على اللوحة</th>
            <th>اللون</th>
            <th>الدلالة بالعربية</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><bdi>Fire</bdi></td>
            <td><span style="color: var(--brand-red); font-weight: 700;">🔴 أحمر</span></td>
            <td>إنذار حريق من كاشف واحد على الأقل في النظام.</td>
          </tr>
          <tr>
            <td><bdi>Fault</bdi></td>
            <td><span style="color: var(--brand-amber); font-weight: 700;">🟡 أصفر</span></td>
            <td>عطل عام (<bdi>generic fault</bdi>).</td>
          </tr>
          <tr>
            <td><bdi>Disablements</bdi></td>
            <td><span style="color: var(--brand-amber); font-weight: 700;">🟡 أصفر</span></td>
            <td>أجهزة أو أجهزة طرفية معطّلة.</td>
          </tr>
          <tr>
            <td><bdi>Mon. Out. Act.</bdi></td>
            <td><span style="color: var(--brand-amber); font-weight: 700;">🟡 أصفر</span></td>
            <td>خرج مراقَب مفعّل.</td>
          </tr>
          <tr>
            <td><bdi>Mon. Out. Dis.</bdi></td>
            <td><span style="color: var(--brand-amber); font-weight: 700;">🟡 أصفر</span></td>
            <td>خرج مراقَب معطّل.</td>
          </tr>
          <tr>
            <td><bdi>Fault Mon. Out.</bdi></td>
            <td><span style="color: var(--brand-amber); font-weight: 700;">🟡 أصفر</span></td>
            <td>عطل في خرج مراقَب.</td>
          </tr>
          <tr>
            <td><bdi>CPU fault</bdi></td>
            <td><span style="color: var(--brand-amber); font-weight: 700;">🟡 أصفر</span></td>
            <td>عطل في وحدة المعالجة المركزية.</td>
          </tr>
          <tr>
            <td><bdi>Power</bdi></td>
            <td><span style="color: var(--brand-green); font-weight: 700;">🟢 أخضر</span></td>
            <td>تغذية رئيسية 220V موجودة.</td>
          </tr>
          <tr>
            <td><bdi>Test</bdi></td>
            <td><span style="color: var(--brand-amber); font-weight: 700;">🟡 أصفر</span></td>
            <td>جهاز واحد على الأقل تحت الاختبار.</td>
          </tr>
          <tr>
            <td><bdi>Silenced</bdi></td>
            <td><span style="color: var(--brand-amber); font-weight: 700;">🟡 أصفر</span></td>
            <td>الإنذار مكتوم.</td>
          </tr>
          <tr>
            <td><bdi>Ext. Activation</bdi></td>
            <td><span style="color: var(--brand-amber); font-weight: 700;">🟡 أصفر</span></td>
            <td>دائرة الإطفاء مفعّلة (غير متاحة حالياً).</td>
          </tr>
          <tr>
            <td><bdi>Ext. Release</bdi></td>
            <td><span style="color: var(--brand-amber); font-weight: 700;">🟡 أصفر</span></td>
            <td>دائرة الإطفاء محرّرة (غير متاحة حالياً).</td>
          </tr>
          <tr>
            <td><bdi>Ext. Out Serv.</bdi></td>
            <td><span style="color: var(--brand-amber); font-weight: 700;">🟡 أصفر</span></td>
            <td>عطل في دائرة الإطفاء (غير متاحة حالياً).</td>
          </tr>
          <tr>
            <td><bdi>Ext. Locked</bdi></td>
            <td><span style="color: var(--brand-amber); font-weight: 700;">🟡 أصفر</span></td>
            <td>دائرة الإطفاء مقفلة (غير متاحة حالياً).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8.2 GUI -->
  <div class="doc-section" id="sec-8-2">
    <div class="section-header">
      <h3 class="section-title">8.2 الواجهة الرسومية</h3>
      <span class="section-page-tag">ص 47 - 48</span>
    </div>
    <p style="margin-bottom: 12px;">تظهر العناصر التالية دائماً في جميع القوائم:</p>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig17}', 'الشكل 17: العناصر الثابتة في الواجهة الرسومية لشاشة اللمس')">
        <img src="{img_fig17}" alt="الشكل 17" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 17:</strong> العناصر الثابتة في الواجهة الرسومية: اسم الصفحة، وتاريخ ووقت الوحدة، ومحتوى الصفحة، ومفتاح الخروج، ومفتاح الرجوع.
      </div>
    </div>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المنطقة</th><th>الوصف والوظيفة</th></tr></thead>
        <tbody>
          <tr><td>1</td><td>اسم الصفحة.</td></tr>
          <tr><td>2</td><td>تاريخ ووقت الوحدة.</td></tr>
          <tr><td>3</td><td>محتوى الصفحة المحددة.</td></tr>
          <tr><td>4</td><td>مفتاح الخروج (<bdi>Exit / Log-Out</bdi>).</td></tr>
          <tr><td>5</td><td>مفتاح الرجوع (<bdi>Back</bdi>).</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 8.3 User Types & 8.4 Access Levels -->
  <div class="doc-section" id="sec-8-3">
    <div class="section-header">
      <h3 class="section-title">8.3 أنواع المستخدمين و 8.4 مستويات الوصول</h3>
      <span class="section-page-tag">ص 48 - 49</span>
    </div>
    <p style="margin-bottom: 12px;">يمكن استخدام اللوحة من ثلاثة أنواع مختلفة من المستخدمين:</p>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 18px;">
      <div style="background-color: var(--bg-tertiary); padding: 16px; border-radius: var(--radius-sm); border-right: 4px solid var(--brand-green);">
        <h4 style="color: var(--brand-green); margin-bottom: 8px;">المستخدم <bdi>User</bdi></h4>
        <ul style="margin-right: 20px; font-size: 0.88rem; line-height: 1.7;">
          <li>عرض أحداث النظام.</li>
          <li>كتم اللوحة والإنذارات.</li>
          <li>إعادة ضبط اللوحة والإنذارات.</li>
          <li>تعطيل الأجهزة.</li>
          <li>اختبار الأجهزة المركّبة.</li>
          <li>تصدير سجل الأحداث إلى <bdi>USB</bdi>.</li>
          <li>تشخيص الأجهزة.</li>
        </ul>
      </div>

      <div style="background-color: var(--bg-tertiary); padding: 16px; border-radius: var(--radius-sm); border-right: 4px solid var(--brand-amber);">
        <h4 style="color: var(--brand-amber); margin-bottom: 8px;">المبرمج <bdi>Programmer</bdi></h4>
        <ul style="margin-right: 20px; font-size: 0.88rem; line-height: 1.7;">
          <li>تكوين الوحدة وتهيئتها.</li>
          <li>عرض أحداث النظام.</li>
          <li>تعطيل الأجهزة.</li>
          <li>اختبار الأجهزة المركّبة.</li>
          <li>إضافة أجهزة جديدة وتكوينها.</li>
          <li>إضافة بطاقات توسعة جديدة إلى الوحدة.</li>
        </ul>
      </div>

      <div style="background-color: var(--bg-tertiary); padding: 16px; border-radius: var(--radius-sm); border-right: 4px solid var(--brand-red);">
        <h4 style="color: var(--brand-red); margin-bottom: 8px;">الدعم الفني <bdi>Technical support</bdi></h4>
        <ul style="margin-right: 20px; font-size: 0.88rem; line-height: 1.7;">
          <li>تنفيذ جميع العمليات المخصصة لفنيي الدعم الفني عبر الاتصال السلكي بحاسوب.</li>
        </ul>
      </div>
    </div>

    <p style="margin-bottom: 12px;">
      لا يستطيع كل مشغّل فتح إلا الشاشات اللازمة لتنفيذ العمليات المسموح بها له. ويمكن لأي مشغّل عرض حالة النظام والأحداث الحالية، لأن هذه العمليات متاحة مباشرة من الصفحة الرئيسية (<bdi>Main page</bdi>) غير المحمية بكلمة مرور.
    </p>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">جدول مستويات الوصول وفق المعيار <bdi>EN 54-2</bdi>:</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>المستوى</th>
            <th>الفئة</th>
            <th>المتطلبات والشروط</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1</strong></td>
            <td>الوصول العام</td>
            <td>لا يتطلب أي رمز وصول.</td>
          </tr>
          <tr>
            <td><strong>2</strong></td>
            <td>المستخدمون (<bdi>Users</bdi>)</td>
            <td>يتطلب رمز وصول، ويُخصّص حتى ثلاثة مشغّلين كحد أقصى.</td>
          </tr>
          <tr>
            <td><strong>3</strong></td>
            <td>المبرمجون (<bdi>Programmers</bdi>)</td>
            <td>يتطلب رمز وصول، <strong>ويجب أن تكون وصلة <bdi>JP3</bdi> مغلقة</strong>.</td>
          </tr>
          <tr>
            <td><strong>4</strong></td>
            <td>الدعم الفني</td>
            <td>يتطلب اتصالاً سلكياً بحاسوب.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- Chapter 9: Basic Operations -->
<div id="view-ch9" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>الفصل 9</span>
    </div>
    <div class="chapter-main-title">
      <span>9 العمليات الأساسية لأي مشغّل</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">ص 50 - 56</span>
        <span class="meta-pill">7 صفحات</span>
      </div>
    </div>
  </div>

  <!-- 9.1 Basic Info Display -->
  <div class="doc-section" id="sec-9-1">
    <div class="section-header">
      <h3 class="section-title">9.1 عرض المعلومات الأساسية</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 50 - 54</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-9-1', '9.1 عرض المعلومات الأساسية')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>
    <p style="margin-bottom: 12px;">تُعرض الصفحة الرئيسية عند التشغيل إذا لم تحدث أي أحداث:</p>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig18}', 'الشكل 18: الصفحة الرئيسية عند التشغيل دون أحداث')">
        <img src="{img_fig18}" alt="الشكل 18" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 18:</strong> الصفحة الرئيسية عند التشغيل دون أحداث. يظهر الشعار واسم اللوحة والتاريخ والوقت، وفي الأسفل مفتاح <bdi>Main Menu</bdi> (القائمة الرئيسية).
      </div>
    </div>

    <p style="margin: 14px 0 10px;">اضغط <bdi>Main Menu</bdi> لعرض القائمة الرئيسية:</p>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig19}', 'الشكل 19: القائمة الرئيسية وإمكانية الوصول دون رمز')">
        <img src="{img_fig19}" alt="الشكل 19" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 19:</strong> القائمة الرئيسية، وتتيح الوصول إلى <bdi>Events</bdi> (الأحداث) و <bdi>Assistance</bdi> (المساعدة) دون إدخال أي رمز.
      </div>
    </div>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>الخيار</th><th>الوظيفة والبيان</th></tr></thead>
        <tbody>
          <tr>
            <td><bdi>Events</bdi></td>
            <td>يفتح قائمة الأحداث (<bdi>Events</bdi>): عرض الأحداث المسجّلة بحسب الفئة أو التاريخ أو الحلقة أو المنطقة.</td>
          </tr>
          <tr>
            <td><bdi>Assistance</bdi></td>
            <td>يفتح صفحة المساعدة (<bdi>Assistance</bdi>): بيانات الاتصال اللازمة لطلب الدعم.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">صفحة الأحداث الحالية (<bdi>Events in Progress</bdi>) عند حدوث حدث:</h4>
    <p style="margin-bottom: 12px;">
      إذا حدث أي نوع من الأحداث، تُعرض صفحة الأحداث الحالية (<bdi>Current events</bdi>) عند التشغيل:
    </p>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig20}', 'الشكل 20: صفحة الأحداث الحالية Events in Progress')">
        <img src="{img_fig20}" alt="الشكل 20" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 20:</strong> صفحة الأحداث الحالية، وتعرض عدد الأجهزة في حالة إنذار أو عطل أو تعطيل أو اختبار، مع مفاتيح التنقل.
      </div>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 14px 0;">
      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th>الحقل</th><th>الوصف في شاشة الأحداث الحالية</th></tr></thead>
          <tbody>
            <tr><td><bdi>Alarms</bdi></td><td>يعرض عدد الأجهزة في حالة إنذار.</td></tr>
            <tr><td><bdi>Faults</bdi></td><td>يعرض عدد الأجهزة في حالة عطل.</td></tr>
            <tr><td><bdi>Exclusion</bdi></td><td>يعرض عدد الأجهزة المعطّلة.</td></tr>
            <tr><td><bdi>Test</bdi></td><td>يعرض عدد الأجهزة تحت الاختبار.</td></tr>
          </tbody>
        </table>
      </div>

      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th>الخيار</th><th>الوظيفة</th></tr></thead>
          <tbody>
            <tr><td><bdi>Log-in</bdi></td><td>لفتح وظائف الوحدة باستخدام رمز الدخول.</td></tr>
            <tr><td><bdi>&lt; &gt;</bdi></td><td>للتنقل بين الصفحات التي تعرض جميع الأحداث.</td></tr>
            <tr><td><bdi>Silence / Buzzer Sil.</bdi></td><td>لكتم جرس اللوحة (وليس إنذارات الأجهزة).</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 9.1.1 View Events -->
    <h4 style="color: var(--brand-blue); margin: 24px 0 8px;">9.1.1 عرض الأحداث (<bdi>Historical Events</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Main menu → Events</bdi></div>
      <div class="path-desc">القائمة الرئيسية ← الأحداث</div>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig21}', 'الشكل 21: قائمة الأحداث Historical Events وخيارات التصنيف')">
        <img src="{img_fig21}" alt="الشكل 21" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 21:</strong> قائمة الأحداث (<bdi>Historical Events</bdi>)، وفيها خيارات: <bdi>All</bdi> و <bdi>Alarms</bdi> و <bdi>Faults</bdi> و <bdi>Date</bdi> و <bdi>Loop</bdi> و <bdi>Zones</bdi>.
      </div>
    </div>

    <h5 style="color: var(--brand-amber); margin: 14px 0 6px;">الإجراءات المتاحة لعرض الأحداث:</h5>
    <ul style="margin-right: 22px; line-height: 1.8;">
      <li><strong>لعرض جميع الأحداث:</strong> اختر <bdi>All</bdi> تُعرض قائمة بجميع الأحداث.</li>
      <li><strong>لعرض جميع الإنذارات:</strong> اختر <bdi>Alarms</bdi> تُعرض قائمة بجميع الإنذارات.</li>
      <li><strong>لعرض جميع الأعطال:</strong> اختر <bdi>Faults</bdi> تُعرض قائمة بجميع الأعطال.</li>
      <li><strong>لعرض أحداث يوم محدد:</strong>
        <ol style="margin-right: 20px;">
          <li>اختر <bdi>Date</bdi>: تظهر شاشة <bdi>Log by Date</bdi> (السجل بحسب التاريخ).</li>
          <li>اضبط تاريخ الأحداث المطلوب عرضها.</li>
          <li>اضغط <bdi>Save</bdi> للتأكيد: تُعرض جميع أحداث اليوم المحدد.</li>
        </ol>
      </li>
      <li><strong>لعرض أحداث حلقة محددة:</strong>
        <ol style="margin-right: 20px;">
          <li>اختر <bdi>Loop</bdi>: تظهر شاشة <bdi>Log by Loop</bdi> (السجل بحسب الحلقة).</li>
          <li>اختر الحلقة المطلوبة.</li>
          <li>اضغط <bdi>Save</bdi> للتأكيد: تُعرض جميع أحداث الحلقة المحددة.</li>
        </ol>
      </li>
      <li><strong>لعرض أحداث منطقة محددة:</strong>
        <ol style="margin-right: 20px;">
          <li>اختر <bdi>Zone</bdi>: تظهر شاشة <bdi>Log by Zone</bdi> (السجل بحسب المنطقة).</li>
          <li>اختر المنطقة المطلوبة.</li>
          <li>اضغط <bdi>Save</bdi> للتأكيد: تُعرض جميع أحداث المنطقة المحددة.</li>
        </ol>
      </li>
    </ul>

    <div class="callout callout-note">
      <div class="callout-title">ملاحظة التصفية من الشاشة الرئيسية</div>
      <div class="callout-content">
        يمكن الدخول إلى قائمة الأحداث باختيار أحد المربعات المعروضة في الصفحة الرئيسية، وعندها لا تُعرض إلا الأحداث المتعلقة بالاختيار نفسه.
      </div>
    </div>

    <!-- 9.1.2 Assistance -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">9.1.2 عرض معلومات المساعدة (<bdi>Assistance</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Main menu → Assistance</bdi></div>
      <div class="path-desc">القائمة الرئيسية ← المساعدة</div>
    </div>
    <p>
      تُعرض في هذه الصفحة المعلومات اللازمة للحصول على الدعم الفني، مثل اسم اللوحة وبيانات مركز الخدمة. يُرجى الاستعانة بها عند الاتصال بالدعم.
    </p>
  </div>

  <!-- 9.2 Log-in -->
  <div class="doc-section" id="sec-9-2">
    <div class="section-header">
      <h3 class="section-title">9.2 تسجيل الدخول (<bdi>Log-in</bdi>)</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 54 - 56</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-9-2', '9.2 تسجيل الدخول')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>

    <div class="callout callout-path">
      <div class="path-code"><bdi>Main page → Log-in</bdi></div>
      <div class="path-desc">الصفحة الرئيسية ← تسجيل الدخول</div>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig22}', 'الشكل 22: شاشة إدخال الرمز Insert Code')">
        <img src="{img_fig22}" alt="الشكل 22" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 22:</strong> شاشة إدخال الرمز (<bdi>Insert Code</bdi>)، وفيها لوحة أرقام ومفتاح <bdi>OK</bdi> ومفتاح <bdi>Back</bdi>. يدعم الرمز الافتراضي خمسة أرقام.
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">رموز الدخول الافتراضية للوحة:</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>المستخدم</th>
            <th>الرمز الافتراضي في المصنع</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>رمز المستخدم <bdi>User code</bdi></td>
            <td><bdi style="font-size: 1.1rem; color: var(--brand-green);">22222, 22223, 22224</bdi></td>
          </tr>
          <tr>
            <td>رمز المبرمج <bdi>Programmer code</bdi></td>
            <td><bdi style="font-size: 1.1rem; color: var(--brand-amber);">33333</bdi></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout callout-note">
      <div class="callout-title">ملاحظة الرموز المعطلة</div>
      <div class="callout-content">
        كلمتا المرور الافتراضيتان للمستخدمين <bdi>22223</bdi> و <bdi>22224</bdi> معطّلتان مصنعياً. وللحصول على تعليمات تمكينهما، راجع القسم 11.2 «تمكين المستخدمين وتغيير رموز الدخول».
      </div>
    </div>

    <h5 style="color: var(--brand-amber); margin: 14px 0 6px;">إجراء تسجيل الدخول:</h5>
    <ol class="step-list">
      <li class="step-item">أدخل أرقام الرمز الخمسة.</li>
      <li class="step-item">اضغط <bdi>OK</bdi> للتأكيد: تُعرض القائمة المناسبة وفق الرمز المُدخل.</li>
    </ol>

    <div class="callout callout-warning">
      <div class="callout-title">⚠️ تحذير أمني</div>
      <div class="callout-content">
        غيّر كلمة المرور في أقرب وقت ممكن لتجنّب الوصول غير المصرّح به إلى النظام (راجع القسم 11.2).
      </div>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; margin: 16px 0;">
      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig23}', 'الشكل 23: قائمة المستخدم User بعد تسجيل الدخول')">
          <img src="{img_fig23}" alt="الشكل 23" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 23:</strong> قائمة المستخدم (<bdi>User</bdi>) بعد تسجيل الدخول، وتضم: الأحداث التاريخية، والمساعدة، والصيانة، وكتم الخروجات، وإعادة الضبط، والإخلاء.
        </div>
      </div>

      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig24}', 'الشكل 24: قائمة البرمجة Programming')">
          <img src="{img_fig24}" alt="الشكل 24" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 24:</strong> قائمة البرمجة (<bdi>Programming</bdi>) التي تظهر بعد الدخول برمز المبرمج، وتتيح الوصول إلى التكوين والصيانة والاختبارات.
        </div>
      </div>
    </div>
  </div>
</div>
"""
