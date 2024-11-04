import math

"""
Функція яка прораховує необхідну кількість інженерів в 
залежності від їх потужностей та необхідної кількості сайтів
"""

def calc_engineer(model1, model2, model3, model4, wl_pow, rf_pow, se_pow, months):
    # Загальна кількість сайтів та кількість сайтів, які залежать від продуктивності SE
    all_sites = model1 + model2 + model3 + model4
    dependent_sites = model1 + model2 + model3

    # Кількість сайтів, які необхідно обробити в місяць для всіх сайтів, щоб вкластися у дедлайн
    sites_per_month = math.ceil(dependent_sites / months)

    # Продуктивність WL та RF з обмеженням SE для M1-M3
    wl_effective_pow_m1_m3 = min(wl_pow, se_pow)
    rf_effective_pow_m1_m3 = min(rf_pow, se_pow)

    # Обчислюємо кількість інженерів для M1-M3 з обмеженою продуктивністю
    wl_engineers_m1_m3 = math.ceil(sites_per_month / wl_effective_pow_m1_m3)
    rf_engineers_m1_m3 = math.ceil(sites_per_month / rf_effective_pow_m1_m3)
    se_engineers = math.ceil(sites_per_month / se_pow)

    # Розрахунок надлишкової продуктивності для M4
    wl_surplus = wl_engineers_m1_m3 * (wl_pow - wl_effective_pow_m1_m3)  # надлишок WL для M4
    rf_surplus = rf_engineers_m1_m3 * (rf_pow - rf_effective_pow_m1_m3)  # надлишок RF для M4

    # Загальна потреба сайтів M4 на місяць
    m4_sites_per_month = math.ceil(model4 / months)

    # Інженери для M4 з урахуванням надлишкової продуктивності
    wl_m4_engineers = max(0, math.ceil((m4_sites_per_month - wl_surplus) / wl_pow))
    rf_m4_engineers = max(0, math.ceil((m4_sites_per_month - rf_surplus) / rf_pow))

    # Загальна кількість інженерів для M1-M3 та M4
    total_wl = wl_engineers_m1_m3 + wl_m4_engineers
    total_rf = rf_engineers_m1_m3 + rf_m4_engineers
    total_se = se_engineers  # SE потрібен тільки для M1-M3

    return {
        'WL Engineers': total_wl,
        'RF Engineers': total_rf,
        'SE Engineers': total_se
    }

engineer_counts = calc_engineer(300, 700, 700, 300, wl_pow=40, rf_pow=30, se_pow=25, months=12)
print(engineer_counts)

