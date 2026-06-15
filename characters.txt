//An OOP program about literally me characters that live inside me

public class characters {
    String name;
    int age;
    String movie;
    String quote;

    public characters(String name, int age, String movie, String quote) {
        this.name = name;
        this.age = age;
        this.movie = movie;
        this.quote = quote;
    }
    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Movie: " + movie);
        System.out.println("Quote: " + quote);
        System.out.println();
    }
    public static void main(String[] args) {
        characters rust = new characters("Rustin Cohle", 35, "True Detective", "Time is a flat circle.");
        characters tyler = new characters("Tyler Durden", 36, "Fight Club", "The things you own end up owning you.");
        characters patrick = new characters("Patrick Bateman", 27, "American Psycho", "I think my mask of sanity...is about to slip.");
        characters louis = new characters("Louis Bloom", 32, "Nightcrawler", "If you want to win the lottery, you have to make the money to buy a ticket.");
        characters driver = new characters("Driver", 30, "Drive", "You give me a time and a place, I give you a five-minute window.");
        characters joi = new characters("Joi", 28, "Blade Runner 2049", "You look lonely...i can fix that.");
        characters travis = new characters("Travis Bickle", 30, "Taxi Driver", "Loneliness has followed me my whole life.");
        characters fleck = new characters("Arthur Fleck", 34, "Joker", "I used to think my life was a tragedy, but now I realize it's a comedy.");
        characters officerk = new characters("Officer K", 35, "Blade Runner 2049", "Officer KD6.3-7, A tall white fountain played.");
        characters henryletham = new characters("Henry Letham", 21, "stay", "You are. You're real. You were just trying to save me but its too late...cause I gotta wake up.");

        rust.displayInfo();
        tyler.displayInfo();
        patrick.displayInfo();
        louis.displayInfo();
        driver.displayInfo();
        joi.displayInfo();
        travis.displayInfo();
        fleck.displayInfo();
        officerk.displayInfo();
        henryletham.displayInfo();

    }
}