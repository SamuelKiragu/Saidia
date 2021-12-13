## SAIDIA WEB APP

Saidia makes it easy for donors to locate orphanages. Using an orphanage list and map feature, donors can easily find orphanages all over the country. To achieve this, the system users have been divided into the following user classes:   
Donor: uses Saidia to find orphanages
Orphanage Manager: uses Saidia to make their orphanage and its corresponding needs access to the donor.
### Development:
Saidia's key development tools were Django, a python framework and Google Maps API.

### Installation & Usage
#### Prerequisites
To run this project locally on your machine you need to have the following:
1. **Python and Django** installed on your computer.   
You can follow any of the procedures available online, that you see fit, to install Python and Django on your computer.
2. **Google Maps API**.   
Hope this link will be of help. https://developers.google.com/maps/documentation/javascript/get-api-key
3. **Database Engine**: Mysql, Postgresql, your choice!
4. **A Browser**. Don’t tell me you don’t have a browser

### Configuration
##### Database Configuration.
1. Change your current working directory to saidia
2. Open settings.py using the editor of your choice
3. Specify your database in the database setting.
4. Run the following commands:
> python manage.py makemigrations
> python manage.py migrate

##### Map API configuration
1. Navigate to main_layout.html
_saida_app/templates/saidia_app/main_layout.html_

2. Add script tag containing your maps API key

### Usage
Execute the following command:

    python manage.py runserver
Using your browser of choice open the following:

    127.0.0.1:8000

### Screenshots
![Login page][screenshots/saidia17.png]
![Login page][screenshots/saidia26.png]
![Login page][screenshots/saidia27.png]
![Login page][screenshots/saidia28.png]
![Login page][screenshots/saidia30.png]
![Login page][screenshots/saidia32.png]
