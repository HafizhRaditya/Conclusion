// An OOP Code about insanity
public class insanity{
    private String level;
    private String causes;
    private String name;

    public insanity(String level, String causes, String name){
        this.level = level;
        this.causes = causes;
        this.name = name;
    }

    public String getLevel(){
        return level;

    }
    public String getCauses(){
        return causes;
    }

    public String getName(){
        return name;
    }

    public void displayInfo(){
        System.out.println("Insanity Name: " + name);
        System.out.println("Level of Insanity: " + level);
        System.out.println("Causes of Insanity: " + causes);
    }

    public static void main(String[] args) {
        insanity insanity1 = new insanity("Severe", "Protection", "Henry Letham");
        insanity insanity2 = new insanity("Mild", "Stress", "John Doe");
        insanity1.displayInfo();
        insanity2.displayInfo();
    }
    
}