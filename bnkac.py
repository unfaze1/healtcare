


class Banka :

       def __init__(self, name ,balance):
            self.balance=balance
            self.name=name

       def __str__(self):
            print( f"Welcome to your account {self.name}\nYour balance is {self.balance}")

       def add_value():
           with open("efe1.csv","r") as file:
               
               liste=[]   
               ask=input("Enter your name ").title().strip()
               person=Banka(ask,0)
               for lines in file:
                  if lines :
                    name, transaction, cost, balance=lines.strip().split(",")
                    liste.append({"name":name,"transaction":transaction,"cost":cost,"cbalance":balance})
                    for i in liste:
                       if i['name']==ask:
                        person.balance=float(i['cbalance'])
                       else:
                        person.balance=0.0  
               return person
       
       @staticmethod
       def main() :
                 kişi=Banka.add_value()
                                                                   
                 print("Welcome to your bank account")
                 veri1=Banka.askadjustment(kişi)         
                 with veri1 as file:
                   table = Banka.get_getbalance(file)  
                   if True:
                      print(table)
                      print("        Your transaction successufly completed\n       İf need anything help call +90[531 661 24 16] ")  
       
       def askadjustment(self):
             text=open("efe1.csv", "a")
             with text as file:
              dct={}
              ask1=input(" whats your transaction(Deposit/Withdraw) ").title().strip()
              ask2=float(input(" how much this transaction cost "))
              match ask1:
                   case "Withdraw":
                        self.balance-=ask2
                   case "Deposit":
                        self.balance+=ask2
              if self.balance < -2000:
                  print("Cant make transaction \nCard limit is exceeded")
                  return False
              else:
               file.write(f"{self.name},{ask1},{ask2},{self.balance} \n")
               dct['Current revenue ']=self.balance
               file.close 
               return open("efe1.csv","r")
             
       def get_getbalance(file):
                  liste=file.readlines()
                  if liste:
                      last_line=liste[-1].strip()
                      name,transaction, cost, cbalance=last_line.rstrip().split(",")
                      return f"Current revenue :{cbalance}| Name:{name}|transaction cost:{cost}|transaction:{transaction}"
                 
       def add_dict(*kwargs,person):
               if person:
                kwargs[f'{person} Current revenue ']=person.balance
                return kwargs
     

if __name__=="__main__":
     Banka.main()    
