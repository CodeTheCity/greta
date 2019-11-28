 Download,Parse,Store in DB, Queries



https://drive.google.com/drive/folders/18n1E2iBzcagheMBk0vGSkLnD6iBfxCvh?usp=sharing
   The data for each sensor can me additionally downloaded there


## Data Schema

3 Collections ( (1)raw , (2)correction(corrected raw) , (3)info - general info for each sensor)

As mongodb does not allow document with size >16 mb , and our document size is 12 mb for each sensor,
having a huge reading list for each sensor can cause problems, the solution for scaling is:

The (1)raw collection is composed of small documents - for each timestamp and location_id :

![](images/readings.png)


The (3)info collection is composed of small documents for each sensor: 

![](images/info.png)



The (2) correction collection to remove or change (from (1)raw to (2)) some of the sensors data that is stuck on constantly 
high humidity and unaccurate data. It has the same structure as (1).


The  sensor raw collection will be sorted in the db by their location_id and timestamp.

![](images/schema.png)



if you run get_data.py , keep big_dump's csv folder empty...old and parcedJson with only json files , no checking for extra files.
