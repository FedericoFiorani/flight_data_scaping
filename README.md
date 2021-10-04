## How reliable is your flight?
_Based on worldwide flight cancellation statistics, which airlines and flight routes are most often affected by cancelled flights? Is there an identifiable pattern in the collected data, with which it's possible to forecast this unfortunate event?_ 

[Flight_data](https://uk.flightaware.com/live/cancelled/)

## Running instructions
-credentials required
-packages required
-tools required

## Grading
Documentation (60% of the final grade)
Source code for the data collection (30% of the final grade)
Overall quality of the data package (10% of the final grade)

## Documentation

1.           	Motivation
1.1   	For what purpose was the dataset created? Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.

...
 
1.2   	Who created this dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?

...
 
1.3   	Who funded the creation of the dataset? If there is an associated grant, please provide the name of the grantor and the grant name and number.
 
...


2.           	Composition
2.1   	What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)? Are there multiple types of in- stances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? Please provide a description.

...
 
2.2   	How many instances are there in total (of each type, if appropriate)?

...
 
2.3   	Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set? If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g., geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).
 
...
 
2.4   	What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or features? In either case, please provide a de- scription.
 
...

2.5   	Is there a label or target associated with each instance? If so, please provide a description.
 
...
 
2.6   	Is any information missing from individual instances? If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include, e.g., redacted text.
 
...
 
2.7   	Are relationships between individual instances made explicit (e.g., users’ movie ratings, social network links)? If so, please describe how these relationships are made explicit.
 
...
 
2.8   	Are there recommended data splits (e.g., training, development/validation, testing)? If so, please provide a description of these splits, explaining the rationale behind them.
 
...
 
2.9   	Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)? If it links to or relies on external resources, a) are there guarantees that they will exist, and remain constant, over time; b) are there official archival versions of the complete dataset (i.e., including the external resources as they ex- isted at the time the dataset was created); c) are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a future user? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate.
 
...

2.10  	Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctorpatient confidentiality, data that includes the content of individuals non-public communications)? If so, please provide a description.
 
....
 
2.11  	Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety? If so, please describe why.
 
...
 
2.12  	Does the dataset relate to people? If not, you may skip the remaining questions in this section.
 
...
 
2.13 Does the dataset identify any subpopulations (e.g., by age, gender)? If so, please describe how these subpopulations are identified and provide a description of their respective distributions within the dataset.
 
...
 
2.14 Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset? If so, please describe how.
 
...
 
 
2.15  	Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)? If so, please provide a description.
 
...
 
 
3.           	Collection Process
3.1   	How was the data associated with each instance acquired? Was the data directly observable (e.g., raw text, movie ratings), reported by sub- jects (e.g., survey responses), or indirectly inferred/derived from other data (e.g., part-of-speech tags, model-based guesses for age or language)? If data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified? If so, please describe how.
 
...
 
3.2   	What mechanisms or procedures were used to collect the data (e.g., hardware apparatus or sensor, manual human curation, software pro- gram, software API)? How were these mechanisms or procedures validated?
 
...
 
3.3   	If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?
 
...
 
3.4   	Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?
 
...
 
3.5   	Over what timeframe was the data collected? Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)? If not, please describe the time- frame in which the data associated with the instances was created.
 
...
 
3.6   	Were any ethical review processes conducted (e.g., by an institutional review board)? If so, please provide a description of these review processes, including the outcomes, as well as a link or other access point to any supporting documentation.
 
...
 
3.7   	Does the dataset relate to people? If not, you may skip the remaining questions in this section.
 
...
 
3.8   	Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g., websites)?
 
...
 
3.9   	Were the individuals in question notified about the data collection? If so, please describe (or show with screenshots or other information) how notice was provided, and provide a link or other access point to, or other- wise reproduce, the exact language of the notification itself.
 
...
 
3.10  	Did the individuals in question consent to the collection and use of their data? If so, please describe (or show with screenshots or other information) how consent was requested and provided, and provide a link or other access point to, or otherwise reproduce, the exact language to which the individuals consented.
 
...
 
 
3.11  	If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or for certain uses? If so, please provide a description, as well as a link or other access point to the mechanism (if appropriate).
 
...
 
3.12  	Has an analysis of the potential impact of the dataset and its use on data subjects (e.g., a data protection impact analysis) been conducted? If so, please provide a description of this analysis, including the outcomes, as well as a link or other access point to any supporting documentation.
 
...

 
4.           	Preprocessing, cleaning, labeling
4.1   	Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)? If so, please provide a description. If not, you may skip the remain- der of the questions in this section.
 
...
 
4.2   	Was the “raw” data saved in addition to the prepro- cessed/cleaned/labeled data (e.g., to support unanticipated future uses)? If so, please provide a link or other access point to the “raw” data.
 
...
 
4.3   	Is the software used to preprocess/clean/label the instances available? If so, please provide a link or other access point.
 
...


5.           	Uses
5.1   	Has the dataset been used for any tasks already? If so, please provide a description.
 
...
 
5.2   	Is there a repository that links to any or all papers or systems that use the dataset? If so, please provide a link or other access point.
 
...
 
5.3   	What (other) tasks could the dataset be used for?
 
...
 
5.4   	Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses? For example, is there anything that a future user might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g., stereotyping, quality of service issues) or other undesirable harms (e.g., financial harms, legal risks) If so, please provide a description. Is there anything a future user could do to mitigate these undesirable harms?
 
...
 
5.5   	Are there tasks for which the dataset should not be used? If so, please provide a description.
 
...
 
 
6.  	Distribution
6.1   	Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created? If so, please provide a description.
 
...
 
6.2   	How will the dataset be distributed (e.g., tarball on website, API, GitHub)? Does the dataset have a digital object identifier (DOI)?
 
....
 
6.3   	When will the dataset be distributed?
 
...
 
6.4   	Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)? If so, please describe this license and/or ToU, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated with these restrictions.
 
...
 
6.5   	Have any third parties imposed IP-based or other restrictions on the data associated with the instances? If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms, as well as any fees associated with these restrictions.
 
...
 
6.6   	Do any export controls or other regulatory restrictions apply to the dataset or to individual instances? If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any supporting documentation.
 
...

 
7.  	Maintenance
7.1   	Who will be supporting/hosting/maintaining the dataset?
 
...
 
7.2   	How can the owner/curator/manager of the dataset be contacted (e.g., email address)?
 
...
 
7.3   	Is there an erratum? If so, please provide a link or other access point.
 
...
 
7.4   	Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances)? If so, please describe how often, by whom, and how updates will be communicated to users (e.g., mailing list, GitHub)?
 
...
 
7.5   	If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were individuals in question told that their data would be retained for a fixed period of time and then deleted)? If so, please describe these limits and explain how they will be enforced.
 
...
 
7.6   	Will older versions of the dataset continue to be sup- ported/hosted/maintained? If so, please describe how. If not, please describe how its obsolescence will be communicated to users.
 
...
 
7.7   	If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so? If so, please provide a description. Will these contributions be validated/verified? If so, please describe how. If not, why not? Is there a process for communicating/distributing these contributions to other users? If so, please provide a description.
 
...




Members: [Federico Fiorani](https://github.com/FedericoFiorani), [Lorenzo Taddei](https://github.com/lorenzotaddei), [Marton Tomka](https://github.com/martontomka11), [Sabine Abrahamse](https://github.com/sabineabra), [Kevin 't Jong](https://github.com/kevintjong)


