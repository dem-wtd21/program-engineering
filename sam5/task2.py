results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 36.9, 21.0, 26.4, 17.1,
           30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

sorted_results = sorted(results)

best_results = sorted_results[:3]
worst_results = sorted_results[-3:]

results_from_10 = [r for r in sorted_results if r >= 10]

print(f"Три лучшие результата: {best_results}")
print(f"Три худшие результата: {worst_results}")
print(f"Все результаты начиная с 10 секунд: {results_from_10}")