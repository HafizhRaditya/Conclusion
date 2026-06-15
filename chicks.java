public class chicks{
    String Name;
    String Background;

public chicks(String Name, String Background){
    this.Name = Name;
    this.Background = Background;
}

public void displayinfo(){
    System.out.println("======");
    System.out.println("Name : " +Name);
    System.out.println("Background : " +Background);
}
public static void main(String[] args) {
    chicks chloe = new chicks("Chloe Price", "The blue haired girl who is addicted to smoke and drugs from a dealer named Frank Bowers");
    chicks rachel = new chicks("Rachel Amber", "The popular girl with her sad own depression bullshit and later she addicted to make love with Chloe, Frank, and Mr. Jefferson");
    chicks max = new chicks("Max Caulfield", "The chick who can rewind time");

    chloe.displayinfo();
    rachel.displayinfo();
    max.displayinfo();
}
}