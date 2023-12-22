#Author Hubert Wawszczak

def validate_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        raise ValueError("Nieprawidłowa długość PESEL lub zawiera niecyfrowe znaki.")

    # Walidacja sumy kontrolnej
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    check_sum = sum(w * int(p) for w, p in zip(weights, pesel))
    valid_check_digit = (10 - check_sum % 10) % 10
    if int(pesel[-1]) != valid_check_digit:
        raise ValueError("Nieprawidłowy numer PESEL.")

    # Walidacja daty urodzenia
    year, month, day = int(pesel[:2]), int(pesel[2:4]), int(pesel[4:6])
    month_adjustment = month // 20 * 100
    year += month_adjustment
    try:
        from datetime import datetime
        datetime(year, month % 20, day)
    except ValueError:
        raise ValueError("Nieprawidłowa data urodzenia w numerze PESEL.")

    return True
