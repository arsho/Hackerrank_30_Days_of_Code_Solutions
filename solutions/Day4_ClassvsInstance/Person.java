/*
  Title     : Day 4: Class vs. Instance
  Domain    : Tutorials
  Author    : Ahmedur Rahman Shovon
  Created   : 03 April 2019
*/
import java.io.*;
import java.util.*;

public class Person {
    private int age;

	public Person(int initialAge) {
  		// Add some more code to run some checks on initialAge
        if(initialAge<0){
            System.out.println("Age is not valid, setting age to 0.");
            initialAge = 0;
        }
        this.age = initialAge;
	}

	public void amIOld() {
  		// Write code determining if this person's age is old and print the correct statement:
        String young = "You are young.";
        String teen = "You are a teenager.";
        String old = "You are old.";
        String message = old;
        if(this.age<13)
            message = young;
        else if(this.age<18)
            message = teen;
        System.out.println(message);
	}

	public void yearPasses() {
  		// Increment this person's age.
        this.age+=1;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int i = 0; i < T; i++) {
			int age = sc.nextInt();
			Person p = new Person(age);
			p.amIOld();
			for (int j = 0; j < 3; j++) {
				p.yearPasses();
			}
			p.amIOld();
			System.out.println();
        }
		sc.close();
    }
}
