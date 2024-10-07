# CSE584 Midterm Project
----------------------------------------------------------------------------------------------
# Fine-Tuning BERT for Attribution of Large Language Model Outputs Using SequenceClassification
 
#### Team Members:
- Krishnasai Paleti - kxp5619@psu.edu
- Mega Sri Shyam - mpb6512@psu.edu
- Raghavendra Jagirdar - rvj5301@psu.edu

## Steps to reproduce results: [CHECK THE PATH BEFORE RUNNING ANY SCRIPT]

### Create an environment on your local machine and activate it
- conda create -p venv python
- conda activate venv/

### Git pull this repository
- pip install -r requirements.txt



### Data

- The data folder contains raw_data folder. This contains the data that has been extracted from first person perspective books and articles using the OpenAI playground RAG capabilities.
- The pythonscripts folder contains the necessary scripts to convert the .txt files into .csv files.
- The pythonscripts folder also contains the necessary scripts to check for duplicity across the files and within the files.
- The notebooks foolder contains the ipynb scripts to generate the xj from the xi files.
- You must have a OpenAI API key and a Groq API key to run the notebooks. You can obtain the API keys from the corresponding websites.
- Run the notebooks to generate the .csv files. You must rename the .csv file default name manually.
- Run the tt_split.ipynb to generate the train, eval and test csvs.


### Models

- The models folder contains the necessary notebooks to run the experiments.
- Upload train, eval and test csv files to google drive along with the notebooks in the models folder.
- Run the notebooks using GPU on colab. 
- The notebooks will ask HuggingFace access token and WandB access token. You can paste your access tokens form HuggingFace and WandB websites. This will create the model cards automatically after each run.


### Visualizations

- The Visualizations folder contains the BertViz notebook used to visualize the attention mechanism in the finetuned and non finetuned models.
- Upload it to the same drive and run it on GPU.

### HuggingFace Model Cards (BERT)

- BatchSize: 32, LR: 5e-5 :- https://huggingface.co/pk248/584_test3
- BatchSize: 32, LR: 2e-5 :- https://huggingface.co/pk248/584_32_2
- BatchSize: 32, LR: 1e-5 :- https://huggingface.co/pk248/584_32_1
- BatchSize: 16, LR: 5e-5 :- https://huggingface.co/pk248/584_test1_1
- Metric Run (32, 5e-5) :- https://huggingface.co/pk248/584_test3_metrics

