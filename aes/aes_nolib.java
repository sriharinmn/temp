import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import java.util.Base64;
import javax.crypto.Cipher;

public class Main {
    public static void main(String[] args) throws Exception{
        //key
        
        KeyGenerator keygen = KeyGenerator.getInstance("AES");
        keygen.init(128);
        SecretKey key = keygen.generateKey();
        
        //ivspec
        
        byte[] iv = new byte[16];
        IvParameterSpec ivspec = new IvParameterSpec(iv);
        
        //cipher
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        
        //encrypt
        cipher.init(Cipher.ENCRYPT_MODE, key, ivspec);
        
        String pt = "hi how are you";
        
        byte[] ct = cipher.doFinal(pt.getBytes());
        
        System.out.println(Base64.getEncoder().encodeToString(ct));
        
        //decrypt
        
        cipher.init(Cipher.DECRYPT_MODE, key, ivspec);
        
        byte[] dc = cipher.doFinal(ct);
        
        System.out.println(new String(dc));
    }
}