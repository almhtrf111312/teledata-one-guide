# -*- coding: utf-8 -*-
"""
Content for Chapter 7: Planning and Connections (ص 19 - 45).
Comprehensive extraction from Teledata One Manual.
"""

def get_ch7_html(images):
    img_fig2 = images.get("fig_2", "")
    img_fig3 = images.get("fig_3", "")
    img_fig4 = images.get("fig_4", "")
    img_fig5 = images.get("fig_5", "")
    img_fig6 = images.get("fig_6", "")
    img_fig7 = images.get("fig_7", "")
    img_fig8 = images.get("fig_8", "")
    img_fig9 = images.get("fig_9", "")
    img_fig10 = images.get("fig_10", "")
    img_fig11 = images.get("fig_11", "")
    img_fig12 = images.get("fig_12", "")
    img_fig13 = images.get("fig_13", "")
    img_fig14 = images.get("fig_14", "")
    img_fig15 = images.get("fig_15", "")
    img_hw_table = images.get("table_hardware_config", "")

    return f"""
<!-- Chapter 7: Planning & Connections -->
<div id="view-ch7" class="chapter-view">
  <div class="chapter-hero">
    <div class="breadcrumbs">
      <a href="#view-cover" onclick="showChapter('cover')">الدليل</a> &gt; <span>الفصل 7</span>
    </div>
    <div class="chapter-main-title">
      <span>7 التخطيط والتوصيلات</span>
      <div class="chapter-meta-pills">
        <span class="meta-pill pill-primary">ص 19 - 45</span>
        <span class="meta-pill">27 صفحة</span>
      </div>
    </div>
    <p style="color: var(--text-secondary); margin-top: 6px;">
      المخططات التفصيلية للوحة المنطقية الرئيسية وبطاقات التوسعة، كابلات الشبكة والحلقات، ومخططات توصيل الأجهزة.
    </p>
  </div>

  <!-- 7.1 TD571/E Main Board -->
  <div class="doc-section" id="sec-7-1">
    <div class="section-header">
      <h3 class="section-title">7.1 مخطط اللوحة المنطقية <bdi>TD571/E</bdi></h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 19 - 21</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-7-1', '7.1 مخطط اللوحة المنطقية TD571/E')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig2}', 'الشكل 2: اللوحة المنطقية الرئيسية TD571/E ومواضع الموصلات')">
        <img src="{img_fig2}" alt="الشكل 2: TD571/E" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 2:</strong> اللوحة المنطقية الرئيسية <bdi>TD571/E</bdi> مع تحديد مواضع الموصلات. الأسماء <bdi>J1, J4, J6, J7, J9, J10, J11, J12, J13, J14, J15, Y1, Y2, Y3, JP2, JP3, JP4</bdi> هي تسميات فنية ثابتة على اللوحة ولا تُترجم.
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">جدول الموصلات المتوفرة على اللوحة الرئيسية:</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead>
          <tr>
            <th>الموصل</th>
            <th>الوظيفة والبيان الفني</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><bdi>J15 & J14</bdi></td>
            <td>توصيل بطاقات توسعة الحلقات <bdi>ONE2</bdi>.</td>
          </tr>
          <tr>
            <td><bdi>J7</bdi></td>
            <td>توصيلات بطاقة <bdi>ONERING</bdi>.</td>
          </tr>
          <tr>
            <td><bdi>Y2</bdi></td>
            <td>توصيل شاشة اللمس.</td>
          </tr>
          <tr>
            <td><bdi>J11</bdi></td>
            <td>توصيلات بطاقة <bdi>ONECONNECT</bdi>.</td>
          </tr>
          <tr>
            <td><bdi>J13</bdi></td>
            <td>تغذية <bdi>AL2</bdi>.</td>
          </tr>
          <tr>
            <td><bdi>J1</bdi></td>
            <td>تغذية <bdi>AL1</bdi> والبطاريات.</td>
          </tr>
          <tr>
            <td><bdi>Y1</bdi></td>
            <td>التحكم في تغذية <bdi>DIM</bdi>.</td>
          </tr>
          <tr>
            <td><bdi>J9</bdi></td>
            <td>إرسال وعودة حلقة الحريق.</td>
          </tr>
          <tr>
            <td><bdi>J4</bdi></td>
            <td><bdi>RS-485</bdi>، وخرج <bdi>AUX</bdi>، وخرج المراقبة، وخرج عطل من النوع C.</td>
          </tr>
          <tr>
            <td><bdi>J10</bdi></td>
            <td>إدخال/إخراج منطقي (<bdi>logical in/out</bdi>).</td>
          </tr>
          <tr>
            <td><bdi>J6</bdi></td>
            <td>توصيل <bdi>RS-232</bdi>.</td>
          </tr>
          <tr>
            <td><bdi>JP3</bdi></td>
            <td>حماية البرمجة (مغلق = ممكّن).</td>
          </tr>
          <tr>
            <td><bdi>JP4</bdi></td>
            <td>ضبط حالة مراقب النظام (<bdi>watchdog</bdi>).</td>
          </tr>
          <tr>
            <td><bdi>JP2</bdi></td>
            <td>ضبط حالة تحديث البرنامج الثابت (مغلق = تحديث <bdi>FW</bdi>).</td>
          </tr>
          <tr>
            <td><bdi>J12</bdi></td>
            <td>اختيار المنفذ التسلسلي (إلى اليمين = <bdi>RS232</bdi>، إلى اليسار = <bdi>LAN</bdi>).</td>
          </tr>
          <tr>
            <td><bdi>Y3</bdi></td>
            <td>منفذ <bdi>USB</bdi>: في لوحة <bdi>TD571E</bdi> يكون المنفذ <bdi>micro USB</bdi>، وفي لوحة أقدم من <bdi>TD571E</bdi> يكون <bdi>mini USB</bdi>.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="callout callout-warning">
      <div class="callout-title">تنبيه الموصلات الداخلية المحددة مسبقاً (ص 20)</div>
      <div class="callout-content">
        الموصلات <bdi>J14, Y1, J1, J13</bdi> و <bdi>J15</bdi> موصلات ذات تمديدات محددة مسبقاً، ويجب توصيلها بعناصر مثبتة أصلاً في لوحة التحكم. ولا يجوز فصلها وإعادة توصيلها إلا في حال الحاجة إلى استبدال اللوحات أو إضافتها.<br>
        أما تمديدات الموصلات <bdi>J11, J6, J10, J4, J9</bdi> و <bdi>J7</bdi> فتختلف بحسب تجهيز النظام الذي تُوصَّل به لوحة التحكم.
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">تفاصيل أطراف الموصلات على اللوحة الرئيسية:</h4>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 10px;">
      <!-- J13 -->
      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th colspan="3">الموصل <bdi>J13</bdi></th></tr><tr><th>الطرف</th><th>الاسم</th><th>الوظيفة</th></tr></thead>
          <tbody>
            <tr><td>1</td><td><bdi>PS2+</bdi></td><td>تغذية موجبة <bdi>PS2</bdi></td></tr>
            <tr><td>2</td><td><bdi>PS2−</bdi></td><td>تغذية سالبة <bdi>PS2</bdi></td></tr>
          </tbody>
        </table>
      </div>

      <!-- J1 -->
      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th colspan="3">الموصل <bdi>J1</bdi></th></tr><tr><th>الطرف</th><th>الاسم</th><th>الوظيفة</th></tr></thead>
          <tbody>
            <tr><td>1</td><td><bdi>PS1+</bdi></td><td>تغذية موجبة <bdi>PS1</bdi></td></tr>
            <tr><td>2</td><td><bdi>PS1−</bdi></td><td>تغذية سالبة <bdi>PS1</bdi></td></tr>
            <tr><td>3</td><td><bdi>BAT −</bdi></td><td>البطاريات — القطب السالب</td></tr>
            <tr><td>4</td><td><bdi>BAT +</bdi></td><td>البطاريات — القطب الموجب</td></tr>
          </tbody>
        </table>
      </div>

      <!-- Y1 -->
      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th colspan="3">الموصل <bdi>Y1</bdi></th></tr><tr><th>الطرف</th><th>الاسم</th><th>الوظيفة</th></tr></thead>
          <tbody>
            <tr><td>1</td><td><bdi>DIM+</bdi></td><td>تحكم <bdi>DIM+</bdi> في تغذية <bdi>PS1</bdi></td></tr>
            <tr><td>2</td><td><bdi>DIM−</bdi></td><td>تحكم <bdi>DIM−</bdi> في تغذية <bdi>PS1</bdi></td></tr>
            <tr><td>3</td><td><bdi>DIM2</bdi></td><td>تحكم <bdi>DIM</bdi> في تغذية <bdi>PS2</bdi></td></tr>
          </tbody>
        </table>
      </div>

      <!-- J9 -->
      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th colspan="3">الموصل <bdi>J9</bdi> (الحلقة الأساسية)</th></tr><tr><th>الطرف</th><th>الاسم</th><th>الوظيفة</th></tr></thead>
          <tbody>
            <tr><td>1</td><td><bdi>FW+</bdi></td><td>إرسال الحلقة +</td></tr>
            <tr><td>2</td><td><bdi>FW−</bdi></td><td>إرسال الحلقة −</td></tr>
            <tr><td>3</td><td><bdi>RET+</bdi></td><td>عودة الحلقة +</td></tr>
            <tr><td>4</td><td><bdi>RET−</bdi></td><td>عودة الحلقة −</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- J4 & J10 -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; margin-top: 16px;">
      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th colspan="3">الموصل <bdi>J4</bdi></th></tr><tr><th>الطرف</th><th>الاسم</th><th>الوظيفة</th></tr></thead>
          <tbody>
            <tr><td>1</td><td><bdi>485−</bdi></td><td>خط <bdi>RS-485</bdi> سالب</td></tr>
            <tr><td>2</td><td><bdi>485+</bdi></td><td>خط <bdi>RS-485</bdi> موجب</td></tr>
            <tr><td>3</td><td><bdi>GND</bdi></td><td>أرضي</td></tr>
            <tr><td>4</td><td><bdi>PSOUT</bdi></td><td>خرج تغذية مساعدة (<bdi>27Vdc @ 500mA</bdi>)</td></tr>
            <tr><td>5</td><td><bdi>SIR+</bdi></td><td>خرج مراقَب + (للأحمال/الصفارات)</td></tr>
            <tr><td>6</td><td><bdi>SIR−</bdi></td><td>خرج مراقَب − (للأحمال/الصفارات)</td></tr>
            <tr><td>7</td><td><bdi>AL</bdi></td><td>خرج عطل <bdi>NC</bdi> (مرحل)</td></tr>
            <tr><td>8</td><td><bdi>AL</bdi></td><td>خرج عطل <bdi>NC</bdi> (مرحل)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th colspan="3">الموصل <bdi>J10</bdi></th></tr><tr><th>الطرف</th><th>الاسم</th><th>الوظيفة</th></tr></thead>
          <tbody>
            <tr><td>1</td><td><bdi>IN1</bdi></td><td>إدخال رقمي 1</td></tr>
            <tr><td>2</td><td><bdi>IN2</bdi></td><td>إدخال رقمي 2</td></tr>
            <tr><td>3</td><td><bdi>OC</bdi></td><td>مجمّع مفتوح (<bdi>open collector</bdi>)</td></tr>
            <tr><td>4</td><td><bdi>GND</bdi></td><td>أرضي</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- 7.2 TD574/E Expansion Board -->
  <div class="doc-section" id="sec-7-2">
    <div class="section-header">
      <h3 class="section-title">7.2 مخطط اللوحة المنطقية <bdi>TD574/E</bdi> (بطاقة التوسعة <bdi>ONE2</bdi>)</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 21 - 26</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-7-2', '7.2 بطاقة التوسعة TD574/E')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>

    <p style="margin-bottom: 12px;">
      تسمح بطاقة التوسعة <bdi>ONE2</bdi> بإضافة حلقتين معنونتين إضافيتين إلى اللوحة. وفي التجهيز الأقصى يمكن إضافة حتى 4 بطاقات <bdi>ONE2</bdi>، بما يمنح حتى <strong>9 حلقات معنونة</strong> (حلقة باللوحة الأم + 8 حلقات ببطاقات التوسعة).
    </p>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig3}', 'الشكل 3: بطاقة التوسعة ONE2 / TD574/E ومواضع الموصلات')">
        <img src="{img_fig3}" alt="الشكل 3" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 3:</strong> بطاقة التوسعة <bdi>TD574/E / ONE2</bdi> مع مواضع الموصلات <bdi>J1, J2, J3, J7, J9, J11, J12, J14</bdi> و <bdi>Y1</bdi>. هذه التسميات فنية ولا تُترجم.
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">الموصلات المتوفرة على بطاقة التوسعة:</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>الموصل</th><th>الوظيفة والبيان</th></tr></thead>
        <tbody>
          <tr><td><bdi>J15 & J14</bdi></td><td>التوصيل باللوحة الرئيسية.</td></tr>
          <tr><td><bdi>J2 & J3</bdi></td><td>موصلات التوسعة <bdi>EXP</bdi> لربط البطاقات فوق بعضها.</td></tr>
          <tr><td><bdi>J7</bdi></td><td>المنفذ التسلسلي لترقية البرنامج الثابت <bdi>FW</bdi>.</td></tr>
          <tr><td><bdi>Y1</bdi></td><td>الخرجان المراقبان <bdi>OUT1</bdi> و <bdi>OUT2</bdi>.</td></tr>
          <tr><td><bdi>J9</bdi></td><td>التوصيل بالحلقة 1.</td></tr>
          <tr><td><bdi>J11</bdi></td><td>التوصيل بالحلقة 2.</td></tr>
          <tr><td><bdi>J12</bdi></td><td>ضبط المنفذ التسلسلي.</td></tr>
        </tbody>
      </table>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin: 16px 0;">
      <!-- Y1 -->
      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th colspan="3">الموصل <bdi>Y1</bdi></th></tr><tr><th>الطرف</th><th>الاسم</th><th>الوظيفة</th></tr></thead>
          <tbody>
            <tr><td>1</td><td><bdi>MON2+</bdi></td><td>خرج المراقبة 2 +</td></tr>
            <tr><td>2</td><td><bdi>MON2−</bdi></td><td>خرج المراقبة 2 −</td></tr>
            <tr><td>3</td><td><bdi>MON1+</bdi></td><td>خرج المراقبة 1 +</td></tr>
            <tr><td>4</td><td><bdi>MON1−</bdi></td><td>خرج المراقبة 1 −</td></tr>
          </tbody>
        </table>
      </div>

      <!-- J9 Loop 1 -->
      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th colspan="3">الموصل <bdi>J9</bdi> — الحلقة 1</th></tr><tr><th>الطرف</th><th>الاسم</th><th>الوظيفة</th></tr></thead>
          <tbody>
            <tr><td>1</td><td><bdi>SEND1+</bdi></td><td>إرسال الحلقة 1 +</td></tr>
            <tr><td>2</td><td><bdi>SEND1−</bdi></td><td>إرسال الحلقة 1 −</td></tr>
            <tr><td>3</td><td><bdi>RET1+</bdi></td><td>عودة الحلقة 1 +</td></tr>
            <tr><td>4</td><td><bdi>RET1−</bdi></td><td>عودة الحلقة 1 −</td></tr>
          </tbody>
        </table>
      </div>

      <!-- J11 Loop 2 -->
      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th colspan="3">الموصل <bdi>J11</bdi> — الحلقة 2</th></tr><tr><th>الطرف</th><th>الاسم</th><th>الوظيفة</th></tr></thead>
          <tbody>
            <tr><td>1</td><td><bdi>SEND2+</bdi></td><td>إرسال الحلقة 2 +</td></tr>
            <tr><td>2</td><td><bdi>SEND2−</bdi></td><td>إرسال الحلقة 2 −</td></tr>
            <tr><td>3</td><td><bdi>RET2+</bdi></td><td>عودة الحلقة 2 +</td></tr>
            <tr><td>4</td><td><bdi>RET2−</bdi></td><td>عودة الحلقة 2 −</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 20px 0 10px;">تركيب بطاقات التوسعة (ص 23 - 26):</h4>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px;">
      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig4}', 'الشكل 4: موضع بطاقة التوسعة الأولى EXP1 على اللوحة الرئيسية')">
          <img src="{img_fig4}" alt="الشكل 4" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 4:</strong> موضع بطاقة التوسعة الأولى <bdi>EXP1</bdi> على اللوحة الرئيسية، مع نقاط التثبيت والمسامير.
        </div>
      </div>

      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig5}', 'الشكل 5: تركيب البطاقة الثانية EXP2 فوق الأولى')">
          <img src="{img_fig5}" alt="الشكل 5" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 5:</strong> تركيب البطاقة الثانية <bdi>EXP2</bdi> فوق البطاقة الأولى، بحيث يدخل موصل <bdi>J3</bdi> في موصل <bdi>J2</bdi>.
        </div>
      </div>
    </div>

    <div class="callout callout-note">
      <div class="callout-title">قاعدة العنونة التلقائية للبطاقات (ص 26)</div>
      <div class="callout-content">
        تُعنون كل بطاقة تلقائياً بحسب موضع تركيبها، لذا من الضروري جداً الالتزام بترتيب البطاقات على النحو التالي:
      </div>
    </div>

    <ol class="step-list">
      <li class="step-item">أطفئ اللوحة، وافصل البطاريات، وأزل المصهر.</li>
      <li class="step-item">أزل واقيات الجوانب (الجانب الأيسر فقط إذا كانت تُركّب بطاقتان <bdi>ONE2</bdi> كحد أقصى).</li>
      <li class="step-item">أدخل 4 مسامير تثبيت <bdi>M/F</bdi> بطول <bdi>5mm</bdi>.</li>
      <li class="step-item">أدخل موصل <bdi>J15</bdi> في بطاقة التوسعة الأولى (<bdi>EXP1</bdi>) في موصل <bdi>J15</bdi> باللوحة الأم (<bdi>TD571/E</bdi>).</li>
      <li class="step-item">ثبّت بطاقة <bdi>EXP1</bdi> بثلاثة براغي <bdi>3×6mm</bdi> ومسمار تثبيت واحد <bdi>M/F</bdi> بطول <bdi>15mm</bdi>.</li>
      <li class="step-item">ركّب بطاقة التوسعة <bdi>EXP2</bdi> فوق بطاقة <bdi>EXP1</bdi>، بإدخال موصل <bdi>J3</bdi> في <bdi>EXP2</bdi> في موصل <bdi>J2</bdi> في <bdi>EXP1</bdi>.</li>
      <li class="step-item">ثبّت بطاقة <bdi>EXP2</bdi> بأربعة براغي <bdi>3×6mm</bdi>.</li>
      <li class="step-item">إذا لزم أكثر من بطاقتي توسعة، أدخل أربعة مسامير تثبيت <bdi>M/F</bdi> بطول <bdi>5mm</bdi>.</li>
      <li class="step-item">أدخل موصل <bdi>J14</bdi> في بطاقة التوسعة الثالثة (<bdi>EXP3</bdi>) في موصل <bdi>J14</bdi> باللوحة الأم (<bdi>TD571/E</bdi>).</li>
      <li class="step-item">ثبّت بطاقة <bdi>EXP3</bdi> ببرغيين <bdi>3×6mm</bdi> ومسماري تثبيت <bdi>M/F</bdi> بطول <bdi>15mm</bdi>.</li>
      <li class="step-item">ركّب بطاقة التوسعة <bdi>EXP4</bdi> فوق بطاقة <bdi>EXP3</bdi>، بإدخال موصل <bdi>J3</bdi> في <bdi>EXP4</bdi> في موصل <bdi>J2</bdi> في <bdi>EXP3</bdi>.</li>
      <li class="step-item">ثبّت بطاقة <bdi>EXP4</bdi> بأربعة براغي <bdi>3×6mm</bdi>.</li>
    </ol>
  </div>

  <!-- 7.3 ONECONNECT -->
  <div class="doc-section" id="sec-7-3">
    <div class="section-header">
      <h3 class="section-title">7.3 بطاقة <bdi>ONECONNECT</bdi> (اختيارية)</h3>
      <span class="section-page-tag">ص 26 - 27</span>
    </div>
    <p style="margin-bottom: 12px;">
      تُورّد بطاقة <bdi>ONECONNECT</bdi>، إن كانت ضمن التجهيز، مع كابل مسطح، ويجب توصيلها باللوحة الرئيسية عبر الموصل <bdi>J11</bdi> كما هو موضح أدناه:
    </p>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig6}', 'الشكل 6: مخطط توصيل بطاقة ONECONNECT باللوحة الأم')">
        <img src="{img_fig6}" alt="الشكل 6" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 6:</strong> مخطط توصيل الكابل المسطح بين بطاقة <bdi>ONECONNECT</bdi> والموصل <bdi>J11</bdi> باللوحة الأم. يوضح الشكل اتجاه الطرف رقم 1 وموضع موصل <bdi>RJ-45</bdi>.
      </div>
    </div>

    <ul style="margin-right: 22px; margin-bottom: 14px; line-height: 1.8;">
      <li>وصّل الكابل المسطح بموصل البطاقة الشبكية (7 أطراف) وبالموصل <bdi>J11</bdi> (6 أطراف) في اللوحة الرئيسية. <strong>اترك الطرف السابع حراً من جهة اللوحة</strong>، لأنه يقابل وظيفة <bdi>NC</bdi>.</li>
      <li>لتجنّب التلف، لا تُجبر الموصل على الدخول بالقوة.</li>
      <li>وصّل لوحة التحكم بالبطاقة الشبكية عبر موصل <bdi>RJ-45</bdi> في البطاقة باستخدام:
        <ul style="margin-right: 20px; margin-top: 4px;">
          <li>كابل شبكة متقاطع <bdi>10BASE-T</bdi>: للتوصيل بالحاسوب المضيف.</li>
          <li>كابل شبكة مباشر <bdi>10BASE-T</bdi>: للتوصيل بموزّع (<bdi>hub</bdi>).</li>
        </ul>
      </li>
    </ul>
  </div>

  <!-- 7.4 ONERING -->
  <div class="doc-section" id="sec-7-4">
    <div class="section-header">
      <h3 class="section-title">7.4 بطاقة <bdi>ONERING</bdi> (اختيارية)</h3>
      <span class="section-page-tag">ص 27 - 30</span>
    </div>
    <p style="margin-bottom: 12px;">
      تسمح بطاقة التوسعة <bdi>ONERING</bdi> بتوصيل حتى <strong>32 لوحة</strong> من طرازي <bdi>TeledataONE</bdi> و <bdi>Olympia</bdi>. والغرض من ذلك تبادل المعلومات بين اللوحات، مع إمكانية تنفيذ تفعيلات خرج متقاطعة.
    </p>
    <p style="margin-bottom: 12px;">
      تُورّد بطاقة <bdi>OLYNET</bdi> مع كابل مسطح، ويجب توصيلها باللوحة الرئيسية عبر الموصل <bdi>J7</bdi>.
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; margin-bottom: 16px;">
      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig7}', 'الشكل 7: توصيل الكابل المسطح بموصل J7 في اللوحة وموصلات Bus')">
          <img src="{img_fig7}" alt="الشكل 7" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 7:</strong> توصيل الكابل المسطح بموصل <bdi>J7</bdi> في اللوحة الرئيسية، وموصلات الناقل <bdi>Bus</bdi> في بطاقة <bdi>OLYNET</bdi>.
        </div>
      </div>

      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig8}', 'الشكل 8: تركيب بطاقة ONERING وتوصيل كابل البيانات')">
          <img src="{img_fig8}" alt="الشكل 8" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 8:</strong> تركيب بطاقة <bdi>ONERING</bdi> داخل اللوحة وتوصيل كابل البيانات والكابل المسطح.
        </div>
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin-bottom: 8px;">مواصفات كابلات شبكة <bdi>CAN bus</bdi>:</h4>
    <ul style="margin-right: 22px; margin-bottom: 12px; line-height: 1.8;">
      <li>استخدم كابل ناقل <bdi>CAN bus</bdi> بمقاومة مضمونة <bdi>120Ω</bdi> (مثل <bdi>Belden 9842</bdi>).</li>
      <li>أقصى مسافة عند سرعة <bdi>50 kbit/s</bdi> هي <strong>1000m</strong>.</li>
    </ul>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>نوع الكابل (المقطع)</th><th>أقصى طول مسموح</th></tr></thead>
        <tbody>
          <tr><td><bdi>0.25 – 0.34 mm²</bdi></td><td><bdi>Up to 40 m</bdi></td></tr>
          <tr><td><bdi>0.34 – 0.6 mm²</bdi></td><td><bdi>Up to 300 m</bdi></td></tr>
          <tr><td><bdi>0.5 – 0.6 mm²</bdi></td><td><bdi>Up to 600 m</bdi></td></tr>
          <tr><td><bdi>0.75 – 0.8 mm²</bdi></td><td><bdi>Up to 1000 m</bdi></td></tr>
        </tbody>
      </table>
    </div>
    <p style="font-size: 0.88rem; color: var(--text-secondary); margin-top: 6px;">
      أما مع كابل حريق مجدول ومحجوب <bdi>1mm²</bdi>، فالحد الأقصى للمسافة عند سرعة <bdi>50 Kbit/s</bdi> هو <strong>400m</strong>.
    </p>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">خطوات تركيب بطاقة <bdi>ONERING</bdi>:</h4>
    <ol class="step-list">
      <li class="step-item">أطفئ اللوحة، وافصل البطاريات، وأزل المصهر.</li>
      <li class="step-item">أدخل أربعة مسامير تثبيت <bdi>M/F</bdi> بطول <bdi>5mm</bdi>.</li>
      <li class="step-item">ركّب بطاقة <bdi>ONERING</bdi> وثبّتها بأربعة براغي <bdi>3×6mm</bdi>.</li>
      <li class="step-item">وصّل كابل البيانات المسطح بموصل <bdi>J7</bdi> في لوحة <bdi>TeledataONE</bdi>.</li>
      <li class="step-item">وصّل كابل التغذية بطرفي <bdi>PSOUT+</bdi> و <bdi>GND</bdi> في موصل <bdi>J4</bdi> بلوحة <bdi>TeledataONE</bdi>.</li>
      <li class="step-item">شغّل اللوحة، بتوصيل البطارية وإدخال المصهر.</li>
    </ol>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-top: 14px;">
      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th colspan="3">الموصل <bdi>J7</bdi> في بطاقة <bdi>OLYNET TD542/A</bdi></th></tr><tr><th>الطرف</th><th>الاسم</th><th>الوظيفة</th></tr></thead>
          <tbody>
            <tr><td>1</td><td><bdi>CH side a</bdi></td><td>ناقل H — الجانب A</td></tr>
            <tr><td>2</td><td><bdi>CL side a</bdi></td><td>ناقل L — الجانب A</td></tr>
            <tr><td>3</td><td><bdi>Gnd/bus</bdi></td><td>مرجع أرضي للناقل</td></tr>
            <tr><td>4</td><td><bdi>Gnd/bus</bdi></td><td>مرجع أرضي للناقل</td></tr>
            <tr><td>5</td><td><bdi>CL side b</bdi></td><td>ناقل L — الجانب B</td></tr>
            <tr><td>6</td><td><bdi>CH side b</bdi></td><td>ناقل H — الجانب B</td></tr>
          </tbody>
        </table>
      </div>

      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th colspan="3">الموصل <bdi>J2</bdi> في بطاقة <bdi>OLYNET TD542/A</bdi></th></tr><tr><th>الطرف</th><th>الاسم</th><th>الوظيفة</th></tr></thead>
          <tbody>
            <tr><td>1</td><td><bdi>12Vdc</bdi></td><td>تغذية +</td></tr>
            <tr><td>2</td><td><bdi>GND</bdi></td><td>تغذية −</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">قاعدة التوصيل الحلقي بين البطاقات:</h4>
    <ul style="margin-right: 22px; line-height: 1.8;">
      <li>الجانب <bdi>CH A</bdi> من <bdi>OLYNET 1</bdi> إلى الجانب <bdi>CH B</bdi> من <bdi>OLYNET 2</bdi>.</li>
      <li>الجانب <bdi>CH A</bdi> من <bdi>OLYNET 2</bdi> إلى الجانب <bdi>CH B</bdi> من <bdi>OLYNET 3</bdi>، وهكذا حتى تُغلق الحلقة بالعودة إلى <bdi>OLYNET 1</bdi>.</li>
      <li>الجانب <bdi>CL A</bdi> من <bdi>OLYNET 1</bdi> إلى الجانب <bdi>CL B</bdi> من <bdi>OLYNET 2</bdi>.</li>
      <li>الجانب <bdi>CL A</bdi> من <bdi>OLYNET 2</bdi> إلى الجانب <bdi>CL B</bdi> من <bdi>OLYNET 3</bdi>، وهكذا حتى تُغلق الحلقة بالعودة إلى <bdi>OLYNET 1</bdi>.</li>
      <li>وصّل أيضاً ناقل الأرضي (<bdi>GND</bdi>) بين كل بطاقتي <bdi>OLYNET</bdi> متتاليتين.</li>
    </ul>

    <div class="callout callout-suggestion">
      <div class="callout-title">مقاومة الأعطال والوضع المتدهور (ص 30)</div>
      <div class="callout-content">
        صُمّمت الشبكة الحلقية <bdi>ONERING</bdi> لضمان العمل حتى في حال قطع الناقل أو حدوث دائرة قصيرة. ويستطيع النظام الحفاظ على نقل البيانات بين اللوحات في وضع متدهور إذا انقطعت التغذية عن بطاقة أو أكثر من بطاقات <bdi>ONERING</bdi>. تحقّق من توصيلات الناقل قبل تشغيل النظام.
      </div>
    </div>
  </div>

  <!-- 7.5 Power & Batteries -->
  <div class="doc-section" id="sec-7-5">
    <div class="section-header">
      <h3 class="section-title">7.5 مصادر التغذية والبطاريات</h3>
      <span class="section-page-tag">ص 31 - 33</span>
    </div>
    <p style="margin-bottom: 12px;">
      يمكن داخل لوحة <bdi>Teledata One</bdi> تركيب حتى مصدري تغذية <bdi>ONEPW</bdi>، ويمكن أن تحتوي اللوحة بطاريتين سعة <bdi>7.2Ah</bdi> أو <bdi>17Ah</bdi>، بحسب بطاقات التوسعة المركّبة.
    </p>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_hw_table}', 'جدول توافق تجهيزات اللوحة والبطاقات ومصادر التغذية ص 32')">
        <img src="{img_hw_table}" alt="جدول التجهيزات ص 32" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>جدول تجهيزات اللوحة (ص 32):</strong> توزيع بطاقات التوسعة ONE2 و PT LAN و ONERING و ONE56 مع مصادر التغذية ONEPW وسعة البطاريات المطلوبة.
      </div>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; margin: 16px 0;">
      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig9}', 'الشكل 9: مواضع مصادر التغذية ONEPW والبطاريات داخل اللوحة')">
          <img src="{img_fig9}" alt="الشكل 9" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 9:</strong> مواضع مصادر التغذية <bdi>ONEPW</bdi> والبطاريات داخل اللوحة.
        </div>
      </div>

      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig10}', 'الشكل 10: توصيل البطاريتين على التوالي وتثبيتهما بأربطة نايلون')">
          <img src="{img_fig10}" alt="الشكل 10" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 10:</strong> توصيل البطاريتين على التوالي وتثبيتهما بأربطة نايلون.
        </div>
      </div>
    </div>

    <div class="callout callout-warning">
      <div class="callout-title">⚠️ توصيل البطاريات الإلزامي</div>
      <div class="callout-content">
        يجب توصيل البطاريات على التوالي (<bdi>in series</bdi>) وتثبيتها بأربطة النايلون الموردة مع الجهاز.
      </div>
    </div>
  </div>

  <!-- 7.6 System Description -->
  <div class="doc-section" id="sec-7-6">
    <div class="section-header">
      <h3 class="section-title">7.6 وصف النظام</h3>
      <span class="section-page-tag">ص 33 - 34</span>
    </div>

    <h4 style="color: var(--brand-blue); margin-bottom: 8px;">7.6.1 العلاقات بين عناصر المنظومة</h4>
    <p style="margin-bottom: 12px;">
      تُجمَّع الأجهزة (الكواشف ونقاط النداء وغيرها) في مناطق (<bdi>zones</bdi>)، وترتبط هذه المناطق فيما بينها بدوال منطقية محددة يمكنها تفعيل خرج واحد أو أكثر.
    </p>

    <!-- Visual schematic box -->
    <div style="background-color: var(--bg-tertiary); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 18px; margin: 14px 0; text-align: center;">
      <div style="display: flex; align-items: center; justify-content: center; gap: 14px; flex-wrap: wrap; font-size: 0.9rem; font-weight: 700;">
        <div style="background-color: var(--bg-card); padding: 10px 16px; border: 2px solid var(--brand-green); border-radius: 6px;">
          المنطقة Z1 ... Zn<br><small style="font-weight: normal; color: var(--text-muted);">كواشف ونقاط نداء</small>
        </div>
        <div style="font-size: 1.5rem; color: var(--text-muted);">➔</div>
        <div style="background-color: var(--bg-card); padding: 10px 16px; border: 2px solid var(--brand-amber); border-radius: 6px;">
          الدالة المنطقية<br><small style="font-weight: normal; color: var(--text-muted);"><bdi>... Z1 OR Z2</bdi></small>
        </div>
        <div style="font-size: 1.5rem; color: var(--text-muted);">➔</div>
        <div style="background-color: var(--bg-card); padding: 10px 16px; border: 2px solid var(--brand-blue); border-radius: 6px;">
          الخرج O1 ... On<br><small style="font-weight: normal; color: var(--text-muted);">وحدات خرج / صفارات / مرحلات</small>
        </div>
      </div>
    </div>

    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig11}', 'الشكل 11: أمثلة على أجهزة الحلقة: كواشف دخان ونقطة نداء يدوية')">
        <img src="{img_fig11}" alt="الشكل 11" class="figure-img" style="max-height: 220px;">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 11:</strong> أمثلة على أجهزة الحلقة: كواشف دخان ونقطة نداء يدوية. جميعها تُعنون وتُربط بالحلقة.
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">7.6.2 توصيل أجهزة الإنذار الصوتية والأحمال</h4>
    <p style="margin-bottom: 12px;">
      يُستخدم الطرفان 5 و6 في الموصل <bdi>J4</bdi> لتوصيل الأحمال (أجهزة الإنذار الصوتية والأجراس ولوحات الإنذار البصرية والصوتية) التي يلزم مراقبة قطعها ودائرتها القصيرة.
    </p>
    <p style="margin-bottom: 12px;">
      تستطيع لوحة التحكم كشف وجود قطع أو دائرة قصيرة في خط توصيل الأحمال. وفي حال حدوث أي من ذلك، تشير اللوحة إليه بإشارة بصرية (رسالة على الشاشة، وإضاءة مؤشر LED أصفر لعطل أجهزة الإنذار) أو بإشارة صوتية (الجرس).
    </p>

    <ul style="margin-right: 22px; line-height: 1.8;">
      <li>وصّل مقاومة نهاية الخط <bdi>3.3kΩ ¼ Watt</bdi> ودايود <bdi>1N4007</bdi>. وعادةً تُورّد هذه المقاومات والدايودات مع لوحة التحكم.</li>
      <li>وصّل الأحمال باللوحة باستخدام كابلات بمقاومة أقصاها <bdi>50Ω</bdi>. وأقصى تيار متاح هو <bdi>27Vdc @ 500mA</bdi>.</li>
      <li>لا يُفعَّل تشخيص هذه الخروجات إلا عندما يكون الحمل غير مفعّل، أي عندما لا تُبلّغ لوحة التحكم عن أي إنذار. وإذا استُخدم حمل مزوّد بدايود حماية داخلي، مثل لوحات الإنذار البصرية والصوتية المحمية من عكس القطبية، فيمكن الاستغناء عن دايود الحماية.</li>
    </ul>
  </div>

  <!-- 7.7 Communication with Detectors & Modules -->
  <div class="doc-section" id="sec-7-7">
    <div class="section-header">
      <h3 class="section-title">7.7 التواصل مع الكواشف والوحدات</h3>
      <div class="section-actions">
        <span class="section-page-tag">ص 34 - 41</span>
        <button class="icon-btn" onclick="toggleBookmark('sec-7-7', '7.7 التواصل مع الكواشف والوحدات')" title="حفظ إشارة مرجعية">🔖</button>
      </div>
    </div>
    <p style="margin-bottom: 12px;">
      تتواصل لوحة <bdi>TeledataONE</bdi> مع أجهزة الكشف والتحكم المعنونة عبر خط مكوّن من سلكين يُسمى <strong>الحلقة (<bdi>loop</bdi>)</strong>.
    </p>
    <p style="margin-bottom: 12px;">
      يمكن استخدام لوحة التحكم في أنظمة الحلقة المفتوحة أو أنظمة الحلقة المغلقة. ووفقاً للمعايير السارية، في الأنظمة التي تحتوي على أكثر من 32 وحدة أو كاشف، يجب استخدام تكوين الحلقة المغلقة.
    </p>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">7.7.1 تكوين الحلقة المفتوحة</h4>
    <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); text-align: center; margin: 12px 0;">
      <div style="font-family: var(--font-mono); font-weight: 700; color: #38bdf8;">
        لوحة [−J9 — FW+/FW] ➔ كاشف [+L1] ➔ وحدة [IN/OUT] ➔ كاشف [+L1] ➔ مقاومة نهاية الخط [3.3kΩ]
      </div>
      <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 6px;">مقاومة نهاية الخط تُركّب بعد آخر جهاز</div>
    </div>
    <p>
      يستخدم هذا التكوين الخطين <bdi>+L</bdi> و <bdi>−L</bdi> على الطرفين <bdi>+FW</bdi> و <bdi>−FW</bdi> في الموصل <bdi>J9</bdi>. ويمكن توصيل حتى <strong>32 كاشفاً ووحدة إدخال/إخراج</strong>.
    </p>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">7.7.2 متطلبات توصيل الحلقة العامة</h4>
    <ul style="margin-right: 22px; margin-bottom: 12px; line-height: 1.8;">
      <li>كابل مكوّن من موصلين مجدولين ومحجوبين.</li>
      <li>الحلقة تحتوي على كواشف ونقاط نداء ووحدات فقط، وألا يتجاوز الطول الإجمالي للخط:</li>
    </ul>

    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>نوع الكابل (المقطع)</th><th>أقصى طول مسموح</th></tr></thead>
        <tbody>
          <tr><td><bdi>2 × 0.5 mm²</bdi></td><td><bdi>Up to 1250 m</bdi></td></tr>
          <tr><td><bdi>2 × 0.75 mm²</bdi></td><td><bdi>Up to 1850 m</bdi></td></tr>
          <tr><td><bdi>2 × 1 mm²</bdi></td><td><bdi>Up to 2500 m</bdi></td></tr>
          <tr><td><bdi>2 × 1.5 mm²</bdi></td><td><bdi>Up to 3500 m</bdi></td></tr>
          <tr><td><bdi>2 × 2.5 mm²</bdi></td><td><bdi>Up to 5000 m</bdi></td></tr>
        </tbody>
      </table>
    </div>

    <ul style="margin-right: 22px; margin-top: 8px; line-height: 1.8;">
      <li>ألا تتجاوز مقاومة الخط <bdi>100Ω</bdi>.</li>
      <li>أن تُمد كابلات الخط في مسار مخصص.</li>
      <li>أن توضع الكابلات على مسافة مناسبة من خطوط الطاقة.</li>
    </ul>

    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">7.7.3 & 7.7.4 تكوين ومتطلبات الحلقة المفتوحة مع تفرعات T</h4>
    <p>
      يمثل كل تفرع T فرعاً إضافياً يتصل بالخط الرئيسي. ويجب احتساب طول جميع الفروع عند التحقق من الحد الأقصى للطول.
    </p>
    <ul style="margin-right: 22px; margin-top: 6px; line-height: 1.8;">
      <li>ألا يتجاوز الطول الإجمالي لجميع الفروع الحد الأقصى المسموح به، وفقاً لمقطع الكابل المستخدم.</li>
      <li>ألا تتجاوز المقاومة الإجمالية من موصلات لوحة التحكم إلى نهاية كل تفرع <bdi>100Ω</bdi>.</li>
    </ul>

    <h4 style="color: var(--brand-blue); margin: 20px 0 8px;">7.7.5 & 7.7.6 تكوين ومتطلبات الحلقة المغلقة</h4>
    <div style="background-color: var(--bg-tertiary); padding: 14px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); text-align: center; margin: 12px 0;">
      <div style="font-family: var(--font-mono); font-weight: 700; color: #38bdf8;">
        لوحة [FW / RET] ➔ كاشف [+L1] ➔ نقطة نداء [−L1] ➔ وحدة [OUT] ➔ وحدة [IN] ➔ كاشف [L1 RET] ➔ عودة RET إلى اللوحة
      </div>
      <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 6px;">تُغلق الحلقة بالعودة إلى اللوحة عبر خط RET في الموصل J9</div>
    </div>
    <p style="margin-bottom: 12px;">
      يستخدم هذا النوع من التكوين خطوط <bdi>−L</bdi> و <bdi>+L</bdi> في <bdi>FW</bdi>، وخطوط <bdi>−L</bdi> و <bdi>+L</bdi> في <bdi>RET</bdi> للموصل <bdi>J9</bdi>. ويمكن توصيل حتى <strong>240 كاشفاً ووحدة إدخال/إخراج</strong>.
    </p>

    <div class="callout callout-warning">
      <div class="callout-title">تنبيه عوازل الخط (ص 36)</div>
      <div class="callout-content">
        عند استخدام كواشف من نوع <bdi>SFx000E</bdi>، يجب تركيب وحدة عزل (<bdi>insulator</bdi>) أو كاشف/وحدة بعازل مدمج لكل <strong>32 جهازاً</strong>، وفقاً للمواصفات السارية.
      </div>
    </div>

    <!-- 7.7.7 Compatible Devices Tables -->
    <h4 style="color: var(--brand-blue); margin: 24px 0 10px;">7.7.7 الأجهزة القابلة للتوصيل بالحلقة</h4>
    
    <h5 style="color: var(--brand-amber); margin: 14px 0 6px;">1. أجهزة بروتوكول <bdi>ONE PROTOCOL</bdi> (ص 37):</h5>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>الجهاز</th><th>الوصف والبيان الفني</th></tr></thead>
        <tbody>
          <tr><td><bdi>ONEDETECTOR1</bdi></td><td>كاشف دخان بصري.</td></tr>
          <tr><td><bdi>ONEDETECTOR</bdi></td><td>كاشف بصري وحساس لمعدل ارتفاع الحرارة عند <bdi>58°C</bdi> (الفئة <bdi>A1</bdi> و <bdi>A1R</bdi>).</td></tr>
          <tr><td><bdi>ONEDETECTOR2</bdi></td><td>كاشف حرارة (الفئة <bdi>A1R</bdi> و <bdi>B</bdi>).</td></tr>
          <tr><td><bdi>ONECALLPOINT</bdi></td><td>نقطة نداء يدوية معنونة.</td></tr>
          <tr><td><bdi>ONEMODULE301</bdi></td><td>وحدة معنونة بثلاثة إدخالات وخرج واحد مراقب مع عازل دائرة قصيرة.</td></tr>
          <tr><td><bdi>ONEMODULE300</bdi></td><td>وحدة معنونة بثلاثة إدخالات مع عازل دائرة قصيرة.</td></tr>
          <tr><td><bdi>ONEMODULE111</bdi></td><td>وحدة معنونة بإدخال واحد وخرج واحد من النوع C وخرج مراقب واحد مع عازل دائرة قصيرة.</td></tr>
          <tr><td><bdi>ONEMODULE120</bdi></td><td>وحدة معنونة بإدخال واحد وخرجين من النوع C مع عازل دائرة قصيرة.</td></tr>
          <tr><td><bdi>ONEMICROM10</bdi></td><td>وحدة إدخال مصغّرة مع عازل دائرة قصيرة.</td></tr>
          <tr><td><bdi>ONEMICROM01</bdi></td><td>وحدة خرج مصغّرة مع عازل دائرة قصيرة.</td></tr>
          <tr><td><bdi>ONEMICROM11</bdi></td><td>وحدة إدخال وإخراج مصغّرة مع عازل دائرة قصيرة.</td></tr>
          <tr><td><bdi>SOUND100</bdi></td><td>جهاز إنذار صوتي معنون وفق <bdi>EN 54-3</bdi> مع عازل دائرة قصيرة.</td></tr>
          <tr><td><bdi>SOUND101</bdi></td><td>جهاز إنذار صوتي معنون وفق <bdi>EN 54-3</bdi> مع ضوء وامض وعازل دائرة قصيرة.</td></tr>
          <tr><td><bdi>SOUND110</bdi></td><td>جهاز إنذار صوتي معنون مع ضوء وامض وفق <bdi>EN 54-3</bdi> و <bdi>EN 54-23</bdi> وعازل دائرة قصيرة.</td></tr>
        </tbody>
      </table>
    </div>
    <p style="font-size: 0.88rem; color: var(--text-secondary); margin-top: 6px;">
      * يمكن عنونة جميع أجهزة <bdi>ONE PROTOCOL</bdi> المذكورة أعلاه باستخدام أداة البرمجة المخصصة <bdi>ONEPROGRAMMER</bdi>.
    </p>

    <h5 style="color: var(--brand-amber); margin: 20px 0 6px;">2. أجهزة بروتوكول <bdi>Argus</bdi> (ص 37 - 38):</h5>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>الجهاز</th><th>الوصف والبيان الفني</th></tr></thead>
        <tbody>
          <tr><td><bdi>SF5100 (40910-8)</bdi></td><td>كاشف دخان بصري.</td></tr>
          <tr><td><bdi>SF5200 (40920-8)</bdi></td><td>كاشف بصري وحساس لمعدل ارتفاع الحرارة عند <bdi>58°C</bdi> (الفئة A1 و A1R).</td></tr>
          <tr><td><bdi>SF5300 (40930-8)</bdi></td><td>كاشف حرارة (الفئة A1R و B).</td></tr>
          <tr><td><bdi>SF5100E (IV100)</bdi></td><td>مثل SF1000 لكن دون عازل.</td></tr>
          <tr><td><bdi>SF5200E (IV200)</bdi></td><td>مثل SF2000 لكن دون عازل.</td></tr>
          <tr><td><bdi>SF5300E (LV350)</bdi></td><td>مثل SF3500 لكن دون عازل.</td></tr>
          <tr><td><bdi>FDVCP500 (40800)</bdi></td><td>نقطة نداء.</td></tr>
          <tr><td><bdi>FDMM10 (40100-m)</bdi></td><td>وحدة إدخال مراقَبة.</td></tr>
          <tr><td><bdi>FDMM01S (40010-m)</bdi></td><td>وحدة خرج مراقَبة.</td></tr>
          <tr><td><bdi>FDMM02 (40002-m)</bdi></td><td>وحدة خرج من النوع C.</td></tr>
          <tr><td><bdi>FDS500 (40300)</bdi></td><td>جهاز إنذار صوتي معنون.</td></tr>
          <tr><td><bdi>FDW2W</bdi></td><td>جهاز إرسال/استقبال للأجهزة اللاسلكية.</td></tr>
          <tr><td><bdi>FDMM12 (40102-m)</bdi></td><td>وحدة إدخال/إخراج.</td></tr>
          <tr><td><bdi>FDMM11S (40110-m)</bdi></td><td>وحدة إدخال/إخراج مراقَبة.</td></tr>
          <tr><td><bdi>FDXMM11S (40110)</bdi></td><td>وحدة إدخال/إخراج مراقَبة.</td></tr>
          <tr><td><bdi>FDMC404 (40110)</bdi></td><td>وحدة بأربعة إدخالات وأربعة خروجات.</td></tr>
          <tr><td><bdi>FDMC602 (40602)</bdi></td><td>وحدة بستة إدخالات وخرجين.</td></tr>
          <tr><td><bdi>FDVCP500IP67 (40801)</bdi></td><td>نقطة نداء قابلة لإعادة الضبط بعد الإنذار.</td></tr>
          <tr><td><bdi>FDCWS100AV</bdi></td><td>جهاز إنذار صوتي إلكتروني معنون مع ضوء وامض.</td></tr>
          <tr><td><bdi>FDVFI100 (40330)</bdi></td><td>ضوء وامض LED معنون.</td></tr>
          <tr><td><bdi>FDVMCZ500 (40500)</bdi></td><td>مؤشر عن بُعد معنون.</td></tr>
          <tr><td><bdi>FDVBLS100/32</bdi></td><td>جهاز إنذار صوتي بـ 32 نغمة.</td></tr>
        </tbody>
      </table>
    </div>
    <p style="font-size: 0.88rem; color: var(--text-secondary); margin-top: 6px;">
      * يمكن عنونة جميع أجهزة Argus المذكورة أعلاه باستخدام أداة البرمجة المخصصة <bdi>FDVPU1000</bdi>.
    </p>

    <h5 style="color: var(--brand-amber); margin: 20px 0 6px;">الأجهزة اللاسلكية المدارة عبر <bdi>FDW2W</bdi> (ص 38 - 39):</h5>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>الجهاز</th><th>الوصف والبيان</th></tr></thead>
        <tbody>
          <tr><td><bdi>SWF1000</bdi></td><td>كاشف دخان بصري لاسلكي.</td></tr>
          <tr><td><bdi>SWF2000</bdi></td><td>كاشف بصري وحساس لمعدل ارتفاع الحرارة عند <bdi>58°C</bdi> (الفئة A1 و A1R).</td></tr>
          <tr><td><bdi>SWF3500</bdi></td><td>كاشف حرارة (الفئة A1R و B).</td></tr>
          <tr><td><bdi>FDWVMI100</bdi></td><td>وحدة إدخال مراقَبة.</td></tr>
          <tr><td><bdi>FDWVMI120</bdi></td><td>وحدة خرج.</td></tr>
          <tr><td><bdi>FDWMCB100</bdi></td><td>وحدة خرج تعمل بالبطارية.</td></tr>
          <tr><td><bdi>FDSGLSP100</bdi></td><td>جهاز إنذار صوتي معنون.</td></tr>
          <tr><td><bdi>FDWCP100</bdi></td><td>نقطة نداء.</td></tr>
        </tbody>
      </table>
    </div>

    <h5 style="color: var(--brand-amber); margin: 20px 0 6px;">3. أجهزة بروتوكول <bdi>Apollo</bdi> (ص 39 - 41):</h5>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>رمز Apollo</th><th>البروتوكول</th><th>وصف الجهاز</th></tr></thead>
        <tbody>
          <!-- IN/OUT -->
          <tr><th colspan="3" style="background-color: var(--bg-tertiary); color: var(--brand-blue);">وحدات الإدخال/الإخراج IN/OUT modules</th></tr>
          <tr><td><bdi>55000-841</bdi></td><td><bdi>XP95</bdi></td><td>وحدة إدخال plus IN مع عازل ضوئي للإدخال.</td></tr>
          <tr><td><bdi>55000-843</bdi></td><td><bdi>XP95</bdi></td><td>وحدة إدخال IN Module.</td></tr>
          <tr><td><bdi>55000-847</bdi></td><td><bdi>XP95</bdi></td><td>وحدة إدخال/إخراج IN/OUT Module.</td></tr>
          <tr><td><bdi>55000-849</bdi></td><td><bdi>XP95</bdi></td><td>وحدة خرج من النوع C.</td></tr>
          <tr><td><bdi>55000-852</bdi></td><td><bdi>XP95</bdi></td><td>وحدة خرج مراقَبة.</td></tr>
          <tr><td><bdi>55000-845</bdi></td><td><bdi>XP95</bdi></td><td>مراقب منطقة مغذّى من الحلقة.</td></tr>
          <tr><td><bdi>55000-875</bdi></td><td><bdi>XP95</bdi></td><td>وحدة خرج من النوع C.</td></tr>
          <tr><td><bdi>55000-760</bdi></td><td><bdi>XP95</bdi></td><td>مفتاح مراقبة مصغّر Mini Switch Monitor.</td></tr>
          <tr><td><bdi>55000-589</bdi></td><td><bdi>XP95</bdi></td><td>وحدة إدخال/إخراج 3+3 دون عازل.</td></tr>
          <tr><td><bdi>55000-588</bdi></td><td><bdi>XP95</bdi></td><td>وحدة إدخال/إخراج 3+3 مع عازل.</td></tr>
          <tr><td><bdi>55000-864</bdi></td><td><bdi>XP95</bdi></td><td>مراقب منطقة، التغذية من الحلقة.</td></tr>
          <!-- Detectors -->
          <tr><th colspan="3" style="background-color: var(--bg-tertiary); color: var(--brand-blue);">الكواشف Detector</th></tr>
          <tr><td><bdi>58000-600</bdi></td><td><bdi>Discovery</bdi></td><td>كاشف بصري Discovery.</td></tr>
          <tr><td><bdi>58000-700</bdi></td><td><bdi>Discovery</bdi></td><td>كاشف متعدد المعايير Multi Discovery.</td></tr>
          <tr><td><bdi>58000-400</bdi></td><td><bdi>Discovery</bdi></td><td>كاشف حرارة Discovery.</td></tr>
          <tr><td><bdi>58000-500</bdi></td><td><bdi>Discovery</bdi></td><td>كاشف أيوني Ion.</td></tr>
          <tr><td><bdi>55000-600</bdi></td><td><bdi>XP95</bdi></td><td>كاشف بصري XP95.</td></tr>
          <tr><td><bdi>55000-885</bdi></td><td><bdi>XP95</bdi></td><td>كاشف متعدد المعايير Multi XP95.</td></tr>
          <tr><td><bdi>55000-400</bdi></td><td><bdi>XP95</bdi></td><td>كاشف حرارة XP95 عند 55°.</td></tr>
          <tr><td><bdi>55000-401</bdi></td><td><bdi>XP95</bdi></td><td>كاشف حرارة XP95 عند 90°.</td></tr>
          <tr><td><bdi>55000-500</bdi></td><td><bdi>XP95</bdi></td><td>كاشف أيوني Ion.</td></tr>
          <!-- Call Points -->
          <tr><th colspan="3" style="background-color: var(--bg-tertiary); color: var(--brand-blue);">نقاط النداء PULSANTI</th></tr>
          <tr><td><bdi>55200-905</bdi></td><td><bdi>XP95</bdi></td><td>نقطة نداء XP95.</td></tr>
          <tr><td><bdi>58200-910</bdi></td><td><bdi>Discovery</bdi></td><td>نقطة نداء Discovery.</td></tr>
          <tr><td><bdi>SA5900-908</bdi></td><td><bdi>XP/Dis/Core</bdi></td><td>نقطة نداء.</td></tr>
          <!-- Bases -->
          <tr><th colspan="3" style="background-color: var(--bg-tertiary); color: var(--brand-blue);">القواعد Bases</th></tr>
          <tr><td><bdi>45681-210</bdi></td><td><bdi>NA</bdi></td><td>قاعدة معنونة عادية.</td></tr>
          <tr><td><bdi>45681-284</bdi></td><td><bdi>NA</bdi></td><td>قاعدة مع عازل.</td></tr>
          <!-- Audiovisual -->
          <tr><th colspan="3" style="background-color: var(--bg-tertiary); color: var(--brand-blue);">الأجهزة السمعية والبصرية Discovery Audiovisual</th></tr>
          <tr><td><bdi>58000-005</bdi></td><td><bdi>Discovery</bdi></td><td>جهاز إنذار صوتي وضوئي.</td></tr>
          <tr><td><bdi>45681-393</bdi></td><td><bdi>Discovery</bdi></td><td>قاعدة جهاز إنذار صوتي مع ضوء.</td></tr>
          <tr><td><bdi>58000-010</bdi></td><td><bdi>Discovery</bdi></td><td>إنذار صوتي بالكلام (Voice alarm).</td></tr>
          <tr><td><bdi>45681-702</bdi></td><td><bdi>Discovery</bdi></td><td>جهاز إنذار صوتي بقاعدة.</td></tr>
          <tr><td><bdi>55000-001 → 012</bdi></td><td><bdi>XP95</bdi></td><td>جهاز إنذار للمساحات المفتوحة.</td></tr>
          <tr><td><bdi>58000-700</bdi></td><td><bdi>XP95</bdi></td><td>جهاز إنذار صوتي بقاعدة XP95 / Discovery.</td></tr>
          <tr><td><bdi>45681-277</bdi></td><td><bdi>XP95</bdi></td><td>جهاز إنذار صوتي مدمج بقاعدة XP95 / Discovery.</td></tr>
          <tr><td><bdi>55000-877</bdi></td><td><bdi>XP95</bdi></td><td>ضوء وامض مغذّى من الحلقة.</td></tr>
          <tr><td><bdi>45681-276</bdi></td><td><bdi>NA</bdi></td><td>جهاز إنذار صوتي بقاعدة مساعدة.</td></tr>
          <!-- Soteria -->
          <tr><th colspan="3" style="background-color: var(--bg-tertiary); color: var(--brand-blue);">كواشف Soteria</th></tr>
          <tr><td><bdi>SA5100-400</bdi></td><td><bdi>Coreprotocol</bdi></td><td>كاشف حرارة.</td></tr>
          <tr><td><bdi>SA5100-600</bdi></td><td><bdi>Coreprotocol</bdi></td><td>كاشف بصري.</td></tr>
          <tr><td><bdi>SA5100-700</bdi></td><td><bdi>Coreprotocol</bdi></td><td>كاشف متعدد المعايير.</td></tr>
          <tr><td><bdi>SA5900-908</bdi></td><td><bdi>Coreprotocol MCP</bdi></td><td>نقطة نداء يدوية.</td></tr>
          <!-- Wireless XPander -->
          <tr><th colspan="3" style="background-color: var(--bg-tertiary); color: var(--brand-blue);">لاسلكي XP95 (XPander)</th></tr>
          <tr><td><bdi>XPA-CB-12034-APO</bdi></td><td><bdi>XP95</bdi></td><td>كاشف دخان بصري XPander.</td></tr>
          <tr><td><bdi>XPA_CB-13032-APO</bdi></td><td><bdi>XP95</bdi></td><td>كاشف متعدد المستشعرات XPander.</td></tr>
          <tr><td><bdi>XPA-CB-11170-APO / 11171</bdi></td><td><bdi>XP95</bdi></td><td>كاشف حرارة XPander بمعدل الارتفاع (A1R) والثابت (CS).</td></tr>
          <tr><td><bdi>XPA-CB-14001-APO / 14002</bdi></td><td><bdi>XP95</bdi></td><td>جهاز إنذار صوتي XPander (أحمر وأبيض).</td></tr>
          <tr><td><bdi>XPA-CB-14003 / 04 / 05</bdi></td><td><bdi>XP95</bdi></td><td>جهاز إنذار صوتي مع مؤشر بصري XPander بألوان وطرازات متعددة.</td></tr>
          <tr><td><bdi>XPA-MC-14006-APO</bdi></td><td><bdi>XP95</bdi></td><td>نقطة نداء يدوية XPander.</td></tr>
          <tr><td><bdi>XPA-IN-14011-APO</bdi></td><td><bdi>XP95</bdi></td><td>وحدة إدخال/إخراج فردية XPander.</td></tr>
          <tr><td><bdi>XPA-IN-14012-APO</bdi></td><td><bdi>XP95</bdi></td><td>وحدة إدخال/إخراج مزدوجة XPander.</td></tr>
          <tr><td><bdi>XPA-IN-14050-APO</bdi></td><td><bdi>XP95</bdi></td><td>وحدة واجهة حلقة متنوعة XPander.</td></tr>
          <!-- Special Detectors -->
          <tr><th colspan="3" style="background-color: var(--bg-tertiary); color: var(--brand-blue);">كواشف خاصة IS / Flame / Beam</th></tr>
          <tr><td><bdi>55000-540</bdi></td><td><bdi>XP95</bdi></td><td>كاشف أيوني IS.</td></tr>
          <tr><td><bdi>55000-640</bdi></td><td><bdi>XP95</bdi></td><td>كاشف بصري IS.</td></tr>
          <tr><td><bdi>55000-440</bdi></td><td><bdi>XP95</bdi></td><td>كاشف حرارة IS.</td></tr>
          <tr><td><bdi>55200-940</bdi></td><td><bdi>XP95</bdi></td><td>نقطة نداء يدوية IS MCP.</td></tr>
          <tr><td>—</td><td><bdi>XP95</bdi></td><td>جميع كواشف اللهب (Flame detectors).</td></tr>
          <tr><td><bdi>55000-268/274</bdi></td><td><bdi>XP95</bdi></td><td>كواشف الشعاع (Beam detectors).</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- 7.8 Host PC Connection -->
  <div class="doc-section" id="sec-7-8">
    <div class="section-header">
      <h3 class="section-title">7.8 التوصيل بالحاسوب المضيف والشبكة</h3>
      <span class="section-page-tag">ص 41 - 42</span>
    </div>
    <p style="margin-bottom: 12px;">
      يمكن توصيل لوحة التحكم بحاسوب مضيف عبر اتصال <bdi>Point2Point</bdi>، أو عبر الشبكة باستخدام واجهة <bdi>LAN</bdi> مناسبة.
    </p>

    <h4 style="color: var(--brand-blue); margin-bottom: 8px;">7.8.1 توصيل <bdi>Point2Point</bdi> (ص 41)</h4>
    <p>
      يمكن تنفيذ هذا النوع من التكوين عبر المنفذ التسلسلي الذي يربط الحاسوب المضيف مباشرة بلوحة التحكم عبر الموصل <bdi>P1</bdi>.
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 12px 0;">
      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th colspan="3">التوصيل للوحات <bdi>TD571D</bdi> والإصدارات السابقة</th></tr><tr><th>جهة اللوحة</th><th>التوصيل</th><th>جهة الحاسوب</th></tr></thead>
          <tbody>
            <tr><td><bdi>7 Jumpered with 8</bdi></td><td>—</td><td><bdi>7 Jumpered with 8</bdi></td></tr>
            <tr><td>4</td><td>يتصل بـ</td><td>2</td></tr>
            <tr><td>3</td><td>يتصل بـ</td><td>3</td></tr>
            <tr><td>1</td><td>يتصل بـ</td><td>5</td></tr>
          </tbody>
        </table>
      </div>

      <div class="table-responsive">
        <table class="doc-table">
          <thead><tr><th colspan="3">التوصيل للوحات <bdi>TD571E</bdi></th></tr><tr><th>جهة اللوحة</th><th>التوصيل</th><th>جهة الحاسوب</th></tr></thead>
          <tbody>
            <tr><td><bdi>7 Jumpered with 8</bdi></td><td>—</td><td><bdi>7 Jumpered with 8</bdi></td></tr>
            <tr><td>2</td><td>يتصل بـ</td><td>2</td></tr>
            <tr><td>3</td><td>يتصل بـ</td><td>3</td></tr>
            <tr><td>5</td><td>يتصل بـ</td><td>5</td></tr>
          </tbody>
        </table>
      </div>
    </div>
    <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 14px;">
      يمكن استخدام هذا الاتصال للتوصيل نقطة بنقطة مع برنامج المضيف من أجل تنزيل إصدار جديد من البرنامج الثابت.
    </p>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">7.8.2 توصيل <bdi>LAN</bdi> أو <bdi>WAN</bdi> (ص 42)</h4>
    <div class="figure-card">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig12}', 'الشكل 12: مخطط اتصال لوحة التحكم عبر LAN أو WAN إلى حاسوب الإشراف المركزي')">
        <img src="{img_fig12}" alt="الشكل 12" class="figure-img">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 12:</strong> مخطط اتصال لوحة التحكم عبر <bdi>LAN</bdi> أو <bdi>WAN</bdi> إلى حاسوب الإشراف المركزي.
      </div>
    </div>

    <h4 style="color: var(--brand-blue); margin: 18px 0 8px;">7.8.3 الشبكة الحلقية للوحات <bdi>Teledata One</bdi></h4>
    <p style="margin-bottom: 12px;">
      يمكن ربط أكثر من لوحة <bdi>Teledata One</bdi> في شبكة حلقية على ناقل مخصص، وذلك بتركيب بطاقة الشبكة الاختيارية <bdi>OLYNET</bdi>. ويمكن في هذه الشبكة تبادل الأحداث والإنذارات حتى <strong>32 لوحة</strong>.
    </p>
  </div>

  <!-- 7.9 Power Supply -->
  <div class="doc-section" id="sec-7-9">
    <div class="section-header">
      <h3 class="section-title">7.9 مصدر التغذية والمواصفات الكهربائية</h3>
      <span class="section-page-tag">ص 43</span>
    </div>

    <h4 style="color: var(--brand-blue); margin-bottom: 8px;">7.9.1 خصائص دخل الشبكة</h4>
    <p style="margin-bottom: 10px;">
      يجب تركيب لوحة التحكم وفق معايير التركيب الوطنية. ويُشترط تنفيذ توصيل بخط تيار متردد منفصل يُعلَّم بلافتة <bdi>FIRE SYSTEM</bdi>.
    </p>
    <ul style="margin-right: 22px; margin-bottom: 12px; line-height: 1.8;">
      <li>استخدم مفتاحاً ثنائي القطب بسعة <bdi>6A</bdi> كحد أدنى.</li>
      <li>يجب أن تكون أسلاك التوصيل ذات مقطع مناسب وعزل لا يقل عن <bdi>600V</bdi>.</li>
      <li>جهد التغذية: <bdi>230 Vac ± 10%</bdi>.</li>
      <li>التردد: <bdi>50/60 Hz</bdi>.</li>
    </ul>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">7.9.2 خصائص التأريض</h4>
    <p style="margin-bottom: 12px;">
      يجب تنفيذ التأريض وفقاً لمعايير <bdi>CEI</bdi> و <bdi>ISPESL</bdi>، وبمقاومة <strong>أقل من 10Ω</strong>.
    </p>

    <h4 style="color: var(--brand-blue); margin: 16px 0 8px;">7.9.3 خصائص تغذية اللوحة والبطاريات</h4>
    <div class="table-responsive">
      <table class="doc-table">
        <thead><tr><th>المعيار الكهربائي</th><th>القيمة المحددة في الدليل</th></tr></thead>
        <tbody>
          <tr><td>جهد تشغيل الخرج</td><td><bdi>27.6 V — بحد أقصى 500mA</bdi></td></tr>
          <tr><td>جهد شاحن البطارية</td><td><bdi>27.6 V — بحد أقصى 900mA</bdi></td></tr>
          <tr><td>حد البطارية المنخفض</td><td><bdi>21.6 V</bdi></td></tr>
          <tr><td>حد تحرير البطارية</td><td><bdi>20.4 V</bdi></td></tr>
          <tr><td>أقصى مقاومة داخلية للبطارية (مع الوصلات)</td><td><bdi>800 mΩ</bdi></td></tr>
        </tbody>
      </table>
    </div>

    <div class="callout callout-warning">
      <div class="callout-title">عمل دائرة شاحن البطارية وتنبيهات الأعطال:</div>
      <div class="callout-content">
        <ul style="margin-right: 20px; line-height: 1.7;">
          <li>في حال انقطاع التغذية، تُغذَّى لوحة التحكم من بطاريات الاحتياط، وينطفئ المؤشر الأخضر <bdi>LED</bdi>.</li>
          <li>إذا انخفض جهد البطارية عن حد البطارية المنخفض (<bdi>21.6V</bdi>)، تُفعَّل إشارة صوتية (الجرس) وإشارة بصرية (رسالة على الشاشة). وفي هذه الحالة، ولإعادة تشغيل لوحة التحكم، يجب إعادة تغذية الشبكة.</li>
          <li>إذا لم تكن هناك بطارية مركّبة، فعند أول فحص دوري للبطارية تجريه اللوحة، تُفعَّل إشارة صوتية وبصرية للإشارة إلى غياب البطاريات.</li>
          <li>إذا كانت المقاومة الداخلية للبطارية (بما فيها مقاومة التلامسات والكابلات) أعلى من <bdi>800 mΩ</bdi>، تُصدر اللوحة إنذاراً صوتياً (الجرس) وبصرياً (رسالة على الشاشة).</li>
          <li>خرج الجهد <bdi>+24V</bdi> للأحمال الخارجية محمي ضد الدوائر القصيرة. وفي حال حدوث دائرة قصيرة، تُفعَّل إشارة صوتية (الجرس) وبصرية (رسالة على الشاشة).</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- 7.10 Internal Wiring -->
  <div class="doc-section" id="sec-7-10">
    <div class="section-header">
      <h3 class="section-title">7.10 التمديدات الداخلية للوحة</h3>
      <span class="section-page-tag">ص 44 - 45</span>
    </div>
    <p style="margin-bottom: 12px;">
      يجب تنفيذ التمديدات الداخلية للوحة بطريقة تسهّل الوصول إليها في حال أعمال الصيانة المستقبلية. ويمكن للكابلات الدخول إلى وحدة اللوحة عبر الفتحات الموجودة في الجزء العلوي من الصندوق وفي ظهره. ويجب استخدام مخرج كابل بقطر <bdi>22mm</bdi>.
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; margin: 16px 0;">
      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig13}', 'الشكل 13: مواضع فتحات مرور الكابلات في صندوق اللوحة')">
          <img src="{img_fig13}" alt="الشكل 13" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 13:</strong> مواضع فتحات مرور الكابلات في صندوق اللوحة (أبعاد <bdi>392mm, 400mm, Ø22mm</bdi>).
        </div>
      </div>

      <div class="figure-card">
        <div class="figure-img-wrapper" onclick="openLightbox('{img_fig14}', 'الشكل 14: مثال على التمديدات الداخلية وتأريض الحجب')">
          <img src="{img_fig14}" alt="الشكل 14" class="figure-img">
          <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
        </div>
        <div class="figure-caption">
          <strong>الشكل 14:</strong> مثال على التمديدات الداخلية للوحة وربط حجب الكابلات بالأرضي.
        </div>
      </div>
    </div>

    <div class="callout callout-warning">
      <div class="callout-title">قاعدة توصيل حجب الكابلات (Cable shields)</div>
      <div class="callout-content">
        من المهم توصيل حجب الكابلات (<bdi>cable shields</bdi>) بطرف أرضي في هيكل اللوحة. <strong>وفي الحلقات المغلقة، وصّل جانباً واحداً فقط من الحجب واترك الجانب الآخر غير موصول</strong> (لتفادي حدوث حلقات أرضية Ground loops).
      </div>
    </div>

    <div class="figure-card" style="margin-top: 18px;">
      <div class="figure-img-wrapper" onclick="openLightbox('{img_fig15}', 'الشكل 15: مثال على تمديدات لوحة مكتملة التجهيز')">
        <img src="{img_fig15}" alt="الشكل 15" class="figure-img" style="max-height: 480px;">
        <div class="zoom-hint">🔍 انقر للتكبير والتنقل</div>
      </div>
      <div class="figure-caption">
        <strong>الشكل 15:</strong> مثال على تمديدات لوحة مكتملة التجهيز مع بطاقات التوسعة ONE2 والبطاريات والتوصيلات المكتملة.
      </div>
    </div>
  </div>
</div>
"""
