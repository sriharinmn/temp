import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;


public class Main{
    public static void main(String[] args) throws Exception{
        //key
        byte[] keyBytes = "8bytekey".getBytes();
        SecretKey key = new SecretKeySpec(keyBytes, "DES");
        
        String pt = "hi how are you";
        
        //cipher
        
        Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
        
        //encrypt
        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] ct = cipher.doFinal(pt.getBytes());
        
        System.out.println(Base64.getEncoder().encodeToString(ct));
        
        System.out.println();
        
        // decrypt
        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] dc = cipher.doFinal(ct);
        System.out.println(new String(dc));
    }
}