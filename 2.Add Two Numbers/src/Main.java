import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int sunLength =  in.nextInt();
        int count = 0;
        while (in.hasNextInt()) {//注意while处理多个case
            int alength = in.nextInt();
            int aNum = in.nextInt();
            int bLength = in.nextInt();
            int bNum = in.nextInt();

            for(int i = 1;i <= aNum;i++){
                for (int j = 1;j <= bNum;j++){
                    int tempa =1;
                    if (i*alength+j*bLength == sunLength){
                        for (int temp=1;temp<=i;temp++){
                            tempa *=
                        }
                        int tempa=
                        count += (aNum/i)
                    }
                }
            }
        }
    }
}