# Stylelure: The Online Fashion Store

Stylelure is a virtual store on the Internet where customers can browse the catalog and select products of interest. The selected items may be collected in a shopping cart. At checkout time, the items in the shopping cart will be presented as an order. At that time, more information will be needed to complete the transaction.

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-1.11-brightgreen.svg)](https://djangoproject.com)




# Abstract

In the emerging global economy, electronic-commerce has increasingly become a necessary component of business strategy and a strong catalyst for economic development. The integration of information and communications technology in business has revolutionized relationships within organizations and those between and among organizations and individuals. Specifically, the use of the internet in business has enhanced productivity, encouraged greater customer participation, and enabled mass customization, besides reducing costs. E-commerce creates new opportunities for performing profitable activities online. It promotes easier cooperation between different groups: businesses sharing information to improve customer relations companies working together to design and build new products/services or multinational companies sharing information for a major marketing campaign. 


# Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/imadarsh1001/stylelure.git
```  

Install the requirements:

```bash
pip install -r requirements.txt --user
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [MIT License](LICENCE).

