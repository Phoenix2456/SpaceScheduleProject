# main.py

import dockingBays as db

# Function to print docking bays information
def print_docking_bays():
    print("Docking Bays:")
    for bay in db.docking_bays:
        print(f"Bay {bay['bay_id']} - Size: {bay['size']}, Schedule: {bay['schedule']}")

# Function to print incoming ships information
def print_incoming_ships():
    print("\nIncoming Ships:")
    for ship in db.incoming_ships:
        print(f"Ship {ship['ship_name']} - Size: {ship['size']}, Arrival: {ship['arrival_time']}, Departure: {ship['departure_time']}")

# Main function
def main():
    print_docking_bays()
    print_incoming_ships()
    

    # Level 1
    # Creat a for loop for each dictionary list in docking_bays and incoming_ships
    
    for bay in db.docking_bays:
        for ship in db.incoming_ships:
            # if size from bay equals to size of ship, print true or false
            if bay['size'] == ship['size']: 
                return True
            return False
                # Extra try
                # print(f"Bay {bay['bay_id']}: {ship['ship_name']} - Size: {bay['size']}")


    # Level 2
    for bay in db.docking_bays:
        for ship in db.incoming_ships:
            if ship['arrival_time'] == bay['schedule']:
                return True
            return False
                # print(f"Ship: {ship['ship_name']}; Arrival: {ship['arrival_time']} - Depart: {ship['departure_time']}")
    # Level 3
    for bay in db.docking_bays:
        for ship in db.incoming_ships:
            print(f"Ship: {ship['ship_name']}; Arrival: {ship['arrival_time']} - Depart: {ship['departure_time']}")



    # TODO: Implement the docking scheduler logic here
    # Levels 1 to 4 and the bonus can be implemented below

if __name__ == "__main__":
    main()
