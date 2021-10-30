public class Items {

	private String name;
	private boolean available;
	
	// Makes the new item
	Items(String name){
		this.name =  name;
		this.available = true;
	}
	
	// getter method for the name
	public String getName() {
		return this.name;
	}
	
	// getter method for the availability
	public boolean getAvailabee() {
		return this.available;
	}
	
	// sets the availability
	public void setAvailable(boolean available) {
		this.available = available;
	}
}
