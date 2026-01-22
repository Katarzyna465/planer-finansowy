import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import date

# ================= 1. KONFIGURACJA =================
st.set_page_config(
    page_title="Planer Finansowy",
    layout="wide",
    page_icon="💳"
)

# ================= 2. PAMIĘĆ DANYCH =================
if "historia" not in st.session_state:
    st.session_state.historia = []

# ================= 3. SIDEBAR =================
st.sidebar.title("🎛️ Panel Kontrolny")

st.sidebar.subheader("📅 Okres")
miesiac = st.sidebar.text_input("Miesiąc", "Marzec 2026")

st.sidebar.subheader("💰 Finanse")
dochod = st.sidebar.number_input("Przychód netto (PLN)", min_value=0.0, value=7500.0, step=100.0)

with st.sidebar.expander("💸 Lista Wydatków Stałych", expanded=True):
    czynsz = st.number_input("🏠 Dom / Media", min_value=0.0, value=2800.0, step=50.0)
    jedzenie = st.number_input("🍔 Żywność", min_value=0.0, value=1500.0, step=50.0)
    transport = st.number_input("⛽ Transport", min_value=0.0, value=600.0, step=50.0)
    rozrywka = st.number_input("🎉 Przyjemności", min_value=0.0, value=400.0, step=50.0)
    inne = st.number_input("🛍️ Inne", min_value=0.0, value=200.0, step=50.0)

# Obliczenia "Live"
wydatki_total = czynsz + jedzenie + transport + rozrywka + inne
oszczednosci = dochod - wydatki_total
procent_oszcz = (oszczednosci / dochod * 100) if dochod > 0 else 0

st.sidebar.markdown("---")
st.sidebar.info(f"💡 Twoje koszty stałe to **{wydatki_total:,.2f} zł** miesięcznie.")

# ================= 4. GŁÓWNY WIDOK =================
st.title(f"📊 Planer Finansowy: {miesiac}")

# Zakładki
tab_dash, tab_plan, tab_hist, tab_kredyt, tab_edu = st.tabs([
    "🏠 Pulpit",
    "📅 Planer Wydatków",
    "📈 Historia",
    "🏦 Kredyt",
    "🎓 Edukacja"
])

# --- ZAKŁADKA 1: PULPIT ---
with tab_dash:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Wpływy", f"{dochod:,.2f} PLN")
    col2.metric("Wydatki", f"{wydatki_total:,.2f} PLN",
                delta=f"-{(wydatki_total / dochod) * 100:.1f}%" if dochod > 0 else "0%")

    color_delta = "normal" if oszczednosci > 0 else "inverse"
    col3.metric("Bilans", f"{oszczednosci:,.2f} PLN", delta=f"{procent_oszcz:.1f}%", delta_color=color_delta)

    cel_min = dochod * 0.2
    status_celu = "✅ Osiągnięty" if oszczednosci >= cel_min else f"❌ Brakuje {cel_min - oszczednosci:.2f}"
    col4.metric("Cel (20%)", f"{cel_min:,.2f} PLN", delta=status_celu, delta_color="off")

    st.markdown("---")

    c1, c2 = st.columns([1.5, 1])
    with c1:
        st.subheader("Gdzie płyną pieniądze?")
        df_pie = pd.DataFrame({
            "Kategoria": ["Dom", "Jedzenie", "Transport", "Rozrywka", "Inne"],
            "Wartość": [czynsz, jedzenie, transport, rozrywka, inne]
        })
        fig_pie = px.pie(df_pie, values="Wartość", names="Kategoria", hole=0.5,
                         color_discrete_sequence=px.colors.qualitative.Pastel)
        fig_pie.update_layout(template="plotly_white")
        st.plotly_chart(fig_pie, use_container_width=True)

    with c2:
        st.subheader("Stan budżetu")
        fig_bar = go.Figure(go.Indicator(
            mode="gauge+number",
            value=(wydatki_total / dochod) * 100 if dochod > 0 else 0,
            title={'text': "Wykorzystanie dochodu (%)"},
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': "#00d4b1"},
                'steps': [
                    {'range': [0, 50], 'color': "#e5e7eb"},
                    {'range': [50, 80], 'color': "#d1d5db"},
                    {'range': [80, 100], 'color': "#9ca3af"}],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90}}))
        fig_bar.update_layout(template="plotly_white", height=300)
        st.plotly_chart(fig_bar, use_container_width=True)

    st.write("###")
    col_save, _ = st.columns([1, 4])
    with col_save:
        if st.button("💾 Zatwierdź i Zapisz Miesiąc"):
            st.session_state.historia.append({
                "Miesiąc": miesiac,
                "Przychód": dochod,
                "Wydatki": wydatki_total,
                "Oszczędności": oszczednosci
            })
            st.success("Miesiąc został dodany do historii!")

