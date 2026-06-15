public class character{
    String name;
    String message;

public character(String name, String message){
    this.name = name;
    this.message = message;
}

public void displayinfo(){
    System.out.println("====MESSAGES====");
    System.out.println("Name :"  +name);
    System.out.println("Message :"  +message);
    System.out.println("================");
}

public static void main(String[] args) {
    character rust = new character("Rust Cohle", "I think human consiusness...is a tragic mistep of evolution");
    character tyler = new character("Tyler Durden", "We're the generations of man raised by a woman...Im wondering if another woman is really the answer we need");
    character lou = new character("Lou Bloom", "You have to get the money...TO BUY THE TICKET");
    character david = new character("David Mills", "I SAW YOU WITH THE BOX WHAT WAS IN THE BOX?");
    character driver = new character("Driver", "I Drive....");
    character narrator = new character("The Narrator", "If this is your first night in fight club...you have to fight");
    character henry = new character("Henry Letham", "You're just trying to save me but its too late...cause I gotta wake up");

    rust.displayinfo();
    tyler.displayinfo();
    lou.displayinfo();
    david.displayinfo();
    driver.displayinfo();
    narrator.displayinfo();
    henry.displayinfo();

}
}