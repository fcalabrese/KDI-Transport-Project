# Public tranportation in Trentino
*Project of the course "Knowledge and Data Integration at the University of Trento - A.Y. 2019-2020*

## Introduction
This respository contains the material of the project course of "Knowledge and data integration". The goal of the project was the definition of a formal model and the integration of data about transportation in Trentino. The team manager of this group is Fabio Molignoni. The work on this project has been done by two different sub-groups:

**informal to formal sub-group**

The informal to formal group created the informal model (which was developed using yEd) and the formal model (which was developed using Protégé). The contribution of each member of the group is defined inside the "Revision History" section of the technical report. In general, even if the technical report has been written by a single person, all the members contributed anyway to the final output of that section.

| Name        | Matricola  | E-mail  |
| ------------- | ------------- | ----- |
| Bogdan Kostić      | 211827 | bogdan.kostic@studenti.unitn.it |
| Evidence Monday      | 204729     |   evidence.monday@studenti.unitn.it |
| Andrea Montibeller | 203264     | andrea.montibeller@studenti.unitn.it |

**data integration**

The data integration group retrieved all the data (both by downloading and scraping them), cleaned them (using RapidMiner) and performed the integration (using Karma). The final visualization has been done using GraphDB. The contribution done by each member of the group can be found in the "Revision History" section of the technical report and in the commits history of this repository.

| Name        | Matricola  | E-mail  |
| ------------- |-------------| -----|
| Federico Calabrese      | 207463 | federico.calabrese@studenti.unitn.it |
| Giacomo Callegari     | 207468     | giacomo.callegari@studenti.unitn.it |
| Fabio Molignoni | 203201     | fabio.molignoni@studenti.unitn.it |

## Repository organization
The repository is organized in this way:
- **/data** contains all the data that has been used during the integration. There are two subfolders: *"raw data"* contains the original downloaded/scraped CSVs, while *"processed data"* contains the final cleaned data that have been used to perform the integration.
- **/formal-model** contains the output of Protégé, i.e. the final OWL formal model attached to the top level ontology.
- **/informal-model** contains the PDF representation of the informal model, along with the source code of yEd that can be used to modify it.
- **/models** contains all the resources used to perform operations on data. *"r2rml" contains all the models used to perform the integration on Karma, *"rapidminer"* contains all the RapidMiner's processes used to transform raw data into processed data. *"scripts"* contains all the Python scripts that have been used throughout the project.

In the root folder there is also the technical report, which describes in detail all the work performed throughout the project.

Due to the size of the knowledge graph it was not possible to load it directly on GitHub. For this reason, you can download the complete linked data at https://drive.google.com/open?id=1WIbw9GmyVB7VFv3F4LMcAf8jsCC3LZoW . We also provide the RDF/XML version here: https://drive.google.com/file/d/1cVP_MFSDAmWNSmPRxjCMNb1m4H3tFUt_/view

## Reproduce the output
As said, inside the *data/raw data* there are all the raw data needed for the integration, also the one obtained through scraping. Anyway, in the *models/scripts* folder there are all the scripts that can be used to perform again the scraping:
-   `filterStreets.py` receives as input the OpenStreetMap data about Trentino (downloadable from here (https://www.openstreetmap.org/export)) and produces as output the CSV for the streets
-   `scrape_trains.py` allows to get all the trains from ViaggiaTreno API
-   `train_detail.py` allows to retrieve additional information for each train from ViaggiaTreno API
-   `tt_delay.py` allows to extract information about the delay from the ViaggiareInTrentino API
-   `json-to-csv.py` is a small scripts that allows to convert json-formatted datasets into CSVs.

Some of the raw data has to be cleaned, merged and processed in order to comply with the format required by Karma. The final data that has been used for the integration can be found inside the folder *data/processed data*. For completeness, we describe anyway the process to generate, from the raw data, the final processed one. First of all, some additional computation has to be done:
-   `findAddress.py` requires as argument the name of the input CSV and requires that, inside the CSV, there are two columns named "latitude" and "longitude". Thi scripts adds an extra column, called "address", which represent the textual address of the location. This script has to be called for each dataset that contains a physical location.
-   `predict_delay.py` allows to compute the average delay for each bus. It expects as input a folder, which contains several CSV: each CSV stores the delay of a particular day computed through the `tt_delay.py` script.

Once this additional data has been computed, it is possible to start working with RapidMiner. All the RapidMiner processes are stored inside the folder *models/rapidminer*. In order to produce the final datasets, you have to run each RapidMiner file.
The final step is to perform the actual integration through Karma. For each dataset in the *processed data* folder there is the appropriate model stored inside the folder *models/r2rml*. For example, for the dataset `bike_sharing.csv` there is the model `bike_sharing-model.ttl`. Once all the datasets have been imported and integrated with the corresponding model it is possible to generate the final knowledge graph using OpenRDF.