# --- ZAKŁADKA 2: PLANER WYDATKÓW  ---
with tab_plan:
    st.header("📅 Nadchodzące Wydatki i Cele")
    st.write("Wydatki, które nie zdarzają się co miesiąc, ale potrafią zrujnować budżet.")

    col_plan1, col_plan2 = st.columns(2)

    # LEWA KOLUMNA: Fundusze Celowe
    with col_plan1:
        st.subheader("🎯 Kalkulator Celu (Sinking Fund)")
        st.info("Chcesz kupić auto, pojechać na wakacje lub opłacić OC? Oblicz, ile musisz odkładać.")

        cel_nazwa = st.text_input("Nazwa celu", "Wakacje 2026")
        cel_kwota = st.number_input("Ile potrzebujesz? (PLN)", min_value=0.0, value=5000.0, step=100.0)
        cel_miesiace = st.number_input("Za ile miesięcy?", min_value=1, value=6, step=1)


        wymagana_kwota = cel_kwota / cel_miesiace

        st.metric(label=f"Odkładaj miesięcznie na: {cel_nazwa}", value=f"{wymagana_kwota:,.2f} PLN")


        if wymagana_kwota > oszczednosci:
            st.warning(
                f"⚠️ Uwaga! Twoje obecne oszczędności z panelu bocznego ({oszczednosci:,.2f} zł) są mniejsze niż ta kwota!")
        else:
            st.success("✅ Stać Cię! Twoje miesięczne oszczędności pokrywają ten cel.")

    # PRAWA KOLUMNA: Ukryte koszty roczne
    with col_plan2:
        st.subheader("🗓️ Wydatki Nieregularne (Roczne)")
        st.write("Wpisz szacunkowe koszty roczne, aby zobaczyć, ile *naprawdę* kosztuje Cię życie.")

        with st.expander("Rozwiń listę nieregularnych wydatków", expanded=True):
            k_ubezpieczenia = st.number_input("Ubezpieczenia (Auto/Dom/Życie)", value=1200.0, step=100.0)
            k_wakacje = st.number_input("Wakacje i wyjazdy", value=3000.0, step=100.0)
            k_prezenty = st.number_input("Prezenty (Święta/Urodziny/Wesela)", value=1000.0, step=100.0)
            k_lekarz = st.number_input("Zdrowie / Dentysta", value=500.0, step=50.0)
            k_serwis = st.number_input("Serwis Auta / Naprawy Domu", value=800.0, step=50.0)
            k_inne_roczne = st.number_input("Inne (np. Subskrypcje roczne)", value=400.0, step=50.0)

        suma_roczna = k_ubezpieczenia + k_wakacje + k_prezenty + k_lekarz + k_serwis + k_inne_roczne
        ukryty_koszt_mc = suma_roczna / 12

        st.markdown("---")
        m_ukryty1, m_ukryty2 = st.columns(2)
        m_ukryty1.metric("Suma roczna", f"{suma_roczna:,.0f} PLN")
        m_ukryty2.metric("Ukryty koszt miesięczny", f"{ukryty_koszt_mc:,.2f} PLN",
                         delta="Tyle powinieneś dodatkowo odkładać!", delta_color="inverse")

