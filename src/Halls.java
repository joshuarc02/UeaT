import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Halls {
	private String name;
	private Items[] menu;
	
	// creates the Halls object
	Halls(String name, String menuName) throws FileNotFoundException{
		this.name = name;
		File menuFile = new File(menuName);
		Scanner menuScanner = new Scanner(menuFile);
		int numMenuItems = menuScanner.nextInt();
		Items[] menu = new Items[numMenuItems];
		for (int i = 0; i < numMenuItems; i++) {
			String currentName = menuScanner.nextLine();
			menu[i] = new Items(currentName);
		}
		menuScanner.close();
	}
	
	// getter method for the name
	public String getName() {
		return this.name;
	}
	
	// creates an array of items from the menu
	public Items[] getMenu() {
		return this.menu;
	}
}
