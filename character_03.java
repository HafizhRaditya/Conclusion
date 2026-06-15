public class character{
    String name;
    String messages;

public character(String name, String messages){
    this.name = name;
    this.messages = messages;
}

public void displayinfo(){
    System.out.println("-----CHARACTER INFO----");
    System.out.println("Name :" + this.name);
    System.out.println("Message:" +this.messages);
    System.out.println("--------------------");
}

public static void main(String[] args) {
    character bateman = new character("Patrick", "My pain continues to elude me");
    character elliot = new character("Elliot", "I want...a way out of loneliness");
    character tyler = new character("Tyler", "You are the all singing all dancing crap in the world");
    character narrator = new character("Narrator", "Everything is a copy...of a copy...of a copy");
    character tony = new character("Tony", "The World Chico.....and everything in it");
    character driver = new character("Driver", "I Drive....");
    character henry = new  character("Henry", "You're just trying to save me but its too late");
    character travis = new  character("Travis", "Here it is.......");
    character jordan = new  character("Jordan", "There is no...nobility in poverty");


    bateman.displayinfo();
    elliot.displayinfo();
    tyler.displayinfo();
    narrator.displayinfo();
    tony.displayinfo();
    driver.displayinfo();
    henry.displayinfo();
    travis.displayinfo();
    jordan.displayinfo();
}

}

