# Proposal Bhumi

## Section 1: Motivation and Purpose

|                    |                                                                       |
|--------------------|-----------------------------------------------------------------------|
| Who am I           | Geospatial Datascientist and Bhumi Volunteer                 |
| Our goal           | To help Bhumi in getting new volunteers and new centers               |
| Target Audience    | Shelter homes and Individuals                                         |
| Secondary Audience | People interested in donating for a cause to support Bhumi's mission  |

Though Bhumi is one of the largest volunteering organisations in India, when they approach new shelter homes to explain what they are doing, what they have achieved, what is their strength and how they have been doing, they need a tool to showcase their capabilities. They conduct orientation session to individuals to register themselves as volunteers. Bhumi people need to explain to individuals about the location of the centers in the city, number of the kids in the center and the existing number of volunteers in that particular shelter home and the number of volunteers they are in need of. Is there an application, where we can access alll these information about Bhumi to approach Shelter homes and prospective volunteers? This is the question that our application `Bhumi` aims to address.

### User Persona

##### Persona 1
Sriram is a 20-year old student and is interested in volunteering in Bhumi in one of the shelter home in Chennai, India. He would like to volunteer for the center which is in dire need of volunteer and is also near to his place where he resides. Further, though Bhumi has been teaching various subjects to the kids, he has specific favourite subject mathematics that he wants to teach to the kids. With these conditions in mind, he can use the application Bhumi to see the location of all the centers where Bhumi is involved to identify the nearest one to his residence. He can also compare the children available and the volunteer available for each center which will make him understand which center is in immediate need of volunteers. Sriram can use application `Bhumi` in order to make a choice that matches his conditions. Through the `Bhumi` application, Sriram will be able to interactively select those centers teaching Maths in Chennai and compare distance, volunteer count and children count in those center to take decision for the volunteering in that particular center.

##### Persona 2 

Mabu is a head of the shelter home and has been hearing a lot about the Bhumi which has been sending their volunteers to educate the children in shelter homes. Before approaching Bhumi he would like to understand where are the centers which are being benefitted by Bhumi located and the number of kids in those center. Also, the number of volunteers that are taking classes in every center. He would like to know the subjects that are taught by Bhumi Volunteers in other centers and if kids in his center would require assistance for those subjects such as computer science.  He would like to understand the overall performance of the Bhumi in India, so that he can approach his management to make them understand the performance of Bhumi and how the kids in his center will be benefitted if Bhumi Volunteers educate the kids in his center.

The data on which the application `Bhumi` is based on India with specific as a reference point, therefore, the target market for our application is any individual living in those cities and Shelter homes located in those cities. The `Bhumi` will guide them in making a more informed decision about the center they wish to volunteer.

### Usage

Any individual who would like to spend his/her free time for volunteering to educate the under priviliged kids will be able to find the necessary information to comparing the different centers accross the city and the studetns/volunteers available. Indeed, they can select any city from the list of cities to view the center details displayed through the aid of a map as well as a bar plot.


## Section 2: Description of the data

We will visualize the center wise dataset, which contains information on the centers across the cities in India. `Children Available`, `Volunteer Count` and `Subjects taught` are the three primary indices included in the dataset. 

The main focus of our dashboard will be the `Volunteer Count` and `Children Available`. This will help in understanding the volunteer student ratio, which is important in Bhumi for successful completion of Bhumi's mission. Whenever Bhumi takes up new center it makes sure the volunteer to student ratio is 1:3 so that the three kids will get quality education from that one volunteer they have been alloted. This way the bonding between the volunteer and kids will also increaase and at the same time kids will also receive quality education.

Apart from the major indices, we also conducted data preprocessing to obtain the center's geolocational features, including `latitude`, and `longitude`, which will allow us to visualize the data on a map.

For our dashboard, we plan to visualize all five aforementioned indices by country and continent. We will allow the user to filter by city and to see the center wise details in that city. 

## Section 3: Research questions and usage scenarios

Through our application, students in the shoes of our fictional character Sriram will be able to answer the following questions:

- Which are the Cities that are benefitted by Bhumi?

- Which Center is in need of volunteers?

- What are the subjects taught in each center ?

- How many kids are benefitted by the program?

