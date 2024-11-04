import math


def calc_engineer(model1, model2, model3, model4, wl_pow, rf_pow, se_pow, months):
    # Загальна кількість сайтів та залежних сайтів
    all_sites = model1 + model2 + model3 + model4
    dependent_sites = model1 + model2 + model3

    # Кількість сайтів, які повинні бути зроблені за місяць для M1-M3
    sites_per_month = math.ceil(dependent_sites / months)

    # Потрібна кількість SE інженерів
    se_needed = math.ceil(sites_per_month / se_pow)

    # Продуктивність обмежується SE для M1-M3, обчислюємо реальну продуктивність для WL та RF на M1-M3
    wl_effective_pow = min(wl_pow, se_pow)
    rf_effective_pow = min(rf_pow, se_pow)

    # Потрібна кількість WL та RF інженерів для M1-M3
    wl_needed_for_m1_m3 = math.ceil(sites_per_month / wl_effective_pow)
    rf_needed_for_m1_m3 = math.ceil(sites_per_month / rf_effective_pow)

    # Додаткова продуктивність WL та RF на M4
    wl_extra_capacity = wl_needed_for_m1_m3 * (wl_pow - wl_effective_pow)
    rf_extra_capacity = rf_needed_for_m1_m3 * (rf_pow - rf_effective_pow)

    # Потрібна кількість WL та RF інженерів для M4
    wl_needed_for_m4 = math.ceil((model4 - wl_extra_capacity * months) / (wl_pow * months))
    rf_needed_for_m4 = math.ceil((model4 - rf_extra_capacity * months) / (rf_pow * months))

    # Загальна кількість WL та RF інженерів
    wl_needed = wl_needed_for_m1_m3 + wl_needed_for_m4
    rf_needed = rf_needed_for_m1_m3 + rf_needed_for_m4

    # Повертаємо кількість інженерів
    return wl_needed, rf_needed, se_needed


def calculate_costs(model1, model2, model3, model4, wl_pow, rf_pow, se_pow, months,
                    survey_price, transportation_price, antenna_price,
                    equip_bbu_rru_3_price, equip_rru_3_price, equip_rru_6_price, dismantling_price):
    # Отримуємо кількість інженерів з першої функції
    wl_engineers, rf_engineers, se_engineers = calc_engineer(model1, model2, model3, model4, wl_pow, rf_pow, se_pow,
                                                             months)

    # Загальна кількість сайтів для M1, M2, M3
    dependent_sites = model1 + model2 + model3

    # Витрати на Survey
    survey_cost = dependent_sites * survey_price

    # Витрати на Transportation
    wl_transport_cost = wl_engineers * min(wl_pow, se_pow) * transportation_price * months
    rf_transport_cost = rf_engineers * min(rf_pow, se_pow) * transportation_price * months
    se_transport_cost = se_engineers * se_pow * transportation_price * months
    model4_transport_cost = 2 * model4 * transportation_price
    transportation_cost = wl_transport_cost + rf_transport_cost + se_transport_cost + model4_transport_cost

    # Витрати на Antenna installation/replacement
    antenna_cost = dependent_sites * antenna_price

    # Витрати на Equipment installation
    equip_bbu_rru_cost = model1 * equip_bbu_rru_3_price
    equip_rru_3_cost = model2 * equip_rru_3_price
    equip_rru_6_cost = model3 * equip_rru_6_price

    # Витрати на Dismantling
    dismantling_cost = dependent_sites * dismantling_price

    # Загальна сума
    total_cost = (survey_cost + transportation_cost + antenna_cost +
                  equip_bbu_rru_cost + equip_rru_3_cost + equip_rru_6_cost + dismantling_cost)

    # Виведення результатів у консоль
    print("Cost Breakdown:")
    print(f"{'Scope of Works':<40} {'Cost (USD)'}")
    print("-" * 50)
    print(f"{'Survey':<40} {survey_cost:.2f}")
    print(f"{'Transportation':<40} {transportation_cost:.2f}")
    print(f"{'Antenna installation/replacement':<40} {antenna_cost:.2f}")
    print(f"{'Equipment installation BBU+RRU(up to 3)':<40} {equip_bbu_rru_cost:.2f}")
    print(f"{'Equipment installation RRU(up to 3)':<40} {equip_rru_3_cost:.2f}")
    print(f"{'Equipment installation RRU(up to 6)':<40} {equip_rru_6_cost:.2f}")
    print(f"{'Dismantling':<40} {dismantling_cost:.2f}")
    print("-" * 50)
    print(f"{'Total':<40} {total_cost:.2f}")


# Приклад виклику функції
calculate_costs(
    model1=300, model2=700, model3=700, model4=300,
    wl_pow=40, rf_pow=30, se_pow=25, months=12,
    survey_price=1.0, transportation_price=1.0, antenna_price=1.0,
    equip_bbu_rru_3_price=2.0, equip_rru_3_price=1.7, equip_rru_6_price=2.5, dismantling_price=0.5
)
