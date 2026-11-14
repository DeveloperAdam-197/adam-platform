# -*- coding: utf-8 -*-
"""
منهج البرمجة والذكاء الاصطناعي - الصف الثاني الثانوي (مصر)
الجزء الأول: المحاكاة البرمجية ومعالجة البيانات والذكاء الاصطناعي
Backend Logic & Simulations in Python
"""

import json
import math
from typing import Dict, List, Any

# ============================================================
# 1. محاكاة الحوسبة الطرفية مقابل السحابية (Edge vs Cloud Computing)
# ============================================================
def simulate_vehicle_reaction(obstacle_distance_m: float, connection_type: str = "edge") -> Dict[str, Any]:
    """
    محاكاة اتخاذ قرار التوقف في سيارة ذاتية القيادة
    المدخلات: المسافة حتى المشاة، نوع الحوسبة (طرفية أو سحابية)
    """
    speed_kmh = 60.0
    speed_ms = speed_kmh / 3.6  # 16.67 m/s
    
    if connection_type.lower() == "edge":
        latency_seconds = 0.002  # 2ms معالجة محلية
        processing_location = "حوسبة طرفية (على متن المركبة)"
    else:
        # تأخير نقل البيانات عبر شبكة الجوال + معالجة السحابة + إرجاع الرد
        latency_seconds = 0.280  # 280ms تأخير سحابي
        processing_location = "حوسبة سحابية مركزية (Cloud Data Center)"
        
    distance_traveled_during_decision = speed_ms * latency_seconds
    braking_distance = (speed_ms ** 2) / (2 * 9.8 * 0.7)  # معامل احتكاك الطريق
    total_stopping_distance = distance_traveled_during_decision + braking_distance
    
    safe_stop = total_stopping_distance < obstacle_distance_m
    margin = obstacle_distance_m - total_stopping_distance
    
    return {
        "connection_type": connection_type,
        "processing_location": processing_location,
        "latency_ms": round(latency_seconds * 1000, 1),
        "distance_traveled_before_brake_m": round(distance_traveled_during_decision, 2),
        "total_stopping_distance_m": round(total_stopping_distance, 2),
        "safe_stop": safe_stop,
        "result_message": "تم التوقف بأمان قبل المشاة!" if safe_stop else "تحذير: اصطدام محتمل بسبب تأخير الشبكة!"
    }


# ============================================================
# 2. محاكاة تقدير المخاطر السيبرانية (Cyber Risk Calculator)
# ============================================================
def calculate_cyber_risk(impact_score: int, probability_score: int) -> Dict[str, Any]:
    """
    معادلة المخاطر: درجة الخطر = التأثير × الاحتمالية
    المقاييس من 1 إلى 5
    """
    risk_score = impact_score * probability_score
    
    if risk_score <= 5:
        level = "منخفض (Low)"
        action = "مخاطرة مقبولة - مراجعة دورية سنوية."
        color = "#10B981"
    elif risk_score <= 12:
        level = "متوسط (Medium)"
        action = "مطلوب خطة معالجة وتدابير وقائية خلال 30 يوماً."
        color = "#F59E0B"
    elif risk_score <= 19:
        level = "مرتفع (High)"
        action = "إجراءات عاجلة لعزل المخاطر وتطبيق ضوابط فورية."
        color = "#EF4444"
    else:
        level = "حرج جداً (Critical)"
        action = "إيقاف العمليات المعرضة وتدخل فريق الطوارئ فوراً!"
        color = "#DC2626"
        
    return {
        "impact": impact_score,
        "probability": probability_score,
        "risk_score": risk_score,
        "max_possible_score": 25,
        "level": level,
        "recommended_action": action,
        "indicator_color": color
    }


# ============================================================
# 3. معالجة بيانات استجابة الـ API واستخراج معلومات الطقس (JSON Processing)
# ============================================================
MOCK_API_DATABASE = {
    "/api/weather/cairo": {
        "status": 200,
        "city": "القاهرة",
        "temperature_c": 31,
        "humidity_pct": 45,
        "condition": "مشمس ☀️",
        "wind_speed_kmh": 14,
        "aqi_index": "جيد (Good)",
        "cached": True
    },
    "/api/products": [
        {"id": 101, "name": "لابتوب دراسي للثانوية", "category": "أجهزة", "price_egp": 8500, "stock": 14},
        {"id": 102, "name": "تابلت تعليمي", "category": "أجهزة", "price_egp": 4200, "stock": 25},
        {"id": 103, "name": "كتاب الذكاء الاصطناعي التفاعلي", "category": "كتب", "price_egp": 120, "stock": 90}
    ]
}

def handle_mock_http_request(endpoint: str, method: str = "GET", payload: Dict = None) -> Dict[str, Any]:
    """
    محاكاة خادم الويب (Backend HTTP Controller)
    """
    if method == "GET":
        if endpoint in MOCK_API_DATABASE:
            return {"status_code": 200, "status_text": "OK", "body": MOCK_API_DATABASE[endpoint]}
        return {"status_code": 404, "status_text": "Not Found", "body": {"error": f"المسار '{endpoint}' غير موجود"}}
        
    elif method == "POST":
        if endpoint == "/api/orders":
            if not payload or "product_id" not in payload:
                return {"status_code": 400, "status_text": "Bad Request", "body": {"error": "بيانات الطلب ناقصة"}}
            return {
                "status_code": 201,
                "status_text": "Created",
                "body": {
                    "order_id": 98214,
                    "product_id": payload.get("product_id"),
                    "customer": payload.get("customer_name", "طالب مصري"),
                    "status": "تم تأكيد الطلب بنجاح وتوجيهه للتوصيل 🚚"
                }
            }
        return {"status_code": 404, "status_text": "Not Found", "body": {"error": "نقطة نهاية غير معروفة"}}
        
    return {"status_code": 405, "status_text": "Method Not Allowed", "body": {"error": "طريقة الطلب غير مدعومة"}}


