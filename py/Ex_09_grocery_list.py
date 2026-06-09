#Create a grocery list and perform various operations. 


#grocery_list = ["fruits", "vegetables", "chicken", "soap", "chips"]


grocery_list = []

#item = input("Add an item: ").strip() #input an item and strip 

while True: 

    #Actions
    
    print ("\n---Shopping List Manager----")
    print ("1) Add item")
    print ("2) View List")
    print ("3) Remove item")
    print ("q) Quit") 

    choice = input ("Choose an option: ").strip().lower()

    if choice =="1":
        item = input("Item to add: ").strip()
        grocery_list.append(item)
        print(f"Added: {item}")

    elif choice == "2":
        if len(grocery_list) == 0:
            print ("Your list is empty.")
        else: 
            print ("\nYour shopping list:")
            for i, item in enumerate(grocery_list,start=1):
                print(f"{i},{item}")

    elif choice =="3": 
        item_to_remove = input ("Item to remove: ").strip()

        if item_to_remove in grocery_list: 
            grocery_list.remove(item_to_remove)
            print (f"Removed: {item_to_remove}")
        else:
            print ("That item is not in your list.")

    elif choice == "q": 
        print ("Bye!")

        break 

    else: 
        print ("Invalid choice. Please choose 1,2,3,or q.")


