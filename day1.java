// read text file and iterate with nested for loop

// read file
import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.ArrayList;
import java.util.Scanner; // Import the Scanner class to read text files

public class ReadFile {
  public static void main(String[] args) {

    ArrayList<Integer> list = new ArrayList<>();

    try {
      File myObj = new File("/Users/korbinianschleifer/desktop/input.txt");
      Scanner myReader = new Scanner(myObj);
      while (myReader.hasNextLine()) {
        String data = myReader.nextLine();
        System.out.println(data);
        int number = Integer.parseInt(data);
        list.add(number);
      }
      myReader.close();
    } catch (FileNotFoundException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }

    for(int i = 0; i < list.size(); i++) {
        for(int j = i + 1; j < list.size(); j++) {
            for(int x = j +1; x < list.size(); x++) {
                if (list.get(i) + list.get(j) + list.get(x) == 2020) {
                    System.out.println("Solution found");
                    System.out.println("number1: " + list.get(i) + " number2: " + list.get(j) + " number3: " + list.get(x));
                    System.out.println(list.get(i) * list.get(j) * list.get(x));
                }
            }
            
        }
    }


  }
}