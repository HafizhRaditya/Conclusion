public class anger {
    private String cause;
    private String cure;

    public anger(String cause, String cure) {
        this.cause = cause;
        this.cure = cure;
    }

    public String getCause() {
        return cause;
    }

    public String getCure() {
        return cure;
    }

    public void displayInfo() {
        System.out.println("Cause of Anger: " + cause);
        System.out.println("Cure for Anger: " + cure);
    }

    public static void main(String[] args) {
        anger angerInstance = new anger("Injustice", "Patience and Understanding");
        angerInstance.displayInfo();
    }
}