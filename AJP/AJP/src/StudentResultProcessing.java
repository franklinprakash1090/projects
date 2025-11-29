import java.util.Scanner;

class Student {
    String name, course;
    int rollNo;

    void inputDetails(Scanner sc) {
        System.out.print("Enter Student Name: ");
        name = sc.nextLine();
        System.out.print("Enter Roll Number: ");
        rollNo = sc.nextInt();
        sc.nextLine(); // Consume newline
        System.out.print("Enter Course Name: ");
        course = sc.nextLine();
    }

    void displayDetails() {
        System.out.println("\n--- Student Details ---");
        System.out.println("Name: " + name);
        System.out.println("Roll Number: " + rollNo);
        System.out.println("Course: " + course);
    }
}

class Result extends Student {
    int marks1, marks2, marks3, total;
    double average;
    char grade;
    void inputMarks(Scanner sc) {
        System.out.print("Enter Marks for Subject 1: ");
        marks1 = sc.nextInt();
        System.out.print("Enter Marks for Subject 2: ");
        marks2 = sc.nextInt();
        System.out.print("Enter Marks for Subject 3: ");
        marks3 = sc.nextInt();
    }
    

    void calculateResult() {
        total = marks1 + marks2 + marks3;
        average = total / 3.0;

        if (average >= 85)
            grade = 'A';
        else if (average >= 70)
            grade = 'B';
        else if (average >= 50)
            grade = 'C';
        else
            grade = 'D';
    }

    void displayResult() {
        System.out.println("\n--- Result Details ---");
        System.out.println("Marks in Subject 1: " + marks1);
        System.out.println("Marks in Subject 2: " + marks2);
        System.out.println("Marks in Subject 3: " + marks3);
        System.out.println("Total Marks: " + total);
        System.out.println("Average Marks: " + average);
        System.out.println("Grade: " + grade);
    }
}

public class StudentResultProcessing {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Result r = new Result();
            r.inputDetails(sc);
            r.inputMarks(sc);
            r.calculateResult();
            r.displayDetails();
            r.displayResult();
        }
    }
}
