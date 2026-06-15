public class character{
    String name;
    String message;

public character (String name, String message){
    this.name=name;
    this.message=message;
}

public void displayinfo(){
    System.out.println("======A Message For You======");
    System.out.println("Name :" +name);
    System.out.println("Message:" +message);
    System.out.println("=============================");
}

public static void main(String[] args) {
    character rust = new character("Rustin", "The world needs bad man");
    character daniel = new character("Daniel", "I'VE ABBONDEND MY CHILD");
    character tyler = new character("Tyler", "Our great depression....is our lives");
    character driver = new character("Driver", "How about this? Shut your mouth");
    character narrator = new  character("Tyler", "We are the all singing...all dancing crap in the world");
    character lou = new character("Lou", "You gotta win a lottery...to buy a ticket");

    rust.displayinfo();
    daniel.displayinfo();
    tyler.displayinfo();
    driver.displayinfo();
    narrator.displayinfo();
    lou.displayinfo();

    
}

}