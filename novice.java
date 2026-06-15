public class novice {
    String Name;
    String Background;

public novice(String Name, String Background){
    this.Name = Name;
    this.Background = Background;
}

public void displayinfo(){
    System.out.println("======");
    System.out.println("Name : " +Name);
    System.out.println("Background : " +Background);
}
public static void main(String[] args) {
    novice paul = new novice("Paul", "The Culprit");
    novice mason = new novice("Mason", "The Victim");

    paul.displayinfo();
    mason.displayinfo();
    
}
}

