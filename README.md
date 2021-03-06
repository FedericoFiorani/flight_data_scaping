## How reliable is your flight?
_Based on worldwide flight cancellation statistics, which airlines and flight routes are most often affected by cancelled flights? Is there an identifiable pattern in the collected data, with which it's possible to forecast this unfortunate event?_ 

[Flight_data](https://uk.flightaware.com/live/cancelled/)

## Running instructions
- Credentials
- Instructions
- Tools

## Grading
Documentation (60% of the final grade)
Source code for the data collection (30% of the final grade)
Overall quality of the data package (10% of the final grade)

## Documentation

Tips for filling in the documentation
- Try to answer all questions to the best of your ability.
- Imagine you would have to work with this data in the future – how would you write up the documentation so that you (and your future self) may understand it?
- In your writing, be as concise as possible. We’ve had some recent experience using tools like Grammarly to improve our writing (there is a free version available), but there are certainly alternatives available!
- The original paper on which the readme template is based on provides a few helpful (filled in) examples that may provide some inspiration.
- If you are familiar with R, you can write your documentation in RMarkdown, which nicely intertwines answers to the questions (e.g., conceptual answers) with details/statistics from the data (i.e., by including code snippets that directly generate overview tables).
- Please pick a good name for your dataset. This name will be the first thing potential users of your data will see. Use it as the title of your documentation (don’t call your dataset “Datasheets for Datasets”!)
- Please skip sections 6 and 7 of the documentation (distribution and maintenance). Do get rid of the example text in these sections though.

## 1.           	Motivation

Motivation (section 1 of your documentation, 10%)
From your answers to all questions in section 1 of the documentation template, the following points need to be addressed:

Motivation for data context (5%)
Clear explanation of the value in collecting the data (“task in mind”), either in the context of a specific research question or business problem. The data collection potentially generates insights into new phenomena. There is clearly value to the larger research community in using the data. Comparable data sets are not available at all, or not publicly available.

Motivation for choice of website/API (5%)
A range of relevant websites and APIs pertaining to the data context is assessed in terms of data availability, research fit & resource use. It is clear why the data was ultimately collected from the focal website/API, and not from others (i.e., the website/API emerges as the one that fits best in terms of research fit and resource use; #1.4).

## 1.1   	For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.

Because of the pandemic, people have significatively changed their flying habits. Flights are being purchased in the proximity of the departure date as is not easy to make long term plans anymore. From the airline perspective, this led to increasing difficulties in managing the flight traffic. This has resulted in a rise in the flight cancellation rate in all the international airports and for all the best-renowned airline companies. The data regarding this problem are not accessible to users or, if published, are only referring to the past 2 days. Our mission is to collect infoprmation regarding cancelled flights in all the airport every day until the creation of a large and very precious dataset. We think that through the observation of historical data regarding this phenomenon, we will be able to provide a useful resource to the public.
 
## 1.2   	Who created this dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?

FlightAware is a digital aviation company and operates the world's largest flight tracking and data platform. With global connectivity to every segment of aviation, FlightAware provides over 10,000 aircraft operators and service providers as well as over 13,000,000 passengers with global flight tracking solutions, predictive technology, analytics, and decision-making tools.
 
## 1.3   	Who funded the creation of the dataset? If there is an associated grant, please provide the name of the grantor and the grant name and number.
 
FlightAware receives data from air traffic control systems in over 45 countries, FlightAware's network of ADS-B ground stations in 195 countries, Aireon global space-based ADS-B, and datalink (satellite/VHF) via every major provider, including ARINC, SITA, Satcom Direct, Garmin, and Honeywell GoDirect. There is no extra funding. 


## 2.           	Composition

Composition (section 2 of your documentation, 20%)
From your answers to all questions in section 2 of the documentation template, the following points need to be addressed:

Entities, linkages, timeframe and algorithmic biases (5%)
The composition of the data is described in detail and accessible to novel users of the data. Potential users learn about which entities are available in the data set, for what time period, and how they are linked to each other. Potential linkages to external data sets are made explicit (e.g., by means of links to external websites or sources that explain more about the used identifiers). Potential algorithmic biases have been identified and clearly explained.

Sampling, construct measurement and data structure (5%)
For each entity, it is explained how the data was sampled, and how variables are measured. Details are given how the data is available (e.g., by means of CSV files per entity, as a combined data set, etc.).

Data inspection per entity (10%)
Each set of entities is accompanied by meaningful summary statistics (e.g., the number of units per entity, means/SD for continuous variables, and frequency distributions per variable, for each entity). Missingness has been investigated (e.g., for individual entities, but also for the collected variables). Any redundancies, errors, or sources of noise have been clearly described. Identified subpopulations are labeled, so that users of the data can more easily get started using the data.


## 2.1   	What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)? Are there multiple types of in- stances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? Please provide a description.

The instances that comprise the dataset represent cancelled flights. There are multiple types, namely the airline in charge of the cancelled flight and the origin airport of the cancelled flight.  
 
## 2.2   	How many instances are there in total (of each type, if appropriate)?

The number of instances are the same for both the airline and the origin airport. The number of instances changes each day and it depends on the number of flight cancellations. There are also unknown airlines in the data, but the scraper does not take them into consideration. The approximately 200 airlines that are listed in the code are analyzed. 
 
## 2.3   	Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g., geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).
 
The dataset contains all possible instances. With between 1500 and 2000 cancelled flights each day, the scraper can run them in about 30 minutes. This means the scraper does not overload the computer. A sampling run has also been done, to see if the code was running smoothly, where only one page per airline was collected. The code for this can be found in the script. 
 
## 2.4   	What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or features? In either case, please provide a de- scription.
 
Each instance consists of text. The text provides the name of the airline and the name of the origin airport, which makes it possible to analyze also geographically. 

## 2.5   	Is there a label or target associated with each instance? If so, please provide a description.
 
The label that is associate with each instance are the 200 airlines that are analyzed. The target is the origin airport that is specific for each flight. 
 
## 2.6   	Is any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include, e.g., redacted text.
 
There are a few unknown airlines with cancelled flights each day, which means this data is missing for the instances. Also, for these unknown airlines, there is no association with an origin airport, which makes it hard to use this data. They usually account for only 1 cancelled flight per airline each day, which is less than 2%. These airlines are not categorized, so the focus is on the remaining 200 known airlines. 
 
## 2.7   	Are relationships between individual instances made explicit (e.g., users’ movie ratings, social network links)? If so, please describe how these relationships are made explicit.
 
The relationship between the name of the airline and the origin airport is made explicit in each case. The origin instances are organizes into the airline instances, like a subcategory. This is also the way the website is structured, so the extraction process makes these explicit relationships easy to maintain. 
 
## 2.8   	Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them.

No, there are not any recommended data splits. All the collected data is pulled together in a single csv-file. 
 
## 2.9   	Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? If it links to or relies on external resources, a) are there guarantees that they will exist, and remain constant, over time; b) are there official archival versions of the complete dataset (i.e., including the external resources as they ex- isted at the time the dataset was created); c) are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a future user? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate.
 
The dataset relies on the number of flights cancelled all over the world and the website FlightAware.com collects the information on these flights. 
Data on flights cancelled everyday will be available, but there are no guarantees that FlightAware.com runs 24 hours a day without crashing. The code scrapes data from the previous day, so unless the website stops working for more than 24 hours, the data can be collected. The structure of the website could change and this requires an update of the code. The data of the website is historically available up to one day before. In this way, a historical data set is created based on everyday scraping, so predictions can be made. There are no restrictions to get access to the data, such as purchase licencees to scrape the website. The data is easily accessible using the "selenium" package. There is no guarantee this will not change in the future. 

The link to the website of cancelled flights: https://uk.flightaware.com/live/cancelled
The link to the website of cancelled flights, one day before: https://uk.flightaware.com/live/cancelled/yesterday
An example of the website that shows the cancelled flights of a certain airline, in this case China Airlines: https://uk.flightaware.com/live/fleet/CCA/cancelled


## 2.10  	Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctorpatient confidentiality, data that includes the content of individuals non-public communications)? If so, please provide a description.
 
The data on cancelled flights is public information. The data is easily available on the internet. FlightAware.com only collects and summarizes this data. 
 
## 2.11  	Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why.
 
The dataset might cause anxiety for passengers who travel a lot by air. The goal of the website, however, is to provide information for people who need data on cancelled flights to for example estimate the risk of cancellation for a flight they are planning.
 
## 2.12  	Does the dataset relate to people? If not, you may skip the remaining questions in this section.
 
The data contains solely about flights. 
 
 
## 3.           	Collection Process

Collection process (section 3 of your documentation, 15%)
From your answers to all questions in section 3 of the documentation template, the following points need to be addressed:

Technical extraction plan (10%)
The technical extraction plan has been described in a way that the data collection could be replicated. This encompasses providing a solid argumentation on why a particular data extraction technology used (e.g., selenium versus Beautifulsoup for websites, a package versus self-coded requests for APIs). It is clear how entities were sampled from the site, and how the navigation scheme was implemented. In particular, users of the data learn about the technical hurdles that needed to be overcome, and which monitoring was in place to guarantee (and validate) data quality. Finally, details are given on how (deployment infrastructure) and when the data collection was executed (e.g., by meaningful summaries of the timestamps in log files), and where the final data set was stored during the collection.

Legal and ethical concerns (5%) For #3.6, the potential legal and/or ethical concerns that may be relevant for the collected data are carefully described.

## 3.1   	How was the data associated with each instance acquired? Was the data directly observable (e.g., raw text, movie ratings), reported by sub- jects (e.g., survey responses), or indirectly inferred/derived from other data (e.g., part-of-speech tags, model-based guesses for age or language)? If data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified? If so, please describe how.
 
The instances were collected beforehand by creating a list of all the airlines displayed on the website. The name of the airlines was used to spot their links to all the cancelled flights for each airline. A "for loop" was used over all the airlines. All the pages with flights were accessed by clicking on "Next 20" on each specific page. The airlines' names are directly observable on the main page, whereas specific flight data is scrapable from specific links for each airline. All the data is scraped in textual form from FlightAware.com. The calculations that can be done are based on the datasets of the scraped data, validated by the source FlightAware.com.
 
## 3.2   	What mechanisms or procedures were used to collect the data (e.g., hardware apparatus or sensor, manual human curation, software pro- gram, software API)? How were these mechanisms or procedures validated?
 
The data is collected with webscraping via python, which means that the data is directly scraped from the website, making use of html scripts and tags. The procedures have been validated by checking the correspondence of the data in the scraped dataset with the data present on the website in html form. 
 
## 3.3   	If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?
 
Initially, a deterministic sampling was used. This means data was collected only from the first page of each airline to understand whether the code was correctly retreiving data from the website. 
 
## 3.4   	Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?
 
The team working on the webscraping project is composed by five students following the Online Data Collection and Management (oDCM) course at Tilburg University, with the support of the professor of this course. The work is aimed at practicing aqcuired knowledge, thus no financial compensation was used. 
 
## 3.5   	Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)? If not, please describe the time- frame in which the data associated with the instances was created.
 
The data has been collected since the 13th of October. With the use of Task Scheduler, the data will be collected daily for an indefinite period of time. 
 
## 3.6   	Were any ethical review processes conducted (e.g., by an institutional review board)? If so, please provide a description of these review processes, including the outcomes, as well as a link or other access point to any supporting documentation.
 
No review processes were done by external agents. 

 
## 4.           	Preprocessing, cleaning, labeling

Preprocessing (section 4 of your documentation, 10%)
From your answers to all questions in section 4 of the documentation template, the following points need to be addressed:

Preprocessing (5%)
Any pre-processing on the fly has been motivated and explained, using a few specific examples. Any further pre-processing after the collection has been described (e.g., such as to anonymize users for privacy concerns, to identify and clean out implausible observations, or to improve data structure for long-term storage, such as rearranging the data structure, relabeling columns into more meaningful and clear variable names).

Accessibility and structure of final data files (5%)
The files have a correct data structure, and variables are of the correct type (e.g., numbers as integers or floats, not as strings; time stamps properly formatted, or Unixtime used). Application of data enrichment and feature engineering strategies (e.g., to derive new variables from the data, where necessary). Data has been normalized (i.e., preferably multiple tables that can be joined together, rather than a wide table that contains many duplicates on some of the variables). If imputation is used, it is indicated which values have been imputed (e.g., interpolated; for example: followers (without missing), and followers_inputed as a TRUE/FALSE variable, indicating which ones were imputed). Finally, the data set is provided in CSV files, including column names, proper use of delimiters (e.g., a “,” may be inappropriate for textual data involving commas). No row names/index column.


## 4.1   	Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remain- der of the questions in this section.
 
The program R was used to clean the dataset, where missing values were deleted. 

## 4.2   	Was the “raw” data saved in addition to the prepro- cessed/cleaned/labeled data (e.g., to support unanticipated future uses)? If so, please provide a link or other access point to the “raw” data.
 
Link to raw data: ... 
 
## 4.3   	Is the software used to preprocess/clean/label the instances available? If so, please provide a link or other access point.
 
The software that was used to clean the data is R, which is publicly available. 
- [R](https://cran.r-project.org/) 


## 5.           	Uses

Uses (section 5 of your documentation, 5%)
From your answers to all questions in section 5 of the documentation template, the following points need to be addressed:

Users of the data learn about tasks the data set could be used for (5%)
From the description, it is clear how the composition of the data set or the way it was preprocessed might affect future use. A clear indication is given for what the data should not be used for, e.g., relating to any of the legal or ethical concerns identified before.

## 5.1   	Has the dataset been used for any tasks already? If so, please provide a description.
 
The dataset has not been used for any tasks yet. 
 
## 5.2   	Is there a repository that links to any or all papers or systems that use the dataset? If so, please provide a link or other access point.

- 
 
## 5.3   	What (other) tasks could the dataset be used for?

Some examples of tasks that can be done with the dataset are: 
- Analyze which airlines are most likely to have their flights cancelled
- Analyze which origin airports are most likely to cancel flights
- Predictions for passengers about the likelihood of the cancellation of their future flight
 
## 5.4   	Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses? For example, is there anything that a future user might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g., stereotyping, quality of service issues) or other undesirable harms (e.g., financial harms, legal risks) If so, please provide a description. Is there anything a future user could do to mitigate these undesirable harms?
 
There are approximately 100 airlines analyzed, which creates a possibility that the dataset that was created is not 100% complete. There may be some missing airlines, however, the largest ones of the world are all included. 
 
## 5.5   	Are there tasks for which the dataset should not be used? If so, please provide a description.
 
The dataset should not be used as a sole method of choosing between potential airlines for a passenger while purchasing flight tickets. It should only be one factor, and the passenger should consider other factors as well, like ticket prices, service on the flight, flight time, etc. 


 
 ## Source Code for the Data Collection
 
Quality of the submitted source code (15%)

- Present and clearly readable (e.g., variable names that are meaningful)
- Inline markdown formatting (e.g., headers, dividers, paragraphs, etc.)
- Well-structured and modular source code (e.g., use of functions)
- Adhere to DRY principles (e.g., for-loops and functions)
- Concise code (e.g., list and dictionary comprehensions)
- With comments and docstrings
- Code blocks run in a linear fashion (i.e., top to bottom execution runs without issues); removal of unnecessary source code and packages that are not needed
- File paths are specified relative to the current script, no absolute paths used
- Error-handling incorporated (e.g., does the scraper still run if the API or website changes?)
- Quality of the technical implementation (15%)

The quality of the technical implementation is judged for web scraping and APIs, as per some of the following dimensions.

Web scraping

- A single vs. multiple entities / web pages
- Degree of complexity required to obtain data (e.g., static websites with a fixed class name vs social media which requires more dynamic approaches such as clicking on buttons and navigating across pages; self-coded extraction code versus use of a package which extracts data automatically)
- Stability of the solution (i.e., navigation path should not be subjective to day-to-day page changes). Can the code be run after submission? Can the code be run on Windows, Mac and Linux?
- Obeying retrieval limits (usage of timers to avoid overloading the server and getting blocked and writing efficient code; create a single BeautifulSoup object per page; avoid making redundant requests)
- Uniqueness (e.g., a combination of data collected through an API and web scraping)

 ## Data Package
Quality of the data package (10%)
- Submitted as a zip file
- Accessible and appropriate directory structure
- No unnecessary files
- Inclusion of meaningful supportive files (e.g., API documentation, screenshots, a video of the scraper in action)
- Raw data files all present
- Documentation properly formatted and no template text (“lorem ips…") remaining



Members: [Federico Fiorani](https://github.com/FedericoFiorani), [Lorenzo Taddei](https://github.com/lorenzotaddei), [Marton Tomka](https://github.com/martontomka11), [Sabine Abrahamse](https://github.com/sabineabra), [Kevin 't Jong](https://github.com/kevintjong)


