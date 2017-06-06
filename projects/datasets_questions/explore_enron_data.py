#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


#How many data points (people) are in the dataset?
print len(enron_data)

#For each person, how many features are available?
print len(enron_data[enron_data.keys()[0]])

# The “poi” feature records whether the person is a person of interest, according to our definition. How many POIs are there in the E+F dataset?
print sum( [x['poi'] for x in enron_data.values()] )

#What is the total value of the stock belonging to James Prentice?
print enron_data['PRENTICE JAMES']['total_stock_value']

#How many email messages do we have from Wesley Colwell to persons of interest?
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

#What’s the value of stock options exercised by Jeffrey K Skilling?
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']

# Of Lay, Skilling and Fastow, Who took home the most money? How much money was it?
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']

#How many folks in this dataset have a quantified salary? What about a known email address?
print len(enron_data) - sum( [x['salary'] == 'NaN' for x in enron_data.values()] )
print len(enron_data) - sum( [x['email_address'] == 'NaN' for x in enron_data.values()] )

#How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? What percentage of people in the dataset as a whole is this?
print sum( [x['total_payments'] == 'NaN' for x in enron_data.values()] )
print sum( [x['total_payments'] == 'NaN' for x in enron_data.values()] )/(len(enron_data)*1.0) * 100

# How many POIs in the E+F dataset have “NaN” for their total payments? What percentage of POI’s as a whole is this?
print sum( [x['total_payments'] == 'NaN' and x['poi'] for x in enron_data.values()] )
print sum( [x['total_payments'] == 'NaN' and x['poi'] for x in enron_data.values()] )/ (sum( [x['poi'] for x in enron_data.values()] ) * 1.0) * 100


"""
Adding in the new POI’s in this example, none of whom we have financial information for, has introduced a subtle problem, that our lack of financial information about them can be picked up by an algorithm as a clue that they’re POIs. 
Another way to think about this is that there’s now a difference in how we generated the data for our two classes--non-POIs all come from the financial spreadsheet, while many POIs get added in by hand afterwards. 
That difference can trick us into thinking we have better performance than we do--suppose you use your POI detector to decide whether a new, unseen person is a POI, and that person isn’t on the spreadsheet. 
Then all their financial data would contain “NaN” but the person is very likely not a POI (there are many more non-POIs than POIs in the world, and even at Enron)--you’d be likely to accidentally identify them as a POI, though!

This goes to say that, when generating or augmenting a dataset, you should be exceptionally careful if your data are coming from different sources for different classes. 
It can easily lead to the type of bias or mistake that we showed here. There are ways to deal with this, for example, you wouldn’t have to worry about this problem if you used only email data--in that case, discrepancies in the financial data wouldn’t matter because financial features aren’t being used. 
There are also more sophisticated ways of estimating how much of an effect these biases can have on your final answer; those are beyond the scope of this course.

For now, the takeaway message is to be very careful about introducing features that come from different sources depending on the class! It’s a classic way to accidentally introduce biases and mistakes.
"""