import os
from datetime import  datetime
import os
JOURNAL_FILE="journal.txt"

def write_entry():
    print("Enter your journal entry (type 'exit' to finish):")
    print("Type your thoughts below. Press Enter on an empty line to finish.")

    Lines=[]
    while True:
        Line=input(">")
        if Line=='':
            break
        Lines.append(Line)

    if not Lines:
        print("No entry was made.")
        return
    
    #a w r
    with open(JOURNAL_FILE, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n============================\n")
        file.write(f"Entry Date: {timestamp}\n")
        file.write(f"============================\n")

        #write the actual entry
        for line in Lines:
            file.write(line + "\n")

    print("Your entry has been saved to the journal.")

def read_journal():
    print("\n  -- reading your journal --")

    if not os.path.exists(JOURNAL_FILE):
        print("No journal entries found.")
        return
    
    #r mode open file for reading
    with open(JOURNAL_FILE, "r") as file:
        content = file.read()
        if content.strip() == "":
            print("Your journal file exists but is empty.")
        else:
            print(content)

def main():
    while True:
        print("\nWelcome to the Journal App!")
        print("1. Write a new journal entry")
        print("2. Read your journal")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            write_entry()
        elif choice == '2':
            read_journal()
        elif choice == '3':
            print("Exiting the Journal App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()