# --- ZAKŁADKA 3: HISTORIA ---
with tab_hist:
    st.subheader("Archiwum Finansowe")
    if st.session_state.historia:
        df_h = pd.DataFrame(st.session_state.historia)
        h1, h2, h3 = st.columns(3)
        suma_oszcz = df_h['Oszczędności'].sum()
        srednie_wydatki = df_h['Wydatki'].mean()
        h1.metric("Łącznie zaoszczędzono", f"{suma_oszcz:,.2f} PLN")
        h2.metric("Średnie wydatki", f"{srednie_wydatki:,.2f} PLN")
        h3.metric("Zarejestrowane miesiące", len(df_h))
        st.markdown("---")
        fig_trend = px.area(df_h, x="Miesiąc", y="Oszczędności", markers=True,
                            title="Trend wzrostu majątku", color_discrete_sequence=['#00d4b1'])
        fig_trend.update_layout(template="plotly_white")
        st.plotly_chart(fig_trend, use_container_width=True)
        col_tabela, col_csv = st.columns([3, 1])
        with col_tabela:
            st.dataframe(df_h, use_container_width=True)
        with col_csv:
            csv_data = df_h.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Pobierz CSV", csv_data, "moje_finanse.csv", "text/csv")
    else:
        st.info("Brak danych. Zapisz pierwszy miesiąc w zakładce Pulpit.")

# --- ZAKŁADKA 4: KALKULATOR KREDYTOWY ---
with tab_kredyt:
    st.subheader("🏦 Symulator Kredytu")
    kc1, kc2 = st.columns(2)
    with kc1:
        kwota_kredytu = st.number_input("Kwota kredytu (PLN)", min_value=0.0, value=300000.0, step=5000.0)
        okres_lat = st.number_input("Okres kredytowania (lata)", min_value=1, value=25, step=1)
    with kc2:
        oprocentowanie = st.number_input("Oprocentowanie roczne (%)", min_value=0.0, value=7.5, step=0.1)
        typ_raty = st.radio("Rodzaj rat", ["Równe", "Malejące (proste)"])

    r = oprocentowanie / 100 / 12
    n = okres_lat * 12
    if kwota_kredytu > 0:
        if typ_raty == "Równe":
            rata = (kwota_kredytu * r * (1 + r) ** n) / ((1 + r) ** n - 1)
            calkowity_koszt = rata * n
        else:
            rata = (kwota_kredytu / n) + (kwota_kredytu * r)
            calkowity_koszt = kwota_kredytu + (kwota_kredytu * (oprocentowanie / 100) * (okres_lat + 1 / 12) / 2)

        st.markdown("---")
        m1, m2, m3 = st.columns(3)
        m1.metric("Miesięczna rata", f"{rata:,.2f} PLN")
        m2.metric("Całkowity koszt", f"{calkowity_koszt:,.2f} PLN")
        m3.metric("Same odsetki", f"{calkowity_koszt - kwota_kredytu:,.2f} PLN", delta="KOSZT", delta_color="inverse")

