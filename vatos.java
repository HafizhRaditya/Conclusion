public class vatos{
    String name;
    String message;

public vatos(String name, String message){
    this.name = name;
    this.message = message;
}

public void displayinfo(){
    System.out.println("======");
    System.out.println("Name : " +name);
    System.out.println("Message : " +message);
    System.out.println("======");
}

public static void main(String[] args) {
    vatos john = new vatos("John Wick", "People keep asking me if im back, and I dont really have the answer. But now yeah...Im thinking Im back");
    vatos rick = new vatos("Rick Grimes", "We...are the walking dead");
    
    john.displayinfo();
    rick.displayinfo();
}
}