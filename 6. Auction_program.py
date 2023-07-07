ascii_art = '''

                                                                             
                         %%                                                     
                        %%%%%%%%%                                               
                         %%  %%%%%%%%%%                                         
                        %%%%%%%%%  %%%%%%                                       
                       %%%%%%%%%%%%%%%                                          
                      %%%%%%%%%%%%%%                                            
                     %%%%%%%%%%%%%%                                             
                    %%%%%%%%%%%%%%%%%%%%%                                       
                   %%%%%%%%%%%%%%%%%%%%%%%%%%%%%/                               
               %%%  %%%%%%%%%%%%    %%%%%%%%%%%%%%%%%%%%                        
               %%%%%%%%%  %%%%%          %%%%%%%%%%%%%%%%%%%%%%                 
                   %%%%%%%%%%(                 %%%%%%%%%%%%%%%%%%%%%%%          
                         %%%%%%%                    %%%%%%%%%%%%%%%%%%%%        
                                                         %%%%%%%%%%%%%%%%       
                                                              %%%%%%%%%%        
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%                                           
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                         
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

'''

import os
# In order for your terminal commands under os.system() to work, you need to emulate your terminal inside the output console. Select 'Edit Configurations' from the 'Run' menu.
# Under the 'Execution' section, select 'Emulate terminal in output console'.

dic = {}
finish_bid = False
winner = ""

def highest_bidder(record_bid):
    high_bid = 0
    for bidder in record_bid:
        bid_amount = record_bid[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder
    print(f"{winner} is placed the highest bid: {high_bid}\n")    # Returns the highest bidder
    print(dic)    # Retruns all the bids


while not finish_bid:
    print(ascii_art)
    name = input("Name of the bidder: ")
    bid = int(input("Enter your bid: Rs. "))
    dic[name] = bid
    others = input("Is there any other bidder present? 'yes' or 'no'? -> ").lower()    # Asking for multiple inputs
    os.system('cls')    # It's used to clear the console
    if others == "no":
        finish_bid = True
        highest_bidder(dic)