# --- ZAKŁADKA 5: EDUKACJA ---
with tab_edu:
    st.header("🎓 Twoje Pieniądze w Czasie")

    edu1, edu2 = st.tabs(["📊 Symulator + Inflacja", "🧠 Baza Wiedzy"])

    # --- 1. SYMULATOR + INFLACJA ---
    with edu1:
        st.subheader("Ile realnie będą warte Twoje oszczędności?")
        c_in1, c_in2, c_in3 = st.columns(3)
        with c_in1:
            daily_spend = st.number_input("Kwota dzienna (PLN)", min_value=0.0, value=20.0, step=1.0)
        with c_in2:
            lata_oszcz = st.number_input("Czas (lata)", min_value=1, value=15, step=1)
        with c_in3:
            st.write("")

        st.markdown("##### ⚙️ Parametry rynkowe")
        c_param1, c_param2 = st.columns(2)
        with c_param1:
            stopa_zwrotu = st.number_input("Zysk z inwestycji (rocznie %)", min_value=0.0, value=6.0, step=0.1) / 100
        with c_param2:
            inflacja = st.number_input("Przewidywana inflacja (rocznie %)", min_value=0.0, value=3.5, step=0.1) / 100

        miesiace = int(lata_oszcz * 12)
        data_chart = []
        temp_wplaty = 0
        temp_val_nominal = 0

        for m in range(1, miesiace + 1):
            wplata_miesieczna = daily_spend * 30
            temp_wplaty += wplata_miesieczna
            temp_val_nominal = (temp_val_nominal + wplata_miesieczna) * (1 + stopa_zwrotu / 12)
            lata_trwania = m / 12
            temp_val_realna = temp_val_nominal / ((1 + inflacja) ** lata_trwania)

            if m % 12 == 0:
                data_chart.append({
                    "Rok": m / 12,
                    "Suma Wpłat": temp_wplaty,
                    "Kwota na koncie (Nominalna)": temp_val_nominal,
                    "Siła Nabywcza (Realna)": temp_val_realna
                })

        final_nominal = temp_val_nominal
        final_real = temp_val_realna
        zysk_nominalny = final_nominal - temp_wplaty

        st.markdown("---")
        res1, res2, res3 = st.columns(3)
        res1.metric("Wpłacona gotówka", f"{temp_wplaty:,.0f} PLN")
        res2.metric("Stan konta (Liczby)", f"{final_nominal:,.0f} PLN", delta=f"Zysk: {zysk_nominalny:,.0f} zł")
        res3.metric("Siła Nabywcza (Realna)", f"{final_real:,.0f} PLN",
                    delta=f"Inflacja 'zjadła': {final_real - final_nominal:,.0f} zł", delta_color="inverse")

        df_chart = pd.DataFrame(data_chart)
        if not df_chart.empty:
            fig_growth = go.Figure()
            fig_growth.add_trace(go.Scatter(x=df_chart["Rok"], y=df_chart["Suma Wpłat"], name='Tyle wpłaciłeś',
                                            line=dict(color='gray', dash='dash')))
            fig_growth.add_trace(
                go.Scatter(x=df_chart["Rok"], y=df_chart["Kwota na koncie (Nominalna)"], name='Stan Konta',
                           line=dict(color='#00d4b1', width=3)))
            fig_growth.add_trace(
                go.Scatter(x=df_chart["Rok"], y=df_chart["Siła Nabywcza (Realna)"], name='Realna Wartość',
                           line=dict(color='#ff4b4b', width=3), fill='tozeroy'))
            fig_growth.update_layout(template="plotly_white", xaxis_title="Lata", yaxis_title="Wartość (PLN)")
            st.plotly_chart(fig_growth, use_container_width=True)

    # --- 2. BAZA WIEDZY ---
    with edu2:
        st.subheader("🧠 Kompendium Wiedzy Finansowej")
        col_w1, col_w2 = st.columns(2)
        with col_w1:
            with st.expander("🎈 Co to jest INFLACJA?", expanded=True):
                st.write("To wzrost cen sprawiający, że za te same pieniądze kupisz mniej.")
            with st.expander("🛡️ PODUSZKA FINANSOWA"):
                st.write("Minimum 3-6 miesięcy kosztów życia na 'czarną godzinę'.")
        with col_w2:
            with st.expander("🍰 Zasada 50/30/20"):
                st.write("50% Potrzeby, 30% Zachcianki, 20% Oszczędności.")
            with st.expander("🥚 Dywersyfikacja"):
                st.write("Nie wkładaj wszystkich jajek do jednego koszyka.")

# ================= 6. STOPKA =================
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #4b5563; font-size: 0.8rem;'>Planer finansowy Pro © 2026 | Built with Python & Streamlit</div>",
    unsafe_allow_html=True)
