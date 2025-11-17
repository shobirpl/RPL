#!/usr/bin/env python3
# coba3.py - Konversi suhu sederhana (Celsius, Fahrenheit, Kelvin, Reaumur)

UNITS = {"C": "Celsius", "F": "Fahrenheit", "K": "Kelvin", "R": "Reaumur"}

def to_celsius(value: float, unit: str) -> float:
    unit = unit.upper()
    if unit == "C":
        return value
    if unit == "F":
        return (value - 32) * 5/9
    if unit == "K":
        return value - 273.15
    if unit == "R":
        return value * 5/4
    raise ValueError("Unit tidak dikenal")

def from_celsius(c: float, unit: str) -> float:
    unit = unit.upper()
    if unit == "C":
        return c
    if unit == "F":
        return c * 9/5 + 32
    if unit == "K":
        return c + 273.15
    if unit == "R":
        return c * 4/5
    raise ValueError("Unit tidak dikenal")

def convert(value: float, from_unit: str, to_unit: str) -> float:
    c = to_celsius(value, from_unit)
    return from_celsius(c, to_unit)

def print_units():
    for k, v in UNITS.items():
        print(f"  {k} - {v}")

def main():
    print("Konversi Suhu - Pilih unit sumber dan tujuan")
    while True:
        try:
            print("\nSatuan tersedia:")
            print_units()
            src = input("Satuan sumber (C/F/K/R) atau Q untuk keluar: ").strip().upper()
            if src == "Q":
                print("Selesai.")
                break
            if src not in UNITS:
                print("Satuan sumber tidak valid.")
                continue

            dst = input("Satuan tujuan (C/F/K/R): ").strip().upper()
            if dst not in UNITS:
                print("Satuan tujuan tidak valid.")
                continue

            raw = input(f"Masukkan nilai suhu ({UNITS[src]}): ").strip()
            value = float(raw.replace(",", "."))  # dukung koma sebagai desimal

            result = convert(value, src, dst)
            print(f"{value:g} {UNITS[src]} = {result:g} {UNITS[dst]}")
        except ValueError:
            print("Input tidak valid. Coba lagi.")
        except KeyboardInterrupt:
            print("\nDibatalkan.")
            break

if __name__ == "__main__":
    main()