import java.security.*;
import java.util.Base64;

public class Main{
    public static void main(String[] args) throws Exception{
        //key
        KeyPairGenerator keygen = KeyPairGenerator.getInstance("DSA");
        keygen.initialize(2048);
        KeyPair pair = keygen.generateKeyPair();
        
        PrivateKey priv = pair.getPrivate();
        PublicKey pub = pair.getPublic();
        
        //msg
        String msg = "hi how are you";
        
        //sign
        
        Signature sign = Signature.getInstance("SHA256withDSA");
        sign.initSign(priv);
        sign.update(msg.getBytes());
        
        byte[] signat = sign.sign();
        
        System.out.println(signat);
        
        //verify
        Signature verify = Signature.getInstance("SHA256withDSA");
        verify.initVerify(pub);
        verify.update(msg.getBytes());
        boolean valid = verify.verify(signat);
        if(valid) System.out.println("valid");
    }
}