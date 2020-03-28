# Bar Project

## Overview

This project involves a "bar" app that considers several things explained below.

A Python app was created using the Django framework, and a default SQLite database.

The Models created are "Counter", "Beer" and another Model that acts as a Many-To-Many relationship between these two.

## Functionalities

The "bar" app consists of an API, with the following functionalities.

### /bar/counters

It renders a web page showing the list of counters of the bar, and when a click is made over any of the items, the availability of every kind of beer on that counter is showed.

### /bar/beers

It renders a web page showing the list of beers, and when a click is made over any of the items, the availability of the selected beer on every counter is showed.

## Considerations

These two web pages perform AJAX calls to /bar/get_beers and /bar/get_counters respectively, to retrieve the information needed about these items, performing the requiered queries over the objects stored on the database.

There is redundancy of code between these two parts of the application, so they could be unified to make it more general.

An admin web page is enabled, that can be accessed through "/admin" just using the credentials "admin" for user, and "admin" for password. Operations over the Model can be performed on this Module.

The "db.sqlite3" is created and filled with some sample data defined on a file called "fill_data.py", following the Models defined as explained above.

The goal of this approach is to show the relationships between Models, Views, and how to move over the different entities of the framework to render web pages with logic, being able to retrieve information via AJAX calls to the defined URLs.
