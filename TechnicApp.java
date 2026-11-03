import java.util.ArrayList;
import java.util.Scanner;

// فئة لتخزين معلومات الطبيب
class Doctor {
    String name;
    String specialization;
    String wilaya;
    String phone;

    public Doctor(String name, String specialization, String wilaya, String phone) {
        this.name = name;
        this.specialization = specialization;
        this.wilaya = wilaya;
        this.phone = phone;
    }

    public void display() {
        System.out.println("----------------------------------------");
        System.out.println("👨‍⚕️ الطبيب: " + name);
        System.out.println("🩺 التخصص: " + specialization);
        System.out.println("📍 الولاية: " + wilaya);
        System.out.println("📞 الهاتف: " + phone);
        System.out.println("----------------------------------------");
    }
}

public class TechnicApp {
    public static void main(String[] args) {
        ArrayList<Doctor> doctors = new ArrayList<>();

        // إضافة بيانات تجريبية لأطباء في الجزائر
        doctors.add(new Doctor("د. أحمد بن علي", "طب عام", "تيارت", "046-55-44-33"));
        doctors.add(new Doctor("د. مراد سليم", "أطفال", "تيارت", "046-11-22-33"));
        doctors.add(new Doctor("د. فاطمة الزهراء", "أسنان", "الجزائر العاصمة", "021-99-88-77"));
        doctors.add(new Doctor("د. كريم مختار", "عظام", "وهران", "041-33-22-11"));

        Scanner scanner = new Scanner(System.in);
        
        System.out.println("========================================");
        System.out.println("     مرحباً بك في تطبيق تيكنيك (Technic)  ");
        System.out.println("========================================");

        while (true) {
            System.out.println("\nاختر العملية:");
            System.out.println("1. عرض كل الأطباء");
            System.out.println("2. البحث حسب التخصص (أو الولاية)");
            System.out.println("3. خروج");
            System.out.print("أدخل رقم الخيار: ");
            
            String choice = scanner.nextLine();

            if (choice.equals("1")) {
                System.out.println("\n--- قائمة الأطباء المسجلين ---");
                for (Doctor d : doctors) {
                    d.display();
                }
            } else if (choice.equals("2")) {
                System.out.print("أدخل كلمة البحث (مثل: تيارت، أسنان، طب عام): ");
                String query = scanner.nextLine().toLowerCase();
                
                boolean found = false;
                System.out.println("\n--- نتائج البحث ---");
                for (Doctor d : doctors) {
                    if (d.specialization.toLowerCase().contains(query) || d.wilaya.toLowerCase().contains(query) || d.name.toLowerCase().contains(query)) {
                        d.display();
                        found = true;
                    }
                }
                if (!found) {
                    System.out.println("❌ لم يتم العثور على نتائج مطابقة.");
                }
            } else if (choice.equals("3")) {
                System.out.println("شكراً لاستخدام تطبيق تيكنيك. إلى اللقاء!");
                break;
            } else {
                System.out.println("خيار غير صحيح، حاول مرة أخرى.");
            }
        }
        scanner.close();
    }
}

