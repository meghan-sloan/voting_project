import pandas as pd
import us #Python library for state data

#create a state dictionary from us state data
state_dict = us.states.mapping('fips', 'abbr')
#reverse the dictionary so the abbreviations are the key
rev_state_dict = {v: k for k, v in state_dict.items()}


def new_code(x):
    '''
    Returns the 3-digit state code
    '''
    return '{0:0=3d}'.format(int(rev_state_dict[x]))

def precinct_code(x):
    return '{0:0=3d}'.format(int(x.split('-')[-1]))
    '''
    Returns only the 3-digits of the precinct code, omitting the state abbreviation
    '''

def get_precinct_address(x, precinct_dict, column):
    try:
        return precinct_dict[x][column]
    except KeyError:
        return 'NOT AVAILABLE'

def mk_polling_dict(df):
    '''
    Formats the polling data frames so the precinct ID is the same format
    as the addresses.csv precinct ID.
    Creates a dictionary of the polling location data using the precinct ID as the key
    '''
    # Create a new column with just the state
    df['state'] = df['State/ZIP'].apply(lambda x: x.split()[0])
    # Create a new column with just the zip
    df['zip'] = df['State/ZIP'].apply(lambda x: x.split()[-1])
    # Turn the state abbreviation into a 3 digit code
    df['state_code'] = df['state'].apply(lambda x: new_code(x))
    # Get the second half of the precinct code and ensure it is 3 digits
    df['precinct_code'] = df['Precinct'].apply(lambda x: precinct_code(x))
    # Combine the state and precinct codes
    df['new_code'] = df['state_code']+'-'+df['precinct_code']
    # Turn the polling dataframe into a dictionary
    new_polling = df.set_index('new_code')
    precinct_dict = new_polling.to_dict('index')
    return precinct_dict


if __name__ == '__main__':
    #Create dataframes for the csvs
    df_address = pd.read_csv('/Users/meghan/DemocracyWorks/data/addresses_fixed.csv', delimiter=';')
    df_polling = pd.read_csv('/Users/meghan/DemocracyWorks/data/precinct_polling_fixed.csv', delimiter=';')

    # Create a dictionary of precint polling data
    precinct_dict = mk_polling_dict(df_polling)

    # Add the polling address to the address dataframe
    df_address['polling_street'] = df_address['Precinct ID'].apply(lambda x: get_precinct_address(x, precinct_dict, 'Street'))
    df_address['polling_city'] = df_address['Precinct ID'].apply(lambda x: get_precinct_address(x, precinct_dict, 'City'))
    df_address['polling_zip'] = df_address['Precinct ID'].apply(lambda x: get_precinct_address(x, precinct_dict, 'zip'))
    df_address['precinct_code'] = df_address['Precinct ID'].apply(lambda x: get_precinct_address(x, precinct_dict, 'precinct_code'))

    # Save to a csv
    df_address.to_csv('/Users/meghan/DemocracyWorks/combined.csv')
