//A simple OOP Program

public class cycle {
    private String name;
    private String role;

    public cycle(String name, String role){
        this.name = name;
        this.role = role;
    }

    public String getName() {
        return name;
    }

    public String getRole() {
        return role;
    }

    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Role: " + role);
    }

    public static void main(String[] args) {
        cycle cycle1 = new cycle("Officer K", "Blade Runner");
        cycle1.displayInfo();
    }
}