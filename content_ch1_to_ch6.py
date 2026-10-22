# -*- coding: utf-8 -*-
"""
Content for Chapters 1 through 6, plus Cover and Legal/Standards notes.
Extracted strictly from pages 1 to 18 of Teledata One Manual.
"""

def get_ch1_to_ch6_html(images):
    img_cover = images.get("cover", "")
    img_fig1 = images.get("fig_1", "")

    return f"""
<!-- Cover & Legal Info -->
<div id="view-cover" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <span>الدليل</span> &gt; <span>الغلاف ومعلومات الملكية</span>
    </div>
    <div class="chapter-main-title">
      <span>لوحة التحكم في إنذار الحريق <bdi>TELEDATA ONE</bdi></span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">دليل المستخدم والتركيب</span>
        <span class="meta-pill">الإصدار 1.3.7</span>
        <span class="meta-pill">نوفمبر 2019</span>
      </div>
    </div>
    <p style="color: var(--text-secondary); margin-top: 8px;">
      ترجمة عربية كاملة مع الحفاظ على أسماء الأزرار والقوائم والمعاملات والمصطلحات التقنية باللغة الإنجليزية كما تظهر على شاشة اللوحة.
    </p>
  </div>

  <div class="figure-card">
    <div class="figure-img-wrapper" onclick="openLightbox('{img_cover}', 'لوحة التحكم في إنذار الحريق Teledata One - The Italian Touch!')">
      <img src="{img_cover}" alt="Teledata One Panel" class="figure-img" style="max-height: 480px;">
      <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
    </div>
    <div class="figure-caption">
      <strong>لوحة Teledata One</strong> — شاشة لمس رسومية ملونة 4.3 بوصة وتصميم إيطالي حديث.
    </div>
  </div>

  <div class="doc-section" id="sec-legal-info">
    <div class="section-header">
      <h3 class="section-title">معلومات الملكية وإقرار المطابقة</h3>
      <span class="section-page-tag">ص 2</span>
    </div>
    <h4 style="color: var(--brand-blue); margin-bottom: 8px;">ملكية المعلومات</h4>
    <p style="margin-bottom: 12px;">
      © حقوق النشر 2015، <bdi>Teledata s.r.l.</bdi> جميع الحقوق محفوظة. يُحظر أي توزيع كلي أو جزئي، أو تعديل، أو إعادة إنتاج لهذا المستند دون تصريح كتابي مسبق من <bdi>Teledata s.r.l.</bdi>، باستثناء الإجراءات التالية:
    </p>
    <ul style="margin-right: 24px; margin-bottom: 14px; line-height: 1.8;">
      <li>طباعة المستند كلياً أو جزئياً بصيغته الأصلية.</li>
      <li>نقل المستند إلى مواقع الويب أو غيرها من الأنظمة الإلكترونية.</li>
      <li>نسخ المحتوى دون تعديله مع الإشارة إلى <bdi>Teledata s.r.l.</bdi> بوصفها مالك حقوق النشر.</li>
    </ul>

    <div class="callout callout-note">
      <div class="callout-title">ℹ️ ملاحظة تجارية</div>
      <div class="callout-content">لا يجوز استخدام محتوى هذا المستند لتطوير محتوى آخر لأغراض تجارية دون تصريح كتابي من <bdi>Teledata s.r.l.</bdi></div>
    </div>

    <div style="background-color: var(--bg-tertiary); padding: 14px 18px; border-radius: var(--radius-sm); margin: 16px 0; font-family: var(--font-mono); font-size: 0.88rem;">
      <strong>تُوجّه طلبات الحصول على نسخ إضافية من هذا المنتج أو المعلومات التقنية إلى:</strong><br>
      <bdi>Teledata s.r.l.<br>
      20132 Milan — Italy — Via G.M. Giulietti, 8<br>
      Tel.: +39 02 27 201 352 / +39 02 25 92 795<br>
      Fax: +39 02 25 93 704<br>
      E-mail: info@teledata-i.com</bdi>
    </div>

    <h4 style="color: var(--brand-blue); margin-top: 18px; margin-bottom: 8px;">إقرار المطابقة المعياري</h4>
    <p style="margin-bottom: 12px;">
      صُمّم هذا الجهاز وفق معايير الجودة والموثوقية والأداء المعتمدة لدى Teledata. ويجب أن يتم تركيب الجهاز تركيباً احترافياً وفقاً للوائح السارية. يستوفي الجهاز التوجيهات والمعايير التالية:
    </p>
    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>المعيار / التوجيه</th>
            <th>البيان والوصف الرسمي</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><bdi>EMC Directive (EMC) 2004/108/EC</bdi></td>
            <td>توجيه التوافق الكهرومغناطيسي</td>
          </tr>
          <tr>
            <td><bdi>Low Voltage Directive (LVD) 2006/95/EC</bdi></td>
            <td>توجيه الجهد المنخفض</td>
          </tr>
          <tr>
            <td><bdi>EN 54-2</bdi></td>
            <td>أنظمة كشف الحريق وإنذار الحريق — معدات التحكم والإشارة</td>
          </tr>
          <tr>
            <td><bdi>EN 54-4 (A2:2006)</bdi></td>
            <td>أنظمة كشف الحريق وإنذار الحريق — معدات التغذية بالطاقة</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout callout-suggestion">
      <div class="callout-title">💡 خصوصية الترجمة المعتمدة في هذا الدليل</div>
      <div class="callout-content">
        هذا المستند ترجمة عربية للدليل الأصلي الصادر باللغة الإنجليزية. أُبقيت أسماء الأزرار والقوائم والمعاملات والمصطلحات التقنية باللغة الإنجليزية كما تظهر على شاشة اللوحة، مع شرح عربي أسفلها أو بجانبها، وذلك لضمان مطابقتها الفعلية لما يراه المشغّل على الجهاز.
      </div>
    </div>
  </div>
</div>

<!-- Chapter 1: Introduction -->
<div id="view-ch1" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>الفصل 1</span>
    </div>
    <div class="chapter-main-title">
      <span>1 مقدمة هذا الدليل</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">ص 7 - 8</span>
        <span class="meta-pill">2 صفحة</span>
      </div>
    </div>
  </div>

  <div class="doc-section" id="sec-1-1">
    <div class="section-header">
      <h3 class="section-title">1.1 الالتزامات المتعلقة بهذا الدليل</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 7</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-1-1', '1.1 الالتزامات المتعلقة بهذا الدليل')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>
    
    <div class="callout callout-warning">
      <div class="callout-title">⚠️ تحذير إلزامي</div>
      <div class="callout-content">
        هذا الدليل جزء لا يتجزأ من الجهاز، ويجب حفظه طوال فترة تشغيله بالكامل. كما يجب إرفاق الدليل مع الجهاز في حال نقله إلى طرف ثالث.
      </div>
    </div>
    
    <p>
      يجب الرجوع إلى هذا الدليل في جميع الحالات المرتبطة بحياة الجهاز التشغيلية، من لحظة استلامه وحتى التخلص منه. ويجب حفظه في مكان نظيف يمكن للمشغلين الوصول إليه، والحفاظ عليه في حالة جيدة.
    </p>
  </div>

  <div class="doc-section" id="sec-1-2">
    <div class="section-header">
      <h3 class="section-title">1.2 بيانات الدليل</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 7</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-1-2', '1.2 بيانات الدليل')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>
    
    <div class="table-responsive">
      <table class="doc-table">
        <tbody>
          <tr>
            <th style="width: 200px;">الجهاز</th>
            <td><bdi>Teledata One</bdi> — لوحة تحكم في إنذار الحريق</td>
          </tr>
          <tr>
            <th>عنوان الدليل</th>
            <td>دليل المستخدم والتركيب</td>
          </tr>
          <tr>
            <th>الرمز أو الإصدار</th>
            <td><bdi>v. 1.3.7 ENG</bdi> (النسخة العربية المرافقة)</td>
          </tr>
          <tr>
            <th>شهر وسنة الطباعة</th>
            <td>نوفمبر 2019</td>
          </tr>
          <tr>
            <th>نوع الدليل</th>
            <td>تعليمات أصلية (<bdi>original instructions</bdi>)</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="doc-section" id="sec-1-3">
    <div class="section-header">
      <h3 class="section-title">1.3 تنبيهات موجهة إلى قرّاء الدليل</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 7 - 8</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-1-3', '1.3 تنبيهات موجهة إلى قرّاء الدليل')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>
    
    <p style="margin-bottom: 14px;">توضح الأشكال التالية المفاهيم الرسومية المستخدمة في هذا النص:</p>

    <div class="callout callout-warning">
      <div class="callout-title">⚠️ تحذير — <bdi>Warning</bdi></div>
      <div class="callout-content">عمليات يجب تنفيذها بعناية فائقة، أو معلومات مهمة تتعلق بالسلامة.</div>
    </div>

    <div class="callout callout-note">
      <div class="callout-title">ℹ️ ملاحظة — <bdi>Note</bdi></div>
      <div class="callout-content">معلومة مهمة تُعرض بعد النص الذي تشير إليه، وغالباً ما تشرح تفصيلاً أو استثناءً.</div>
    </div>

    <div class="callout callout-suggestion">
      <div class="callout-title">💡 اقتراح — <bdi>Suggestions</bdi></div>
      <div class="callout-content">معلومات عملية تساعد على تحقيق تشغيل سليم وفعال للجهاز.</div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">كيف تقرأ هذا الدليل العربي</h4>
    <p>
      اعتمد هذا الدليل أسلوباً ثنائي اللغة في المواضع التقنية: يبقى اسم الزر أو القائمة أو المعامل كما هو بالإنجليزية تماماً كما يظهر على شاشة اللوحة، ويوضع أمامه أو أسفله شرحه بالعربية. والسبب أن تغيير هذه المسميات إلى العربية قد يجعلها لا تطابق ما يراه المشغّل فعلياً على الجهاز.
    </p>
    <p style="margin-top: 10px;">
      أما النصوص الوصفية والتعليمات والتحذيرات فقد عُرّبت تعريباً كاملاً يراعي السياق والمعنى، لا الترجمة الحرفية كلمة بكلمة.
    </p>

    <div class="callout callout-path" style="margin-top: 16px;">
      <div class="path-code"><bdi>Programming menu → Configure → System</bdi></div>
      <div class="path-desc">المسار على الشاشة: قائمة البرمجة ← التكوين ← النظام</div>
    </div>

    <div class="callout callout-note" style="margin-top: 14px;">
      <div class="callout-title">ملاحظة حول الصور (ص 8)</div>
      <div class="callout-content">
        الصور ولقطات الشاشة مأخوذة من الدليل الأصلي، وهي بالإنجليزية لأنها تمثل واجهة الجهاز الفعلية. وقد أُضيف أسفل كل صورة شرح عربي يوضح ما تعرضه وما يجب ملاحظته فيها.
      </div>
    </div>
  </div>
</div>

<!-- Chapter 2: Safety & Warranty -->
<div id="view-ch2" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>الفصل 2</span>
    </div>
    <div class="chapter-main-title">
      <span>2 السلامة والضمان</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">ص 9</span>
        <span class="meta-pill">1 صفحة</span>
      </div>
    </div>
  </div>

  <div class="doc-section" id="sec-2-1">
    <div class="section-header">
      <h3 class="section-title">2.1 قواعد السلامة</h3>
      <span class="section-page-tag">ص 9</span>
    </div>
    <p>
      تهدف المعلومات الواردة في هذا الفصل إلى ضمان تركيب الجهاز والتعامل معه بشكل صحيح. ويُفترض أن كل من يتعامل مع الجهاز على دراية بمحتوى هذا الفصل.
    </p>
  </div>

  <div class="doc-section" id="sec-2-2">
    <div class="section-header">
      <h3 class="section-title">2.2 الاستخدام المقصود</h3>
      <span class="section-page-tag">ص 9</span>
    </div>
    <p style="margin-bottom: 12px;">
      يجب تركيب الجهاز واستخدامه فقط بالطريقة الموضحة في هذا الدليل، وللأغراض المبينة في المواد الإعلانية التي توزعها <bdi>Teledata S.r.l.</bdi> ولا يجوز توصيله إلا بمعدات ومكونات وأجهزة من إنتاج أطراف ثالثة، وبالطريقة الموصى بها والمسموح بها في هذا الدليل أو من قبل <bdi>Teledata S.r.l.</bdi> مباشرة.
    </p>
    <p>
      صُمّم الجهاز وصُنع واختُبر لاستيفاء معايير السلامة المعلنة. وإذا اتُبعت تعليمات هذا الدليل أثناء تصميم الأنظمة التي يُركّب فيها، وأثناء التركيب والاستخدام، فإن الجهاز لا يشكل خطراً على الأشخاص أو الممتلكات.
    </p>
  </div>

  <div class="doc-section" id="sec-2-3">
    <div class="section-header">
      <h3 class="section-title">2.3 قيود الضمان</h3>
      <span class="section-page-tag">ص 9</span>
    </div>
    <p style="margin-bottom: 12px;">
      لا تتحمل Teledata المسؤولية عن أضرار مباشرة أو غير مباشرة تلحق بالأشخاص أو الممتلكات نتيجة استخدام الجهاز في ظروف غير الظروف المقصودة.
    </p>
    <p style="margin-bottom: 12px;">
      يجب أن يقوم فنيون مؤهلون بتركيب هذا الجهاز مع الالتزام الصارم بتعليمات هذا الدليل، ووفقاً للقوانين والمعايير ولوائح السلامة المحلية السارية.
    </p>
    
    <div class="callout callout-warning">
      <div class="callout-title">شروط استحقاق وسقوط الضمان</div>
      <div class="callout-content">
        يضمن هذا المنتج ضد عيوب المواد وعيوب التصنيع لمدة <strong>12 شهراً</strong> من تاريخ الفحص.<br>
        <strong>ولا يشمل الضمان العيوب الناتجة عن:</strong>
        <ul style="margin-right: 20px; margin-top: 6px;">
          <li>الاستخدام غير السليم أو الإهمال.</li>
          <li>الأضرار الناتجة عن التعرض للعوامل الجوية.</li>
          <li>التخريب المتعمد.</li>
          <li>تآكل المواد.</li>
        </ul>
        <div style="margin-top: 8px; font-weight: 700; color: var(--brand-red);">
          يسقط الضمان عندما تكون الأعطال ناتجة عن استخدام غير سليم أو عن إجراءات تشغيل غير منصوص عليها في دليل المستخدم هذا.
        </div>
      </div>
    </div>
  </div>

  <div class="doc-section" id="sec-2-4">
    <div class="section-header">
      <h3 class="section-title">2.4 الدعم الفني</h3>
      <span class="section-page-tag">ص 9</span>
    </div>
    <p style="margin-bottom: 14px;">
      أُعدّ هذا الدليل بعناية وهو موجّه إلى الفنيين المؤهلين. ولأي استفسارات أو طلبات تقنية خاصة، يُرجى التواصل مع فريقنا. يمكنكم الكتابة أو الاتصال للحصول على مساعدة من أشخاص قادرين على الإجابة عن أسئلتكم وتقديم الدعم:
    </p>
    <div class="table-responsive">
      <table class="doc-table">
        <tbody>
          <tr>
            <th style="width: 200px;">البريد الإلكتروني للخدمة</th>
            <td><bdi>info@teledata-i.com</bdi></td>
          </tr>
          <tr>
            <th>هاتف الخدمة</th>
            <td><bdi>+39 0227201352</bdi></td>
          </tr>
          <tr>
            <th>فاكس الخدمة</th>
            <td><bdi>+39 022593704</bdi></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- Chapter 3: Product Identification -->
<div id="view-ch3" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>الفصل 3</span>
    </div>
    <div class="chapter-main-title">
      <span>3 تعريف المنتج</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">ص 10 - 12</span>
        <span class="meta-pill">3 صفحات</span>
      </div>
    </div>
  </div>

  <div class="doc-section" id="sec-3-1">
    <div class="section-header">
      <h3 class="section-title">3.1 بيانات تعريف الشركة المصنعة</h3>
      <span class="section-page-tag">ص 10</span>
    </div>
    <div class="table-responsive">
      <table class="doc-table">
        <tbody>
          <tr>
            <th style="width: 180px;">الشركة</th>
            <td><bdi>Teledata s.r.l.</bdi></td>
          </tr>
          <tr>
            <th>المقر الرئيسي</th>
            <td><bdi>20132 Milan — Italy — Via G.M. Giulietti, 8</bdi></td>
          </tr>
          <tr>
            <th>مركز التشغيل</th>
            <td><bdi>20063 Cernusco Sul Naviglio — Italy — Via Brescia, 24</bdi></td>
          </tr>
          <tr>
            <th>الهاتف</th>
            <td><bdi>+39 02 27 201 352 / +39 02 25 92 795</bdi></td>
          </tr>
          <tr>
            <th>الفاكس</th>
            <td><bdi>+39 02 25 93 704</bdi></td>
          </tr>
          <tr>
            <th>البريد الإلكتروني</th>
            <td><bdi>info@teledata-i.com</bdi></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="doc-section" id="sec-3-2">
    <div class="section-header">
      <h3 class="section-title">3.2 محتويات العبوة</h3>
      <span class="section-page-tag">ص 10</span>
    </div>
    <p style="margin-bottom: 12px;">تحتوي العبوة على العناصر التالية:</p>
    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>الوصف</th>
            <th>الكمية</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>لوحة <bdi>Teledata One</bdi></td>
            <td>1</td>
          </tr>
          <tr>
            <td>طقم الكابلات</td>
            <td>1</td>
          </tr>
          <tr>
            <td>طقم المقاومات والدايودات والوصلات (<bdi>jumpers</bdi>)</td>
            <td>1</td>
          </tr>
          <tr>
            <td>دليل التركيب والمستخدم (هذا الدليل)</td>
            <td>1</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="doc-section" id="sec-3-3">
    <div class="section-header">
      <h3 class="section-title">3.3 تحديد الطراز والرقم التسلسلي</h3>
      <span class="section-page-tag">ص 10 - 11</span>
    </div>
    <p style="margin-bottom: 14px;">
      يوجد داخل لوحة التحكم ملصق تعريفي لا يجوز إزالته تحت أي ظرف. يُرجى الرجوع إلى بيانات اللوحة عند طلب الصيانة أو أعمال الصيانة الدورية أو الملحقات.
    </p>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig1}', 'الشكل 1: لوحة البيانات المعدنية المثبتة داخل اللوحة')">
        <img src="{img_fig1}" alt="الشكل 1" class="figure-img" style="max-height: 440px;">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 1:</strong> لوحة البيانات المعدنية المثبتة داخل اللوحة، وتظهر عليها علامة <bdi>CE</bdi> واسم الشركة والطراز <bdi>TELEDATA ONE</bdi> ورقم المنتج والرقم التسلسلي وبيانات التغذية الكهربائية. استخدم هذه البيانات عند التواصل مع الدعم الفني.
      </div>
    </div>
  </div>

  <div class="doc-section" id="sec-3-4">
    <div class="section-header">
      <h3 class="section-title">3.4 مطابقة المعايير</h3>
      <span class="section-page-tag">ص 11 - 12</span>
    </div>
    <ul style="margin-right: 22px; margin-bottom: 16px; line-height: 1.8;">
      <li><bdi>EN 54-2</bdi>: أنظمة كشف الحريق وإنذار الحريق — معدات التحكم والإشارة.</li>
      <li><bdi>EN 54-4</bdi>: أنظمة كشف الحريق وإنذار الحريق — معدات التغذية بالطاقة (مدمجة في لوحة التحكم).</li>
      <li><strong>نوع المنتج:</strong> أنظمة كشف وإنذار حريق للمباني.</li>
      <li><strong>الاستخدام المقصود:</strong> السلامة من الحريق.</li>
    </ul>

    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>الخاصية الأساسية</th>
            <th>المواصفة الفنية المنسقة <bdi>EN 54-2:1997/A1:2006:AC1999</bdi></th>
            <th>المواصفة الفنية المنسقة <bdi>EN 54-4:1997/A2:2006/AC:1999</bdi></th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>الأداء في ظروف الحريق</td>
            <td><bdi>cl. 4, 5, 7</bdi></td>
            <td>—</td>
          </tr>
          <tr>
            <td>زمن الاستجابة (زمن الاستجابة للحريق)</td>
            <td><bdi>cl. 7.1, 7.7</bdi></td>
            <td>—</td>
          </tr>
          <tr>
            <td>الموثوقية التشغيلية</td>
            <td><bdi>cl. 4, 5, 6, 7, 8, 9, 10, 12, 13, 14</bdi></td>
            <td><bdi>cl. 4, 5, 6, 7, 8</bdi></td>
          </tr>
          <tr>
            <td>متانة الموثوقية: مقاومة الحرارة</td>
            <td><bdi>cl. 15.4</bdi></td>
            <td><bdi>cl. 9.5</bdi></td>
          </tr>
          <tr>
            <td>متانة الموثوقية: مقاومة الاهتزاز</td>
            <td><bdi>cl. 15.6, 15.7, 15.15</bdi></td>
            <td><bdi>cl. 9.7, 9.8, 9.15</bdi></td>
          </tr>
          <tr>
            <td>متانة الموثوقية: الاستقرار الكهربائي</td>
            <td><bdi>cl. 15.8, 15.13</bdi></td>
            <td><bdi>cl. 9.9</bdi></td>
          </tr>
          <tr>
            <td>متانة الموثوقية: مقاومة الرطوبة</td>
            <td><bdi>cl. 15.5, 15.14</bdi></td>
            <td><bdi>cl. 9.6, 9.14</bdi></td>
          </tr>
        </tbody>
      </table>
    </div>
    <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 8px;">
      * تشير <bdi>cl.</bdi> إلى رقم البند في المعيار الأوروبي المقابل.
    </p>
  </div>
</div>

<!-- Chapter 4: Device Management -->
<div id="view-ch4" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>الفصل 4</span>
    </div>
    <div class="chapter-main-title">
      <span>4 إدارة الجهاز</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">ص 13</span>
        <span class="meta-pill">1 صفحة</span>
      </div>
    </div>
  </div>

  <div class="doc-section" id="sec-4-1">
    <div class="section-header">
      <h3 class="section-title">4.1 النقل</h3>
      <span class="section-page-tag">ص 13</span>
    </div>
    <p>
      بعد تغليف الجهاز وتعبئته بعناية، يجب اتخاذ الاحتياطات المعتادة أثناء النقل، أي تثبيت الصندوق وتأمينه لمنع انقلابه أو سقوطه بما قد يتلف الجهاز. كما يجب مراعاة حدود درجة الحرارة.
    </p>
  </div>

  <div class="doc-section" id="sec-4-2">
    <div class="section-header">
      <h3 class="section-title">4.2 الظروف البيئية</h3>
      <span class="section-page-tag">ص 13</span>
    </div>
    <p style="margin-bottom: 12px;">يجب مراعاة حدود درجة الحرارة التالية:</p>
    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>الحالة</th>
            <th>نطاق درجة الحرارة</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>التخزين والنقل</td>
            <td><bdi>-40 °C / +70 °C</bdi></td>
          </tr>
          <tr>
            <td>التشغيل</td>
            <td><bdi>-5 °C / +40 °C</bdi></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="doc-section" id="sec-4-3">
    <div class="section-header">
      <h3 class="section-title">4.3 فك التغليف</h3>
      <span class="section-page-tag">ص 13</span>
    </div>
    <p>
      عند استلام الجهاز، يجب فك التغليف بعناية مع الحرص على التخلص من النفايات وفقاً للوائح التخلص من النفايات السارية.
    </p>
  </div>

  <div class="doc-section" id="sec-4-4">
    <div class="section-header">
      <h3 class="section-title">4.4 الاستبدال</h3>
      <span class="section-page-tag">ص 13</span>
    </div>
    <p>
      لاستبدال جهاز قديم، افصل الجهاز القديم ووصّل الجهاز الجديد وفقاً لمخططات التركيب المعنية. وتخلص من الجهاز القديم وفقاً للوائح التخلص من النفايات السارية.
    </p>
  </div>

  <div class="doc-section" id="sec-4-5">
    <div class="section-header">
      <h3 class="section-title">4.5 التخلص من الجهاز</h3>
      <span class="section-page-tag">ص 13</span>
    </div>
    <div class="callout callout-warning">
      <div class="callout-title">⚠️ تحذير بيئي</div>
      <div class="callout-content">
        تجنّب إتلاف الجهاز بالحرق أو التخلص منه في المجاري المائية. يجب التخلص من المنتج بطريقة آمنة.
      </div>
    </div>
    <p>
      قبل التخلص من المنتج، يجب إزالة البطاريات من جميع المنتجات التي تحتوي على بطاريات، مع الحرص على تجنب حدوث دوائر قصيرة. ويجب مراعاة اللوائح السارية بشأن التخلص من البطاريات.
    </p>
  </div>
</div>

<!-- Chapter 5: Introduction & Specs -->
<div id="view-ch5" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>الفصل 5</span>
    </div>
    <div class="chapter-main-title">
      <span>5 مقدمة عن <bdi>Teledata One</bdi> والمواصفات التقنية</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">ص 14 - 17</span>
        <span class="meta-pill">4 صفحات</span>
      </div>
    </div>
  </div>

  <div class="doc-section" id="sec-5-1">
    <div class="section-header">
      <h3 class="section-title">5.1 الخصائص العامة</h3>
      <span class="section-page-tag">ص 14</span>
    </div>
    <p style="margin-bottom: 12px;">
      <bdi>Teledata One</bdi> لوحة تحكم في كشف الحريق قابلة للبرمجة عبر معالج دقيق. وتعتمد اللوحة نظاماً معنوناً تناظرياً (<bdi>analogue addressed</bdi>)، مع إدارة مستقلة للإشارات وإجراءات الإنذار.
    </p>
    <p style="margin-bottom: 12px;">
      تستطيع اللوحة إدارة كشف الحريق عبر خط تناظري معنون واحد، قابل للتوسعة حتى <strong>9 خطوط</strong>. ويمكن لكل حلقة التحكم بما يصل إلى <strong>240 كاشفاً ووحدة إدخال/إخراج</strong>، أو 126 جهازاً (من <bdi>Apollo XP95/Discovery</bdi>)، أو 240 جهازاً (من <bdi>Apollo Soteria</bdi>).
    </p>
    <p style="margin-bottom: 12px;">
      يُجهّز النظام بمعالج دقيق <bdi>32-bit</bdi> مع ذاكرة RAM وذاكرة وميضية (<bdi>flash</bdi>) وذاكرة <bdi>EEPROM</bdi> للتخزين غير المتطاير لبيانات التكوين.
    </p>
    <p style="margin-bottom: 12px;">
      يمكن برمجة لوحة التحكم باستخدام شاشة اللمس، أو باستيراد بيانات البرمجة من ذاكرة <bdi>USB</bdi>.
    </p>
    <p>
      وكما هي الحال في جميع منتجات Teledata، يمكن إدارة Teledata One عبر برنامج الإشراف والتحكم المدمج.
    </p>
  </div>

  <div class="doc-section" id="sec-5-2">
    <div class="section-header">
      <h3 class="section-title">5.2 احتياطات التركيب</h3>
      <span class="section-page-tag">ص 14</span>
    </div>
    
    <div class="callout callout-warning">
      <div class="callout-title">⚠️ تحذير — السلامة الكهربائية</div>
      <div class="callout-content">
        اللوحات الإلكترونية مزوّدة بأشباه موصلات حساسة للشحنات الكهربائية الساكنة. لذلك يجب التعامل مع اللوحات من أطرافها فقط، وعدم لمس مكوناتها الإلكترونية.
      </div>
    </div>

    <ul style="margin-right: 22px; margin-bottom: 14px; line-height: 1.8;">
      <li>يجب تنفيذ تأريض جيد لتقليل احتمال التلف وحساسية الضوضاء الكهربائية.</li>
      <li>أثناء تصميم النظام، يجب مراعاة زمن الاستقلالية المطلوب من أجل تحديد سعة البطاريات المستخدمة.</li>
      <li>افصل البطاريات وتغذية التيار المتردد وأي مصدر تغذية آخر قبل إدخال أو إزالة أي لوحة إلكترونية وقبل تنفيذ أي عمل صيانة على لوحة التحكم (باستثناء تحميل إصدار جديد من البرنامج الثابت FW).</li>
      <li>قد تتسبب الأجهزة الطرفية غير المتوافقة مع لوحة التحكم — مثل الكواشف والوحدات وأجهزة الإنذار الصوتية — في تشغيل غير سليم للوحة أو حتى في تلفها. لذلك من الضروري استخدام مواد متوافقة مع لوحات تحكم Teledata.</li>
    </ul>

    <div class="callout callout-note">
      <div class="callout-title">البطاريات المطلوبة</div>
      <div class="callout-content">
        يجب استخدام لوحة <bdi>Teledata One</bdi> مع بطاريتين <bdi>12V — 7.2Ah</bdi> أو <bdi>17Ah</bdi>.
      </div>
    </div>
  </div>

  <div class="doc-section" id="sec-5-3">
    <div class="section-header">
      <h3 class="section-title">5.3 المواصفات التقنية</h3>
      <span class="section-page-tag">ص 14 - 15</span>
    </div>

    <h4 style="color: var(--brand-blue); margin-bottom: 8px;">5.3.1 خصائص العتاد <bdi>HARDWARE</bdi></h4>
    <ul style="margin-right: 22px; margin-bottom: 18px; line-height: 1.8;">
      <li>لوحة تحكم معنونة بمعالج دقيق <bdi>32-bit</bdi>.</li>
      <li>حلقة واحدة معنونة ببروتوكول رقمي، قابلة للتكوين كحلقة مفتوحة أو مغلقة.</li>
      <li>قابلة للتوسعة حتى <strong>9 حلقات</strong>.</li>
      <li>شاشة لمس رسومية (<bdi>4.3" TFT 272×480</bdi>).</li>
      <li>حماية من الدائرة القصيرة في الحلقة.</li>
      <li>14 مؤشر <bdi>LED</bdi> أمامياً.</li>
      <li>خرج واحد مراقب لصفارة أو مُطالب هاتفي (<bdi>24Vdc @ 500mA</bdi>).</li>
      <li>خرج عام من النوع C (<bdi>30Vdc / 120Vac @ 1A</bdi>).</li>
      <li>خرج عام مفتوح المجمّع (<bdi>open collector</bdi>).</li>
      <li>خط <bdi>RS-485</bdi> واحد للأجهزة الطرفية.</li>
      <li>منفذ <bdi>RS-232/microUSB</bdi> للبرمجة.</li>
      <li>مؤشر <bdi>LED</bdi> جانبي ملوّن.</li>
      <li>56 مؤشر منطقة <bdi>LED</bdi> (لوحة اختيارية).</li>
      <li>سعة البطاريات: <bdi>2×7.2Ah</bdi> أو <bdi>2×17Ah</bdi> مع إدارة شاحن وفق <bdi>EN54-4</bdi>.</li>
      <li>خرج تغذية مساعدة <bdi>AUX</bdi> مراقب <bdi>24Vdc @ 500mA</bdi> مع حماية من الدائرة القصيرة.</li>
      <li>الأبعاد: <bdi>410 × 410 × 120 mm</bdi>.</li>
      <li>التغذية: <bdi>230V AC</bdi>.</li>
    </ul>

    <h4 style="color: var(--brand-blue); margin-bottom: 8px;">5.3.2 خصائص البرمجيات</h4>
    <ul style="margin-right: 22px; margin-bottom: 18px; line-height: 1.8;">
      <li>حتى 240 جهازاً معنوناً لكل حلقة (<bdi>Teledata</bdi>).</li>
      <li>حتى 240 جهازاً معنوناً لكل حلقة (<bdi>Argus</bdi>).</li>
      <li>حتى 126 جهازاً معنوناً لكل حلقة (<bdi>Apollo XP95/Discovery</bdi>).</li>
      <li>حتى 240 جهازاً معنوناً لكل حلقة (<bdi>Apollo Soteria</bdi>).</li>
      <li>تقسيم حتى 192 منطقة كشف.</li>
      <li>255 دالة منطقية.</li>
      <li>أرشيف يحتفظ بأكثر من <strong>850 حدثاً</strong>.</li>
      <li>برمجة تلقائية للحلقات التناظرية.</li>
      <li>عنونة تلقائية للحلقات التناظرية.</li>
      <li>تخطيط الأجهزة (<bdi>Devices Mapping</bdi>).</li>
      <li>الاتصال بلوحات تحكم أخرى عبر شبكة مقاومة للأعطال (<bdi>fault tolerant</bdi>).</li>
      <li>إدارة لغات متعددة.</li>
      <li>قابلة للتخصيص الكامل بشعار شخصي ولون ومؤشرات LED جانبية متعددة الألوان.</li>
      <li>إدارة أنواع مختلفة من الكواشف والوحدات التناظرية:
        <ul style="margin-right: 24px; margin-top: 4px;">
          <li>كواشف حرارية وبصرية ومختلطة.</li>
          <li>وحدات إدخال <bdi>Input Modules</bdi>.</li>
          <li>وحدات خرج <bdi>Output Modules</bdi>.</li>
          <li>نقاط نداء معنونة <bdi>Addressed call points</bdi>.</li>
          <li>أجهزة إنذار صوتية معنونة <bdi>Addressable sirens</bdi>.</li>
          <li>مترجم لاسلكي <bdi>Wireless translator</bdi>.</li>
        </ul>
      </li>
    </ul>
  </div>

  <div class="doc-section" id="sec-5-4">
    <div class="section-header">
      <h3 class="section-title">5.4 البيانات التقنية</h3>
      <span class="section-page-tag">ص 16 - 17</span>
    </div>

    <h4 style="color: var(--brand-blue); margin-bottom: 8px;">5.4.1 لوحة البيانات (<bdi>Datum plate</bdi>)</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>البند</th>
            <th>القيمة</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>الجهد الابتدائي</td>
            <td><bdi>230 Vac / 50 Hz</bdi></td>
          </tr>
          <tr>
            <td>الاستهلاك الابتدائي</td>
            <td><bdi>~ 300 mA</bdi></td>
          </tr>
          <tr>
            <td>مصهر 230V~</td>
            <td><bdi>F4Ah</bdi></td>
          </tr>
        </tbody>
      </table>
    </div>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">5.4.2 الخصائص الكهربائية</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>البند</th>
            <th>القيمة</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>أدنى جهد تشغيل</td>
            <td><bdi>21.6 V</bdi></td>
          </tr>
          <tr>
            <td>بطاريات الاحتياط</td>
            <td><bdi>n° 2 (12Vdc / 17Ah or 12Vdc / 7.2Ah)</bdi></td>
          </tr>
          <tr>
            <td>أقصى مقاومة داخلية للبطارية</td>
            <td><bdi>800 mΩ</bdi></td>
          </tr>
          <tr>
            <td>التيار المتاح للأحمال الخارجية</td>
            <td><bdi>500 mA</bdi></td>
          </tr>
          <tr>
            <td>استهلاك وضع الانتظار</td>
            <td><bdi>300 mA – 12V</bdi></td>
          </tr>
          <tr>
            <td>خط أجهزة الإنذار المراقب</td>
            <td><bdi>Max. 500 mA – 27.6 V DC</bdi></td>
          </tr>
          <tr>
            <td>مرحّل الأعطال</td>
            <td><bdi>Max. 1A – 30V DC / 120V AC</bdi></td>
          </tr>
        </tbody>
      </table>
    </div>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">5.4.3 الخصائص الوظيفية</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>البند</th>
            <th>القيمة أو الوصف</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>لوحة مفاتيح التشغيل</td>
            <td>شاشة لمس</td>
          </tr>
          <tr>
            <td>الرسائل البصرية</td>
            <td>مؤشرات <bdi>LED</bdi></td>
          </tr>
          <tr>
            <td>الرسائل الصوتية</td>
            <td>جرس (<bdi>buzzer</bdi>)</td>
          </tr>
          <tr>
            <td>عرض الأحداث</td>
            <td><bdi>480×272 TFT 4.3"</bdi></td>
          </tr>
          <tr>
            <td>خرج تسلسلي للحاسوب</td>
            <td><bdi>N° 1 – RS232</bdi></td>
          </tr>
          <tr>
            <td>سجل الأحداث</td>
            <td><bdi>Max. 850</bdi></td>
          </tr>
          <tr>
            <td>وضع التشغيل</td>
            <td>محمي / غير محمي (<bdi>Guarded/Unguarded</bdi>)</td>
          </tr>
          <tr>
            <td>مفتاح عتاد البرمجة/الإدارة</td>
            <td>كلمة مرور متعددة المستويات</td>
          </tr>
          <tr>
            <td>عدد الخطوط التناظرية</td>
            <td>حلقة واحدة قابلة للتوسعة إلى 9 حلقات</td>
          </tr>
          <tr>
            <td>استثناء الخط التناظري</td>
            <td>مفرد — متعدد</td>
          </tr>
          <tr>
            <td>وحدات الإدخال/الإخراج والكواشف لكل خط</td>
            <td><bdi>Max. 240</bdi></td>
          </tr>
          <tr>
            <td>نوع البرمجة</td>
            <td>يدوية أو عبر الحاسوب</td>
          </tr>
          <tr>
            <td>تكوين الخط التناظري</td>
            <td>192 منطقة برمجية</td>
          </tr>
          <tr>
            <td>توصيل الخطوط التناظرية</td>
            <td>حلقة مفتوحة أو مغلقة</td>
          </tr>
          <tr>
            <td>طول خطوط الكواشف</td>
            <td><bdi>Max. 5000 m</bdi></td>
          </tr>
          <tr>
            <td>نوع الكابل</td>
            <td>محجوب — محجوب (<bdi>Shielded</bdi>)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">5.4.4 الخصائص الميكانيكية</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>البند</th>
            <th>القيمة</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>مستوى الحماية</td>
            <td><bdi>IP30</bdi></td>
          </tr>
          <tr>
            <td>الخزانة</td>
            <td>حديد</td>
          </tr>
          <tr>
            <td>الأبعاد (العرض × الطول × العمق)</td>
            <td><bdi>410 × 410 × 120 mm</bdi></td>
          </tr>
          <tr>
            <td>الوزن (دون بطاريات)</td>
            <td><bdi>6 kg</bdi></td>
          </tr>
          <tr>
            <td>الطلاء</td>
            <td>راتنج إيبوكسي (<bdi>Epoxy resin</bdi>)</td>
          </tr>
          <tr>
            <td>اللون</td>
            <td>أسود، أبيض</td>
          </tr>
          <tr>
            <td>فتحات مرور المواسير</td>
            <td><bdi>4 × 25 mm</bdi></td>
          </tr>
        </tbody>
      </table>
    </div>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">5.4.5 الخصائص البيئية</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>البند</th>
            <th>القيمة</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>درجة حرارة التخزين</td>
            <td><bdi>(-40 ÷ +70) °C</bdi></td>
          </tr>
          <tr>
            <td>درجة حرارة التشغيل</td>
            <td><bdi>(-5 ÷ +40) °C</bdi></td>
          </tr>
          <tr>
            <td>رطوبة التشغيل (نسبية)</td>
            <td><bdi>90 %</bdi></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<!-- Chapter 6: Hardware Configuration -->
<div id="view-ch6" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>الفصل 6</span>
    </div>
    <div class="chapter-main-title">
      <span>6 تكوين العتاد</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">ص 18</span>
        <span class="meta-pill">1 صفحة</span>
      </div>
    </div>
  </div>

  <div class="doc-section" id="sec-6-1">
    <div class="section-header">
      <h3 class="section-title">6.1 تجهيزات لوحة التحكم</h3>
      <span class="section-page-tag">ص 18</span>
    </div>
    <p style="margin-bottom: 12px;">عند تجهيز لوحة التحكم بكامل التجهيزات، يمكن أن تشمل:</p>
    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>المكوّن</th>
            <th>الوظيفة والبيان</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><bdi>1 main logic board (TD571/E)</bdi></td>
            <td>اللوحة المنطقية الرئيسية، وتُدار عبرها الحلقة الأولى وجميع وظائف اللوحة.</td>
          </tr>
          <tr>
            <td><bdi>4 loop expansion logic boards (ONE2)</bdi></td>
            <td>لوحات توسعة الحلقات، كل بطاقة تضيف حلقتين معنونتين، وبحد أقصى 4 بطاقات.</td>
          </tr>
          <tr>
            <td><bdi>1 synoptic led (ONE56)</bdi></td>
            <td>لوحة مؤشرات المنطقة الإضافية (56 مؤشر LED).</td>
          </tr>
          <tr>
            <td><bdi>1 ONECONNECT network card</bdi></td>
            <td>بطاقة اتصال شبكي LAN أو WAN.</td>
          </tr>
          <tr>
            <td><bdi>1 ONERING card</bdi></td>
            <td>بطاقة ربط اللوحات في شبكة حلقية.</td>
          </tr>
          <tr>
            <td><bdi>2 batteries (max 12V @ 18Ah)</bdi></td>
            <td>بطاريتا احتياط لتغذية اللوحة عند انقطاع الشبكة.</td>
          </tr>
          <tr>
            <td><bdi>1 additional power supply (ONEPW)</bdi></td>
            <td>مصدر تغذية إضافي عند زيادة الأحمال.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout callout-note">
      <div class="callout-title">الحد الأقصى لعدد الحلقات</div>
      <div class="callout-content">
        الحد الأقصى لعدد الحلقات في التجهيز الكامل هو <strong>9 حلقات</strong>: الحلقة الأولى على اللوحة الرئيسية (<bdi>TD571/E</bdi>)، و8 حلقات على بطاقات <bdi>ONE2</bdi> الأربع.
      </div>
    </div>
  </div>
</div>
"""
