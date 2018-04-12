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
        return '{} not available'.format(column)

if __name__ == '__main__':
    #Create dataframes for the csvs
    df_address = pd.read_csv('/Users/meghan/DemocracyWorks/data/addresses_fixed.csv', delimiter=';')
    df_polling = pd.read_csv('/Users/meghan/DemocracyWorks/data/precinct_polling_fixed.csv', delimiter=';')
    # Create a new column with just the state
    df_polling['state'] = df_polling['State/ZIP'].apply(lambda x: x.split()[0])
    # Turn the state abbreviation into a 3 digit code
    df_polling['state_code'] = df_polling['state'].apply(lambda x: new_code(x))
    # Get the second half of the precinct code and ensure it is 3 digits
    df_polling['precinct_code'] = df_polling['Precinct'].apply(lambda x: precinct_code(x))
    # Combine the state and precinct codes
    df_polling['new_code'] = df_polling['state_code']+'-'+df_polling['precinct_code']
    # Turn the polling dataframe into a dictionary
    new_polling = df_polling.set_index('new_code')
    precinct_dict = new_polling.to_dict('index')
    # Add the polling address to the address dataframe
    df_address['polling_street'] = df_address['Precinct ID'].apply(lambda x: get_precinct_address(x, precinct_dict, 'Street'))
    df_address['polling_city'] = df_address['Precinct ID'].apply(lambda x: get_precinct_address(x, precinct_dict, 'City'))
    df_address['polling_zip'] = df_address['Precinct ID'].apply(lambda x: get_precinct_address(x, precinct_dict, 'State/ZIP'))

    df_address.to_csv('/Users/meghan/DemocracyWorks/combined.csv')
