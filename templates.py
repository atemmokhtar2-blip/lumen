from html import escape


def get_awareness_template(app_name: str) -> str:
    title = escape(app_name)
    return f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="description" content="صفحة توعوية لاختبار وعي المستخدم بالتصيد وسلامة الأذونات">
  <title>{title}</title>
  <style>
    :root {{ color-scheme: dark; font-family: system-ui, sans-serif; }}
    body {{ margin: 0; min-height: 100vh; background: #07111f; color: #e5eef8; display: grid; place-items: center; }}
    main {{ width: min(720px, 92vw); padding: 2rem; background: #0e2035; border: 1px solid #234361; border-radius: 18px; box-shadow: 0 18px 60px #0008; }}
    h1 {{ color: #7dd3fc; margin-top: 0; }}
    li {{ margin: .8rem 0; line-height: 1.7; }}
    .safe {{ padding: 1rem; border-right: 4px solid #34d399; background: #052e2b; border-radius: 8px; }}
    code {{ color: #bae6fd; }}
  </style>
</head>
<body>
<main>
  <h1>{title}</h1>
  <p>هذه صفحة توعوية دفاعية. لا تجمع أي بيانات ولا تطلب الوصول إلى الكاميرا أو الميكروفون أو الموقع أو الشاشة.</p>
  <div class="safe"><strong>الوضع الآمن مفعّل:</strong> لا توجد قناة تحكم عن بُعد أو نقطة رفع بيانات.</div>
  <h2>قواعد التحقق</h2>
  <ul>
    <li>لا تمنح أذونات حساسة لصفحة لا تتوقعها أو لا تثق بمصدرها.</li>
    <li>تحقق من النطاق، واتصال HTTPS، وسبب طلب الإذن قبل الموافقة.</li>
    <li>استخدم خصائص <code>HttpOnly</code> و<code>Secure</code> و<code>SameSite</code> للكوكيز الحساسة.</li>
    <li>أوقف أي طلب غير متوقع للكاميرا أو الميكروفون أو مشاركة الشاشة، وراجعه مع مسؤول الأمن.</li>
  </ul>
</main>
</body>
</html>"""
