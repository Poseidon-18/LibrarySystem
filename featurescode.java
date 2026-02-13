import java.util.Scanner;

public class featurescode {

    // this is heavily inspired by Bro Code Codes, as i am a beginner in Java + giving him credit ofc
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        
        boolean isRunning = true;
        String choice;

        while (isRunning) {
            System.out.println("\nHello, So what do you want to do today?");
            System.out.println("1. Add a new book");
            System.out.println("2. View books");
            System.out.println("3. Exit this space");
            
            System.out.print("Enter your Choice: ");

            choice = scanner.nextLine();
            switch (choice) {
                case "1" -> add_book();
                case "2" -> show_books();
                case "3" -> {
                    System.out.println("Goodbye!");
                    isRunning = false;
                }
                default -> System.out.println("Not a valid choice, please try again.");
            }
        }
        
        scanner.close();
    }

    static void add_book() {
        System.out.print("Book title: ");
        String bookName = scanner.nextLine();
        
        System.out.print("Author: ");
        String bookAuthor = scanner.nextLine();
        
        // Logic for adding would go here (or just a print for now)
        System.out.println("Book '" + bookName + "' by " + bookAuthor + " added! (Simulated)");
    }

    static void show_books() {
        // This is where you'd loop through your data
        System.out.println("\n--- Displaying Books ---");
        System.out.println("Information on the books : 1, 'The Metamorphosis' by Franz Kafka");
        System.out.println("Information on the books : 2, 'Python Crash Course' by Eric Matthes");
    }
}