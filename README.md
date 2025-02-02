# PRA2_datavis

Aquest repositori conté el projecte **PRA2** de l'assignatura de *Visualització de dades* del màster universitat de Ciència de Dades de la UOC. El projecte inclou l'anàlisi i visualitzacions interactives creades amb dades de les societats laborals catalanes entre octubre de 2023 i 2024.

## Estructura del repositori

```
PRA2_datavis/
|
├── data/                    # Datasets utilitzats per a l'anàlisi
├── output/                  # Resultats generats (CSV i Excel)
├── logo/                    # Recursos visuals, com el logo utilitzat
├── prepare_visualization.py # Script Python per preparar i preprocessar les dades
├── data_preparation.xlsx    # Fitxer Excel amb els resultats processats i resum de les tasques
└── README.md                # Documentació principal del projecte
```

### Descripció dels continguts

1. **`data/`**
   - Aquesta carpeta conté els datasets utilitzats per a la preparació de les visualitzacions obtinguts del portal de transparència de le Generalitat de Catalunya (https://analisi.transparenciacatalunya.cat/Treball/Societats-laborals-en-actiu/xfiz-zxak/about_data)

2. **`output/`**
   - Carpeta on es desaran els resultats processats, tant en format **CSV** com **Excel**.

3. **`logo/`**
   - Inclou recursos visuals, com el logo utilitzat en la presentació o documentació.

4. **`prepare_visualization.py`**
   - Conté l'script Python que processa i prepara els datasets per generar els outputs necessaris per a les visualitzacions interactives.
   - Llibreries utilitzades:
     - **Pandas**: Per al tractament i transformació de les dades.
     - **openpyxl**: Per exportar els resultats a un fitxer Excel, útil per a l'anàlisi posterior.

5. **`data_preparation.xlsx`**
   - Fitxer Excel amb els resultats processats, que permet una revisió i manipulació més fàcil de les dades.

## Instal·lació

Per executar l'script Python, assegura't de tenir les següents dependències instal·lades:

```bash
pip install pandas openpyxl
```

## Execució de l'script

1. Assegura't que els datasets estan disponibles a la carpeta `data/`.
2. Executa l'script Python:

```bash
python prepare_visualization.py
```

3. Els resultats es desaran com a:
   - **CSV** i **Excel** dins la carpeta `output/`.

## Visualització
La visualització creada a partir de l'eina de **Flourish.studio** està disponible al següent enllaç web: https://public.flourish.studio/story/2820699/

## Llicència

Aquest projecte està llicenciat sota la **Llicència MIT**. Consulta el fitxer `LICENSE` per a més detalls.

---

### Autor
Aquest projecte ha estat desenvolupat com a part de l'assignatura de *Visualització de dades*. 
