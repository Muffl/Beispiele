def median(lst):
    """
    Berechnet den Median einer Liste von Zahlen.
    
    Args:
    - lst (list): Eine Liste von Zahlen.

    Returns:
    - float: Der Median der Liste.
    """
    sorted_lst = sorted(lst)
    lst_len = len(sorted_lst)
    
    # Wenn die Liste eine ungerade Anzahl von Elementen hat
    if lst_len % 2 == 1:
        return sorted_lst[lst_len // 2]
    # Wenn die Liste eine gerade Anzahl von Elementen hat
    else:
        return (sorted_lst[(lst_len - 1) // 2] + sorted_lst[lst_len // 2]) / 2.0

# Test
zahlen = [5, 2, 9, 1, 6, 5]
print(median(zahlen))  # Sollte 5.0 ausgeben
