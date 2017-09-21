# Set Up service type choices
service_choices = (
    ('Onetime', 'One time'),
    ('Onceaweek', 'Once a week'),
    ('EveryTwoWeeks', 'Every Two Weeks'),
    ('EveryMonth', 'Every Month'),
    ('SpringDeepCleaning', 'Spring/Deep Cleaning'),
    ('Moveinout', 'Move-in/out')
)

# Set Up choices for extra service
extra_service_choices = (
    ('1', 'Clean Oven ($30)'),
    ('2', 'Clean Fridge ($30)'),
    ('3', 'Clean Interior Window ($25)'),
    ('4', 'Garage or Patio Sweep ($25)'),
)

# Set Up choices for referrer
referrer_choices = (
    ('Google Search', 'Google Search'),
    ('Flyers', 'Flyers'),
    ('Newspaper Ad', 'Newspaper Ad'),
    ('Church Ad', 'Church Ad'),
    ('Other', 'Other'),
)
# Set up choices for Number of bedrooms bathrooms
onebed1bath = "1b1b"
onebedonefivbath = "1b15b"
twobedtwofivbath = "2b15b"
twobedtwobath = "2b2b"
twobedtwofivbath = "2b25b"
threebedonebath = "3b1b"
threebedtwobath = "3b2b"
threebedtwofivbath = "3b25b"
threebedthreebath = "3b3b"
fourbedonebath = "4b1b"
fourbedonefivbath = "4b15b"
fourbedtwobath = "4b2b"
fourbedtwofivbath = "4b2.5b"
fourbedthreebath = "4b3b"
fourbedthreefivbath = "4b35b"
fourbedfourbath = "4b4b"
fourbedfourfivbath = "4b45b"
fivebedonebath = "5b1b"
fivebedonefivbath = "5b15b"
fivebedtwobath = "5b2b"
fivebedtwofivbath = "5b25b"
fivebedthreebath = "5b3b"
fivebedthreefivbath = "5b35b"
fivebedfourbath = "5b4b"
fivebedfourfivbath = "5b45b"
fivebedfivbath = "5b5b"
sixandup = "6up"

house_choices = (
        (onebed1bath, "1 bedroom 1 bathroom"),
        (onebedonefivbath , "1 bedroom 1.5 bathroom"),
        (twobedtwofivbath , "2 bedrooms 1 bathroom"),
        (twobedtwobath , "2 bedrooms two bathrooms"),
        (twobedtwofivbath , "2 bedrooms 2.5 bathrooms"),
        (threebedonebath , "3 bedrooms 1 bathroom"),
        (threebedtwobath , "3 bedrooms 2 bathrooms"),
        (threebedtwofivbath , "3 bedrooms 2.5 bathrooms"),
        (threebedthreebath , "3 bedrooms 3 bathrooms"),
        (fourbedonebath , "4 bedrooms 1 bathroom"),
        (fourbedonefivbath , "4 bedrooms 1.5 bathrooms"),
        (fourbedtwobath , "4 bedrooms 2 bathrooms"),
        (fourbedtwofivbath , "4 bedrooms 2.5 bathrooms"),
        (fourbedthreebath , "4 bedrooms 3 bathrooms"),
        (fourbedthreefivbath , "4 bedrooms 3.5 bathrooms"),
        (fourbedfourbath , "4 bedrooms 4 bathrooms"),
        (fourbedfourfivbath , "4 bedrooms 4.5 bathrooms"),
        (fivebedonebath , "5 bedrooms 1 bathroom"),
        (fivebedonefivbath , "5 bedrooms 1.5 bathroom"),
        (fivebedtwobath , "5 bedrooms 2 bathrooms"),
        (fivebedtwofivbath , "5 bedrooms 2.5 bathrooms"),
        (fivebedthreebath , "5 bedrooms 3 bathrooms"),
        (fivebedthreefivbath , "5 bedrooms 3.5 bathrooms"),
        (fivebedfourbath , "5 bedrooms 4 bathrooms"),
        (fivebedfourfivbath , "5 bedrooms 4.5 bathrooms"),
        (fivebedfivbath , "5 bedrooms 5 bathrooms"),
        (sixandup , "More than 6 bedorooms"),
)

# Set Up Square Footage Choices
square_footage_choices = (('Under 1000', 'Under 1000'),
    ('1001to1500', '1001 to 1500'),
    ('1501to2000', '1501 to 2000'),
    ('2001to2500', '2001 to 2500'),
    ('2501to3000', '2501 to 3000'),
    ('3001to3500', '3001 to 3500'),
    ('3501to4000', '3501 to 4000'),
    ('4001to4500', '4001 to 4500'),
    ('4501to5000', '5001 to 5000'),
    ('Morethan5001', 'More than 5001'),
)

# Set up choices for State
state_choices = (
    ('FL', 'FL'),
)
