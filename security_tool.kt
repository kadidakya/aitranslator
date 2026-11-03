import java.net.InetSocketAddress
import java.net.Socket

fun main() {
    println("""
    ==================================================
           أداة الفحص الأمني: abdelkader 1november      
    ==================================================
    """.trimIndent())

    print("أدخل عنوان الـ IP للفحص (مثال: 127.0.0.1 أو 192.168.1.1): ")
    val ip = readLine()?.trim()

    if (ip.isNullOrEmpty()) {
        println("[!] لم يتم إدخال عنوان IP. تم إلغاء العملية.")
        return
    }

    val portsToScan = listOf(21, 22, 53, 80, 443, 3389, 5555, 8080)

    println("\n[+] جاري فحص العنوان $ip عبر أداة abdelkader 1november ...\n")

    for (port in portsToScan) {
        val isOpen = checkPort(ip, port, 800)
        if (isOpen) {
            println("[+] المنفذ $port : مفتوح (OPEN)")
        } else {
            println("[-] المنفذ $port : مغلق (CLOSED)")
        }
    }

    println("\n[✔] اكتمل الفحص بنجاح بواسطة abdelkader 1november.")
}

fun checkPort(ip: String, port: Int, timeout: Int): Boolean {
    return try {
        val socket = Socket()
        socket.connect(InetSocketAddress(ip, port), timeout)
        socket.close()
        true
    } catch (e: Exception) {
        false
    }
}

