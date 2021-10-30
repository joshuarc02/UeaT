
public class Halls {
	private String name;
	private Items[] menu;
	
	Halls(String name, Items[] menu){
		this.name = name;
		this.menu = menu;
	}
	
	public String getName() {
		return this.name;
	}
	
	public Items[] getMenu() {
		return this.menu;
	}
}
