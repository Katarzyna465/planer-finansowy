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



### 4. Technologie i narzędzia

Projekt został zrealizowany przy użyciu następujących technologii:

* *Język programowania:* Python 3.x
* *Framework aplikacji:* Streamlit
* *Analiza i przetwarzanie danych:* Pandas
* *Wizualizacja danych:* Plotly
* *Kontrola wersji i repozytorium:* Git / GitHub, w podpunkcie a a w podpunkce b to ### b. Architektura uruchomieniowa

Aplikacja jest uruchamiana lokalnie. Logika biznesowa wykonywana jest przez interpreter języka Python, a interfejs użytkownika wyświetlany jest w przeglądarce internetowej.

* Środowisko uruchomieniowe: Python 3.8+
* Interfejs: Przeglądarka internetowa" potem do 5 podpunktu dałabym to "## 5. Testowanie

### a. Scenariusze testowe (Test Cases)

| ID | Scenariusz testowy | Oczekiwany rezultat | Status |
|----|-------------------|---------------------|--------|
| *TC-01* | **Obliczanie miesięcznego bilansu**<br>Wprowadzenie przychodu 5000 zł i sumy wydatków 3000 zł. | System wyświetla poprawny bilans (+2000 zł) oraz komunikat o nadwyżce budżetowej. | ✅ OK |
| *TC-02* | **Wizualizacja struktury wydatków**<br>Wprowadzenie wydatków w różnych kategoriach (np. jedzenie, czynsz). | Wykres kołowy (Plotly) generuje się poprawnie i odzwierciedla procentowy udział kategorii. | ✅ OK |
| *TC-03* | **Symulacja "Efektu Latte"**<br>Zmiana ceny kawy i częstotliwości zakupu w symulatorze. | Wykres prognozy oszczędności dynamicznie aktualizuje się, pokazując kwotę po 10 latach. | ✅ OK |
| *TC-04* | **Kalkulator Kredytowy**<br>Wprowadzenie kwoty kredytu, oprocentowania i okresu spłaty. | Aplikacja wylicza poprawną wysokość miesięcznej raty oraz całkowity koszt kredytu. | ✅ OK |
| *TC-05* | **Trwałość danych (Eksport)**<br>Użycie przycisku "Pobierz dane jako CSV". | Przeglądarka pobiera plik .csv, który zawiera poprawnie sformatowane dane z historii. | ✅ OK |
| *TC-06* | **Walidacja danych wejściowych**<br>Próba wpisania ujemnej kwoty przychodu. | System blokuje operację lub wyświetla ostrzeżenie. | ✅ OK |

### b. Podsumowanie testów

Testy funkcjonalne zostały przeprowadzone manualnie w środowisku lokalnym. Aplikacja działa stabilnie, a weryfikacja kluczowych funkcjonalności (obliczenia finansowe, generowanie wykresów, eksport danych) zakończyła się wynikiem pozytywnym. Nie wykryto błędów krytycznych uniemożliwiających korzystanie z programu.



## Instrukcja uruchomienia

### Wymagania
- Python 3.8+
- Przeglądarka internetowa

### Uruchomienie
```bash
pip install streamlit pandas plotly
streamlit run app.py


