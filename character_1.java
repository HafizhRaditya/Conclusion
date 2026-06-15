public class character{
    String name;
    String message;

public character(String name, String message){
    this.name=name;
    this.message=message;
}
public void displayinfo(){
    System.out.println("====MESSAGES====");
    System.out.println("Name: " +name);
    System.out.println("Message: " +message);
    System.out.println("================");

}

public static void main(String[] args) {
    character tyler = new character("Tyler", "You are the all singing all dancing crap in the world.");
    character patrick = new character("Patrick", "There are no more barriers to cross");
    character travis = new character("Travis", "Here is a man who would stood up against the cunt the dog the filth the shit");
    character thomas = new character("Thomas", "Nearly got....FUCKING EVERYTHING");
    character rust = new character("Rust", "We keep the other bad man from the door");
    character narrator = new character("Narrator", "Everything is a copy of a copy of a copy");
    character driver = new character("Driver", "I Drive.....");

    tyler.displayinfo();
    patrick.displayinfo();
    travis.displayinfo();
    thomas.displayinfo();
    rust.displayinfo();
    narrator.displayinfo();
    driver.displayinfo();
}
}