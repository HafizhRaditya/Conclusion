public class rustcohle {
    public String personality;
    public String catchphrase;
    public int age;
    public String friends;
    public String victims;

    public rustcohle(String personality, String catchphrase, int age, String friends, String victims) {
        this.personality = personality;
        this.catchphrase = catchphrase;
        this.age = age;
        this.friends = friends;
        this.victims = victims;
    }

    public static void main(String[] args) {
        rustcohle character = new rustcohle("Introvert", "Time is a flat circle", 35, "Marty Hart", "Dora Lang");
        System.out.println("Personality: " + character.personality);
        System.out.println("Catchphrase: " + character.catchphrase);
        System.out.println("Age: " + character.age);
        System.out.println("Friends: " + character.friends);
        System.out.println("Victims: " + character.victims);
    }

}