# ============================================================
# 4. معالجة وتصفية بيانات الطلاب (Python Data Analysis)
# ============================================================
def analyze_student_grades(students: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    تحليل نتائج طلاب مادة البرمجة والذكاء الاصطناعي
    حساب المتوسط، وتحديد الأوائل، وتصنيف التقديرات
    """
    if not students:
        return {"error": "لا توجد بيانات"}
        
    scores = [s["score"] for s in students]
    avg_score = sum(scores) / len(scores)
    max_score = max(scores)
    min_score = min(scores)
    
    top_students = [s["name"] for s in students if s["score"] == max_score]
    
    grades_count = {"ممتاز": 0, "جيد جداً": 0, "جيد": 0, "مقبول": 0, "يحتاج دعم": 0}
    for s in students:
        sc = s["score"]
        if sc >= 85:
            grades_count["ممتاز"] += 1
        elif sc >= 75:
            grades_count["جيد جداً"] += 1
        elif sc >= 65:
            grades_count["جيد"] += 1
        elif sc >= 50:
            grades_count["مقبول"] += 1
        else:
            grades_count["يحتاج دعم"] += 1
            
    return {
        "total_students": len(students),
        "average_score": round(avg_score, 1),
        "highest_score": max_score,
        "lowest_score": min_score,
        "top_performers": top_students,
        "grades_distribution": grades_count
    }


# ============================================================
# 5. نموذج ذكاء اصطناعي مبسط: شجرة قرار لاقتراح المسار الجامعي (Decision Tree AI)
# ============================================================
def recommend_academic_track(math_grade: int, coding_interest: bool, logic_puzzle_score: int) -> Dict[str, str]:
    """
    نموذج ذكاء اصطناعي مبني على القواعد وشجرة القرار (Rule-based Expert System / Decision Tree)
    لمساعدة طلاب الصف الثاني الثانوي في توجيه شغفهم التقني
    """
    if math_grade >= 85 and logic_puzzle_score >= 8:
        if coding_interest:
            track = "علوم البيانات والذكاء الاصطناعي (Data Science & AI)"
            reason = "تمتلك مهارات رياضية ممتازة وشغفاً برمجياً عالياً، وهو التوليفة المثالية للتعلم العميق وتحليل الخوارزميات."
        else:
            track = "الأمن السيبراني وعلم التشفير (Cybersecurity & Cryptography)"
            reason = "الرياضيات العالية والتفكير المنطقي يؤهلانك لكسر وتصميم شفرات الحماية وبروتوكولات الأمان."
    elif coding_interest:
        track = "تطوير الويب وهندسة البرمجيات (Web Development & Software Engineering)"
        reason = "شغفك بالبناء والتطبيق يجعلك مهندس برمجيات واعداً لبناء تطبيقات متكاملة واجهات وخوادم."
    else:
        track = "تصميم تجربة المستخدم وتفاعل الإنسان والحاسوب (UI/UX & HCI)"
        reason = "القدرة على الملاحظة والتعاطف مع احتياجات المستخدم تضعك في موقع مثالي لتصميم منتجات رقمية سهلة الاستخدام."
        
    return {
        "recommended_track": track,
        "explanation": reason
    }


# ============================================================
# اختبار تشغيلي للسكريبت
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("🚀 منصة البرمجة والذكاء الاصطناعي - المحاكاة الخلفية")
    print("=" * 60)
    
    # تجربة محاكاة الحوسبة الطرفية
    res_edge = simulate_vehicle_reaction(25.0, "edge")
    res_cloud = simulate_vehicle_reaction(25.0, "cloud")
    print(f"\n1. الحوسبة الطرفية: تأخير {res_edge['latency_ms']}ms -> مسافة التوقف: {res_edge['total_stopping_distance_m']}m ({res_edge['result_message']})")
    print(f"2. الحوسبة السحابية: تأخير {res_cloud['latency_ms']}ms -> مسافة التوقف: {res_cloud['total_stopping_distance_m']}m ({res_cloud['result_message']})")
    
    # تجربة حساب المخاطر
    risk = calculate_cyber_risk(impact_score=5, probability_score=4)
    print(f"\n3. تقييم المخاطر (تأثير 5 × احتمالية 4 = {risk['risk_score']}): {risk['level']} -> {risk['recommended_action']}")
    
    # تجربة استجابة API
    weather_resp = handle_mock_http_request("/api/weather/cairo")
    print(f"\n4. طلب API طقس القاهرة: رمز الحالة {weather_resp['status_code']} -> {weather_resp['body']['condition']} {weather_resp['body']['temperature_c']}°C")
    
    print("\n✅ تم تشغيل كافة دوال المحاكاة بنجاح!")
