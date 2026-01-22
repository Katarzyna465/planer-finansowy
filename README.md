#  Planer Finansowy

## Interaktywny Planer Finansowy i Symulator Decyzji Ekonomicznych



## 1. Charakterystyka oprogramowania

### a. Nazwa skrócona
**Planer Finansowy**

### b. Nazwa pełna
**Interaktywny Planer Finansowy i Symulator Decyzji Ekonomicznych**

### c. Sumaryczny opis i cele
Planer Finansowy jest aplikacją webową stworzoną w języku Python z wykorzystaniem frameworka Streamlit.  
Celem aplikacji jest wspomaganie użytkownika w zarządzaniu budżetem domowym poprzez bieżące monitorowanie przychodów i wydatków oraz analizę kondycji finansowej w ujęciu miesięcznym i długoterminowym.

System umożliwia wprowadzanie danych finansowych, automatyczne obliczanie bilansu oraz wizualizację struktury wydatków.  
Dodatkowo aplikacja pełni funkcję edukacyjną, oferując symulator „Efektu Latte” oraz kalkulator kredytowy.



## 2. Prawa autorskie

### a. Autorzy
- Katarzyna Baniak (283015)  
- Joanna Ośka (277976)

### b. Warunki licencyjne
Oprogramowanie zostało udostępnione na zasadach licencji **MIT License**.



## 3. Specyfikacja wymagań

### Wymagania funkcjonalne i pozafunkcjonalne

| ID   | Nazwa wymagania | Opis | Priorytet | Kategoria |
|-----|----------------|------|----------|-----------|
| W-01 | Wprowadzanie danych finansowych | Wprowadzanie przychodu i wydatków w 5 kategoriach | 1 | Funkcjonalne |
| W-02 | Obliczanie bilansu | Automatyczne obliczanie wydatków i bilansu | 1 | Funkcjonalne |
| W-03 | Wizualizacja struktury wydatków | Interaktywny wykres kołowy | 1 | Funkcjonalne |
| W-04 | Zapis danych do historii | Zapis danych do historii i CSV | 1 | Funkcjonalne |
| W-05 | Monitorowanie oszczędności | Prezentacja oszczędności i prognoza | 1 | Funkcjonalne |
| W-06 | Kalkulator kredytowy | Obliczanie rat i kosztu | 2 | Funkcjonalne |
| W-07 | Efekt Latte | Symulacja długoterminowa | 2 | Funkcjonalne |
| W-08 | Eksport danych | Eksport do CSV | 2 | Funkcjonalne |
| W-09 | Responsywność interfejsu | Dostosowanie UI | 2 | Pozafunkcjonalne |
| W-10 | Walidacja danych | Obsługa błędów | 1 | Pozafunkcjonalne |



## 4. Architektura systemu

### a. Architektura rozwoju
- Python 3.x  
- Streamlit  
- Pandas  
- Plotly  
- Git / GitHub

### b. Architektura uruchomieniowa
- Przeglądarka internetowa  
- Streamlit  
- Pandas  
- Plotly



## 5. Test

### a. Scenariusze testowe
- Obliczanie bilansu
- Zapis danych
- Monitorowanie oszczędności
- Kalkulator kredytowy

### b. Sprawozdanie z testów
Testy zostały przeprowadzone w środowisku lokalnym. Nie stwierdzono błędów krytycznych.



## Instrukcja uruchomienia

### Wymagania
- Python 3.8+
- Przeglądarka internetowa

### Uruchomienie
```bash
pip install streamlit pandas plotly
streamlit run app.py


