//I wanna make an OOP code about vehicles, I will create a public class Vehicles
//After that there will be classes which extends from the public class Vehicles
//The classes are : Tuner, Muscle, and Exotic

public class Vehicles {
    String type;
    String manufacturer;
    String model;
    int year;

    public Vehicles(String manufacturer, String type, String model, int year) {
        this.manufacturer = manufacturer;
        this.type = type;
        this.model = model;
        this.year = year;
    }

static class Tuner extends Vehicles {
    public Tuner(String manufacturer, String type, String model, int year) {
        super(manufacturer, type, model, year);
    }
}
static class Muscle extends Vehicles {
    public Muscle(String manufacturer, String type, String model, int year) {
        super(manufacturer, type, model, year);
    }
}
static class Exotic extends Vehicles {
    public Exotic(String manufacturer, String type, String model, int year) {
        super(manufacturer, type, model, year);
    }
}
public void displayinfo() {
    System.out.println("___Vehicle Information___");
    System.out.println("Manufacturer:" + manufacturer);
    System.out.println("Type:" + type);
    System.out.println("Model:" + model);
    System.out.println("Year:" + year);
    System.out.println();
}
public static void main(String[] args) {
    // Muscle vehicles
    Muscle muscle1 = new Muscle("Dodge", "Muscle", "Charger", 1969);
    Muscle muscle2 = new Muscle("Dodge", "Muscle", "Challenger", 1971);
    Muscle muscle3 = new Muscle("Ford", "Muscle", "Mustang GT", 2005);
    Muscle muscle4 = new Muscle("Ford", "Muscle", "Mustang Boss 429", 1969);
    Muscle muscle5 = new Muscle("Plymouth", "Muscle", "RoadRunner", 1970);
    Muscle muscle6 = new Muscle("Chevrolet", "Muscle", "Camaro SS", 1969);
    Muscle muscle7 = new Muscle("Chevrolet", "Muscle", "Chevelle SS", 1970);

    // Tuner vehicles
    Tuner tuner1 = new Tuner("Mitsubishi", "Tuner", "Eclipse GSX", 1999);
    Tuner tuner2 = new Tuner("Honda", "Tuner", "S2000", 2000);
    Tuner tuner3 = new Tuner("Toyota", "Tuner", "Corolla GT-S (AE86)", 1986);
    Tuner tuner4 = new Tuner("VW", "Tuner", "Golf GTI", 2005);
    Tuner tuner5 = new Tuner("Lexus", "Tuner", "IS300", 2004);
    Tuner tuner6 = new Tuner("Nissan", "Tuner", "Silvia S15", 2002);

    // Exotic vehicles
    Exotic exotic1 = new Exotic("Lamborghini", "Exotic", "Murcielago", 2003);
    Exotic exotic2 = new Exotic("Lamborghini", "Exotic", "Gallardo", 2003);
    Exotic exotic3 = new Exotic("Porsche", "Exotic", "Carrera GT", 2005);
    Exotic exotic4 = new Exotic("Porsche", "Exotic", "911 Turbo", 2002);
    Exotic exotic5 = new Exotic("Lotus", "Exotic", "Elise", 2005);
    Exotic exotic6 = new Exotic("Aston Martin", "Exotic", "DB9", 2003);
    Exotic exotic7 = new Exotic("McLaren", "Exotic", "SLR", 2003);

    // Display all vehicles
    muscle1.displayinfo();
    muscle2.displayinfo();
    muscle3.displayinfo();
    muscle4.displayinfo();
    muscle5.displayinfo();
    muscle6.displayinfo();
    muscle7.displayinfo();

    tuner1.displayinfo();
    tuner2.displayinfo();
    tuner3.displayinfo();
    tuner4.displayinfo();
    tuner5.displayinfo();
    tuner6.displayinfo();

    exotic1.displayinfo();
    exotic2.displayinfo();
    exotic3.displayinfo();
    exotic4.displayinfo();
    exotic5.displayinfo();
    exotic6.displayinfo();
    exotic7.displayinfo();
}
}
