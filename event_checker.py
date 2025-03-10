import os

# step 1: Let user define the event name
event_name = input("🎉 WELCOME! What's the name of your event? ").strip()
filename = f"{event_name.lower().replace(' ', '_')}_guests.txt"

# step 2: Initialize the event file if it doesn't exist
if not os.path.exists(filename):
    with open(filename, "w") as file:
        print(f"✅ Event '{event_name}' created! Guest list initialized.")
else:
    print(f"📁 Found existing guest list for '{event_name}'.")  

# Step 3: Menu loop for guest management
while True:
    print("\n🔷 Menu: Choose an option")
    print("1. Add a guest")
    print("2. Remove a guest")
    print("3. View Guest List")
    print("4. Check if someone is still checked in")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    # Option 1: Add guests
    if choice == "1":
        new_guest = input("Enter guest name to check in: ").strip()
        with open(filename, "a") as file:
            file.write(new_guest + "\n")
        print(f"✅ {new_guest} has checked in!")
    
    # Option 2: Remove Guests
    elif choice == "2":
        remove_guest = input("Enter Guest name to check out: ").strip()
        temp_list = []

        with open(filename, "r") as file:
            temp_list = [line.strip() for line in file]
        if remove_guest in temp_list:
            temp_list.remove(remove_guest)
            with open(filename, "w") as file:
                for guest in temp_list:
                    file.write(guest + "\n")
            print(f"❌ {remove_guest} has been checked out")
        else:
            print(f"⚠ {remove_guest} is not in the guest list!")
    
    # Option 3: View current Guest List
    elif choice == "3":
        print("\n📋 Current Guests:")
        with open(filename, "r") as file:
            guests = file.readlines()
            if guests:
                for guest in guests:
                    print(f"🔷 {guest.strip()}")
            else:
                print("⚠ No guests checked in yet")
    
    # Option 4: Check if guest is still checked in
    elif choice == "4":
        check_guest = input("Enter guest name to check: ").strip()
        with open(filename, "r") as file:
            checked_in = [line.strip() for line in file]
        if check_guest in checked_in:
            print(f"✅ {check_guest} is still checked in!")
        else:
            print(f"❌ {check_guest} is checked out.")
    
    # Option 5: Exit the program
    elif choice == "5":
        print(f"👋 Thanks for managing '{event_name}'! Goodbye!")
        break
    else:
        print("⚠ Invalid Choice! Please enter a number from the list: ")