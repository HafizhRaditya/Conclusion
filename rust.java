public class rust {
    String fullname;
    String message;
    String partner;
    String city;

    public rust(String fullname, String message, String partner, String city) {
        this.fullname = fullname;
        this.message = message;
        this.partner = partner;
        this.city = city;
    }

    public void displayinfo() {
        System.out.println("============");
        System.out.println("Fullname : " + fullname);
        System.out.println("Message : " + message);
        System.out.println("Partner : " + partner);
        System.out.println("City : " + city);
        System.out.println("============");
    }

    public static void main(String[] args) {
        rust character = new rust("Rustin Cohle", "Time Is A Flat Circle", "Marty Hart", "Louisiana");
        character.displayinfo();
    }
}