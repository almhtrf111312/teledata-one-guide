# -*- coding: utf-8 -*-
"""
Content for Chapter 11 (Usage), Concluding Notes, Faults & Codes view, and Maintenance Guide.
Extracted strictly from pages 85 to 95 of Teledata One Manual.
"""

def get_ch11_and_end_html(images):
    img_fig41 = images.get("fig_41", "")
    img_fig42 = images.get("fig_42", "")
    img_fig43 = images.get("fig_43", "")

    return f"""
<!-- Chapter 11: Usage -->
<div id="view-ch11" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>الفصل 11</span>
    </div>
    <div class="chapter-main-title">
      <span>11 الاستخدام</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">ص 85 - 94</span>
        <span class="meta-pill">10 صفحات</span>
      </div>
    </div>
    <p style="color: var(--text-secondary); margin-top: 6px;">
      إدارة الإنذارات، كتم وإعادة الضبط، الإخلاء، فحص حالة وتشخيص الأجهزة، اختبار المشي، كشف التعارضات، تعطيل وتمكين العناصر، وتغيير كلمات المرور.
    </p>
  </div>

  <!-- 11.1 Events Log -->
  <div class="doc-section" id="sec-11-1">
    <div class="section-header">
      <h3 class="section-title">11.1 عرض الأحداث (<bdi>Event Log</bdi>)</h3>
      <span class="section-page-tag">ص 85 - 86</span>
    </div>
    <p style="margin-bottom: 12px;">الوظائف التالية متاحة لكل من المستخدم والمبرمج.</p>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig41}', 'الشكل 41: قائمة سجل الأحداث Event Log')">
        <img src="{img_fig41}" alt="الشكل 41" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 41:</strong> قائمة سجل الأحداث <bdi>Event Log</bdi>، وتتيح العرض بحسب الفئة أو التاريخ أو الحلقة أو المنطقة. راجع القسم 9.1.1 للحصول على وصف المعلومات المعروضة.
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">11.1.1 تصدير البيانات إلى USB</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>User menu → Maintenance → Export → Events</bdi></div>
      <div class="path-desc">قائمة المستخدم ← الصيانة ← تصدير ← الأحداث</div>
    </div>
    <p style="margin-bottom: 12px;">تتيح هذه الوظيفة تصدير ذاكرة الأحداث من اللوحة إلى ذاكرة <bdi>USB</bdi>.</p>

    <div class="callout callout-note">
      <div class="callout-title">متطلبات ذاكرة USB</div>
      <div class="callout-content">
        اللوحة متوافقة مع ذاكرة USB بسعة تصل إلى <strong>16Gb</strong> مهيأة بصيغة <strong>FAT32</strong> وجدول تخصيص <strong>4096 byte</strong>.
      </div>
    </div>

    <p style="margin: 12px 0;">
      عند اختيار <bdi>Events</bdi>، يُحفظ ملف بصيغة <bdi>.csv</bdi> على ذاكرة USB باسم <bdi>EVNTLOG.CSV</bdi>، ويمكن فتحه ببرنامج مثل Excel. وإذا كان الملف موجوداً مسبقاً فسيُستبدل وتُفقد أي بيانات سابقة. وتعتمد مدة التصدير على عدد الأحداث؛ فلوحة بذاكرة ممتلئة تحتاج نحو <strong>60 ثانية</strong>.
    </p>

    <div class="callout callout-warning">
      <div class="callout-title">⚠️ تحذير</div>
      <div class="callout-content">لتجنّب تلف البيانات، لا تفصل ذاكرة USB، ولا توقف إجراء التصدير، ولا تُطفئ اللوحة.</div>
    </div>
  </div>

  <!-- 11.2 Users & Passwords -->
  <div class="doc-section" id="sec-11-2">
    <div class="section-header">
      <h3 class="section-title">11.2 تمكين المستخدمين وتغيير رموز الدخول</h3>
      <span class="section-page-tag">ص 86</span>
    </div>
    <p style="margin-bottom: 12px;">
      لا يستطيع تمكين أو تعطيل دخول المستخدم إلا المشغّل المبرمج (<bdi>Programmer</bdi>). ويمكن لكل مشغّل تغيير رمز الدخول الشخصي الخاص به.
    </p>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">11.2.1 المبرمج</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Programming menu → Configure → Password</bdi></div>
      <div class="path-desc">قائمة البرمجة ← التكوين ← كلمة المرور</div>
    </div>

    <h5 style="color: var(--brand-amber); margin: 12px 0 6px;">تمكين دخول المستخدم (Users 22223 و 22224):</h5>
    <ol class="step-list">
      <li class="step-item">اضبط جميع المستخدمين الذين يجب أن يسجّلوا الدخول إلى الوحدة على <bdi>Yes</bdi>.</li>
      <li class="step-item">اضغط <bdi>Save</bdi> للتأكيد.</li>
    </ol>

    <h5 style="color: var(--brand-amber); margin: 16px 0 6px;">تغيير رمز دخول المبرمج:</h5>
    <ol class="step-list">
      <li class="step-item">اختر خيار <bdi>Change</bdi>: تظهر صفحة تغيير الرمز.</li>
      <li class="step-item">أدخل الرمز الجديد.</li>
      <li class="step-item">أكّد الرمز الجديد لحفظه.</li>
    </ol>
  </div>

  <!-- 11.3 Alarms Management -->
  <div class="doc-section" id="sec-11-3">
    <div class="section-header">
      <h3 class="section-title">11.3 إدارة الإنذارات</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 86 - 87</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-11-3', '11.3 إدارة الإنذارات')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>
    <p style="margin-bottom: 12px;">
      في حال استلام إنذار من أي جهاز، ستُفعّل اللوحة فوراً خرج الصفارة الداخلي وتُضيء المؤشر الأحمر في الواجهة الأمامية. كما يُضيء الجهاز الذي في حالة إنذار مؤشره الأحمر.
    </p>

    <div class="callout callout-note">
      <div class="callout-title">حماية تحميل الحلقة</div>
      <div class="callout-content">
        لتجنّب تحميل الحلقة بشكل زائد، في حال وجود أكثر من إنذار واحد، سَيُفعَّل <strong>حد أقصى 10 مؤشرات حمراء</strong> على الأجهزة.
      </div>
    </div>

    <!-- 11.3.1 Silence -->
    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">11.3.1 كتم الإنذارات واللوحة (<bdi>Silence / Rearm</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>User menu → Silence</bdi></div>
      <div class="path-desc">قائمة المستخدم ← كتم</div>
    </div>
    <p style="margin-bottom: 12px;">
      بمجرد الضغط على هذا المفتاح، يتحول إلى <bdi>Rearm</bdi> (إعادة تسليح). وتتيح هذه الوظيفة كتم إنذارات النظام واللوحة مؤقتاً للتحقق مما إذا كان الحريق قد وقع فعلاً، وإعادة ضبطها إذا لزم الأمر.
    </p>
    <ul style="margin-right: 22px; line-height: 1.8;">
      <li><strong>في حال الإنذار الكاذب:</strong> أَعِد ضبط اللوحة (راجع 11.3.2).</li>
      <li><strong>في حال الإنذار الحقيقي:</strong> اضغط مفتاح <bdi>Siren Reset</bdi> لإعادة تشغيل أجهزة الإنذار الصوتية.</li>
    </ul>

    <!-- 11.3.2 Reset -->
    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">11.3.2 إعادة ضبط الإنذارات واللوحة (<bdi>Reset</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>User menu → Reset</bdi></div>
      <div class="path-desc">قائمة المستخدم ← إعادة الضبط</div>
    </div>
    <p style="margin-bottom: 12px;">
      تعيد هذه الوظيفة ضبط الإنذارات التي أُطلقت والوحدة. وإذا لم تكن الإنذارات أو الأعطال قد زالت قبل إعادة الضبط، فستظل معروضة على الشاشة بعدها.
    </p>

    <div class="callout callout-note">
      <div class="callout-title">إعادة ضبط عتادية (<bdi>Hardware reset</bdi>)</div>
      <div class="callout-content">
        يمكن تنفيذ إعادة ضبط عتادية (<bdi>Hardware reset</bdi>) عبر الزر المخصص على اللوحة الرئيسية.
      </div>
    </div>

    <!-- 11.3.3 Evacuation -->
    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">11.3.3 الإخلاء (<bdi>Evacuation</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>User menu → Evacuation</bdi></div>
      <div class="path-desc">قائمة المستخدم ← الإخلاء</div>
    </div>
    <p style="margin-bottom: 10px;">
      تضع هذه الميزة اللوحة في وضع الإخلاء، فتُفعَّل جميع الخروجات وأجهزة الإنذار الصوتية المهيأة لذلك.
    </p>

    <div class="callout callout-warning">
      <div class="callout-title">⚠️ تنبيه تفعيل الإخلاء الفوري</div>
      <div class="callout-content">
        عند تفعيل الإخلاء، تُفعَّل جميع وحدات الخرج المبرمجة على «تفعيل الإخلاء» (<bdi>Activate evacuation</bdi> — راجع 10.4) حتى لو لم تكن منطقتها فعّالة، وحتى لو لم تكن الدالة المنطقية المرتبطة بها صالحة بعد.
      </div>
    </div>
  </div>

  <!-- 11.4 Devices Status & Diagnostics -->
  <div class="doc-section" id="sec-11-4">
    <div class="section-header">
      <h3 class="section-title">11.4 فحص حالة وتشخيص الأجهزة</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 87 - 88</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-11-4', '11.4 تشخيص حالة الأجهزة')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin-bottom: 8px;">11.4.1 فحص حالة الحلقة (<bdi>Loop Status</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Maintenance → Loop → Status</bdi></div>
      <div class="path-desc">الصيانة ← الحلقة ← الحالة</div>
    </div>
    <p>اختر الحلقة المطلوبة: يُعرض نوع الحلقة وحالتها.</p>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">11.4.2 إعادة ضبط الحلقة (<bdi>Loop Reset</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Maintenance → Loop → Reset</bdi></div>
      <div class="path-desc">الصيانة ← الحلقة ← إعادة الضبط</div>
    </div>
    <p>اختر الحلقة المطلوبة: تُعاد ضبطها تلقائياً.</p>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">11.4.3 تشغيل تشخيص الأجهزة ونظافة الكواشف (<bdi>Diagnostics</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Maintenance → Diagnostics</bdi></div>
      <div class="path-desc">الصيانة ← التشخيص</div>
    </div>
    <p style="margin-bottom: 12px;">تتيح هذه الوظيفة فحص نظافة الأجهزة الموصولة.</p>

    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>اللون في التشخيص</th>
            <th>حالة الكاشف ونظافته</th>
            <th>الإجراء المطلوب</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span style="color: var(--brand-green); font-weight: 700;">🟢 أخضر</span></td>
            <td>كاشف نظيف.</td>
            <td>حالة ممتازة، لا يتطلب إجراء.</td>
          </tr>
          <tr>
            <td><span style="color: #a3e635; font-weight: 700;">🟡 أصفر مخضر</span></td>
            <td>كاشف نظافته متوسطة.</td>
            <td>مقبول تشغيلياً، يُتابع دورياً.</td>
          </tr>
          <tr>
            <td><span style="color: var(--brand-amber); font-weight: 700;">🟠 برتقالي</span></td>
            <td>كاشف يقترب من الاتساخ.</td>
            <td>يُدرج في جدول الصيانة القريب للتنظيف.</td>
          </tr>
          <tr>
            <td><span style="color: var(--brand-red); font-weight: 700;">🔴 أحمر</span></td>
            <td>كاشف متسخ.</td>
            <td>يتطلب صيانة أو تنظيفاً أو استبدالاً فورياً لتفادي الإنذار الكاذب.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p style="margin-top: 10px;">
      <strong>الإجراء:</strong> اختر الحلقة المطلوبة: تُعرض جميع الأجهزة الموصولة. اضغط على كاشف واحد لعرض التفاصيل.
    </p>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">11.4.4 تصدير التشخيص إلى USB</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>User Menu → Maintenance → Export → Diagnostics</bdi></div>
      <div class="path-desc">قائمة المستخدم ← الصيانة ← تصدير ← التشخيص</div>
    </div>
    <p>
      يُنشأ على ذاكرة USB ملف بصيغة <bdi>.csv</bdi> باسم <bdi>1DIAGLP.CSV</bdi>، حيث يمثل الرقم الحلقة المختارة. وتعتمد المدة على عدد الأجهزة: فحلقة بـ 240 جهازاً تحتاج نحو <strong>240 ثانية</strong>.
    </p>
  </div>

  <!-- 11.5 Device Testing -->
  <div class="doc-section" id="sec-11-5">
    <div class="section-header">
      <h3 class="section-title">11.5 اختبار الأجهزة</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 89 - 90</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-11-5', '11.5 اختبار الأجهزة')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>
    <p style="margin-bottom: 12px;">الوظائف التالية متاحة لكل من المستخدم والمبرمج.</p>

    <!-- 11.5.1 Walk Test -->
    <h4 style="color: var(--brand-blue); margin-bottom: 8px;">11.5.1 تشغيل اختبار المشي (<bdi>Walk Test</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Maintenance → Test → Sensors/Modules → Walk Test</bdi></div>
      <div class="path-desc">الصيانة ← الاختبار ← الكواشف/الوحدات ← اختبار المشي</div>
    </div>
    <p style="margin-bottom: 12px;">
      يُستخدم اختبار المشي للتحقق من أن الأجهزة قادرة على توليد إنذار يدوياً. وعندما تكون الأجهزة في هذا الوضع، <strong>لا يولّد النظام أي إنذار ولا ينفّذ الإجراءات المرتبطة به</strong>.
    </p>

    <ul style="margin-right: 22px; margin-bottom: 12px; line-height: 1.8;">
      <li><bdi>Single</bdi>: لاختبار جهاز واحد فقط (اضغط Single ثم اختر حلقة وعنوان الجهاز).</li>
      <li><bdi>Zone</bdi>: لاختبار أجهزة منطقة محددة (اضغط Zone ثم اختر المنطقة).</li>
      <li><bdi>Loop</bdi>: لاختبار أجهزة حلقة محددة (اضغط Loop ثم اختر الحلقة).</li>
    </ul>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>اللون</th><th>حالة الجهاز في اختبار المشي</th></tr></thead>
        <tbody>
          <tr>
            <td><span style="color: var(--brand-green); font-weight: 700;">🟢 أخضر</span></td>
            <td>اكتمل الاختبار بنجاح.</td>
          </tr>
          <tr>
            <td><span style="color: var(--brand-red); font-weight: 700;">🔴 أحمر</span></td>
            <td>الجهاز لم ينتقل بعد إلى حالة الإنذار.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 11.5.2 Comm Test -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">11.5.2 اختبار الاتصال مع الوحدات والكواشف</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Maintenance → Test → Sensors/Modules → Sensors/Modules</bdi></div>
      <div class="path-desc">الصيانة ← الاختبار ← الكواشف/الوحدات ← الكواشف/الوحدات</div>
    </div>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>اللون</th><th>حالة اتصال الجهاز</th></tr></thead>
        <tbody>
          <tr>
            <td><span style="color: var(--brand-green); font-weight: 700;">🟢 أخضر</span></td>
            <td>الجهاز موصول بشكل صحيح.</td>
          </tr>
          <tr>
            <td><span style="color: var(--brand-red); font-weight: 700;">🔴 أحمر</span></td>
            <td>خطأ في اتصال الجهاز.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 11.5.3 Conflicts -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">11.5.3 تحديد التعارضات (<bdi>Conflicts</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Maintenance → Test → Conflicts</bdi></div>
      <div class="path-desc">الصيانة ← الاختبار ← التعارضات</div>
    </div>
    <p>
      تتيح هذه الوظيفة التحقق مما إذا كان جهازان يحملان العنوان نفسه على الحلقة نفسها في النظام. اختر الحلقة المطلوب البحث فيها فتُعرض أي تعارضات تلقائياً، وإذا ظهرت أجهزة بالعنوان نفسه فغيّر عنوان أحدها.
    </p>

    <!-- 11.5.4 Mismatch -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">11.5.4 تحديد حالات عدم التطابق (<bdi>Mismatch</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Maintenance → Test → Mismatch</bdi></div>
      <div class="path-desc">الصيانة ← الاختبار ← عدم التطابق</div>
    </div>
    <p>
      تتيح هذه الوظيفة التحقق مما إذا كان الجهاز الموجود على الحلقة يطابق فعلاً نوع الجهاز المبرمج في اللوحة (مثلاً، هل بُرمج كاشف كوحدة أو العكس). وصحّح أي حالة عدم تطابق تظهر.
    </p>

    <!-- 11.5.5 LED Test -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">11.5.5 اختبار عمل مؤشرات <bdi>LED</bdi></h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Maintenance → Test → Led</bdi></div>
      <div class="path-desc">الصيانة ← الاختبار ← المؤشرات</div>
    </div>
    <p>
      تتيح هذه الوظيفة التحقق من أن جميع مؤشرات LED في اللوحة وقيم عرض RGB تعمل بشكل صحيح.
    </p>
  </div>

  <!-- 11.6 Disablements -->
  <div class="doc-section" id="sec-11-6">
    <div class="section-header">
      <h3 class="section-title">11.6 تعطيل عناصر النظام (<bdi>Disablements</bdi>)</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 90 - 93</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-11-6', '11.6 تعطيل عناصر النظام')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>

    <div class="callout callout-path">
      <div class="path-code"><bdi>Maintenance → Disablements</bdi></div>
      <div class="path-desc">الصيانة ← التعطيلات</div>
    </div>

    <div class="callout callout-warning">
      <div class="callout-title">⚠️ تحذير أمني حرج</div>
      <div class="callout-content">
        الأجهزة المعطّلة لا ترسل أي إشارة إنذار أو عطل، وهذا يُضعف سلامة النظام. لا تعطّل جهازاً إلا عند الضرورة القصوى، وأَعِد إدراجه في أقرب وقت ممكن.
      </div>
    </div>

    <p style="margin-bottom: 12px;">
      تتيح هذه الوظيفة تجاوز (<bdi>bypass</bdi>) جهاز أو أكثر من أجهزة الوحدة وإعادة إدراجه. وتتجاهل هذه الميزة أي معلومات يتلقاها الجهاز المستثنى. ويمكن تعطيل: الأجهزة، الحلقة، المناطق، الخروجات، والمنطقة المحمية أو غير المحمية.
    </p>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>الرمز على الشاشة</th><th>حالة العنصر</th></tr></thead>
        <tbody>
          <tr><td><bdi style="font-size: 1.2rem; color: var(--brand-red);">⦸</bdi></td><td>عنصر معطّل (كاشف في المثال).</td></tr>
          <tr><td><bdi style="font-size: 1.2rem; color: var(--brand-green);">◉</bdi></td><td>عنصر ممكّن (كاشف في المثال).</td></tr>
        </tbody>
      </table>
    </div>

    <div class="figure-card" style="margin: 16px 0;">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig42}', 'الشكل 42: شاشة تعطيل الأجهزة في الحلقة 1')">
        <img src="{img_fig42}" alt="الشكل 42" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 42:</strong> شاشة تعطيل الأجهزة في الحلقة 1 (<bdi>Disablement Device Loop n.1</bdi>). يظهر الجهاز 001 معلّماً كمعطّل، بينما الأجهزة الأخرى ممكنة.
      </div>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-top: 14px;">
      <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm);">
        <strong style="color: var(--brand-blue);">11.6.1 تعطيل/تمكين جهاز:</strong>
        <p style="font-size: 0.88rem; margin-top: 6px;">
          اختر الحلقة التي تحتوي على الجهاز المراد تجاوزه ← اختر الجهاز المراد تجاوزه ← اضغط <bdi>Save</bdi> للتأكيد.
        </p>
      </div>

      <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm);">
        <strong style="color: var(--brand-amber);">11.6.2 تعطيل/تمكين حلقة:</strong>
        <p style="font-size: 0.88rem; margin-top: 6px;">
          تحذير: تجاوز حلقة يعني تجاوز جميع الأجهزة الموصولة بها تلقائياً. اختر الحلقة واضغط <bdi>Save</bdi>.
        </p>
      </div>

      <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm);">
        <strong style="color: var(--brand-purple);">11.6.3 تعطيل/تمكين منطقة:</strong>
        <p style="font-size: 0.88rem; margin-top: 6px;">
          تحذير: تجاوز منطقة يعني تجاوز جميع الحلقات والأجهزة المرتبطة بها تلقائياً. اختر المنطقة واضغط <bdi>Save</bdi>.
        </p>
      </div>

      <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm);">
        <strong style="color: var(--brand-green);">11.6.4 تعطيل/تمكين خرج:</strong>
        <p style="font-size: 0.88rem; margin-top: 6px;">
          يمكن تعطيل: جميع الخروجات <bdi>All Outputs</bdi>، وخرج اللوحة المراقَب، وأجهزة الإنذار الصوتية <bdi>Sounders</bdi>، والمناطق، ومناطق الخرج.
        </p>
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">11.6.5 تعطيل/تمكين الوضع المحمي (<bdi>Protected</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Maintenance → Disablements → Protected</bdi></div>
      <div class="path-desc">الصيانة ← التعطيلات ← المحمي</div>
    </div>
    <p>
      يمكن هنا تعطيل أو تمكين وضع المنطقة المحمية. وعندما تظهر المنطقة باللون الأخضر يكون الوضع المحمي ممكّناً.
    </p>
  </div>

  <!-- 11.7 User Password & Maintenance Expiry -->
  <div class="doc-section" id="sec-11-7">
    <div class="section-header">
      <h3 class="section-title">11.7 تعديل كلمة مرور المستخدم وتذكير الصيانة</h3>
      <span class="section-page-tag">ص 94</span>
    </div>

    <div class="callout callout-path">
      <div class="path-code"><bdi>Maintenance → Change password</bdi></div>
      <div class="path-desc">الصيانة ← تغيير كلمة المرور (المستوى الثاني فقط)</div>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig43}', 'الشكل 43: شاشة تغيير كلمة مرور المستخدم Modify Programming Password')">
        <img src="{img_fig43}" alt="الشكل 43" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 43:</strong> شاشة تغيير كلمة مرور المستخدم (<bdi>Modify Programming Password</bdi>).
      </div>
    </div>

    <p style="margin-bottom: 12px;">
      تتيح هذه الميزة تعديل كلمة مرور المستخدم المسجّل دخوله. اختر خيار <bdi>Change</bdi> ثم أدخل الرمز الجديد وأكّده لحفظه. ويجب استخدام هذا الرمز الجديد عند تسجيل الدخول التالي.
    </p>

    <!-- 11.7.1 Maint Expiry -->
    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">11.7.1 تذكير الصيانة (<bdi>Maintenance Expiry</bdi>)</h4>
    <div class="callout callout-path">
      <div class="path-code"><bdi>Maintenance → Maint. Expiry</bdi></div>
      <div class="path-desc">الصيانة ← انتهاء الصيانة</div>
    </div>
    <p>
      يمكن هنا برمجة رسالة تظهر عند انتهاء موعد الصيانة. وستظهر نافذة حدث منبثقة عند منتصف ليل التاريخ المحدد لتذكير الفني والمشغل بوجوب إجراء الصيانة الدورية.
    </p>
  </div>
</div>

<!-- Concluding Notes (ص 95) -->
<div id="view-notes" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>ملاحظات ختامية</span>
    </div>
    <div class="chapter-main-title">
      <span>ملاحظات ختامية</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">ص 95</span>
        <span class="meta-pill">1 صفحة</span>
      </div>
    </div>
  </div>

  <div class="doc-section">
    <h4 style="color: var(--brand-blue); margin-bottom: 8px;">خصوصية هذه الترجمة</h4>
    <p style="margin-bottom: 12px;">
      أُعدّ هذا الدليل العربي ليكون مرجعاً عملياً كاملاً لمشغّلي وفنيي لوحة <bdi>Teledata One</bdi>. وقد تُرجمت جميع النصوص الوصفية والتعليمات والتحذيرات ترجمة سياقية كاملة، مع الإبقاء على:
    </p>
    <ul style="margin-right: 22px; margin-bottom: 16px; line-height: 1.8;">
      <li>أسماء الأزرار والقوائم والشاشات كما تظهر على الجهاز.</li>
      <li>المعاملات التقنية الواردة في جداول التكوين، مع شرح عربي مقابلها.</li>
      <li>أسماء الموصلات واللوحات والطرازات ورموز المنتجات.</li>
      <li>أرقام المعايير الأوروبية وبنودها.</li>
      <li>أسماء الملفات وصيغها وأوامر المسارات.</li>
    </ul>
    <p style="margin-bottom: 14px;">
      أما الصور ولقطات الشاشة فقد أُبقيت كما هي لأنها تمثل الواجهة الفعلية للجهاز، وأُضيف أسفل كل صورة شرح عربي يوضح محتواها.
    </p>

    <div class="callout callout-warning">
      <div class="callout-title">⚠️ تنبيه مهم: النسخة المرجعية</div>
      <div class="callout-content">
        في حال وجود أي تعارض بين هذه الترجمة والنسخة الإنجليزية الأصلية الصادرة عن <bdi>Teledata s.r.l.</bdi>، فالنسخة الإنجليزية الأصلية هي المرجع المعتمد، خصوصاً فيما يتعلق بالبيانات الكهربائية ومتطلبات التركيب والمعايير.
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">بيانات الاتصال الرسمية:</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <tbody>
          <tr><th style="width: 180px;">الشركة</th><td><bdi>Teledata s.r.l.</bdi></td></tr>
          <tr><th>العنوان</th><td><bdi>Via G.M. Giulietti, 8 — 20132 Milan — Italy</bdi></td></tr>
          <tr><th>الهاتف</th><td><bdi>+39 02 27 201 352</bdi></td></tr>
          <tr><th>الفاكس</th><td><bdi>+39 02 25 93 704</bdi></td></tr>
          <tr><th>البريد الإلكتروني</th><td><bdi>info@teledata-i.com</bdi></td></tr>
        </tbody>
      </table>
    </div>
    <div style="text-align: center; margin-top: 24px; font-weight: 700; color: var(--text-muted);">
      — نهاية الدليل —
    </div>
  </div>
</div>

<!-- Special View: Faults, Messages & Diagnostic Codes -->
<div id="view-faults" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>الأعطال والرسائل والأكواد</span>
    </div>
    <div class="chapter-main-title">
      <span>الأعطال والرسائل والأكواد التشخيصية</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">دليل تشخيصي سريع</span>
        <span class="meta-pill">مستخرج بالكامل من الدليل</span>
      </div>
    </div>
    <p style="color: var(--text-secondary); margin-top: 6px;">
      جدول شامل لكل رسالة عطل، مؤشر حالة LED، موصل، وكود وارد في الدليل، مع معناه بالعربية ورقم صفحته ورابط مباشر إليه.
    </p>
  </div>

  <div class="doc-section">
    <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 16px;">
      <button class="action-btn active" onclick="filterFaults('all', this)">الكل</button>
      <button class="action-btn" onclick="filterFaults('led', this)">مؤشرات LED</button>
      <button class="action-btn" onclick="filterFaults('screen', this)">رسائل الشاشة</button>
      <button class="action-btn" onclick="filterFaults('hw', this)">الموصلات والأطراف</button>
      <button class="action-btn" onclick="filterFaults('diag', this)">حالات التشخيص</button>
    </div>

    <div class="table-responsive">
      <table class="doc-table" id="faults-table">
        <thead>
          <tr>
            <th>الاسم / الكود الإنجليزي</th>
            <th>المعنى بالعربية</th>
            <th>نوع / لون المؤشر</th>
            <th>الصفحة</th>
            <th>إجراء وتفاصيل الدليل</th>
          </tr>
        </thead>
        <tbody id="faults-tbody">
          <!-- Dynamically populated or static rows with direct jump links -->
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- Special View: Maintenance Guide & Printable Log -->
<div id="view-maint" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>دليل الصيانة الدوري</span>
    </div>
    <div class="chapter-main-title">
      <span>دليل الصيانة والتفتيش الدوري</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">إجراءات الصيانة الرسمية</span>
        <span class="meta-pill">جدول متابعة قابل للطباعة</span>
      </div>
    </div>
    <p style="color: var(--text-secondary); margin-top: 6px;">
      مجموعة كاملة لجميع إجراءات التفتيش والاختبار الدوري المستخرجة من الدليل حصراً.
    </p>
  </div>

  <div class="doc-section">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
      <h3 class="section-title">إجراءات الفحص والاختبار الدورية المعتمدة في اللوحة</h3>
      <button class="action-btn btn-accent" onclick="window.print()">🖨️ طباعة جدول المتابعة</button>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-bottom: 20px;">
      <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm); border-right: 4px solid var(--brand-blue);">
        <strong style="color: var(--brand-blue);">1. اختبار المشي (<bdi>Walk Test</bdi>):</strong>
        <p style="font-size: 0.88rem; margin-top: 4px;">
          يُنفّذ عبر <bdi>Maintenance → Test → Sensors/Modules → Walk Test</bdi>. يسمح باختبار استجابة الكواشف يدوياً دون إطلاق صفارات الإنذار الفعلية.
        </p>
      </div>

      <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm); border-right: 4px solid var(--brand-green);">
        <strong style="color: var(--brand-green);">2. تشخيص نظافة الكواشف (<bdi>Diagnostics</bdi>):</strong>
        <p style="font-size: 0.88rem; margin-top: 4px;">
          يُنفّذ عبر <bdi>Maintenance → Diagnostics</bdi>. يقيس مستوى اتساخ غرفة الكواشف (أخضر = نظيف، أصفر مخضر = متوسط، برتقالي = يقترب من الاتساخ، أحمر = متسخ يلزم تنظيفه أو استبداله فوراً).
        </p>
      </div>

      <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm); border-right: 4px solid var(--brand-amber);">
        <strong style="color: var(--brand-amber);">3. فحص البطاريات والمقاومة الداخلية:</strong>
        <p style="font-size: 0.88rem; margin-top: 4px;">
          تُجري اللوحة فحصاً دورياً أوتوماتيكياً للبطاريات. إذا تجاوزت المقاومة الداخلية <bdi>800mΩ</bdi> أو هبط الجهد دون <bdi>21.6V</bdi> تطلق اللوحة عطلاً صوتياً وبصرياً.
        </p>
      </div>

      <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm); border-right: 4px solid var(--brand-purple);">
        <strong style="color: var(--brand-purple);">4. ضبط تذكير انتهاء الصيانة (<bdi>Maint. Expiry</bdi>):</strong>
        <p style="font-size: 0.88rem; margin-top: 4px;">
          يُبرمج عبر <bdi>Maintenance → Maint. Expiry</bdi>. يُحدّد تاريخ انتهاء فترة الصيانة وتظهر نافذة منبثقة عند منتصف الليل لإلزام الفحص.
        </p>
      </div>
    </div>

    <!-- Printable Maintenance Log Sheet -->
    <div class="print-checklist-header">
      <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--border-light); padding-bottom: 8px;">
        <div>
          <h2 style="font-size: 1.3rem; font-weight: 800;">سجل متابعة الصيانة والتفتيش الدوري — لوحة Teledata One</h2>
          <span style="font-size: 0.82rem; color: var(--text-muted);">مطابق لمتطلبات الصيانة الدورية EN 54-2 / EN 54-4</span>
        </div>
        <div style="text-align: left; font-size: 0.85rem;">
          <strong>رقم اللوحة التسلسلي:</strong> ............................<br>
          <strong>الموقع / المبنى:</strong> ............................
        </div>
      </div>

      <div class="checklist-meta-grid">
        <div class="meta-field"><span>اسم الفني المسؤول:</span> ............................................</div>
        <div class="meta-field"><span>الشركة المعتمدة:</span> ............................................</div>
        <div class="meta-field"><span>تاريخ الفحص:</span> ...... / ...... / 202...</div>
      </div>
    </div>

    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 40px;">#</th>
            <th>بند الفحص والتفتيش</th>
            <th>المعيار المطلوب بالدليل</th>
            <th>النتيجة</th>
            <th>ملاحظات الفني</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>فحص التغذية الرئيسية 230V~</td>
            <td>مؤشر Power مضاء أخضر ودخل Vac ±10% 230</td>
            <td>☐ مطابق  ☐ غير مطابق</td>
            <td></td>
          </tr>
          <tr>
            <td>2</td>
            <td>فحص جهد بطاريات الاحتياط</td>
            <td>جهد الشاحن 27.6V وحالة الجهد أعلى من 21.6V</td>
            <td>☐ مطابق  ☐ غير مطابق</td>
            <td></td>
          </tr>
          <tr>
            <td>3</td>
            <td>المقاومة الداخلية للبطاريات</td>
            <td>أقل من 800 mΩ مع الوصلات والكابلات</td>
            <td>☐ مطابق  ☐ غير مطابق</td>
            <td></td>
          </tr>
          <tr>
            <td>4</td>
            <td>مقاومة التأريض العام</td>
            <td>أقل من 10Ω وفق CEI و ISPESL</td>
            <td>☐ مطابق  ☐ غير مطابق</td>
            <td></td>
          </tr>
          <tr>
            <td>5</td>
            <td>اختبار عطل الأرضي Ground Fault</td>
            <td>اختبار التأريض وتفادي تسرب الشيلد في Various</td>
            <td>☐ مطابق  ☐ غير مطابق</td>
            <td></td>
          </tr>
          <tr>
            <td>6</td>
            <td>مقاومة نهاية خط الخرج المراقب J4</td>
            <td>مقاومة 3.3kΩ ¼W ودايود 1N4007 سليم</td>
            <td>☐ مطابق  ☐ غير مطابق</td>
            <td></td>
          </tr>
          <tr>
            <td>7</td>
            <td>تشخيص نظافة الكواشف Diagnostics</td>
            <td>فحص حالة كواشف الحلقات باللون (أخضر/أصفر مخضر)</td>
            <td>☐ مطابق  ☐ غير مطابق</td>
            <td></td>
          </tr>
          <tr>
            <td>8</td>
            <td>اختبار المشي Walk Test</td>
            <td>استجابة الكواشف ونقاط النداء اليدوية بنجاح</td>
            <td>☐ مطابق  ☐ غير مطابق</td>
            <td></td>
          </tr>
          <tr>
            <td>9</td>
            <td>فحص التعارضات وعدم التطابق</td>
            <td>لا توجد تعارضات عناوين ولا حالات Mismatch</td>
            <td>☐ مطابق  ☐ غير مطابق</td>
            <td></td>
          </tr>
          <tr>
            <td>10</td>
            <td>فحص مؤشرات LED وشاشة اللمس</td>
            <td>اختبار LED RGB والشاشة تعمل بدقة</td>
            <td>☐ مطابق  ☐ غير مطابق</td>
            <td></td>
          </tr>
          <tr>
            <td>11</td>
            <td>تصدير سجل الأحداث EVNTLOG.CSV</td>
            <td>حفظ نسخة احتياطية على فلاش USB بصيغة FAT32</td>
            <td>☐ تم الحفظ  ☐ لم يتم</td>
            <td></td>
          </tr>
          <tr>
            <td>12</td>
            <td>ضبط تاريخ الصيانة القادمة</td>
            <td>برمجة التاريخ في Maintenance → Maint. Expiry</td>
            <td>☐ تم الضبط  ☐ لم يتم</td>
            <td></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div style="margin-top: 20px; display: flex; justify-content: space-between; font-size: 0.9rem; padding: 12px; background-color: var(--bg-tertiary); border-radius: var(--radius-sm);">
      <div><strong>توقيع الفني المنفّذ:</strong> ........................................</div>
      <div><strong>توقيع المشرف / مدير السلامة:</strong> ........................................</div>
      <div><strong>التاريخ:</strong> ...... / ...... / 202...</div>
    </div>
  </div>
</div>
"""
