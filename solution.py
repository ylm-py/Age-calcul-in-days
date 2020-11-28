#created by : Yassine

# defining leap and ordinary years on a dictionary using this format :
# <month> : [total days : last month's total days + the month that was before it]
months_of_leap_year = {
    'january': [31, 0],
    'february': [29, 31],
    'march': [31, 60],
    'april': [30, 91],
    'may': [31, 121],
    'june': [30, 152],
    'july': [31, 182],
    'august': [31, 213],
    'september': [30, 244],
    'october': [31, 274],
    'november': [30, 305],
    'december': [31, 335]
}
months_of_ordinary_year = {
    'january': [31, 0],
    'february': [28, 31],
    'march': [31, 59],
    'april': [30, 90],
    'may': [31, 120],
    'june': [30, 151],
    'july': [31, 181],
    'august': [31, 212],
    'september': [30, 243],
    'october': [31, 273],
    'november': [30, 304],
    'december': [31, 334]
}
# storing a list of leap years that i got from google to use later
# you can get creative and generate them
leap_years = [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004,
              2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096, 2104, 2108, 2112,
              2116, 2120, 2124, 2128, 2132, 2136, 2140, 2144, 2148, 2152, 2156, 2160, 2164, 2168, 2172, 2176, 2180, 2184, 2188, 2192, 2196, 2204, 2208, 2212, 2216, 2220,
              2224, 2228, 2232, 2236, 2240, 2244, 2248, 2252, 2256, 2260, 2264, 2268, 2272, 2276, 2280, 2284, 2288, 2292, 2296, 2304, 2308, 2312, 2316, 2320, 2324, 2328,
              2332, 2336, 2340, 2344, 2348, 2352, 2356, 2360, 2364, 2368, 2372, 2376, 2380, 2384, 2388, 2392, 2396, 2400, 2404, 2408, 2412, 2416, 2420, 2424, 2428, 2432,
              2436, 2440, 2444, 2448, 2452, 2456, 2460, 2464, 2468, 2472, 2476, 2480, 2484, 2488, 2492, 2496, 2504, 2508, 2512, 2516, 2520, 2524, 2528, 2532, 2536, 2540,
              2544, 2548, 2552, 2556, 2560, 2564, 2568, 2572, 2576, 2580, 2584, 2588, 2592, 2596, 2604, 2608, 2612, 2616, 2620, 2624, 2628, 2632, 2636, 2640, 2644, 2648,
              2652, 2656, 2660, 2664, 2668, 2672, 2676, 2680, 2684, 2688, 2692, 2696, 2704, 2708, 2712, 2716, 2720, 2724, 2728, 2732, 2736, 2740, 2744, 2748, 2752, 2756,
              2760, 2764, 2768, 2772, 2776, 2780, 2784, 2788, 2792, 2796, 2800, 2804, 2808, 2812, 2816, 2820, 2824, 2828, 2832, 2836, 2840, 2844, 2848, 2852, 2856, 2860,
              2864, 2868, 2872, 2876, 2880, 2884, 2888, 2892, 2896, 2904, 2908, 2912, 2916, 2920, 2924, 2928, 2932, 2936, 2940, 2944,2948, 2952, 2956, 2960, 2964, 2968,
              2972, 2976, 2980, 2984, 2988, 2992, 2996, 3004, 3008, 3012, 3016, 3020, 3024, 3028, 3032, 3036, 3040, 3044, 3048]


# creating the main function
def age_calculator(birthday, birthmonth, birthyear, current_day, current_month, current_year):
    number_of_leap_years = 0
    for x in range(birthyear, current_year): #using a for loop we determine the number of leap years between the birthyear and the current year
        if x in leap_years:
            number_of_leap_years += 1
    age_in_years = int(current_year) - int(birthyear)
    number_of_ordinary_years = age_in_years - number_of_leap_years
    age_in_days = (number_of_ordinary_years * 365) + (number_of_leap_years * 366)

    # getting the number of days from 01/01/birthyear till birthday/birthmonth/birthyear
    if birthyear in leap_years:
        days_in_birthyear = (months_of_leap_year[str(birthmonth.lower())][-1] + birthday)
    else:
        days_in_birthyear = (months_of_ordinary_year[str(birthmonth.lower())][-1] + birthday)


    # getting the number of days from 01/01/current_year till current_day/current_month/current_year
    if current_year in leap_years:
        days_in_currentyear = months_of_leap_year[current_month.lower()][-1] + current_day
    else:
        days_in_currentyear = months_of_ordinary_year[current_month.lower()][-1] + current_day

    age_in_days += (days_in_currentyear - days_in_birthyear)
    print(f'Age : {age_in_days} day (excluding today)\n ')
# Test case :
age_calculator(25, 'january', 2000, 28, 'march', 2020) #1

# You'll get an error if the month is not typed correctly or if the day = 01,02..
# Also if the day number above 31 the results won't be correct


