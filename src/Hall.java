import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Hall {
	private String name;
	private Item[] menu;
	
	// creates the Halls object
	Hall(String name, String menuName) throws FileNotFoundException{
		this.name = name;
		File menuFile = new File(menuName);
		Scanner menuScanner = new Scanner(menuFile);
		int numMenuItems = menuScanner.nextInt();
		Item[] menu = new Item[numMenuItems];
		for (int i = 0; i < numMenuItems; i++) {
			String currentName = menuScanner.nextLine();
			menu[i] = new Item(currentName);
		}
		menuScanner.close();
	}
	
	// getter method for the name
	public String getName() {
		return this.name;
	}
	
	// creates an array of items from the menu
	public Item[] getMenu() {
		return this.menu;
	}
}
