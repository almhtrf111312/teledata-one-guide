# -*- coding: utf-8 -*-
"""
Content for Chapter 10: Configuration (التكوين) ص 57 - 84.
Comprehensive extraction from Teledata One Manual.
"""

def get_ch10_html(images):
    img_fig25 = images.get("fig_25", "")
    img_fig26 = images.get("fig_26", "")
    img_fig27 = images.get("fig_27", "")
    img_fig28 = images.get("fig_28", "")
    img_fig29 = images.get("fig_29", "")
    img_fig30 = images.get("fig_30", "")
    img_fig31 = images.get("fig_31", "")
    img_fig32 = images.get("fig_32", "")
    img_fig33 = images.get("fig_33", "")
    img_fig34 = images.get("fig_34", "")
    img_fig35 = images.get("fig_35", "")
    img_fig36 = images.get("fig_36", "")
    img_fig37 = images.get("fig_37", "")
    img_fig38 = images.get("fig_38", "")
    img_fig39 = images.get("fig_39", "")
    img_fig40 = images.get("fig_40", "")

    return f"""
<!-- Chapter 10: Configuration -->
<div id="view-ch10" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>الفصل 10</span>
    </div>
    <div class="chapter-main-title">
      <span>10 التكوين</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">ص 57 - 84</span>
        <span class="meta-pill">28 صفحة</span>
      </div>
    </div>
    <p style="color: var(--text-secondary); margin-top: 6px;">
      إعداد بطاقات التوسعة، العنونة والبرمجة التلقائية، تكوين الكواشف والوحدات والمناطق ودوال الخرج المنطقية، وإعدادات النظام والتقويم.
    </p>
  </div>

  <div class="callout callout-warning">
    <div class="callout-title">صلاحيات الوصول (ص 57)</div>
    <div class="callout-content">
      لا يمكن تنفيذ الوظائف الموصوفة أدناه إلا من قِبل مشغّلين مصرّح لهم يملكون رمز دخول خاصاً بالمهمة المطلوب تنفيذها (رمز المبرمج <bdi>33333</bdi> مع وصلة <bdi>JP3</bdi> مغلقة).
    </div>
  </div>

  <!-- 10.1 Panel Setup -->
  <div class="doc-section" id="sec-10-1">
    <div class="section-header">
      <h3 class="section-title">10.1 إعداد اللوحة</h3>
      <span class="section-page-tag">ص 57 - 60</span>
    </div>
    <p style="margin-bottom: 12px;">الوظائف التالية مخصصة للمبرمج. لإعداد اللوحة بعد التركيب يجب:</p>
    <ul style="margin-right: 22px; margin-bottom: 16px; line-height: 1.8;">
      <li>ضبط عدد بطاقات التوسعة المركّبة.</li>
      <li>ضبط عناوين الأجهزة.</li>
      <li>ضبط أسماء الأجهزة الموصولة وخصائصها.</li>
      <li>تجميع الأجهزة في مناطق.</li>
      <li>ضبط العلاقات بين المناطق.</li>
      <li>إنشاء دوال منطقية لتشغيل الخروجات.</li>
      <li>ضبط تفعيل الخروجات.</li>
      <li>ضبط التقويم.</li>
    </ul>

    <!-- 10.1.1 Expansion Cards -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">10.1.1 إعداد بطاقات التوسعة</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → System → Additional Cards → Loop</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← النظام ← البطاقات الإضافية ← الحلقة</div>
    </div>
    <p style="margin-bottom: 12px;">تتيح هذه الوظيفة تحديد عدد بطاقات <bdi>ONE2</bdi> الإضافية المركّبة على اللوحة.</p>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig25}', 'الشكل 25: شاشة Loop Expansion لاختيار عدد بطاقات توسعة الحلقات')">
        <img src="{img_fig25}" alt="الشكل 25" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 25:</strong> شاشة <bdi>Loop Expansion</bdi> لاختيار عدد بطاقات توسعة الحلقات من 0 إلى 4. كل بطاقة تساوي حلقتين (<bdi>Each card is equal to 2 Loop</bdi>).
      </div>
    </div>

    <div class="callout callout-note">
      <div class="callout-title">ملاحظة التوسعة</div>
      <div class="callout-content">كل بطاقة توسعة تحتوي على حلقتين معنونتين إضافيتين.</div>
    </div>

    <h5 style="color: var(--brand-amber); margin: 12px 0 6px;">الإجراء:</h5>
    <ol class="step-list">
      <li class="step-item">اختر عدد البطاقات الإضافية في الوحدة.</li>
      <li class="step-item">اضغط <bdi>Save</bdi> للتأكيد.</li>
    </ol>
    <p style="font-size: 0.88rem; color: var(--text-secondary); margin-top: 4px;">
      * لإزالة بطاقة <bdi>ONE2</bdi> إضافية، اضغط مرة أخرى على الكمية المحددة.
    </p>

    <h4 style="color: var(--brand-blue); margin: 22px 0 8px;">إعداد بطاقة الشبكة <bdi>OlyNet</bdi>:</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming Menu → Configure → System → Additional Cards → OlyNet</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← النظام ← البطاقات الإضافية ← OlyNet</div>
    </div>
    <p style="margin-bottom: 10px;">
      تتيح هذه الوظيفة ضبط جميع المعاملات اللازمة لكي يعمل نظام <bdi>OlyNet</bdi> بشكل صحيح. وللحصول على هذه الوظيفة، يجب أن تكون بطاقة <bdi>OneRing</bdi> الإضافية مركّبة في اللوحة، وأن تكون اللوحة موصولة في حلقة مع لوحات <bdi>TeledataONE</bdi> أو <bdi>Olympia</bdi> أخرى.
    </p>
    <ol class="step-list">
      <li class="step-item">اختر عدد اللوحات الموصولة في الحلقة.</li>
      <li class="step-item">اختر كل لوحة على حدة، وأكّد الطراز وعدد الحلقات المستخدمة.</li>
      <li class="step-item">اضبط معرّف <bdi>ID</bdi> للوحة التي يجري تكوينها.</li>
      <li class="step-item">اضبط الأوامر المقبولة من الشبكة.</li>
      <li class="step-item">اضغط <bdi>Save</bdi> للتأكيد.</li>
    </ol>

    <!-- 10.1.2 Auto Addr -->
    <h4 style="color: var(--brand-blue); margin: 24px 0 8px;">10.1.2 تشغيل العنونة التلقائية (<bdi>Auto Addr.</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → Auto Addr.</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← العنونة التلقائية</div>
    </div>
    <p>
      تضبط هذه الوظيفة عنواناً تلقائياً لجميع الأجهزة الموصولة باللوحة، دون استخدام المبرمج اليدوي.
    </p>

    <!-- 10.1.3 Auto Progr -->
    <h4 style="color: var(--brand-blue); margin: 24px 0 8px;">10.1.3 تشغيل البرمجة الذاتية (<bdi>Auto Progr.</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → Auto Progr.</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← البرمجة التلقائية</div>
    </div>
    <p style="margin-bottom: 12px;">تبحث هذه الوظيفة عن جميع الأجهزة الموصولة باللوحة وتحفظها.</p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; margin: 14px 0;">
      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig26}', 'الشكل 26: شاشة بدء البرمجة الذاتية واختيار الحلقة المطلوبة')">
          <img src="{img_fig26}" alt="الشكل 26" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 26:</strong> شاشة بدء البرمجة الذاتية واختيار الحلقة المطلوبة.
        </div>
      </div>

      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig27}', 'الشكل 27: ملخص البرمجة الذاتية للحلقة 1 بعد انتهائها')">
          <img src="{img_fig27}" alt="الشكل 27" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 27:</strong> ملخص البرمجة الذاتية للحلقة 1 بعد انتهائها. تظهر أرقام الأجهزة المكتشفة، وتشير الرموز إلى الأجهزة المتجاوبة وغير المتجاوبة.
        </div>
      </div>
    </div>
    <p style="font-size: 0.9rem;">
      <strong>الإجراء:</strong> اختر الحلقة المطلوبة: تبدأ البرمجة الذاتية، وتُعرض الأجهزة التي عُثر عليها كما في المثال.
    </p>
  </div>

  <!-- 10.2 All In All Out -->
  <div class="doc-section" id="sec-10-2">
    <div class="section-header">
      <h3 class="section-title">10.2 تكوين <bdi>All In All Out</bdi></h3>
      <span class="section-page-tag">ص 60 - 62</span>
    </div>

    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → Devices/Zones → All In All Out</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← الأجهزة/المناطق ← All In All Out</div>
    </div>

    <p style="margin-bottom: 12px;">
      هذه ميزة أمان تتيح تفعيل جميع الخروجات قبل الانتهاء من تكوين الأسباب والنتائج. وافتراضياً يكون <bdi>All In All Out</bdi> ممكّناً، لذا عند أول إنذار من أي إدخال تُفعَّل جميع الخروجات. وبعد اكتمال البرنامج والتحقق منه، يمكن تغييره إلى معطّل.
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; margin: 14px 0;">
      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig28}', 'الشكل 28: قائمة Device/Zone')">
          <img src="{img_fig28}" alt="الشكل 28" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 28:</strong> قائمة <bdi>Device/Zone</bdi> التي تضم: الكواشف، والوحدات، والمناطق، والدوال المنطقية، ومناطق الخرج، و <bdi>All In All Out</bdi>.
        </div>
      </div>

      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig29}', 'الشكل 29: شاشة All In All Out')">
          <img src="{img_fig29}" alt="الشكل 29" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 29:</strong> شاشة <bdi>All In All Out</bdi> لتمكين أو تعطيل التفعيل العام للخروجات.
        </div>
      </div>
    </div>

    <div class="callout callout-note">
      <div class="callout-title">ملاحظة التفعيل الفردي</div>
      <div class="callout-content">
        عند تغيير الإعداد العام لهذا المعامل، تتبع جميع الخروجات الحالة الجديدة. ويمكن تفعيل هذه الوظيفة لجهاز خرج واحد على حدة (راجع القسم 10.4).
      </div>
    </div>
  </div>

  <!-- 10.3 Detectors Configuration -->
  <div class="doc-section" id="sec-10-3">
    <div class="section-header">
      <h3 class="section-title">10.3 تكوين الكواشف (<bdi>Detectors</bdi>)</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 62 - 63</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-10-3', '10.3 تكوين الكواشف')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>

    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → Devices/Zones → Detectors</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← الأجهزة/المناطق ← الكواشف</div>
    </div>
    <p style="margin-bottom: 12px;">الوظائف التالية مخصصة للمبرمج. تتيح هذه الوظيفة: إضافة كاشف، تعديل كاشف مضاف مسبقاً، نسخ إعدادات كاشف إلى كاشف واحد أو أكثر متتالٍ، وحذف كاشف.</p>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">جدول معاملات الكاشف:</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل على الشاشة</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>Name</bdi></td><td>اسم تعريف الكاشف.</td></tr>
          <tr><td><bdi>Type</bdi></td><td>نوع الكاشف الموصول (بصري <bdi>Optical</bdi>، حراري <bdi>Thermal</bdi>، بصري/حراري).</td></tr>
          <tr><td><bdi>Radio</bdi></td><td>يحدد الأجهزة اللاسلكية. وعند استخدام أجهزة لاسلكية يجب تركيب محول لاسلكي <bdi>FDW2W</bdi>.</td></tr>
          <tr><td><bdi>Verify Alarms</bdi></td><td>يمكّن إجراء التحقق من الإنذار لمدة زمنية قابلة للبرمجة عبر المعامل <bdi>Verify seconds</bdi>.</td></tr>
          <tr><td><bdi>Verify seconds</bdi></td><td>الفاصل الزمني بالثواني الذي يجب أن يبقى فيه الكاشف في حالة إنذار قبل أن تعرض اللوحة إنذار الحريق. وإذا ضُبط على صفر، فلن تنتقل اللوحة إلى حالة الإنذار إلا عند استلام ثلاثة إنذارات متتالية من الكاشف خلال 60 ثانية من وصول الأول. ويُهمل الإنذاران الأولان وتُعاد ضبط الكاشف.</td></tr>
          <tr><td><bdi>Slave sounder</bdi></td><td>يغيّر هذا الإعداد خرج LED البعيد للكاشف ليعمل كخرج للوحة. وإذا ضُبط على <bdi>YES</bdi> فتُراعى الإعدادات التالية:<br>• <bdi>Activate Evacuation</bdi>: يتبع هذا الخرج أمر الإخلاء.<br>• <bdi>All In All Out</bdi>: يتبع هذا الخرج وضع التفعيل الأمني AIAO.<br>• <bdi>Silenceable</bdi>: يتبع هذا الخرج أمر كتم الخروج أو إعادة تسليحه.</td></tr>
          <tr><td><bdi>Sensitivity management</bdi><br><small>(لكواشف الدخان فقط)</small></td><td>• <bdi>24 H</bdi>: يبقى مستوى الحساسية كما هو طوال اليوم.<br>• <bdi>Night</bdi>: تزيد الحساسية درجة واحدة أثناء الليل.<br>• <bdi>Fixed</bdi>: حساسية ثابتة على <bdi>Medium High</bdi>.<br>وإذا اختيرت إدارة Night، فيجب أيضاً ضبط المعامل Weekly Trend.</td></tr>
          <tr><td><bdi>Sensitivity</bdi></td><td>مستوى حساسية الكاشف (<bdi>Low, Medium Low, Medium High, High</bdi>).</td></tr>
          <tr><td><bdi>Weekly trend</bdi></td><td>يضبط النمط الأسبوعي لإدارة حساسية الكاشف (راجع القسم 10.9.5).</td></tr>
          <tr><td><bdi>Deactivate part</bdi><br><small>(للكواشف المتعددة فقط)</small></td><td>• <bdi>Day</bdi>: اختر الجزء المطلوب تعطيله (الدخان أو الحرارة).<br>• <bdi>Night</bdi>: اختر الجزء المطلوب تعطيله (الدخان أو الحرارة).<br>وإذا استُخدمت هذه الميزة، فيجب أيضاً ضبط المعامل Weekly Trend.</td></tr>
          <tr><td><bdi>Weekly trend</bdi></td><td>يضبط النمط الأسبوعي لتعطيل جزء من الكاشف (راجع القسم 10.9.5).</td></tr>
        </tbody>
      </table>
    </div>

    <h5 style="color: var(--brand-amber); margin: 20px 0 8px;">إجراءات تكوين الكاشف (ص 63):</h5>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px;">
      <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm);">
        <strong style="color: var(--brand-green);">إضافة كاشف:</strong>
        <ol style="margin-right: 18px; margin-top: 6px; font-size: 0.88rem; line-height: 1.7;">
          <li>اختر خيار <bdi>Add</bdi>: تُعرض قائمة بحلقات النظام.</li>
          <li>اختر الحلقة التي سيُضاف إليها الكاشف.</li>
          <li>اختر رقم كاشف غير مستخدم: تظهر نافذة إعدادات الكاشف.</li>
          <li>أدخل الإعدادات المطلوبة.</li>
          <li>اضغط <bdi>Next</bdi> للانتقال إلى الشاشة التالية.</li>
          <li>اضغط <bdi>Save</bdi> للتأكيد.</li>
        </ol>
      </div>

      <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm);">
        <strong style="color: var(--brand-blue);">تعديل كاشف:</strong>
        <ol style="margin-right: 18px; margin-top: 6px; font-size: 0.88rem; line-height: 1.7;">
          <li>اختر خيار <bdi>Edit</bdi>: تُعرض قائمة بحلقات النظام.</li>
          <li>اختر الحلقة التي تحتوي على الكاشف.</li>
          <li>اختر الكاشف المطلوب.</li>
          <li>عدّل الإعدادات.</li>
          <li>اضغط <bdi>Save</bdi> للتأكيد.</li>
        </ol>
      </div>

      <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm);">
        <strong style="color: var(--brand-red);">حذف كاشف:</strong>
        <ol style="margin-right: 18px; margin-top: 6px; font-size: 0.88rem; line-height: 1.7;">
          <li>اختر خيار <bdi>Delete</bdi>: تُعرض قائمة بالحلقات.</li>
          <li>اختر الحلقة التي تحتوي على الكاشف.</li>
          <li>لحذف كاشف واحد، اضغط على الكاشف مرتين. لحذف عدة كواشف متتالية، اضغط على أول وآخر كاشف في النطاق.</li>
          <li>اضغط <bdi>Save</bdi> لحذف الكاشف أو الكواشف.</li>
        </ol>
      </div>

      <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm);">
        <strong style="color: var(--brand-purple);">نسخ كاشف:</strong>
        <ol style="margin-right: 18px; margin-top: 6px; font-size: 0.88rem; line-height: 1.7;">
          <li>اختر خيار <bdi>Copy</bdi>: تُعرض قائمة بالحلقات.</li>
          <li>اختر الحلقة التي تحتوي على الكاشف المراد نسخ إعداداته.</li>
          <li>اختر الكاشف المصدر.</li>
          <li>اختر أول كاشف في المجموعة الهدف ثم آخر كاشف.</li>
          <li>اضغط <bdi>Save</bdi> لتطبيق الإعدادات على جميع الكواشف المحددة.</li>
        </ol>
      </div>
    </div>
  </div>

  <!-- 10.4 Modules Configuration -->
  <div class="doc-section" id="sec-10-4">
    <div class="section-header">
      <h3 class="section-title">10.4 تكوين الوحدات (<bdi>Modules</bdi>)</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 64 - 66</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-10-4', '10.4 تكوين الوحدات')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>

    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → Devices/Zones → Modules</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← الأجهزة/المناطق ← الوحدات</div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">1. معاملات جميع أنواع الوحدات:</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>Name</bdi></td><td>اسم تعريف الوحدة.</td></tr>
          <tr><td><bdi>Radio</bdi></td><td>يحدد الأجهزة اللاسلكية. وعند استخدامها يجب تركيب محوّل لاسلكي <bdi>FDW2W</bdi>.</td></tr>
          <tr><td><bdi>Type</bdi></td><td>نوع الوحدة: <bdi>Argus</bdi> (إدخال، خرج، موسّع)، أو <bdi>Apollo</bdi> (إدخال، خرج، موسّع، متعدد 1+1، متعدد 2+2، متعدد 3+3).</td></tr>
        </tbody>
      </table>
    </div>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">2. معاملات وحدة الإدخال:</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>Type</bdi></td><td>نوع الوحدة (إدخال، نقطة نداء غاز <bdi>Call point Gas</bdi>).</td></tr>
          <tr><td><bdi>Alarm test</bdi></td><td>يمكّن إجراء التحقق من الإنذار لمدة قابلة للبرمجة عبر المعامل <bdi>Verify seconds</bdi>.</td></tr>
          <tr><td><bdi>Test seconds</bdi></td><td>الفاصل الزمني بالثواني الذي يجب أن يبقى فيه الجهاز في حالة إنذار قبل عرض إنذار الحريق. وإذا ضُبط على صفر، فلا تنتقل اللوحة إلى الإنذار إلا عند استلام ثلاثة إنذارات متتالية خلال 60 ثانية من وصول الأول، ويُهمل الإنذاران الأولان وتُعاد ضبط الوحدة.</td></tr>
          <tr><td><bdi>Strength alarm</bdi></td><td>يمنح الإدخال القدرة على إعادة ضبط مؤقتي <bdi>T1</bdi> و <bdi>T2</bdi> للوضع المحمي أو غير المحمي للمناطق، وتفعيل الخروجات.</td></tr>
          <tr><td><bdi>Technological</bdi></td><td>يحدد إشارة الإنذار بأنها «تكنولوجية» وبالتالي أقل خطورة. وعند ضبط وحدة كتكنولوجية يمكن ضبط ثلاث وظائف أخرى: <bdi>Fault</bdi> و <bdi>Self Restore</bdi> و <bdi>Pre-Alarm</bdi>.</td></tr>
          <tr><td><bdi>Fault</bdi></td><td>يُفسَّر الحدث المراقَب من اللوحة كعطل ويُدار على هذا الأساس، ويظهر على الشاشة تحت <bdi>Fault-Technology</bdi> للوحدة المبرمجة.</td></tr>
          <tr><td><bdi>Self restore</bdi></td><td>يتيح إعادة الضبط التلقائي للوحة بعد عودة الإدخال إلى حالة الانتظار. ويُفعَّل في حال المراقبة التكنولوجية أو العطل.</td></tr>
          <tr><td><bdi>Pre-alarm</bdi></td><td>يشغّل وظيفة ما قبل الإنذار. وعند كشف حدث ما قبل إنذار: تُشغَّل جميع وحدات الخرج المرتبطة بمناطق الخرج التي أُطلق فيها ما قبل الإنذار (راجع 10.6)، ويومض مؤشر اللوحة الأحمر، وإذا لم يُعَد ضبط ما قبل الإنذار خلال زمن ما قبل الإنذار أو حدث إنذار فعلي، يضيء مؤشر اللوحة الأحمر باستمرار.</td></tr>
        </tbody>
      </table>
    </div>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">3. معاملات وحدة الخرج:</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>Type</bdi></td><td>نوع الوحدة (خرج، وامض <bdi>Flasher</bdi>، صفارة <bdi>Siren</bdi>، مؤشر مكرر <bdi>LED Repeater</bdi>).</td></tr>
          <tr><td><bdi>Reset sensors</bdi></td><td>تُستخدم هذه الميزة عادةً لإعادة ضبط الأجهزة التقليدية غير الموصولة مباشرة بالحلقة. وفي كل مرة تُعاد فيها ضبط اللوحة، يُفعَّل هذا الخرج لنحو <strong>5 ثوانٍ</strong>.</td></tr>
          <tr><td><bdi>All In All Out</bdi></td><td>يتبع هذا الخرج وضع التفعيل الأمني AIAO.</td></tr>
          <tr><td><bdi>Silenceable</bdi></td><td>يتبع هذا الخرج أمر كتم الخروج أو إعادة تسليحه.</td></tr>
          <tr><td><bdi>Activate Evacuation</bdi></td><td>إذا فُعِّل، يُنشَّط الخرج عند أمر إخلاء من المستخدم، حتى لو لم تكن منطقته أو الدالة المنطقية المرتبط بها صالحة بعد.</td></tr>
          <tr><td><bdi>Volume</bdi><br><small>(لطراز الصفارة FDVBLS100/32 أو FDVBS100-AV/32 فقط)</small></td><td>مستوى صوت الصفارة، ويضبط النغمة أيضاً.</td></tr>
        </tbody>
      </table>
    </div>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">4. معاملات <bdi>Multi I/O</bdi>:</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>Type</bdi></td><td>نوع الوحدة (<bdi>Multi I/O 1+1, 2+2, 3+3</bdi>).</td></tr>
          <tr><td><bdi>Choose device</bdi></td><td>تُستخدم لضبط أجهزة كل خط إدخال وإخراج. ففي 1+1 يكون لدينا جهازان (إدخال وإخراج)، وفي 2+2 أربعة أجهزة (إدخالان وإخراجان)، وفي 3+3 ستة أجهزة (ثلاثة إدخالات وثلاثة خروجات).</td></tr>
          <tr><td><bdi>Input type</bdi></td><td>نوع وحدة الإدخال التي يمكن إدراجها (إدخال، زر <bdi>throttle</bdi>).</td></tr>
          <tr><td><bdi>Output type</bdi></td><td>نوع وحدة الخرج التي يمكن إدراجها (خرج، وامض، صفارة، مؤشر مكرر).</td></tr>
        </tbody>
      </table>
    </div>

    <div class="callout callout-warning">
      <div class="callout-title">تنبيه عناوين الوحدات المتعددة (ص 65)</div>
      <div class="callout-content">
        من المهم تذكّر أن الوحدات المتعددة تشغل عناوين متعددة، بحسب كونها 1+1 أو 2+2 أو 3+3، لأن الإدخال/الإخراج يشغل عنواناً افتراضياً إضافياً يلي عنوان الوحدة الفيزيائية.
      </div>
    </div>
  </div>

  <!-- 10.5 Zones Configuration -->
  <div class="doc-section" id="sec-10-5">
    <div class="section-header">
      <h3 class="section-title">10.5 تكوين المناطق (<bdi>Zones</bdi>)</h3>
      <span class="section-page-tag">ص 66 - 69</span>
    </div>

    <div class="callout callout-suggestion">
      <div class="callout-title">اقتراح فهم تسلسل النظام</div>
      <div class="callout-content">قبل البدء بهذه العمليات، تأكد من فهمك لطريقة تفاعل عناصر النظام المختلفة (راجع القسم 7.6.1).</div>
    </div>

    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → Devices/Zones → Zones</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← الأجهزة/المناطق ← المناطق</div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">10.5.1 ربط حدث بمنطقة (ص 67)</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>Alarm</bdi></td><td>تُفعَّل المنطقة بإنذار من الأجهزة المرتبطة.</td></tr>
          <tr><td><bdi>Fault</bdi></td><td>تُفعَّل المنطقة بعطل في الأجهزة المرتبطة.</td></tr>
          <tr><td><bdi>Technol.</bdi></td><td>تُفعَّل المنطقة بحدث «تكنولوجي» من الأجهزة المرتبطة.</td></tr>
          <tr><td><bdi>Coincidence</bdi></td><td>معامل قابل للبرمجة لكل حدث، وهو عدد الأحداث التي يجب تسجيلها لتفعيل المنطقة.</td></tr>
        </tbody>
      </table>
    </div>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">10.5.2 ربط الحلقات بالمناطق (ص 67)</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>All system</bdi></td><td>إذا اختير <bdi>Yes</bdi>، تُربط جميع أجهزة النظام بالمنطقة. وإذا اختير <bdi>No</bdi>، اختر الحلقة التي تُفعّل المنطقة.</td></tr>
          <tr><td><bdi>Loop</bdi></td><td>اختر الحلقة كاملة التي ستُرتبط بالمنطقة المبرمجة.</td></tr>
        </tbody>
      </table>
    </div>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">10.5.3 ربط الأجهزة بالمناطق</h4>
    <p>
      اختر خيار <bdi>Device</bdi>، ثم اختر الحلقة المطلوبة فتُعرض جميع أجهزة الحلقة، ثم اختر جميع الأجهزة المراد ربطها بالمنطقة واضغط <bdi>Back</bdi> لحفظ الاختيار.
    </p>

    <div class="callout callout-note">
      <div class="callout-title">ملاحظة تعدد المناطق للجهاز الواحد (ص 68)</div>
      <div class="callout-content">
        يمكن إضافة الجهاز نفسه إلى <strong>12 منطقة مختلفة</strong> في الوقت نفسه.
      </div>
    </div>

    <!-- 10.5.4 Zone Operation Parameters & Timers -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">10.5.4 ضبط معاملات تشغيل المنطقة والوضع المحمي (<bdi>T1 & T2</bdi>)</h4>
    <p style="margin-bottom: 12px;">
      تتيح هذه الوظيفة ضبط سلوك المنطقة أسبوعياً، وهو أمر مفيد لتجاوز الوحدة في أيام أو أوقات معينة.
    </p>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>Zone name</bdi></td><td>الاسم المعطى للمنطقة.</td></tr>
          <tr><td><bdi>Weekly trend</bdi></td><td>النمط الأسبوعي المرتبط بالمنطقة (راجع 10.9.5).</td></tr>
          <tr><td><bdi>Autoexclusion</bdi></td><td>استثناء تلقائي للمنطقة وفق النمط الأسبوعي.</td></tr>
          <tr><td><bdi>Protected</bdi></td><td>إذا ضُبط على <bdi>Yes</bdi>، يمكن ضبط الأزمنة <bdi>T1</bdi> و <bdi>T2</bdi> و <bdi>T2B</bdi> وضبط المسح الأسبوعي للأنماط.</td></tr>
          <tr><td><bdi>T1</bdi></td><td>مرحلة التحذير؛ عند تفعيلها تكون المنطقة في حالة إنذار، لكن الخروجات المرتبطة لم تُفعَّل بعد.</td></tr>
          <tr><td><bdi>T2</bdi></td><td>زمن التحقيق للتحقق المادي من صحة الإنذار. ويعمل <bdi>T2B</bdi> بالطريقة نفسها، لكن فقط إذا كان التحذير صادراً من زر.</td></tr>
          <tr><td><bdi>Weekly trend survey</bdi></td><td>بضبط هذا المعامل يمكن برمجة المنطقة محمية أو غير محمية خلال الأسبوع.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="callout callout-suggestion">
      <div class="callout-title">إجراء التحقق من ضبط المنطقة كمنطقة محمية (ص 68 - 69):</div>
      <div class="callout-content">
        <ol style="margin-right: 20px; line-height: 1.8;">
          <li>أدخل رمز المستوى الثالث <bdi>33333</bdi>.</li>
          <li>اختر قسم <bdi>Configure</bdi> ← ادخل قسم <bdi>System</bdi> ← اضغط قسم <bdi>General</bdi> ← ادخل قسم <bdi>Various</bdi>.</li>
          <li>تحقق من أن الطرفين <bdi>T1</bdi> و <bdi>T2</bdi> ممكّنان.</li>
          <li>نفّذ <bdi>Log-Out</bdi>.</li>
          <li>أدخل رمز المستوى الثاني <bdi>22222</bdi>.</li>
          <li>اختر قسم <bdi>Maintenance</bdi> ← اختر قسم <bdi>Exclusions</bdi> ← ادخل قسم <bdi>Protected</bdi>.</li>
          <li>تحقق من أن المنطقة المبرمجة كـ محمية تظهر <strong>باللون الأخضر</strong>.</li>
        </ol>
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">10.5.5 ربط وحدة خرج بمنطقة (ص 69)</h4>
    <p>
      تتيح هذه الوظيفة ربط وحدات الخرج بمنطقة مباشرة. وعند تفعيل المنطقة، تُشغَّل وحدات الخرج تلقائياً. <strong>والحد الأقصى لعدد الخروجات التي يمكن إضافتها إلى المنطقة هو 60</strong>.
    </p>
  </div>

  <!-- 10.6 Output Zones -->
  <div class="doc-section" id="sec-10-6">
    <div class="section-header">
      <h3 class="section-title">10.6 تكوين مناطق الخرج (<bdi>Output Zones</bdi>)</h3>
      <span class="section-page-tag">ص 70</span>
    </div>

    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → Devices/Zones → Output Zones</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← الأجهزة/المناطق ← مناطق الخرج</div>
    </div>

    <p style="margin-bottom: 12px;">
      تتيح هذه الوظيفة ربط وحدات الخرج بمناطق الخرج. والحد الأقصى لعدد الخروجات التي يمكن إضافتها إلى منطقة الخرج هو <strong>60</strong>.
    </p>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr>
            <td><bdi>Activations</bdi></td>
            <td>نوع الحدث الذي يفعّل المنطقة (إنذار <bdi>Alarm</bdi>، ما قبل إنذار الغاز <bdi>Pre-alarm Gas</bdi>).</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h5 style="color: var(--brand-amber); margin: 14px 0 6px;">إنشاء منطقة خرج:</h5>
    <ol class="step-list">
      <li class="step-item">اختر خيار <bdi>Add</bdi>: تُعرض قائمة بمناطق الخرج.</li>
      <li class="step-item">اختر أول منطقة خرج متاحة.</li>
      <li class="step-item">اضبط المعاملات المطلوبة ثم اضغط <bdi>Next</bdi>.</li>
      <li class="step-item">اختر الحلقة التي تتضمن وحدة الخرج المراد ربطها، ثم اختر وحدة الخرج.</li>
      <li class="step-item">اضغط <bdi>Save</bdi> للتأكيد.</li>
    </ol>
  </div>

  <!-- 10.7 Logic Functions -->
  <div class="doc-section" id="sec-10-7">
    <div class="section-header">
      <h3 class="section-title">10.7 تكوين الدوال المنطقية (<bdi>Logic functions</bdi>)</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 70 - 74</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-10-7', '10.7 تكوين الدوال المنطقية')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>

    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → Devices/Zones → Logic functions</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← الأجهزة/المناطق ← الدوال المنطقية</div>
    </div>

    <p style="margin-bottom: 12px;">
      الدوال المنطقية هي علاقات الأسباب والنتائج بين الأحداث التي تقع في اللوحة. ويمكن للدوال المنطقية أن تربط ما يلي: الكواشف، الوحدات، المناطق، الإنذارات القادمة من نظام <bdi>OlyNet</bdi>، والدوال المنطقية الأخرى.
    </p>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">المعاملات المنطقية وجدول الصواب والخطأ (ص 71):</h4>
    <ul style="margin-right: 22px; margin-bottom: 14px; line-height: 1.8;">
      <li><bdi>AND</bdi> «و»: يتحقق الخرج عندما تتحقق جميع المدخلات.</li>
      <li><bdi>OR</bdi> «أو»: يتحقق الخرج عند تحقق أي مدخل.</li>
      <li><bdi>NOT</bdi> «ليس»: يعكس حالة المدخل.</li>
      <li><bdi>XOR</bdi> «أو الحصرية»: يتحقق الخرج عند اختلاف المدخلات.</li>
    </ul>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin: 14px 0;">
      <!-- AND -->
      <div class="table-responsive">
        <table class="doc-table" style="text-align: center;">
          <thead><tr><th colspan="3">AND</th></tr><tr><th>A</th><th>B</th><th>Y</th></tr></thead>
          <tbody>
            <tr><td>0</td><td>0</td><td>0</td></tr>
            <tr><td>0</td><td>1</td><td>0</td></tr>
            <tr><td>1</td><td>0</td><td>0</td></tr>
            <tr><td>1</td><td>1</td><td>1</td></tr>
          </tbody>
        </table>
      </div>

      <!-- OR -->
      <div class="table-responsive">
        <table class="doc-table" style="text-align: center;">
          <thead><tr><th colspan="3">OR</th></tr><tr><th>A</th><th>B</th><th>Y</th></tr></thead>
          <tbody>
            <tr><td>0</td><td>0</td><td>0</td></tr>
            <tr><td>0</td><td>1</td><td>1</td></tr>
            <tr><td>1</td><td>0</td><td>1</td></tr>
            <tr><td>1</td><td>1</td><td>1</td></tr>
          </tbody>
        </table>
      </div>

      <!-- NOT -->
      <div class="table-responsive">
        <table class="doc-table" style="text-align: center;">
          <thead><tr><th colspan="2">NOT</th></tr><tr><th>A</th><th>Y</th></tr></thead>
          <tbody>
            <tr><td>0</td><td>1</td></tr>
            <tr><td>1</td><td>0</td></tr>
          </tbody>
        </table>
      </div>

      <!-- XOR -->
      <div class="table-responsive">
        <table class="doc-table" style="text-align: center;">
          <thead><tr><th colspan="3">XOR</th></tr><tr><th>A</th><th>B</th><th>Y</th></tr></thead>
          <tbody>
            <tr><td>0</td><td>0</td><td>0</td></tr>
            <tr><td>0</td><td>1</td><td>1</td></tr>
            <tr><td>1</td><td>0</td><td>1</td></tr>
            <tr><td>1</td><td>1</td><td>0</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">إعدادات ومعاملات الدالة المنطقية:</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>Detectors</bdi></td><td>الحلقة والعنوان المكوّنان للدالة.</td></tr>
          <tr><td><bdi>Modules</bdi></td><td>الحلقة والعنوان المكوّنان للدالة.</td></tr>
          <tr><td><bdi>Zone</bdi></td><td>رقم المنطقة.</td></tr>
          <tr><td><bdi>OlyNet</bdi></td><td>اختر اللوحة المعنية والجهاز اللازم (كاشف، وحدة، منطقة... إلخ).</td></tr>
          <tr><td><bdi>Event</bdi></td><td>اختر نوع الحدث:<br>• للكاشف: إنذار <bdi>Alarm</bdi>، عطل <bdi>Fault</bdi>، تعطيل <bdi>Disablements</bdi>.<br>• للوحدة: إنذار <bdi>Alarm</bdi>، ما قبل الإنذار <bdi>Pre-Alarm</bdi>، عطل <bdi>Fault</bdi>، تعطيل <bdi>Disablements</bdi>، تكنولوجي <bdi>Technological</bdi>.</td></tr>
          <tr><td><bdi>Logic function</bdi></td><td>رقم دالة منطقية أخرى تفعّل هذه الدالة.</td></tr>
          <tr><td><bdi>Delay</bdi></td><td>زمن التأخير بالثواني بين تفعيل الدالة المنطقية وتفعيل الخرج.</td></tr>
          <tr><td><bdi>Length</bdi></td><td>زمن تفعيل الخرج بالثواني. <strong>وإذا ضُبط على 0000، تبقى الخروجات فعّالة حتى يُعيد المشغّل ضبطها</strong>.</td></tr>
          <tr><td><bdi>Output Zone Associate</bdi></td><td>الخروجات التي تُفعّلها الدوال المنطقية. ويجب أن تكون هذه الخروجات مبرمجة مسبقاً (راجع 10.6).</td></tr>
        </tbody>
      </table>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 18px 0;">
      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig30}', 'الشكل 30: مثال بناء الدالة المنطقية n.001')">
          <img src="{img_fig30}" alt="الشكل 30" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 30:</strong> مثال على بناء الدالة المنطقية <bdi>n.001</bdi> باستخدام الكواشف والوحدات والمناطق، مع ظهور التعبير المنطقي في الأعلى: <bdi>(L01M032A | L01M033A) & (L01D001A |</bdi>
        </div>
      </div>

      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig31}', 'الشكل 31: نافذة اختيار المدخلات والأحداث')">
          <img src="{img_fig31}" alt="الشكل 31" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 31:</strong> نافذة اختيار المدخلات وأنواع الأحداث المرتبطة بالدالة المنطقية (<bdi>And (&), Or (|), Not (!), Xor (^)</bdi>).
        </div>
      </div>

      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig32}', 'الشكل 32: إعدادات التأخير ومدة التفعيل')">
          <img src="{img_fig32}" alt="الشكل 32" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 32:</strong> نافذة إعدادات الدالة المنطقية: التأخير <bdi>Delay</bdi> ومدة التفعيل <bdi>Duration/Length</bdi> ومنطقة الخرج <bdi>OutPut Zone Associate</bdi>.
        </div>
      </div>
    </div>
  </div>

  <!-- 10.8 System Parameters -->
  <div class="doc-section" id="sec-10-8">
    <div class="section-header">
      <h3 class="section-title">10.8 ضبط معاملات النظام (<bdi>System Parameters</bdi>)</h3>
      <span class="section-page-tag">ص 74 - 80</span>
    </div>

    <!-- 10.8.1 Language -->
    <h4 style="color: var(--brand-blue); margin-bottom: 8px;">10.8.1 ضبط اللغة (<bdi>Language</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → System → General → Language</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← النظام ← عام ← اللغة</div>
    </div>
    <p style="margin-bottom: 10px;">
      اختر اللغة المطلوبة: تُطبّق اللغة المختارة فوراً. واللغات المتاحة (من الإصدار 3.0A07) هي 16 لغة:
    </p>
    <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px;">
      <span class="meta-pill">الإيطالية Italian</span>
      <span class="meta-pill">الإنجليزية English</span>
      <span class="meta-pill">التركية Turkish</span>
      <span class="meta-pill">الفرنسية French</span>
      <span class="meta-pill">الفارسية Farsi</span>
      <span class="meta-pill pill-primary">العربية Arabic</span>
      <span class="meta-pill">البولندية Polish</span>
      <span class="meta-pill">الإستونية Estonian</span>
      <span class="meta-pill">الرومانية Romanian</span>
      <span class="meta-pill">البرتغالية Portuguese</span>
      <span class="meta-pill">الدانماركية Danish</span>
      <span class="meta-pill">السلوفينية Slovenian</span>
      <span class="meta-pill">الهولندية Dutch</span>
      <span class="meta-pill">سنغافورة Singapore</span>
      <span class="meta-pill">العبرية Hebrew</span>
      <span class="meta-pill">الصينية Chinese</span>
      <span class="meta-pill">الليتوانية Lithuanian</span>
      <span class="meta-pill">الإسبانية Spanish</span>
    </div>

    <!-- 10.8.2 Panel Info -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">10.8.2 إدخال معلومات اللوحة (<bdi>Panel info</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → System → General → Panel info</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← النظام ← عام ← معلومات اللوحة</div>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig33}', 'الشكل 33: شاشة Panel Info')">
        <img src="{img_fig33}" alt="الشكل 33" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 33:</strong> شاشة <bdi>Panel Info</bdi> لضبط اسم اللوحة وبيانات مركز الدعم ولون الخلفية والشعار المخصص.
      </div>
    </div>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>Panel name</bdi></td><td>الاسم المعطى للوحدة.</td></tr>
          <tr><td><bdi>Support center</bdi></td><td>بيانات الاتصال بمركز الخدمة.</td></tr>
          <tr><td><bdi>Background</bdi></td><td>لون خلفية لوحة التحكم (أسود <bdi>Black</bdi>، أزرق <bdi>Blue</bdi>، أخضر <bdi>Green</bdi>).</td></tr>
          <tr><td><bdi>Logo Costum</bdi></td><td>إدخال كلمة المرور لتخصيص اللوحة بشعار مخصص (<bdi>Custom Logo</bdi>).</td></tr>
        </tbody>
      </table>
    </div>

    <!-- 10.8.3 Buzzer-LED -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">10.8.3 ضبط سلوك المؤشرات والجرس (<bdi>Buzzer-led</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → System → General → Buzzer-led</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← النظام ← عام ← الجرس والمؤشرات</div>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig34}', 'الشكل 34: شاشة ضبط الجرس ومؤشرات LED')">
        <img src="{img_fig34}" alt="الشكل 34" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 34:</strong> شاشة ضبط الجرس ومؤشرات <bdi>LED</bdi> والإضاءة الخلفية.
      </div>
    </div>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>Buzzer</bdi></td><td>يمكّن جرس اللوحة. ويصدر الجرس في حال العطل أو الإنذار.</td></tr>
          <tr><td><bdi>Blinking led</bdi></td><td>يفعّل وظيفة وميض المؤشرات <bdi>LED</bdi> في الأجهزة المركّبة على الحلقة. ويومض المؤشر عند استعلام اللوحة عنه.</td></tr>
          <tr><td><bdi>Red led</bdi></td><td>يضبط لون وميض مؤشر الجهاز على الأحمر. ويومض المؤشر عند استعلام اللوحة عنه.</td></tr>
          <tr><td><bdi>Led Backlight</bdi></td><td>يضبط لون الإضاءة الخلفية للوحة (أخضر، أبيض، أزرق). واضغط على اللون المحدد لإلغاء الإضاءة الخلفية.</td></tr>
        </tbody>
      </table>
    </div>

    <!-- 10.8.4 Supervision -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">10.8.4 ضبط الاتصالات عن بُعد (<bdi>Supervision</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Settings → System → General → Supervision</bdi></div>
      <div class="path-desc">قائمة البرمجة ← الإعدادات ← النظام ← عام ← الإشراف</div>
    </div>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>Baud Rate</bdi></td><td>اختر إحدى القيم المتاحة (<bdi>9600, 19200, 38400, 57600</bdi>). اختر أعلى قيمة للحصول على اتصال أسرع. وإذا كانت بطاقة الشبكة PT-LAN مركّبة، فاضبط المعامل نفسه في البطاقة.</td></tr>
          <tr><td><bdi>Physical address</bdi></td><td>العنوان الفيزيائي للمشرف.</td></tr>
          <tr><td><bdi>Logic address</bdi></td><td>العنوان المنطقي للمشرف.</td></tr>
        </tbody>
      </table>
    </div>

    <!-- 10.8.5 Loop Type -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">10.8.5 ضبط خصائص الحلقة (<bdi>Loop type</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → System → General → Loop type</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← النظام ← عام ← نوع الحلقة</div>
    </div>
    <p>تتيح هذه الوظيفة تحديد ما إذا كانت كل حلقة في النظام <strong>مفتوحة أو مغلقة</strong>.</p>

    <!-- 10.8.6 Factory Values -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">10.8.6 استعادة إعدادات المصنع (<bdi>Values Factory</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → System → Values Factory</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← النظام ← قيم المصنع</div>
    </div>
    <div class="callout callout-warning">
      <div class="callout-title">⚠️ تحذير لا رجعة فيه</div>
      <div class="callout-content">بمجرد بدء هذا الإجراء لا يمكن إيقافه، وسَتُحذف جميع تغييرات الإعدادات.</div>
    </div>

    <!-- 10.8.7 Peripherals -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">10.8.7 ضبط خصائص الأجهزة الطرفية (<bdi>Peripherals</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → System → Peripherals</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← النظام ← الأجهزة الطرفية</div>
    </div>
    <ul style="margin-right: 22px; line-height: 1.8;">
      <li>لوحات مفاتيح عن بُعد (<bdi>Remote Keypads</bdi>) — بحد أقصى <strong>16 لوحة</strong> على خط RS 485.</li>
      <li>لوحات محاكاة عن بُعد (<bdi>Remote Mimic Panels</bdi>) — بحد أقصى <strong>16 لوحة</strong>.</li>
    </ul>

    <!-- 10.8.8 USB Export -->
    <h4 style="color: var(--brand-blue); margin: 22px 0 8px;">10.8.8 تصدير البيانات إلى USB (<bdi>Export to USB</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → System → USB → Export</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← النظام ← USB ← تصدير</div>
    </div>

    <div class="callout callout-note">
      <div class="callout-title">متطلبات ذاكرة USB</div>
      <div class="callout-content">
        اللوحة متوافقة مع ذاكرات USB بسعة تصل إلى <strong>16Gb</strong> مهيأة بصيغة <strong>FAT32</strong> مع جدول تخصيص بحجم <strong>4096 byte</strong>. ويجب تهيئة الذاكرة بهذه الطريقة باستخدام حاسوب.
      </div>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig35}', 'الشكل 35: شاشة تصدير البيانات Export to Usb')">
        <img src="{img_fig35}" alt="الشكل 35" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 35:</strong> شاشة تصدير البيانات <bdi>Export</bdi>، وتتيح اختيار <bdi>Configuration</bdi> أو <bdi>Historical Events</bdi> أو <bdi>Diagnostic</bdi>.
      </div>
    </div>

    <ul style="margin-right: 22px; line-height: 1.8;">
      <li><strong>اختر <bdi>Configuration</bdi>:</strong> يُحفظ ملف على ذاكرة USB بصيغته الخاصة غير القابلة للتعديل باسم <bdi>ONELOOP.CFG</bdi>. وإذا كان الملف موجوداً مسبقاً فسيُستبدل وتُفقد أي بيانات تصدير سابقة. ومدة التصدير نحو <strong>3 ثوانٍ</strong>.</li>
      <li><strong>اختيار <bdi>Events</bdi>:</strong> يُحفظ ملف بصيغة <bdi>.csv</bdi> على ذاكرة USB يمكن فتحه ببرنامج مثل Excel، باسم <bdi>EVNTLOG.CSV</bdi>. مدة التصدير للوحة ممتلئة بالكامل نحو <strong>60 ثانية</strong>.</li>
      <li><strong>اختيار <bdi>Diagnostics</bdi>:</strong> يجب أيضاً اختيار الحلقة المطلوبة. يُنشأ على ذاكرة USB ملف باسم <bdi>1DIAGLP.CSV</bdi> (حيث يمثل الرقم أمام اسم الملف الحلقة المختارة). والحلقة التي تضم 240 جهازاً تحتاج نحو <strong>240 ثانية</strong>.</li>
    </ul>

    <div class="callout callout-warning">
      <div class="callout-title">⚠️ تحذير حماية البيانات</div>
      <div class="callout-content">لتجنّب تلف البيانات، لا تفصل ذاكرة USB، ولا توقف إجراء التصدير، ولا تُطفئ اللوحة أثناء العملية.</div>
    </div>

    <!-- 10.8.9 USB Import -->
    <h4 style="color: var(--brand-blue); margin: 22px 0 8px;">10.8.9 استيراد البيانات من USB (<bdi>Import from USB</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → System → USB → Import</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← النظام ← USB ← استيراد</div>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig36}', 'الشكل 36: شاشة استيراد التكوين Import')">
        <img src="{img_fig36}" alt="الشكل 36" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 36:</strong> شاشة استيراد التكوين <bdi>Import</bdi> من ذاكرة USB (<bdi>Attention! The Programming will be Overwritten</bdi>).
      </div>
    </div>

    <p style="margin-bottom: 12px;">
      يجب أن يوجد في جذر الذاكرة ملف تكوين باسم <bdi>ONELOOP.CFG</bdi>. سيُستبدل تكوين اللوحة بالتكوين الموجود على ذاكرة USB. ومدة الاستيراد نحو <strong>20 ثانية</strong>، وبعد انتهائه تُعاد اللوحة إلى التشغيل بالتكوين الجديد.
    </p>

    <!-- 10.8.10 Various -->
    <h4 style="color: var(--brand-blue); margin: 22px 0 8px;">10.8.10 إعدادات نظام متنوعة (<bdi>Various</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → System → General → Various</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← النظام ← عام ← متنوعة</div>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig37}', 'الشكل 37: شاشة الإعدادات المتنوعة Various')">
        <img src="{img_fig37}" alt="الشكل 37" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 37:</strong> شاشة الإعدادات المتنوعة <bdi>Various</bdi>، وتضم التحكم في T1 & T2 وزمن الكتم ومراقبة عطل الأرضي.
      </div>
    </div>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr>
            <td><bdi>T1 & T2 control</bdi></td>
            <td>يحدد هذا المعامل ما إذا كانت اللوحة قادرة على التحكم في إجراء T1 و T2 أم لا.</td>
          </tr>
          <tr>
            <td><bdi>Silencing time</bdi></td>
            <td>زمن كتم الجرس في حال استمرار الإنذار. ويعود الجرس للعمل بعد هذه المدة إذا لم يُعَد ضبط الإنذار.</td>
          </tr>
          <tr>
            <td><bdi>Ground Fault Control</bdi></td>
            <td>يُنفّذ اختبار عطل الأرضي للتحقق من تسربات أرضي شبكة الطاقة وتأريض إشارة الحلقة. فعّل هذا الخيار لتصحيح أخطاء التركيب، وخصوصاً الدوائر القصيرة بين التأريض وإشارات الوحدة (مثل تلامس بين حجب الكابل وأحد الموصلات).</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 10.9 Calendar & Time -->
  <div class="doc-section" id="sec-10-9">
    <div class="section-header">
      <h3 class="section-title">10.9 ضبط التقويم والوقت (<bdi>Calendar & Time</bdi>)</h3>
      <span class="section-page-tag">ص 80 - 84</span>
    </div>

    <!-- 10.9.1 Date & Time -->
    <h4 style="color: var(--brand-blue); margin-bottom: 8px;">10.9.1 ضبط التاريخ والوقت (<bdi>Date and Time</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → Date & Time → Date and Time</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← التاريخ والوقت ← التاريخ والوقت</div>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig38}', 'الشكل 38: شاشة Clock لضبط التاريخ والوقت')">
        <img src="{img_fig38}" alt="الشكل 38" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 38:</strong> شاشة ضبط التاريخ والوقت الحاليين (<bdi>Clock</bdi>). اضبط التاريخ والوقت ثم اضغط <bdi>Save</bdi> للتأكيد.
      </div>
    </div>

    <!-- 10.9.2 Summertime -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">10.9.2 ضبط التوقيت الصيفي (<bdi>Summertime</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → Date & Time → Summertime</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← التاريخ والوقت ← التوقيت الصيفي</div>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig39}', 'الشكل 39: شاشة التوقيت الصيفي Summertime')">
        <img src="{img_fig39}" alt="الشكل 39" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 39:</strong> شاشة التوقيت الصيفي <bdi>Summertime</bdi> بخياراتها الثلاثة.
      </div>
    </div>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>الخيار</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>Automatic</bdi></td><td>تنتقل اللوحة تلقائياً إلى التوقيت الصيفي.</td></tr>
          <tr><td><bdi>Manual</bdi></td><td>ضبط شهر ويوم بداية ونهاية التوقيت الصيفي يدوياً.</td></tr>
          <tr><td><bdi>Not managed</bdi></td><td>الوظيفة غير ممكنة، ولا تُحتسب أي فترة توقيت صيفي.</td></tr>
        </tbody>
      </table>
    </div>

    <!-- 10.9.3 Holidays -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">10.9.3 ضبط العطلات (<bdi>Holidays</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → Date & Time → Holidays</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← التاريخ والوقت ← العطلات</div>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig40}', 'الشكل 40: شاشة برمجة العطلات Festivity / Holidays')">
        <img src="{img_fig40}" alt="الشكل 40" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 40:</strong> شاشة برمجة العطلات <bdi>Holidays</bdi>.
      </div>
    </div>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعامل</th><th>الشرح بالعربية</th></tr></thead>
        <tbody>
          <tr><td><bdi>Holiday no.</bdi></td><td>معرّف العطلة (من 1 إلى 12).</td></tr>
          <tr><td><bdi>Day</bdi></td><td>يوم العطلة.</td></tr>
          <tr><td><bdi>Month</bdi></td><td>شهر العطلة.</td></tr>
        </tbody>
      </table>
    </div>

    <!-- 10.9.4 Time Slot -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">10.9.4 ضبط الفواصل الزمنية (<bdi>Time Slot</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → Date & Time → Time Slot</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← التاريخ والوقت ← الفواصل الزمنية</div>
    </div>
    <p style="margin-bottom: 12px;">تتيح هذه الوظيفة ضبط حتى <strong>255 فاصلاً زمنياً يومياً</strong>.</p>
    <ul style="margin-right: 22px; line-height: 1.8;">
      <li><strong>إنشاء فاصل زمني جديد:</strong> اختر <bdi>Add</bdi> ← اختر فاصلاً زمنياً غير مضبوط ← اضبط تاريخ ووقت البداية [1] وتاريخ ووقت النهاية [2] للفاصل الزمني ← اضغط <bdi>Save</bdi> للتأكيد.</li>
      <li><strong>تعديل فاصل زمني موجود:</strong> اختر <bdi>Edit</bdi> ← اختر الفاصل المراد تعديله ← غيّر أوقات البداية والنهاية ← اضغط <bdi>Save</bdi> للتأكيد.</li>
      <li><strong>حذف فاصل زمني:</strong> اختر <bdi>Delete</bdi> ← اختر الفاصل المراد حذفه ← اضغط <bdi>Save</bdi> للتأكيد.</li>
    </ul>

    <!-- 10.9.5 Weekly Trends -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">10.9.5 ضبط الأنماط الأسبوعية (<bdi>Weekly trends</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Settings → Date & Time → Weekly trends</bdi></div>
      <div class="path-desc">قائمة البرمجة ← الإعدادات ← التاريخ والوقت ← الأنماط الأسبوعية</div>
    </div>
    <p style="margin-bottom: 12px;">تتيح هذه الوظيفة ربط الفواصل الزمنية المنشأة مسبقاً بأيام الأسبوع.</p>
    <ul style="margin-right: 22px; line-height: 1.8;">
      <li><strong>إنشاء نمط أسبوعي جديد:</strong> اختر <bdi>Add</bdi> ← اختر نمطاً أسبوعياً غير مضبوط ← اختر الفاصل الزمني المراد ربطه بكل يوم من أيام الأسبوع (راجع 10.9.4) ← اضغط <bdi>Save</bdi> للتأكيد.</li>
      <li><strong>تعديل نمط أسبوعي موجود:</strong> اختر <bdi>Edit</bdi> ← اختر النمط المراد تعديله ← عدّل الفواصل الزمنية المرتبطة بالأيام ← اضغط <bdi>Save</bdi> للتأكيد.</li>
      <li><strong>حذف نمط أسبوعي موجود:</strong> اختر <bdi>Delete</bdi> ← اختر النمط المراد حذفه ← اضغط <bdi>Save</bdi> للتأكيد.</li>
    </ul>
  </div>
</div>
"""
