public class Bank{
  private CheckingAccount accountOne;
  private CheckingAccount accountTwo;
  private CheckingAccount accountThree;
  public Bank(){
    accountOne = new CheckingAccount("Zeus", 100);
    accountTwo = new CheckingAccount("Hades", 200);
    accountThree = new CheckingAccount("Odin", 800);
  }

  public static void main(String[] args){
    Bank bankOfGods = new Bank();
    System.out.println(bankOfGods.accountThree.name);
    System.out.println(bankOfGods.accountThree.balance);
}
}