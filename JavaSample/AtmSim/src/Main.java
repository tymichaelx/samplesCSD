
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        ArrayList<Double> balance = new ArrayList<>();
        ArrayList<Double> withdrawal = new ArrayList<>();
        int userInput = -1;
        ArrayList<Integer> inputHistory = new ArrayList<>();
        ArrayList<Double> depositAmt = new ArrayList<>();

        // Starting balance
        balance.add(1000.00);

        do{
            do {
                printMenu();
                if (in.hasNextInt()) {
                    userInput = in.nextInt();
                }
                if (userInput < 1 || userInput > 4) {
                    System.out.println("Invalid menu choice.");
                }
            } while ((userInput < 1) || (userInput > 4));

            System.out.println();

            if (userInput == 1) {
                inputHistory.add(1);
                System.out.printf("Your current balance is $%,.2f.\n", balance.get(balance.size() - 1));
                balance.add(balance.get(balance.size() - 1));
            } else if (userInput == 2) {
                System.out.print("Enter deposit amount: ");
                depositAmt.add(in.nextDouble());
                balance.add(balance.get(balance.size() - 1) + depositAmt.get(depositAmt.size() - 1));
                System.out.printf("Your updated balance is $%,.2f.\n", balance.get(balance.size() - 1));
                inputHistory.add(2);
            } else if (userInput == 3) {
                System.out.print("Enter withdrawal amount: ");
                withdrawal.add(in.nextDouble());
                if (withdrawal.get(withdrawal.size() - 1) <= balance.get(balance.size() - 1)) {
                    balance.add(balance.get(balance.size() - 1) - withdrawal.get(withdrawal.size() - 1));
                    System.out.printf("Your updated balance is $%,.2f.\n", balance.get(balance.size() - 1));
                    inputHistory.add(3);
                } else {
                    System.out.printf("Insufficient funds. Your current balance is $%,.2f.\n",
                            balance.get(balance.size() - 1));
                }
            } else {
                System.out.println("Good-bye.");
                inputHistory.add(4);
            }
        } while (userInput != 4);

        System.out.println();

        printHistory(inputHistory, balance, depositAmt, withdrawal);
    }
    public static void printMenu() {
        System.out.print("\nEnter the number of your desired transaction: ");
        System.out.println();
        System.out.println("1. Balance");
        System.out.println("2. Deposit");
        System.out.println("3. Withdrawal");
        System.out.println("4. Quit");
        System.out.println();
    }

    public static void printHistory(ArrayList<Integer> inputHistory, ArrayList<Double> balance,
                                    ArrayList<Double> depositAmt, ArrayList<Double> withdrawal) {
        int depositNum = 0;
        int withdrawalNum = 0;
        int balanceNum = 0;

        System.out.println("\nATM History (valid transactions only)");
        System.out.println("=====================================");

        for (int i = 0; i < inputHistory.size(); i++) {

            if (inputHistory.get(i) == 1) {
                System.out.printf("1. Bala. request / transaction amount: $0.00 " +
                        "Current balance after transaction: $%,.2f\n", balance.get(i + 1));
                balanceNum++;
            } else if (inputHistory.get(i) == 2) {
                System.out.printf("2. Depo. request / transaction amount: $%,.2f " +
                        "Current balance after transaction: $%,.2f\n", depositAmt.get(depositNum), balance.get(i + 1));
                depositNum++;
            } else if (inputHistory.get(i) == 3) {
                System.out.printf("3. With. request / transaction amount: $%,.2f " +
                        "Current balance after transaction: $%,.2f\n", withdrawal.get(withdrawalNum), balance.get(i + 1));
                withdrawalNum++;
            } else {
                System.out.printf("4. Quit request / transaction amount: $0.00 " +
                        "Current balance after transaction: $%,.2f\n", balance.get(balance.size() - 1));
            }
        }
        System.out.println();
        System.out.println("1. Balance request(s): " + balanceNum);
        System.out.println("2. Deposit request(s): " + depositNum);
        System.out.println("3. Withdrawal request(s): " + withdrawalNum);
        System.out.println("4. Quit request(s): 1");

    }
}
